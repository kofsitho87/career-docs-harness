from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
WORK_DIR = ROOT / "tmp" / "pdfs" / "wanted-portfolio"
SLIDES_DIR = WORK_DIR / "slides"
JPEG_DIR = WORK_DIR / "jpeg"
OUTPUT_PDF = ROOT / "output" / "pdf" / "heewung-song-ai-product-engineer-portfolio.pdf"
CONTACT_SHEET = WORK_DIR / "contact-sheet.jpg"

PAGE_WIDTH = 16 * 72
PAGE_HEIGHT = 9 * 72
EXPECTED_SLIDES = 28
CAPTURE_WIDTH = 1920
CAPTURE_HEIGHT = 1080

# Bounding boxes measured from the final 1920 x 1080 HTML slide.
# Coordinates use the browser's top-left origin and are converted to PDF points below.
CONTACT_LINKS = (
    ("mailto:kofsitho@naver.com", (376, 697.890625, 210.28125, 46.46875)),
    ("https://github.com/kofsitho87", (602.28125, 697.890625, 117.28125, 46.46875)),
    ("https://www.linkedin.com/in/kofsitho", (735.5625, 697.890625, 129.640625, 46.46875)),
    ("https://kofsitho87.github.io/my-tech-blog", (881.203125, 697.890625, 135.921875, 46.46875)),
    ("https://medium.com/@kofsitho", (1033.125, 697.890625, 124.453125, 46.46875)),
)


def load_slide_paths() -> list[Path]:
    paths = sorted(SLIDES_DIR.glob("slide-*.png"))
    if len(paths) != EXPECTED_SLIDES:
        raise RuntimeError(f"Expected {EXPECTED_SLIDES} slides, found {len(paths)}")
    for path in paths:
        with Image.open(path) as image:
            if image.size != (CAPTURE_WIDTH, CAPTURE_HEIGHT):
                raise RuntimeError(f"Unexpected slide size for {path.name}: {image.size}")
    return paths


def build_contact_sheet(paths: list[Path]) -> None:
    columns = 4
    thumb_width = 384
    thumb_height = 216
    label_height = 28
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * thumb_width, rows * (thumb_height + label_height)), "#101512")
    draw = ImageDraw.Draw(sheet)

    for index, path in enumerate(paths):
        row, column = divmod(index, columns)
        x = column * thumb_width
        y = row * (thumb_height + label_height)
        with Image.open(path) as image:
            thumb = image.convert("RGB").resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            sheet.paste(thumb, (x, y))
        draw.text((x + 10, y + thumb_height + 6), f"Slide {index + 1:02d}", fill="#d8e5dc")

    sheet.save(CONTACT_SHEET, "JPEG", quality=88, optimize=True)


def browser_rect_to_pdf(rect: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
    x, y, width, height = rect
    scale_x = PAGE_WIDTH / CAPTURE_WIDTH
    scale_y = PAGE_HEIGHT / CAPTURE_HEIGHT
    return (
        x * scale_x,
        PAGE_HEIGHT - (y + height) * scale_y,
        (x + width) * scale_x,
        PAGE_HEIGHT - y * scale_y,
    )


def add_contact_links(pdf: canvas.Canvas) -> None:
    for url, browser_rect in CONTACT_LINKS:
        pdf.linkURL(url, browser_rect_to_pdf(browser_rect), relative=0, thickness=0)


def build_pdf(paths: list[Path]) -> None:
    JPEG_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    pdf = canvas.Canvas(str(OUTPUT_PDF), pagesize=(PAGE_WIDTH, PAGE_HEIGHT), pageCompression=1)
    pdf.setTitle("Song Heewung - AI Product Engineer Portfolio")
    pdf.setAuthor("Song Heewung")
    pdf.setSubject("AI Product Engineering Portfolio")
    pdf.setCreator("Codex PDF workflow")

    for index, path in enumerate(paths, start=1):
        jpeg_path = JPEG_DIR / f"slide-{index:02d}.jpg"
        with Image.open(path) as image:
            image.convert("RGB").save(jpeg_path, "JPEG", quality=88, optimize=True, progressive=True)
        pdf.drawImage(ImageReader(str(jpeg_path)), 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT)
        if index == EXPECTED_SLIDES:
            add_contact_links(pdf)
        pdf.showPage()

    pdf.save()


def validate_pdf() -> None:
    reader = PdfReader(str(OUTPUT_PDF))
    if len(reader.pages) != EXPECTED_SLIDES:
        raise RuntimeError(f"Expected {EXPECTED_SLIDES} PDF pages, found {len(reader.pages)}")
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - PAGE_WIDTH) > 0.1 or abs(height - PAGE_HEIGHT) > 0.1:
            raise RuntimeError(f"Unexpected PDF page size on page {index}: {width} x {height}")

    annotations = reader.pages[-1].get("/Annots") or []
    link_annotations = []
    for annotation_ref in annotations:
        annotation = annotation_ref.get_object()
        if annotation.get("/Subtype") != "/Link":
            continue
        action = annotation.get("/A")
        if action and action.get("/S") == "/URI":
            link_annotations.append(str(action.get("/URI")))

    expected_urls = [url for url, _ in CONTACT_LINKS]
    if link_annotations != expected_urls:
        raise RuntimeError(f"Unexpected final-page links: {link_annotations}")


def main() -> None:
    paths = load_slide_paths()
    build_contact_sheet(paths)
    build_pdf(paths)
    validate_pdf()
    print(OUTPUT_PDF)


if __name__ == "__main__":
    main()
