"""Validate local image assets referenced by Markdown and HTML outputs."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup

MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def validate_assets(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        references: list[tuple[str, str]] = []
        if path.suffix.lower() in {".html", ".htm"}:
            soup = BeautifulSoup(content, "html.parser")
            for image in soup.find_all("img"):
                source = str(image.get("src", ""))
                references.append((source, str(image.get("alt", ""))))
                if not image.get("alt"):
                    errors.append(f"{path}: image missing alt text: {source}")
        else:
            references.extend((source, "markdown") for source in MARKDOWN_IMAGE.findall(content))

        for source, _ in references:
            parsed = urlparse(source)
            if parsed.scheme or source.startswith("//"):
                continue
            target = unquote(source.split("#", 1)[0].split("?", 1)[0])
            if target and not (path.parent / target).resolve().is_file():
                errors.append(f"{path}: missing image asset {source}")
    return errors
