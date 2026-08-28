"""Build a deployable static portfolio directory from configured HTML and local assets."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup


def build_site(source_html: Path, output_root: Path) -> dict[str, int | str]:
    if not source_html.is_file():
        raise FileNotFoundError(f"portfolio HTML not found: {source_html}")
    soup = BeautifulSoup(source_html.read_text(encoding="utf-8"), "html.parser")
    assets: dict[str, Path] = {}
    for image in soup.find_all("img", src=True):
        source = str(image["src"])
        if source.startswith(("http://", "https://", "data:", "//")):
            continue
        source_path = (source_html.parent / source).resolve()
        target_name = source_path.name
        if target_name in assets and assets[target_name] != source_path:
            raise ValueError(f"portfolio asset filename collision: {target_name}")
        assets[target_name] = source_path
        image["src"] = f"./assets/{target_name}"

    output_root.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="career-harness-site-") as temporary_directory:
        staging = Path(temporary_directory) / "dist"
        staging.mkdir()
        (staging / "index.html").write_text(str(soup), encoding="utf-8")
        copied = 0
        for target_name, source_path in sorted(assets.items()):
            if not source_path.is_file():
                raise FileNotFoundError(f"portfolio asset not found: {source_path}")
            target_path = staging / "assets" / target_name
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, target_path)
            copied += 1
        if output_root.exists():
            shutil.rmtree(output_root)
        shutil.copytree(staging, output_root)
    return {"output": str(output_root), "assets": copied}
