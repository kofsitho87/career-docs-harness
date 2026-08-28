from __future__ import annotations

import os
import subprocess
import tempfile
from importlib import import_module
from pathlib import Path

import yaml

from scripts.lib.ingest_project import (
    github_repository_slug,
    ingest_project,
    is_github_location,
)


def git(repository: Path, *arguments: str, environment: dict[str, str] | None = None) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )
    return result.stdout.strip()


def create_project(root: Path) -> Path:
    project = root / "voice-agent"
    project.mkdir()
    git(project, "init")
    (project / "docs").mkdir()
    (project / "src").mkdir()
    (project / "README.md").write_text(
        "# Voice Agent\n\n상담 업무를 자동화하는 합성 프로젝트입니다.\n",
        encoding="utf-8",
    )
    (project / "docs" / "architecture.md").write_text(
        "# Architecture\n\nAPI, orchestration, tools를 분리합니다.\n",
        encoding="utf-8",
    )
    (project / "pyproject.toml").write_text(
        '[project]\nname = "voice-agent"\nversion = "0.1.0"\n', encoding="utf-8"
    )
    (project / "src" / "tokenizer.py").write_text(
        'print("tracked source code")\n', encoding="utf-8"
    )
    (project / ".env").write_text("TOP_SECRET=should-not-appear\n", encoding="utf-8")
    git(project, "add", ".")
    commit_environment = os.environ.copy()
    commit_environment.update(
        {
            "GIT_AUTHOR_NAME": "Sample Author",
            "GIT_AUTHOR_EMAIL": "sample@example.com",
            "GIT_COMMITTER_NAME": "Sample Author",
            "GIT_COMMITTER_EMAIL": "sample@example.com",
        }
    )
    git(project, "commit", "-m", "Initial project", environment=commit_environment)
    return project


def create_harness_root(root: Path) -> None:
    (root / "sources" / "projects").mkdir(parents=True)
    (root / "sources" / "manifest.yaml").write_text(
        "version: 1\nsources: []\n", encoding="utf-8"
    )


def test_local_project_snapshot_defaults_to_docs_and_deduplicates() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary_root = Path(temporary_directory)
        project = create_project(temporary_root)
        harness_root = temporary_root / "harness"
        create_harness_root(harness_root)
        original_head = git(project, "rev-parse", "HEAD")

        first, first_created = ingest_project(
            str(project), repository_root=harness_root
        )
        second, second_created = ingest_project(
            str(project), repository_root=harness_root
        )

        assert first_created is True
        assert second_created is False
        assert first == second
        assert first["type"] == "project_repository"
        snapshot = (harness_root / first["path"]).read_text(encoding="utf-8")
        assert "Voice Agent" in snapshot
        assert "architecture.md" in snapshot
        assert "pyproject.toml" in snapshot
        assert "tracked source code" not in snapshot
        assert "TOP_SECRET" not in snapshot
        assert "`.env`" not in snapshot
        assert git(project, "rev-parse", "HEAD") == original_head
        manifest = yaml.safe_load(
            (harness_root / "sources" / "manifest.yaml").read_text(encoding="utf-8")
        )
        assert len(manifest["sources"]) == 1


def test_include_code_adds_safe_tracked_source_only() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary_root = Path(temporary_directory)
        project = create_project(temporary_root)
        harness_root = temporary_root / "harness"
        create_harness_root(harness_root)

        entry, created = ingest_project(
            str(project), repository_root=harness_root, include_code=True
        )

        assert created is True
        snapshot = (harness_root / entry["path"]).read_text(encoding="utf-8")
        assert "tracked source code" in snapshot
        assert "TOP_SECRET" not in snapshot
        assert entry["metadata"]["included_code_files"] == 1


def test_github_location_detection() -> None:
    assert is_github_location("https://github.com/example/project") is True
    assert is_github_location("git@github.com:example/project.git") is True
    assert is_github_location("/Users/example/project") is False
    assert github_repository_slug("https://github.com/example/project") == "example/project"
    assert github_repository_slug("git@github.com:example/project.git") == "example/project"


def test_github_url_uses_temporary_clone_pipeline(monkeypatch) -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary_root = Path(temporary_directory)
        project = create_project(temporary_root)
        harness_root = temporary_root / "harness"
        create_harness_root(harness_root)
        project_module = import_module("scripts.lib.ingest_project")

        def fake_clone(_: str, destination: Path) -> None:
            subprocess.run(
                ["git", "clone", "--quiet", str(project), str(destination)], check=True
            )

        monkeypatch.setattr(project_module, "clone_github_repository", fake_clone)
        entry, created = project_module.ingest_project(
            "https://github.com/example/voice-agent",
            repository_root=harness_root,
        )

        assert created is True
        assert entry["origin"] == "https://github.com/example/voice-agent"
        assert entry["metadata"]["project"] == "voice-agent"
