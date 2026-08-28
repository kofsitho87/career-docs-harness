from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import yaml

from scripts.lib.validate_memory import validate_repository

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def create_repository(root: Path) -> None:
    shutil.copytree(PROJECT_ROOT / "schemas", root / "schemas")
    shutil.copy(PROJECT_ROOT / "harness.yaml", root / "harness.yaml")
    (root / "sources").mkdir()
    (root / "memory").mkdir()
    for relative_path in (
        "sources/manifest.yaml",
        "memory/preferences.yaml",
        "memory/timeline.yaml",
        "memory/claims.yaml",
        "memory/evidence.yaml",
        "memory/conflicts.yaml",
    ):
        source_path = PROJECT_ROOT / relative_path
        target_path = root / relative_path
        shutil.copy(source_path, target_path)


def test_empty_memory_skeleton_is_valid() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        create_repository(repository_root)

        assert validate_repository(repository_root) == []


def test_unknown_source_reference_is_rejected() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        create_repository(repository_root)
        claims_path = repository_root / "memory" / "claims.yaml"
        claims = yaml.safe_load(claims_path.read_text(encoding="utf-8"))
        claims["claims"].append(
            {
                "id": "claim-example-impact",
                "statement": "성과를 만들었다",
                "project_id": None,
                "status": "verified",
                "source_refs": ["source-missing-aaaaaaaaaaaa"],
                "visibility": "public",
                "allowed_outputs": ["resume"],
                "user_edited": False,
                "last_updated": None,
            }
        )
        claims_path.write_text(
            yaml.safe_dump(claims, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )

        errors = validate_repository(repository_root)

        assert "claim claim-example-impact: unknown source ref source-missing-aaaaaaaaaaaa" in errors
