"""Validate memory schemas, source references, and output-safe claim state."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from scripts.lib.schema import SchemaValidationError, load_yaml, validate_yaml_file

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

SCHEMA_DOCUMENTS = {
    "harness.yaml": "harness.schema.json",
    "sources/manifest.yaml": "source-manifest.schema.json",
    "memory/preferences.yaml": "preferences.schema.json",
    "memory/timeline.yaml": "timeline.schema.json",
    "memory/claims.yaml": "claims.schema.json",
    "memory/evidence.yaml": "evidence.schema.json",
    "memory/conflicts.yaml": "conflicts.schema.json",
}


def duplicate_ids(records: list[dict[str, Any]]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for record in records:
        record_id = str(record.get("id", ""))
        if record_id in seen:
            duplicates.add(record_id)
        seen.add(record_id)
    return duplicates


def validate_source_refs(
    records: list[dict[str, Any]],
    source_ids: set[str],
    label: str,
) -> list[str]:
    errors: list[str] = []
    for record in records:
        for source_ref in record.get("source_refs", []):
            if source_ref not in source_ids:
                errors.append(f"{label} {record.get('id')}: unknown source ref {source_ref}")
    return errors


def validate_repository(repository_root: Path = REPOSITORY_ROOT) -> list[str]:
    errors: list[str] = []
    for relative_path, schema_name in SCHEMA_DOCUMENTS.items():
        document_path = repository_root / relative_path
        try:
            validate_yaml_file(document_path, schema_name, repository_root / "schemas")
        except (OSError, SchemaValidationError) as error:
            errors.extend(str(error).splitlines())

    if errors:
        return errors

    manifest = load_yaml(repository_root / "sources" / "manifest.yaml")
    timeline = load_yaml(repository_root / "memory" / "timeline.yaml")
    claims_document = load_yaml(repository_root / "memory" / "claims.yaml")
    evidence_document = load_yaml(repository_root / "memory" / "evidence.yaml")
    conflicts_document = load_yaml(repository_root / "memory" / "conflicts.yaml")

    sources = manifest.get("sources", [])
    entries = timeline.get("entries", [])
    claims = claims_document.get("claims", [])
    evidence = evidence_document.get("evidence", [])
    conflicts = conflicts_document.get("conflicts", [])
    source_ids = {entry["id"] for entry in sources}
    claim_ids = {claim["id"] for claim in claims}

    for label, records in (
        ("source", sources),
        ("timeline", entries),
        ("claim", claims),
        ("evidence", evidence),
        ("conflict", conflicts),
    ):
        for duplicate in sorted(duplicate_ids(records)):
            errors.append(f"duplicate {label} ID: {duplicate}")

    errors.extend(validate_source_refs(entries, source_ids, "timeline"))
    errors.extend(validate_source_refs(claims, source_ids, "claim"))
    errors.extend(validate_source_refs(evidence, source_ids, "evidence"))

    for claim in claims:
        if claim["status"] == "verified" and not claim["source_refs"]:
            errors.append(f"claim {claim['id']}: verified claim requires source refs")
        if claim["status"] == "conflicted":
            errors.append(f"claim {claim['id']}: conflicted claim is not output-safe")

    for item in evidence:
        for claim_id in item["claim_ids"]:
            if claim_id not in claim_ids:
                errors.append(f"evidence {item['id']}: unknown claim ID {claim_id}")

    for conflict in conflicts:
        if conflict["status"] == "open" and conflict["resolution"] is not None:
            errors.append(f"conflict {conflict['id']}: open conflict cannot have resolution")
        if conflict["status"] == "resolved" and not conflict["resolution"]:
            errors.append(f"conflict {conflict['id']}: resolved conflict needs resolution")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Career Harness memory.")
    parser.add_argument(
        "--root", type=Path, default=REPOSITORY_ROOT, help="Repository root"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_repository(args.root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("memory and source schemas are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
