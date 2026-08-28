"""Capture a safe, immutable career source snapshot from a Git project."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from scripts.lib.scan_sensitive_info import SECRET_PATTERNS
from scripts.lib.source_manifest import (
    register_source,
    repository_path,
    sha256_bytes,
    slugify,
    source_id,
    utc_now,
)

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

OpenWikiRunner = Callable[[Path, str], str]

OPENWIKI_MODES = {"auto", "required", "off"}
OPENWIKI_PROMPT = """Read the existing OpenWiki and repository evidence. Return a concise factual project briefing for career documentation with these headings: Purpose, Architecture, Core Workflows, Key Modules, Data and Integrations, Testing and Operations, Security Boundaries, and Questions About Personal Contribution. Do not modify the wiki or repository. Do not infer who implemented a component or claim business impact without explicit evidence."""
ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

DOCUMENT_EXTENSIONS = {".md", ".mdx", ".rst", ".adoc", ".txt"}
CODE_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".go",
    ".h",
    ".hpp",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".sh",
    ".sql",
    ".swift",
    ".ts",
    ".tsx",
    ".vue",
}
MANIFEST_NAMES = {
    "cargo.toml",
    "dockerfile",
    "go.mod",
    "makefile",
    "package.json",
    "pom.xml",
    "pyproject.toml",
}
SENSITIVE_NAME_TOKENS = {
    "credential",
    "credentials",
    "password",
    "secret",
    "secrets",
    "token",
    "tokens",
}
SKIP_PARTS = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
    "venv",
}


class ProjectIngestionError(RuntimeError):
    """Raised when a project repository cannot be safely captured."""


def run_command(command: list[str], *, allow_failure: bool = False) -> str:
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode and not allow_failure:
        message = result.stderr.strip() or result.stdout.strip() or "command failed"
        raise ProjectIngestionError(f"{' '.join(command[:3])}: {message}")
    return result.stdout.strip()


def git_output(repository: Path, *arguments: str, allow_failure: bool = False) -> str:
    return run_command(
        ["git", "-C", str(repository), *arguments], allow_failure=allow_failure
    )


def is_github_location(value: str) -> bool:
    if value.startswith("git@github.com:"):
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "ssh"} and parsed.hostname == "github.com"


def github_repository_slug(location: str) -> str:
    if location.startswith("git@github.com:"):
        path = location.split(":", 1)[1]
    else:
        path = urlparse(location).path.lstrip("/")
    slug = path.removesuffix(".git").rstrip("/")
    if slug.count("/") != 1:
        raise ProjectIngestionError(f"invalid GitHub repository URL: {location}")
    return slug


def clone_github_repository(location: str, destination: Path) -> None:
    if shutil.which("gh"):
        run_command(
            [
                "gh",
                "repo",
                "clone",
                github_repository_slug(location),
                str(destination),
                "--",
                "--depth=100",
            ]
        )
        return
    run_command(["git", "clone", "--depth=100", location, str(destination)])


def default_openwiki_runner(repository: Path, message: str) -> str:
    executable = shutil.which("openwiki")
    if not executable:
        raise ProjectIngestionError("openwiki CLI is not installed")
    try:
        result = subprocess.run(
            [executable, "code", "-p", message],
            cwd=repository,
            check=False,
            capture_output=True,
            text=True,
            timeout=900,
        )
    except subprocess.TimeoutExpired as error:
        raise ProjectIngestionError("openwiki CLI timed out after 900 seconds") from error
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "openwiki failed"
        raise ProjectIngestionError(ANSI_ESCAPE.sub("", detail)[-1200:])
    output = ANSI_ESCAPE.sub("", result.stdout).strip()
    if not output:
        raise ProjectIngestionError("openwiki CLI returned no project briefing")
    return output


def openwiki_markdown_sections(
    wiki_root: Path, *, maximum_pages: int = 80, maximum_bytes: int = 600_000
) -> tuple[list[str], int]:
    sections: list[str] = []
    used_bytes = 0
    for page_path in sorted(wiki_root.rglob("*.md"))[:maximum_pages]:
        content = read_text_file(page_path, maximum_bytes=160_000)
        if content is None:
            continue
        encoded_size = len(content.encode("utf-8"))
        if used_bytes + encoded_size > maximum_bytes:
            break
        relative_path = page_path.relative_to(wiki_root.parent)
        sections.append(render_file_section(relative_path, content))
        used_bytes += encoded_size
    return sections, len(sections)


def collect_openwiki_context(
    repository: Path,
    *,
    mode: str,
    runner: OpenWikiRunner,
) -> dict[str, Any]:
    if mode not in OPENWIKI_MODES:
        raise ProjectIngestionError(f"invalid OpenWiki mode: {mode}")
    wiki_root = repository / "openwiki"
    detected = wiki_root.is_dir()
    result: dict[str, Any] = {
        "detected": detected,
        "cli_used": False,
        "briefing": None,
        "sections": [],
        "pages": 0,
        "error": None,
    }
    if mode == "off":
        return result
    if not detected:
        if mode == "required":
            raise ProjectIngestionError("OpenWiki required but project has no openwiki/ directory")
        return result

    with tempfile.TemporaryDirectory(prefix="career-harness-openwiki-") as temporary_directory:
        workspace = Path(temporary_directory) / "repository"
        run_command(["git", "clone", "--quiet", "--no-hardlinks", str(repository), str(workspace)])
        workspace_wiki = workspace / "openwiki"
        if workspace_wiki.exists():
            shutil.rmtree(workspace_wiki)
        shutil.copytree(wiki_root, workspace_wiki)

        try:
            briefing = runner(workspace, OPENWIKI_PROMPT).strip()
            if contains_secret(briefing):
                raise ProjectIngestionError("OpenWiki briefing contained a possible credential")
            result["briefing"] = briefing[:160_000]
            result["cli_used"] = True
        except Exception as error:  # OpenWiki provider and runtime failures use fallback in auto mode.
            if mode == "required":
                raise ProjectIngestionError(f"OpenWiki required but failed: {error}") from error
            error_message = str(error)[-1200:]
            result["error"] = (
                "OpenWiki CLI failed; details omitted because they resembled a credential."
                if contains_secret(error_message)
                else error_message
            )

        sections, page_count = openwiki_markdown_sections(workspace_wiki)
        result["sections"] = sections
        result["pages"] = page_count
    return result


def tracked_files(repository: Path) -> list[Path]:
    lines = git_output(repository, "ls-files").splitlines()
    return sorted(Path(line) for line in lines if line.strip())


def is_sensitive_path(path: Path) -> bool:
    lowered_parts = [part.lower() for part in path.parts]
    name = path.name.lower()
    if any(part in SKIP_PARTS for part in lowered_parts):
        return True
    if name == ".env" or name.startswith(".env."):
        return True
    if path.suffix.lower() in {".key", ".p12", ".pem"}:
        return True
    normalized_name = name.replace("_", "-").replace(".", "-")
    name_tokens = set(re.split(r"-+", normalized_name))
    return bool(name_tokens & SENSITIVE_NAME_TOKENS) or "private-key" in normalized_name


def is_document(path: Path) -> bool:
    name = path.name.lower()
    if name.startswith(("readme", "architecture", "contributing", "design")):
        return path.suffix.lower() in DOCUMENT_EXTENSIONS or not path.suffix
    return "docs" in {part.lower() for part in path.parts} and path.suffix.lower() in DOCUMENT_EXTENSIONS


def is_manifest(path: Path) -> bool:
    name = path.name.lower()
    return (
        name in MANIFEST_NAMES
        or name.startswith("requirements") and path.suffix.lower() == ".txt"
        or name.startswith(("docker-compose", "compose"))
        and path.suffix.lower() in {".yaml", ".yml"}
    )


def contains_secret(content: str) -> bool:
    return any(pattern.search(content) for pattern in SECRET_PATTERNS.values())


def read_text_file(path: Path, *, maximum_bytes: int) -> str | None:
    if not path.is_file() or path.stat().st_size > maximum_bytes:
        return None
    content = path.read_text(encoding="utf-8", errors="replace")
    if "\x00" in content or contains_secret(content):
        return None
    return content.strip()


def fence_language(path: Path) -> str:
    suffix = path.suffix.lower().lstrip(".")
    return {"py": "python", "sh": "bash", "yml": "yaml"}.get(suffix, suffix)


def render_file_section(relative_path: Path, content: str) -> str:
    language = fence_language(relative_path)
    return f"### `{relative_path.as_posix()}`\n\n````{language}\n{content}\n````\n"


def snapshot_repository(
    repository: Path,
    *,
    origin: str,
    repository_root: Path = REPOSITORY_ROOT,
    include_code: bool = False,
    maximum_code_files: int = 50,
    maximum_content_bytes: int = 800_000,
    project_name: str | None = None,
    openwiki_mode: str = "auto",
    openwiki_runner: OpenWikiRunner = default_openwiki_runner,
) -> tuple[dict[str, Any], bool]:
    repository = repository.resolve()
    if not (repository / ".git").exists():
        raise ProjectIngestionError(f"not a Git repository: {repository}")

    head = git_output(repository, "rev-parse", "HEAD")
    branch = git_output(repository, "branch", "--show-current", allow_failure=True) or "detached"
    remote = git_output(repository, "config", "--get", "remote.origin.url", allow_failure=True)
    status = git_output(repository, "status", "--porcelain", allow_failure=True)
    files = [path for path in tracked_files(repository) if not is_sensitive_path(path)]
    tree_files = files[:2000]
    tree_truncated = len(files) > len(tree_files)
    history = git_output(
        repository,
        "log",
        "-n",
        "100",
        "--date=short",
        "--pretty=format:%h%x09%ad%x09%an%x09%s",
        allow_failure=True,
    )
    openwiki_context = collect_openwiki_context(
        repository, mode=openwiki_mode, runner=openwiki_runner
    )

    document_paths = [path for path in files if is_document(path) or is_manifest(path)]
    code_paths = [path for path in files if path.suffix.lower() in CODE_EXTENSIONS]
    selected_paths = document_paths + (code_paths[:maximum_code_files] if include_code else [])
    selected_paths = list(dict.fromkeys(selected_paths))

    sections: list[str] = []
    included_documents = 0
    included_code = 0
    used_bytes = 0
    for relative_path in selected_paths:
        absolute_path = repository / relative_path
        content = read_text_file(absolute_path, maximum_bytes=120_000)
        if content is None:
            continue
        encoded_size = len(content.encode("utf-8"))
        if used_bytes + encoded_size > maximum_content_bytes:
            break
        sections.append(render_file_section(relative_path, content))
        used_bytes += encoded_size
        if relative_path in document_paths:
            included_documents += 1
        else:
            included_code += 1

    project_name = project_name or repository.name.removesuffix(".git")
    tree = "\n".join(f"- `{path.as_posix()}`" for path in tree_files)
    if tree_truncated:
        tree += f"\n- ... {len(files) - len(tree_files)} more tracked files"
    history_section = history or "No commit history available."
    openwiki_parts: list[str] = []
    if openwiki_context["detected"] and openwiki_mode != "off":
        openwiki_parts.append("## OpenWiki Priority Context\n")
        if openwiki_context["briefing"]:
            openwiki_parts.append(
                "### OpenWiki CLI Project Briefing\n\n"
                + str(openwiki_context["briefing"])
                + "\n"
            )
        if openwiki_context["sections"]:
            openwiki_parts.append("### OpenWiki Pages\n\n")
            openwiki_parts.extend(openwiki_context["sections"])
        if openwiki_context["error"]:
            openwiki_parts.append(
                "### OpenWiki Fallback Notice\n\n"
                f"CLI briefing unavailable; existing wiki pages were used. {openwiki_context['error']}\n"
            )

    content = (
        f"# Project Repository Snapshot: {project_name}\n\n"
        f"- Origin: {origin}\n"
        f"- Remote: {remote or 'none'}\n"
        f"- Branch: {branch}\n"
        f"- HEAD: {head}\n"
        f"- Working tree dirty: {'yes' if status else 'no'}\n"
        f"- Tracked files: {len(files)}\n"
        f"- Code included: {'yes' if include_code else 'no'}\n\n"
        + ("\n".join(openwiki_parts) + "\n" if openwiki_parts else "")
        + "## Tracked Tree\n\n"
        f"{tree}\n\n"
        "## Recent Commit Metadata\n\n"
        f"````text\n{history_section}\n````\n\n"
        "## Selected Project Content\n\n"
        + ("\n".join(sections) if sections else "No safe text documents selected.\n")
    )
    content_bytes = content.encode("utf-8")
    digest = sha256_bytes(content_bytes)
    mode = "code" if include_code else "docs"
    if openwiki_context["detected"] and openwiki_mode != "off":
        mode = f"openwiki-{mode}"
    projects_root = repository_root / "sources" / "projects"
    projects_root.mkdir(parents=True, exist_ok=True)
    snapshot_path = projects_root / (
        f"{slugify(project_name)}-{head[:12]}-{mode}-{digest[:12]}.md"
    )
    if not snapshot_path.exists():
        snapshot_path.write_bytes(content_bytes)

    relative_snapshot = repository_path(snapshot_path, repository_root)
    entry_id = source_id(f"project-{project_name}-{mode}", digest)
    return register_source(
        repository_root / "sources" / "manifest.yaml",
        entry_id=entry_id,
        source_type="project_repository",
        path=relative_snapshot,
        origin=origin,
        digest=digest,
        extracted_text_path=relative_snapshot,
        captured_at=utc_now(),
        status="verified",
        metadata={
            "project": project_name,
            "head": head,
            "branch": branch,
            "remote": remote or None,
            "working_tree_dirty": bool(status),
            "tracked_files": len(files),
            "included_documents": included_documents,
            "included_code_files": included_code,
            "openwiki_mode": openwiki_mode,
            "openwiki_detected": bool(openwiki_context["detected"]),
            "openwiki_cli_used": bool(openwiki_context["cli_used"]),
            "openwiki_pages": int(openwiki_context["pages"]),
            "openwiki_cli_error": openwiki_context["error"],
        },
    )


def ingest_project(
    location: str,
    *,
    repository_root: Path = REPOSITORY_ROOT,
    include_code: bool = False,
    maximum_code_files: int = 50,
    openwiki_mode: str = "auto",
    openwiki_runner: OpenWikiRunner = default_openwiki_runner,
) -> tuple[dict[str, Any], bool]:
    if is_github_location(location):
        with tempfile.TemporaryDirectory(prefix="career-harness-project-") as temporary_directory:
            clone_path = Path(temporary_directory) / "repository"
            clone_github_repository(location, clone_path)
            github_name = github_repository_slug(location).split("/", 1)[1]
            return snapshot_repository(
                clone_path,
                origin=location,
                repository_root=repository_root,
                include_code=include_code,
                maximum_code_files=maximum_code_files,
                project_name=github_name,
                openwiki_mode=openwiki_mode,
                openwiki_runner=openwiki_runner,
            )

    local_path = Path(location).expanduser().resolve()
    return snapshot_repository(
        local_path,
        origin=str(local_path),
        repository_root=repository_root,
        include_code=include_code,
        maximum_code_files=maximum_code_files,
        openwiki_mode=openwiki_mode,
        openwiki_runner=openwiki_runner,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ingest a local or GitHub project repository as a safe source snapshot."
    )
    parser.add_argument("location")
    parser.add_argument("--include-code", action="store_true")
    parser.add_argument("--max-code-files", type=int, default=50)
    parser.add_argument("--openwiki", choices=sorted(OPENWIKI_MODES), default="auto")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entry, created = ingest_project(
        args.location,
        include_code=args.include_code,
        maximum_code_files=args.max_code_files,
        openwiki_mode=args.openwiki,
    )
    action = "ingested" if created else "already registered"
    print(f"{action} {entry['id']}: {entry['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
