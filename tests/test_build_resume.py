from __future__ import annotations

from pathlib import Path

from scripts.lib.build_resume import markdown_to_html

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_markdown_resume_renders_semantic_html_and_links() -> None:
    markdown_text = """# 홍길동

- GitHub: [example](https://github.com/example)

## Professional Summary

AI 제품을 설계하고 운영했습니다.

## Experience

### Example

- 시스템을 설계했습니다.
<!-- claims: claim-example -->
"""
    css = (PROJECT_ROOT / "templates" / "resume" / "resume.css").read_text(
        encoding="utf-8"
    )

    rendered = markdown_to_html(markdown_text, css, "홍길동 이력서")

    assert '<html lang="ko">' in rendered
    assert "<h1>홍길동</h1>" in rendered
    assert '<a href="https://github.com/example">example</a>' in rendered
    assert "@page" in rendered
    assert "claim-example" in rendered
