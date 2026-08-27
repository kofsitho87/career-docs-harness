"""Scan public outputs for credentials and non-allowlisted contact information."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[ps]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{20,}", re.IGNORECASE),
}
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_PATTERN = re.compile(r"(?<!\d)(?:\+?82[- ]?)?0?1[016789][- ]?\d{3,4}[- ]?\d{4}(?!\d)")


def load_allowlist(path: Path) -> dict[str, set[str]]:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    return {
        "emails": set(document.get("emails", [])),
        "phones": set(document.get("phones", [])),
        "urls": set(document.get("urls", [])),
    }


def scan_sensitive_info(paths: list[Path], allowlist_path: Path) -> list[str]:
    allowlist = load_allowlist(allowlist_path)
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"{path}: possible {label}")
        for email in sorted(set(EMAIL_PATTERN.findall(content)) - allowlist["emails"]):
            errors.append(f"{path}: email is not allowlisted: {email}")
        for phone in sorted(set(PHONE_PATTERN.findall(content)) - allowlist["phones"]):
            errors.append(f"{path}: phone is not allowlisted: {phone}")
    return errors
