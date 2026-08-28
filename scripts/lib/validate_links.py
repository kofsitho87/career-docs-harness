"""Validate local Markdown and HTML links without making network requests."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def is_local_reference(value: str) -> bool:
    parsed = urlparse(value)
    return not parsed.scheme and not value.startswith(("#", "//"))


def local_references(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".html", ".htm"}:
        soup = BeautifulSoup(content, "html.parser")
        return [
            str(element.get(attribute))
            for element in soup.find_all(True)
            for attribute in ("href", "src")
            if element.get(attribute) and is_local_reference(str(element.get(attribute)))
        ]
    return [value for value in MARKDOWN_LINK.findall(content) if is_local_reference(value)]


def validate_links(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            continue
        for reference in local_references(path):
            target = unquote(reference.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            if not (path.parent / target).resolve().exists():
                errors.append(f"{path}: broken local link {reference}")
    return errors
