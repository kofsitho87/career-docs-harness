from __future__ import annotations

import tempfile
from pathlib import Path

import yaml

from scripts.lib.record_interview import record_interview


def test_interview_answer_becomes_verified_deduplicated_source() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        (repository_root / "sources" / "interviews").mkdir(parents=True)
        manifest_path = repository_root / "sources" / "manifest.yaml"
        manifest_path.write_text("version: 1\nsources: []\n", encoding="utf-8")

        first, first_created = record_interview(
            topic="목표 직무",
            question="어떤 역할을 원하나요?",
            answer="AI Product Engineer를 원합니다.",
            recorded_at="2026-08-27T00:00:00Z",
            repository_root=repository_root,
        )
        second, second_created = record_interview(
            topic="목표 직무",
            question="어떤 역할을 원하나요?",
            answer="AI Product Engineer를 원합니다.",
            recorded_at="2026-08-27T00:00:00Z",
            repository_root=repository_root,
        )

        assert first_created is True
        assert second_created is False
        assert first == second
        assert first["type"] == "interview"
        assert first["status"] == "verified"
        assert (repository_root / first["path"]).is_file()
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        assert len(manifest["sources"]) == 1
