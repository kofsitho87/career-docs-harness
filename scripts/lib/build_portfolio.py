"""Build a themed slide portfolio HTML document from a validated YAML outline."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from scripts.lib.schema import load_schema, validate_data

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_ROOT = REPOSITORY_ROOT / "templates" / "portfolio"


def load_outline(path: Path, repository_root: Path = REPOSITORY_ROOT) -> dict[str, Any]:
    outline = yaml.safe_load(path.read_text(encoding="utf-8"))
    validate_data(
        outline,
        load_schema("portfolio-outline.schema.json", repository_root / "schemas"),
        str(path),
    )
    slide_ids = [slide["id"] for slide in outline["slides"]]
    if len(slide_ids) != len(set(slide_ids)):
        raise ValueError("portfolio outline slide IDs must be unique")
    return outline


def build_portfolio(
    outline_path: Path,
    output_path: Path,
    *,
    repository_root: Path = REPOSITORY_ROOT,
) -> dict[str, Any]:
    outline = load_outline(outline_path, repository_root)
    template_root = repository_root / "templates" / "portfolio"
    theme_root = template_root / "themes" / outline["theme"]
    environment = Environment(
        loader=FileSystemLoader(template_root),
        autoescape=select_autoescape(["html", "xml"]),
        keep_trailing_newline=True,
    )
    template = environment.get_template("base/index.html")
    rendered = template.render(
        outline=outline,
        components_css=(template_root / "base" / "components.css").read_text(
            encoding="utf-8"
        ),
        theme_css=(theme_root / "theme.css").read_text(encoding="utf-8"),
        presentation_js=(template_root / "base" / "presentation.js").read_text(
            encoding="utf-8"
        ),
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    return {
        "output": str(output_path),
        "theme": outline["theme"],
        "slides": len(outline["slides"]),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build portfolio HTML from YAML outline.")
    parser.add_argument("--outline", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = build_portfolio(args.outline, args.output)
    print(f"built {result['output']}")
    print(f"  theme {result['theme']} · slides {result['slides']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
