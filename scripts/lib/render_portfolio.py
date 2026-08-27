"""Render slide HTML to PNGs, a contact sheet, and a verified 16:9 PDF."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

from scripts.lib.create_contact_sheet import create_contact_sheet
from scripts.lib.validate_slides import validate_portfolio_html

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PAGE_WIDTH_PT = 16 * 72
PAGE_HEIGHT_PT = 9 * 72


class PortfolioRenderError(RuntimeError):
    """Raised when slide visual or PDF validation fails."""


def validate_pdf(pdf_path: Path, expected_slides: int) -> dict[str, Any]:
    reader = PdfReader(str(pdf_path))
    if len(reader.pages) != expected_slides:
        raise PortfolioRenderError(
            f"portfolio PDF has {len(reader.pages)} pages; expected {expected_slides}"
        )
    links: list[str] = []
    text_chars = 0
    for page_number, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - PAGE_WIDTH_PT) > 1 or abs(height - PAGE_HEIGHT_PT) > 1:
            raise PortfolioRenderError(
                f"page {page_number} is not 16:9: {width:.2f} x {height:.2f}pt"
            )
        text_chars += len((page.extract_text() or "").strip())
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            if action and action.get("/S") == "/URI":
                links.append(str(action.get("/URI")))
    if text_chars < expected_slides * 10:
        raise PortfolioRenderError("portfolio PDF text extraction is unexpectedly empty")
    return {"pages": len(reader.pages), "links": sorted(set(links)), "text_chars": text_chars}


def render_portfolio(
    html_path: Path,
    *,
    repository_root: Path = REPOSITORY_ROOT,
    pdf_path: Path | None = None,
    render_root: Path | None = None,
    check_memory_ids: bool = True,
) -> dict[str, Any]:
    errors = validate_portfolio_html(
        html_path, repository_root=repository_root, check_memory_ids=check_memory_ids
    )
    if errors:
        raise PortfolioRenderError("\n".join(errors))

    config = yaml.safe_load(
        (repository_root / "harness.yaml").read_text(encoding="utf-8")
    )
    pdf_path = pdf_path or repository_root / config["portfolio"]["pdf_output"]
    render_root = render_root or repository_root / "tmp" / "pdfs" / "portfolio"
    slides_root = render_root / "slides"
    slides_root.mkdir(parents=True, exist_ok=True)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    slide_paths: list[Path] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        slides = page.locator(".slide")
        count = slides.count()
        overflow = page.evaluate(
            """
            () => Array.from(document.querySelectorAll('.slide')).map((slide, index) => ({
              index: index + 1,
              horizontal: slide.scrollWidth > slide.clientWidth + 1,
              vertical: slide.scrollHeight > slide.clientHeight + 1,
            })).filter((result) => result.horizontal || result.vertical)
            """
        )
        if overflow:
            browser.close()
            raise PortfolioRenderError(f"slide overflow detected: {overflow}")
        for index in range(count):
            slide_path = slides_root / f"slide-{index + 1:02d}.png"
            slides.nth(index).screenshot(path=str(slide_path))
            slide_paths.append(slide_path)
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf_path),
            width="16in",
            height="9in",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        browser.close()

    contact_sheet = create_contact_sheet(slide_paths, render_root / "contact-sheet.jpg")
    pdf_result = validate_pdf(pdf_path, len(slide_paths))
    return {
        **pdf_result,
        "pdf": str(pdf_path),
        "slides": [str(path) for path in slide_paths],
        "contact_sheet": str(contact_sheet),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render and verify a slide portfolio.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--render-root", type=Path)
    parser.add_argument("--skip-memory-ids", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = render_portfolio(
        args.input,
        pdf_path=args.output,
        render_root=args.render_root,
        check_memory_ids=not args.skip_memory_ids,
    )
    print(f"rendered {result['pdf']}")
    print(f"  pages {result['pages']} · text {result['text_chars']} chars")
    print(f"  contact sheet {result['contact_sheet']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
