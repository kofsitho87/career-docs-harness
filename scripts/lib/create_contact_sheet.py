"""Create a labeled contact sheet from rendered 16:9 slide images."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def create_contact_sheet(
    slide_paths: list[Path], output_path: Path, *, columns: int = 4
) -> Path:
    if not slide_paths:
        raise ValueError("no slide images provided")
    thumb_width = 384
    thumb_height = 216
    label_height = 28
    rows = (len(slide_paths) + columns - 1) // columns
    sheet = Image.new(
        "RGB", (columns * thumb_width, rows * (thumb_height + label_height)), "#101512"
    )
    draw = ImageDraw.Draw(sheet)

    for index, slide_path in enumerate(slide_paths):
        row, column = divmod(index, columns)
        x = column * thumb_width
        y = row * (thumb_height + label_height)
        with Image.open(slide_path) as image:
            thumb = image.convert("RGB").resize(
                (thumb_width, thumb_height), Image.Resampling.LANCZOS
            )
            sheet.paste(thumb, (x, y))
        draw.text((x + 10, y + thumb_height + 6), f"Slide {index + 1:02d}", fill="#d8e5dc")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path, "JPEG", quality=90, optimize=True)
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a portfolio contact sheet.")
    parser.add_argument("output", type=Path)
    parser.add_argument("slides", nargs="+", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = create_contact_sheet(args.slides, args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
