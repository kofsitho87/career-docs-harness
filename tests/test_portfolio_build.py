from __future__ import annotations

import tempfile
from pathlib import Path

import yaml

from scripts.lib.build_portfolio import build_portfolio
from scripts.lib.build_site import build_site
from scripts.lib.validate_slides import validate_portfolio_html

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_OUTLINE = PROJECT_ROOT / "examples" / "sample-candidate" / "portfolio" / "outline.yaml"


def test_all_themes_build_from_one_semantic_outline() -> None:
    original = yaml.safe_load(SAMPLE_OUTLINE.read_text(encoding="utf-8"))
    rendered_by_theme: dict[str, str] = {}
    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary_root = Path(temporary_directory)
        for theme in ("editorial", "minimal", "technical"):
            outline = dict(original)
            outline["theme"] = theme
            outline_path = temporary_root / f"{theme}.yaml"
            outline_path.write_text(
                yaml.safe_dump(outline, allow_unicode=True, sort_keys=False), encoding="utf-8"
            )
            output_path = temporary_root / f"{theme}.html"
            result = build_portfolio(outline_path, output_path)
            rendered = output_path.read_text(encoding="utf-8")
            rendered_by_theme[theme] = rendered

            assert result["slides"] == 10
            assert f'data-theme="{theme}"' in rendered
            assert validate_portfolio_html(output_path, check_memory_ids=False) == []

    assert len(set(rendered_by_theme.values())) == 3


def test_site_build_creates_index_from_portfolio_html() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary_root = Path(temporary_directory)
        html_path = temporary_root / "portfolio" / "html" / "index.html"
        build_portfolio(SAMPLE_OUTLINE, html_path)
        dist_path = temporary_root / "portfolio" / "dist"

        result = build_site(html_path, dist_path)

        assert (dist_path / "index.html").is_file()
        assert result["assets"] == 0
