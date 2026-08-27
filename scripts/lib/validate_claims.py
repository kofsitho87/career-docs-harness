"""Validate claim IDs embedded in career outputs against memory claims."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

CLAIM_COMMENT = re.compile(r"claims:\s*([a-z0-9,\-\s]+)", re.IGNORECASE)
CLAIM_ATTRIBUTE = re.compile(r'data-claim-ids=["\']([^"\']*)["\']', re.IGNORECASE)


def extract_claim_ids(content: str) -> set[str]:
    identifiers: set[str] = set()
    for pattern in (CLAIM_COMMENT, CLAIM_ATTRIBUTE):
        for match in pattern.findall(content):
            identifiers.update(value.strip() for value in match.split(",") if value.strip())
    return identifiers


def validate_claims(paths: list[Path], memory_path: Path) -> list[str]:
    document = yaml.safe_load(memory_path.read_text(encoding="utf-8"))
    claims = {claim["id"]: claim for claim in document.get("claims", [])}
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            continue
        for claim_id in sorted(extract_claim_ids(path.read_text(encoding="utf-8"))):
            claim = claims.get(claim_id)
            if claim is None:
                errors.append(f"{path}: unknown claim ID {claim_id}")
                continue
            if claim["status"] != "verified":
                errors.append(f"{path}: claim {claim_id} is {claim['status']}, not verified")
            if not claim["source_refs"]:
                errors.append(f"{path}: claim {claim_id} has no source refs")
            if claim["visibility"] != "public":
                errors.append(f"{path}: claim {claim_id} is not public")
    return errors
