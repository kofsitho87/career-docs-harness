"""Store an authentication-free web text snapshot as an immutable source."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

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


def capture_web_snapshot(
    *,
    url: str,
    title: str,
    text: str,
    repository_root: Path = REPOSITORY_ROOT,
    captured_at: str | None = None,
) -> tuple[dict, bool]:
    parsed_url = urlparse(url)
    if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
        raise ValueError("web snapshot URL must use http or https")
    if not text.strip():
        raise ValueError("web snapshot text cannot be empty")

    captured_at = normalize_datetime(captured_at)
    web_root = repository_root / "sources" / "web"
    web_root.mkdir(parents=True, exist_ok=True)
    date_prefix = captured_at[:10]
    content = (
        f"# {title}\n\n"
        f"- Source URL: {url}\n"
        f"- Captured at: {captured_at}\n\n"
        "---\n\n"
        f"{text.strip()}\n"
    )
    content_bytes = content.encode("utf-8")
    digest = sha256_bytes(content_bytes)
    filename = f"{date_prefix}-{slugify(title)}-{digest[:12]}.md"
    snapshot_path = web_root / filename
    if not snapshot_path.exists():
        snapshot_path.write_bytes(content_bytes)
    entry_id = source_id(title, digest)
    relative_path = repository_path(snapshot_path, repository_root)
    return register_source(
        repository_root / "sources" / "manifest.yaml",
        entry_id=entry_id,
        source_type="web_snapshot",
        path=relative_path,
        origin=url,
        digest=digest,
        extracted_text_path=relative_path,
        captured_at=captured_at,
        metadata={"title": title, "host": parsed_url.netloc},
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Register a browser text snapshot.")
    parser.add_argument("--url", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--input", required=True, type=Path, help="Plain-text snapshot file")
    parser.add_argument("--captured-at")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entry, created = capture_web_snapshot(
        url=args.url,
        title=args.title,
        text=args.input.read_text(encoding="utf-8"),
        captured_at=args.captured_at,
    )
    action = "captured" if created else "already registered"
    print(f"{action} {entry['id']}: {entry['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
