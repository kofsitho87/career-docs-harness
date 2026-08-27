"""현재 대표 포트폴리오 HTML을 16:9 벡터 PDF로 빌드한다.

v4 HTML의 인쇄 CSS(`@media print`)와 Chromium 인쇄 경로를 사용해
텍스트 선택과 외부 링크가 유지되는 PDF를 만든다.

실행:
    uv run --with playwright --with pypdf python3 scripts/build_portfolio_pdf.py
"""

from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "portfolio" / "html" / "heewung-song-portfolio.html"
OUTPUT_PDF = ROOT / "portfolio" / "pdf" / "heewung-song-portfolio-v4.pdf"

EXPECTED_SLIDES = 30
PAGE_WIDTH_PT = 16 * 72
PAGE_HEIGHT_PT = 9 * 72
VIEWPORT = {"width": 1920, "height": 1080}


def render() -> None:
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as play:
        browser = play.chromium.launch()
        # 덱은 저장된 테마가 없으면 prefers-color-scheme을 따라간다(4196행).
        # Chromium 기본값이 light라 그대로 두면 라이트 테마로 인쇄된다.
        page = browser.new_page(viewport=VIEWPORT, color_scheme="dark")
        page.goto(SOURCE.as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.evaluate(
            "document.documentElement.classList.remove('theme-light');"
            "document.documentElement.classList.add('theme-dark');"
        )
        # 인쇄 CSS가 모든 슬라이드를 펼치지만, 카운터 애니메이션은 화면에서만 돌기 때문에
        # 최종 수치가 찍히도록 data-count 요소를 목표값으로 확정한다.
        page.evaluate(
            """
            document.querySelectorAll('[data-count]').forEach(function (el) {
              var target = parseFloat(el.dataset.count);
              var prefix = el.dataset.prefix || '';
              var suffix = el.dataset.suffix || '';
              el.textContent = prefix + Math.round(target).toLocaleString() + suffix;
            });
            document.querySelectorAll('.an').forEach(function (el) { el.style.animation = 'none'; });
            """
        )
        page.emulate_media(media="print")
        page.pdf(
            path=str(OUTPUT_PDF),
            width="16in",
            height="9in",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=False,
        )
        browser.close()


def validate() -> None:
    reader = PdfReader(str(OUTPUT_PDF))
    if len(reader.pages) != EXPECTED_SLIDES:
        raise RuntimeError(f"슬라이드 {EXPECTED_SLIDES}장을 기대했지만 {len(reader.pages)}쪽이 나왔다")

    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - PAGE_WIDTH_PT) > 1 or abs(height - PAGE_HEIGHT_PT) > 1:
            raise RuntimeError(f"{index}쪽 크기가 어긋난다: {width} x {height}")

    urls = []
    for page in reader.pages:
        for ref in page.get("/Annots") or []:
            annotation = ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A")
            if action and action.get("/S") == "/URI":
                urls.append(str(action.get("/URI")))

    text = (reader.pages[0].extract_text() or "").strip()
    print(f"{OUTPUT_PDF}")
    print(f"  쪽수 {len(reader.pages)} · {PAGE_WIDTH_PT}x{PAGE_HEIGHT_PT}pt (16:9)")
    print(f"  링크 {len(urls)}개: {sorted(set(urls))}")
    print(f"  1쪽 텍스트 추출 {len(text)}자 (0이면 이미지로 굳은 것)")


def main() -> None:
    render()
    validate()


if __name__ == "__main__":
    main()
