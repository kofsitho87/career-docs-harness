"""Run the synthetic candidate through resume and portfolio build pipelines."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.lib.build_portfolio import build_portfolio
from scripts.lib.build_resume import build_resume
from scripts.lib.build_site import build_site
from scripts.lib.render_portfolio import render_portfolio

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    sample_root = REPOSITORY_ROOT / "examples" / "sample-candidate"
    output_root = REPOSITORY_ROOT / "tmp" / "pdfs" / "e2e-sample"
    portfolio_html = output_root / "portfolio" / "index.html"
    output_root.mkdir(parents=True, exist_ok=True)

    resume_result = build_resume(
        sample_root / "resume" / "master.md",
        output_root / "sample-resume.pdf",
        html_path=output_root / "sample-resume.html",
    )
    portfolio_build = build_portfolio(
        sample_root / "portfolio" / "outline.yaml", portfolio_html
    )
    portfolio_result = render_portfolio(
        portfolio_html,
        pdf_path=output_root / "sample-portfolio.pdf",
        render_root=output_root / "render",
        check_memory_ids=False,
    )
    site_result = build_site(portfolio_html, output_root / "dist")
    report = {
        "resume": resume_result,
        "portfolio_build": portfolio_build,
        "portfolio_render": portfolio_result,
        "site": site_result,
    }
    report_path = output_root / "report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"sample e2e passed: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
