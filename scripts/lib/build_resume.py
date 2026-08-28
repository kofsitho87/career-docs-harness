"""Render a Markdown resume to polished HTML and text-preserving A4 PDF."""

from __future__ import annotations

import argparse
import html
from pathlib import Path
from typing import Any

import markdown
import yaml
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CSS = REPOSITORY_ROOT / "templates" / "resume" / "resume.css"

A4_WIDTH_PT = 595.28
A4_HEIGHT_PT = 841.89


class ResumeBuildError(RuntimeError):
    """Raised when resume rendering or validation fails."""


def load_config(repository_root: Path = REPOSITORY_ROOT) -> dict[str, Any]:
    return yaml.safe_load((repository_root / "harness.yaml").read_text(encoding="utf-8"))


def markdown_to_html(markdown_text: str, css_text: str, title: str) -> str:
    body = markdown.markdown(
        markdown_text,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html5",
    )
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>{css_text}</style>
</head>
<body>
{body}
</body>
</html>
"""


def validate_pdf(pdf_path: Path, *, maximum_pages: int = 3) -> dict[str, Any]:
    reader = PdfReader(str(pdf_path))
    if not reader.pages:
        raise ResumeBuildError("resume PDF has no pages")
    if len(reader.pages) > maximum_pages:
        raise ResumeBuildError(
            f"resume PDF has {len(reader.pages)} pages; maximum is {maximum_pages}"
        )

    links: list[str] = []
    extracted_text = []
    for page_number, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - A4_WIDTH_PT) > 1 or abs(height - A4_HEIGHT_PT) > 1:
            raise ResumeBuildError(
                f"page {page_number} is not A4: {width:.2f} x {height:.2f}pt"
            )
        extracted_text.append(page.extract_text() or "")
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            if action and action.get("/S") == "/URI":
                links.append(str(action.get("/URI")))

    text = "\n".join(extracted_text).strip()
    if len(text) < 20:
        raise ResumeBuildError("resume PDF text extraction is unexpectedly empty")
    return {"pages": len(reader.pages), "links": sorted(set(links)), "text_chars": len(text)}


def build_resume(
    markdown_path: Path,
    pdf_path: Path,
    *,
    repository_root: Path = REPOSITORY_ROOT,
    css_path: Path | None = None,
    html_path: Path | None = None,
) -> dict[str, Any]:
    markdown_path = markdown_path.resolve()
    pdf_path = pdf_path.resolve()
    if not markdown_path.is_file():
        raise ResumeBuildError(f"resume Markdown not found: {markdown_path}")

    css_path = (css_path or repository_root / "templates" / "resume" / "resume.css").resolve()
    html_path = (
        html_path or repository_root / "resume" / ".build" / "master.html"
    ).resolve()
    html_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    rendered_html = markdown_to_html(
        markdown_path.read_text(encoding="utf-8"),
        css_path.read_text(encoding="utf-8"),
        markdown_path.stem,
    )
    html_path.write_text(rendered_html, encoding="utf-8")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 1600})
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        horizontal_overflow = page.evaluate(
            """
            () => Array.from(document.body.querySelectorAll('*')).filter((element) => {
              const rect = element.getBoundingClientRect();
              return rect.left < -1 || rect.right > document.documentElement.clientWidth + 1;
            }).map((element) => element.tagName + ':' + (element.textContent || '').slice(0, 40))
            """
        )
        if horizontal_overflow:
            browser.close()
            raise ResumeBuildError(
                "resume HTML has horizontal overflow: " + ", ".join(horizontal_overflow[:5])
            )
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        browser.close()

    result = validate_pdf(pdf_path)
    result["html"] = str(html_path)
    result["pdf"] = str(pdf_path)
    return result


def parse_args() -> argparse.Namespace:
    config = load_config()
    parser = argparse.ArgumentParser(description="Build a Markdown resume as A4 PDF.")
    parser.add_argument(
        "--input",
        type=Path,
        default=REPOSITORY_ROOT / config["resume"]["master"],
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPOSITORY_ROOT / config["resume"]["pdf_output"],
    )
    parser.add_argument("--html-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = build_resume(args.input, args.output, html_path=args.html_output)
    print(f"built {result['pdf']}")
    print(f"  pages {result['pages']} · links {len(result['links'])} · text {result['text_chars']} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
