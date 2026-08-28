from __future__ import annotations

import json
import tempfile
from pathlib import Path

import yaml

from scripts.lib.ingest_github import capture_github
from scripts.lib.ingest_web_snapshot import capture_web_snapshot


def create_repository(root: Path) -> None:
    (root / "sources" / "web").mkdir(parents=True)
    (root / "sources" / "github").mkdir(parents=True)
    (root / "sources" / "manifest.yaml").write_text(
        "version: 1\nsources: []\n", encoding="utf-8"
    )


def test_web_snapshot_is_authentication_free_and_deduplicated() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        create_repository(repository_root)

        first, first_created = capture_web_snapshot(
            url="https://www.linkedin.com/in/example",
            title="LinkedIn Profile",
            text="AI Engineer at Example",
            captured_at="2026-08-27T00:00:00Z",
            repository_root=repository_root,
        )
        second, second_created = capture_web_snapshot(
            url="https://www.linkedin.com/in/example",
            title="LinkedIn Profile",
            text="AI Engineer at Example",
            captured_at="2026-08-27T00:00:00Z",
            repository_root=repository_root,
        )

        assert first_created is True
        assert second_created is False
        assert first == second
        snapshot = (repository_root / first["path"]).read_text(encoding="utf-8")
        assert "Source URL" in snapshot
        assert "cookie" not in snapshot.lower()


def test_github_capture_keeps_only_public_fields() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        create_repository(repository_root)

        profile = {
            "login": "example",
            "name": "Example User",
            "bio": "AI Engineer",
            "email": "private@example.com",
            "public_repos": 2,
        }
        repositories = [
            {
                "name": "public-repo",
                "full_name": "example/public-repo",
                "html_url": "https://github.com/example/public-repo",
                "private": False,
                "language": "Python",
            },
            {"name": "private-repo", "private": True},
        ]

        def runner(command: list[str]) -> str:
            if command[-1] == "users/example":
                return json.dumps(profile)
            return json.dumps(repositories)

        entry, created = capture_github(
            "example", repository_root=repository_root, runner=runner
        )

        assert created is True
        snapshot = json.loads((repository_root / entry["path"]).read_text(encoding="utf-8"))
        assert snapshot["profile"]["login"] == "example"
        assert "email" not in snapshot["profile"]
        assert [repository["name"] for repository in snapshot["repositories"]] == [
            "public-repo"
        ]
        manifest = yaml.safe_load(
            (repository_root / "sources" / "manifest.yaml").read_text(encoding="utf-8")
        )
        assert manifest["sources"][0]["origin"] == "https://github.com/example"
