"""Conflict-preserving merge helpers for provenance-backed memory records."""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from scripts.lib.source_manifest import utc_now

STATUS_PRIORITY = {
    "unverified": 0,
    "inferred": 1,
    "verified": 2,
    "conflicted": -1,
}

CONTROL_FIELDS = {"id", "status", "source_refs", "user_edited", "last_updated"}


def unique_strings(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def stronger_status(left: str, right: str) -> str:
    if "conflicted" in {left, right}:
        return "conflicted"
    return left if STATUS_PRIORITY.get(left, -1) >= STATUS_PRIORITY.get(right, -1) else right


def conflict_id(record_id: str, field: str, left: Any, right: Any) -> str:
    payload = json.dumps([record_id, field, left, right], ensure_ascii=False, sort_keys=True)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    safe_field = "".join(character if character.isalnum() else "-" for character in field.lower())
    safe_field = "-".join(part for part in safe_field.split("-") if part)
    return f"conflict-{safe_field or 'field'}-{digest}"


def build_conflict(
    *,
    record_id: str,
    field: str,
    existing_value: Any,
    incoming_value: Any,
    existing_sources: list[str],
    incoming_sources: list[str],
    resolution: str | None,
) -> dict[str, Any]:
    return {
        "id": conflict_id(record_id, field, existing_value, incoming_value),
        "record_id": record_id,
        "field": field,
        "values": [
            {"value": existing_value, "source_refs": unique_strings(existing_sources)},
            {"value": incoming_value, "source_refs": unique_strings(incoming_sources)},
        ],
        "status": "resolved" if resolution else "open",
        "resolution": resolution,
        "created_at": utc_now(),
    }


def merge_record(
    existing: dict[str, Any], incoming: dict[str, Any]
) -> tuple[dict[str, Any], list[dict[str, Any]], list[str]]:
    """Merge one record while preserving conflicts and direct user edits."""
    if existing.get("id") != incoming.get("id"):
        raise ValueError("cannot merge records with different IDs")

    merged = copy.deepcopy(existing)
    conflicts: list[dict[str, Any]] = []
    changes: list[str] = []
    record_id = str(existing["id"])
    existing_sources = list(existing.get("source_refs", []))
    incoming_sources = list(incoming.get("source_refs", []))

    for field, incoming_value in incoming.items():
        if field in CONTROL_FIELDS:
            continue
        existing_value = merged.get(field)
        if is_empty(existing_value):
            if not is_empty(incoming_value):
                merged[field] = copy.deepcopy(incoming_value)
                changes.append(f"{record_id}.{field}: added")
            continue
        if is_empty(incoming_value):
            continue
        if existing_value == incoming_value:
            continue

        if incoming.get("user_edited", False):
            merged[field] = copy.deepcopy(incoming_value)
            merged["user_edited"] = True
            conflicts.append(
                build_conflict(
                    record_id=record_id,
                    field=field,
                    existing_value=existing_value,
                    incoming_value=incoming_value,
                    existing_sources=existing_sources,
                    incoming_sources=incoming_sources,
                    resolution="incoming_user_value_applied",
                )
            )
            changes.append(f"{record_id}.{field}: user value applied")
            continue

        if existing.get("user_edited", False):
            conflicts.append(
                build_conflict(
                    record_id=record_id,
                    field=field,
                    existing_value=existing_value,
                    incoming_value=incoming_value,
                    existing_sources=existing_sources,
                    incoming_sources=incoming_sources,
                    resolution="existing_user_value_preserved",
                )
            )
            changes.append(f"{record_id}.{field}: existing user value preserved")
            continue

        conflicts.append(
            build_conflict(
                record_id=record_id,
                field=field,
                existing_value=existing_value,
                incoming_value=incoming_value,
                existing_sources=existing_sources,
                incoming_sources=incoming_sources,
                resolution=None,
            )
        )
        merged["status"] = "conflicted"
        changes.append(f"{record_id}.{field}: conflict recorded")

    merged["source_refs"] = unique_strings(existing_sources + incoming_sources)
    if merged.get("status") != "conflicted":
        merged["status"] = stronger_status(
            str(existing.get("status", "unverified")),
            str(incoming.get("status", "unverified")),
        )
    merged["user_edited"] = bool(
        existing.get("user_edited", False) or incoming.get("user_edited", False)
    )
    merged["last_updated"] = utc_now()
    return merged, conflicts, changes


def merge_collection(
    existing_records: list[dict[str, Any]], incoming_records: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    """Merge collections by stable record ID."""
    records_by_id = {record["id"]: copy.deepcopy(record) for record in existing_records}
    conflicts: list[dict[str, Any]] = []
    changes: list[str] = []

    for incoming in incoming_records:
        record_id = incoming["id"]
        if record_id not in records_by_id:
            records_by_id[record_id] = copy.deepcopy(incoming)
            records_by_id[record_id].setdefault("last_updated", utc_now())
            changes.append(f"{record_id}: added")
            continue
        merged, record_conflicts, record_changes = merge_record(
            records_by_id[record_id], incoming
        )
        records_by_id[record_id] = merged
        conflicts.extend(record_conflicts)
        changes.extend(record_changes)

    return (
        [records_by_id[record_id] for record_id in sorted(records_by_id)],
        conflicts,
        changes,
    )


def append_changelog(changelog_path: Path, changes: list[str]) -> None:
    if not changes:
        return
    changelog_path.parent.mkdir(parents=True, exist_ok=True)
    if not changelog_path.exists():
        changelog_path.write_text("# Memory Changelog\n", encoding="utf-8")
    timestamp = utc_now()
    with changelog_path.open("a", encoding="utf-8") as stream:
        stream.write(f"\n## {timestamp}\n\n")
        for change in changes:
            stream.write(f"- {change}\n")
