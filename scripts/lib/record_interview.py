"""Record a user interview answer as immutable, provenance-ready source text."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

from scripts.lib.source_manifest import (
    register_source,
    repository_path,
    sha256_bytes,
    slugify,
    source_id,
)

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def normalize_datetime(value: str | None) -> str:
    if value is None:
        return datetime.now(UTC).isoformat().replace("+00:00", "Z")
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC).isoformat().replace("+00:00", "Z")


def record_interview(
    *,
    topic: str,
    question: str,
    answer: str,
    repository_root: Path = REPOSITORY_ROOT,
    recorded_at: str | None = None,
) -> tuple[dict, bool]:
    if not topic.strip() or not question.strip() or not answer.strip():
        raise ValueError("topic, question, and answer are required")

    recorded_at = normalize_datetime(recorded_at)
    content = (
        f"# Interview: {topic.strip()}\n\n"
        f"- Recorded at: {recorded_at}\n\n"
        f"## Question\n\n{question.strip()}\n\n"
        f"## Answer\n\n{answer.strip()}\n"
    )
    content_bytes = content.encode("utf-8")
    digest = sha256_bytes(content_bytes)
    interview_root = repository_root / "sources" / "interviews"
    interview_root.mkdir(parents=True, exist_ok=True)
    snapshot_path = interview_root / f"{slugify(topic)}-{digest[:12]}.md"
    if not snapshot_path.exists():
        snapshot_path.write_bytes(content_bytes)

    relative_path = repository_path(snapshot_path, repository_root)
    entry_id = source_id(f"interview-{topic}", digest)
    return register_source(
        repository_root / "sources" / "manifest.yaml",
        entry_id=entry_id,
        source_type="interview",
        path=relative_path,
        origin="user_interview",
        digest=digest,
        extracted_text_path=relative_path,
        captured_at=recorded_at,
        status="verified",
        metadata={"topic": topic.strip()},
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Record a user interview answer.")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--question", required=True)
    parser.add_argument("--answer", required=True)
    parser.add_argument("--recorded-at")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entry, created = record_interview(
        topic=args.topic,
        question=args.question,
        answer=args.answer,
        recorded_at=args.recorded_at,
    )
    action = "recorded" if created else "already registered"
    print(f"{action} {entry['id']}: {entry['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
