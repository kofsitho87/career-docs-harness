"""Static and provenance validation for generated slide portfolio HTML."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

import yaml
from bs4 import BeautifulSoup

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def is_remote_reference(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "data", "mailto"} or value.startswith("#")


def memory_ids(repository_root: Path) -> tuple[set[str], set[str]]:
    claims = yaml.safe_load(
        (repository_root / "memory" / "claims.yaml").read_text(encoding="utf-8")
    ).get("claims", [])
    evidence = yaml.safe_load(
        (repository_root / "memory" / "evidence.yaml").read_text(encoding="utf-8")
    ).get("evidence", [])
    return ({item["id"] for item in claims}, {item["id"] for item in evidence})


def validate_portfolio_html(
    html_path: Path,
    *,
    repository_root: Path = REPOSITORY_ROOT,
    minimum_slides: int | None = None,
    maximum_slides: int | None = None,
    check_memory_ids: bool = True,
) -> list[str]:
    errors: list[str] = []
    if not html_path.is_file():
        return [f"portfolio HTML not found: {html_path}"]

    config = yaml.safe_load(
        (repository_root / "harness.yaml").read_text(encoding="utf-8")
    )
    minimum_slides = minimum_slides or config["portfolio"]["slide_count"]["minimum"]
    maximum_slides = maximum_slides or config["portfolio"]["slide_count"]["maximum"]
    content = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(content, "html.parser")
    slides = soup.select(".slide[data-slide-id]")
    if not minimum_slides <= len(slides) <= maximum_slides:
        errors.append(
            f"slide count {len(slides)} is outside {minimum_slides}–{maximum_slides}"
        )

    slide_ids = [slide.get("data-slide-id", "") for slide in slides]
    if len(slide_ids) != len(set(slide_ids)):
        errors.append("slide IDs must be unique")

    known_claims, known_evidence = memory_ids(repository_root)
    for index, slide in enumerate(slides, start=1):
        title = slide.find(["h1", "h2"])
        if title is None or not title.get_text(strip=True):
            errors.append(f"slide {index} has no visible title")
        if not slide.get_text(" ", strip=True):
            errors.append(f"slide {index} is empty")

        if check_memory_ids:
            claim_ids = [value for value in slide.get("data-claim-ids", "").split(",") if value]
            evidence_ids = [
                value for value in slide.get("data-evidence-ids", "").split(",") if value
            ]
            for claim_id in claim_ids:
                if claim_id not in known_claims:
                    errors.append(f"slide {index} references unknown claim {claim_id}")
            for evidence_id in evidence_ids:
                if evidence_id not in known_evidence:
                    errors.append(f"slide {index} references unknown evidence {evidence_id}")

    for element in soup.find_all(src=True):
        source = str(element["src"])
        if is_remote_reference(source):
            continue
        resolved = (html_path.parent / source).resolve()
        if not resolved.is_file():
            errors.append(f"missing local asset: {source}")

    for placeholder in ("TODO", "{{", "{%"):
        if placeholder in content:
            errors.append(f"unresolved placeholder in portfolio HTML: {placeholder}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated portfolio HTML.")
    parser.add_argument("html", type=Path)
    parser.add_argument("--skip-memory-ids", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_portfolio_html(args.html, check_memory_ids=not args.skip_memory_ids)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("portfolio slides are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
