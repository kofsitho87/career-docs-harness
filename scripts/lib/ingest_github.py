"""Capture public GitHub profile and repository metadata through the gh CLI."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any

from scripts.lib.source_manifest import (
    register_source,
    repository_path,
    sha256_bytes,
    slugify,
    source_id,
    utc_now,
)

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

Runner = Callable[[list[str]], str]

PROFILE_FIELDS = (
    "login",
    "name",
    "bio",
    "company",
    "location",
    "blog",
    "html_url",
    "created_at",
    "updated_at",
    "public_repos",
)

REPOSITORY_FIELDS = (
    "name",
    "full_name",
    "html_url",
    "description",
    "homepage",
    "language",
    "topics",
    "fork",
    "archived",
    "created_at",
    "updated_at",
    "pushed_at",
    "stargazers_count",
    "forks_count",
)


def default_runner(command: list[str]) -> str:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout


def select_fields(data: dict[str, Any], fields: tuple[str, ...]) -> dict[str, Any]:
    return {field: data.get(field) for field in fields}


def build_public_snapshot(
    profile: dict[str, Any], repositories: list[dict[str, Any]]
) -> dict[str, Any]:
    return {
        "profile": select_fields(profile, PROFILE_FIELDS),
        "repositories": [
            select_fields(repository, REPOSITORY_FIELDS)
            for repository in repositories
            if not repository.get("private", False)
        ],
        "note": "Repository counts and popularity metrics are evidence context, not career achievements.",
    }


def capture_github(
    username: str,
    *,
    repository_root: Path = REPOSITORY_ROOT,
    runner: Runner = default_runner,
) -> tuple[dict, bool]:
    profile = json.loads(runner(["gh", "api", f"users/{username}"]))
    repositories = json.loads(
        runner(["gh", "api", f"users/{username}/repos?per_page=100&sort=updated"])
    )
    snapshot = build_public_snapshot(profile, repositories)

    github_root = repository_root / "sources" / "github"
    github_root.mkdir(parents=True, exist_ok=True)
    content = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"
    content_bytes = content.encode("utf-8")
    digest = sha256_bytes(content_bytes)
    snapshot_path = github_root / f"{slugify(username)}-{digest[:12]}.json"
    if not snapshot_path.exists():
        snapshot_path.write_bytes(content_bytes)
    entry_id = source_id(f"github-{username}", digest)
    relative_path = repository_path(snapshot_path, repository_root)
    return register_source(
        repository_root / "sources" / "manifest.yaml",
        entry_id=entry_id,
        source_type="github",
        path=relative_path,
        origin=f"https://github.com/{username}",
        digest=digest,
        extracted_text_path=relative_path,
        captured_at=utc_now(),
        metadata={"username": username, "repository_count": len(snapshot["repositories"])},
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture public GitHub metadata with gh.")
    parser.add_argument("username")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entry, created = capture_github(args.username)
    action = "captured" if created else "already registered"
    print(f"{action} {entry['id']}: {entry['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
