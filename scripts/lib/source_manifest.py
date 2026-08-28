"""Source manifest helpers with deterministic IDs and content hashes."""

from __future__ import annotations

import hashlib
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from scripts.lib.schema import load_schema, load_yaml, validate_data, write_yaml


def utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def source_id(label: str, digest: str) -> str:
    return f"source-{slugify(label)}-{digest[:12]}"


def repository_path(path: Path, repository_root: Path) -> str:
    return path.resolve().relative_to(repository_root.resolve()).as_posix()


def load_manifest(manifest_path: Path) -> dict[str, Any]:
    if not manifest_path.exists():
        return {"version": 1, "sources": []}
    data = load_yaml(manifest_path)
    return data or {"version": 1, "sources": []}


def find_source_by_hash(
    manifest: dict[str, Any], digest: str, source_type: str | None = None
) -> dict[str, Any] | None:
    for entry in manifest.get("sources", []):
        if entry.get("sha256") != digest:
            continue
        if source_type is not None and entry.get("type") != source_type:
            continue
        return entry
    return None


def register_source(
    manifest_path: Path,
    *,
    entry_id: str,
    source_type: str,
    path: str,
    origin: str,
    digest: str,
    extracted_text_path: str | None,
    captured_at: str | None = None,
    status: str = "verified",
    metadata: dict[str, Any] | None = None,
    schema_root: Path | None = None,
) -> tuple[dict[str, Any], bool]:
    """Register a source and return (entry, created). Exact hashes are deduplicated."""
    manifest = load_manifest(manifest_path)
    existing = find_source_by_hash(manifest, digest, source_type)
    if existing is not None:
        return existing, False

    entry = {
        "id": entry_id,
        "type": source_type,
        "path": path,
        "origin": origin,
        "sha256": digest,
        "imported_at": utc_now(),
        "captured_at": captured_at,
        "extracted_text_path": extracted_text_path,
        "status": status,
        "metadata": metadata or {},
    }
    manifest.setdefault("sources", []).append(entry)
    manifest["sources"].sort(key=lambda item: item["id"])

    if schema_root is None:
        schema = load_schema("source-manifest.schema.json")
    else:
        schema = load_schema("source-manifest.schema.json", schema_root)
    validate_data(manifest, schema, str(manifest_path))
    write_yaml(manifest_path, manifest)
    return entry, True
