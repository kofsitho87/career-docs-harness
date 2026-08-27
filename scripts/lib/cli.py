"""Unified user-facing command line for Career Harness workflows."""

from __future__ import annotations

import argparse
import http.server
from pathlib import Path
from typing import Any

import yaml

from scripts import setup_agents
from scripts.lib.build_portfolio import build_portfolio
from scripts.lib.build_resume import build_resume
from scripts.lib.build_site import build_site
from scripts.lib.ingest_files import ingest_file
from scripts.lib.render_portfolio import render_portfolio
from scripts.lib.scan_sensitive_info import scan_sensitive_info
from scripts.lib.validate_assets import validate_assets
from scripts.lib.validate_claims import validate_claims
from scripts.lib.validate_links import validate_links
from scripts.lib.validate_memory import validate_repository
from scripts.lib.validate_slides import validate_portfolio_html

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def load_config(repository_root: Path = REPOSITORY_ROOT) -> dict[str, Any]:
    return yaml.safe_load((repository_root / "harness.yaml").read_text(encoding="utf-8"))


def configured_outputs(repository_root: Path, config: dict[str, Any]) -> list[Path]:
    paths = [
        repository_root / config["resume"]["master"],
        repository_root / config["portfolio"]["source"],
    ]
    tailored_root = repository_root / config["resume"]["tailored_root"]
    if tailored_root.is_dir():
        paths.extend(sorted(tailored_root.glob("*.md")))
    return [path for path in paths if path.is_file()]


def initialize(repository_root: Path = REPOSITORY_ROOT) -> None:
    config = load_config(repository_root)
    directories = (
        repository_root / config["sources"]["root"],
        repository_root / config["memory"]["root"],
        repository_root / config["resume"]["tailored_root"],
        repository_root / config["portfolio"]["dist"],
        repository_root / "targets",
        repository_root / "drafts" / "resume",
        repository_root / "drafts" / "portfolio",
    )
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    setup_agents.write_adapters(repository_root)
    print("career harness initialized without replacing existing user data")


def run_checks(repository_root: Path = REPOSITORY_ROOT) -> list[str]:
    config = load_config(repository_root)
    errors = validate_repository(repository_root)
    errors.extend(setup_agents.check_adapters(repository_root))
    outputs = configured_outputs(repository_root, config)
    errors.extend(validate_claims(outputs, repository_root / "memory" / "claims.yaml"))
    errors.extend(validate_links(outputs))
    errors.extend(validate_assets(outputs))
    errors.extend(
        scan_sensitive_info(outputs, repository_root / "privacy.allowlist.yaml")
    )
    portfolio_source = repository_root / config["portfolio"]["source"]
    if portfolio_source.is_file():
        errors.extend(validate_portfolio_html(portfolio_source, repository_root=repository_root))
    return errors


def command_ingest(args: argparse.Namespace) -> int:
    for source_path in args.paths:
        entry, created = ingest_file(source_path)
        action = "ingested" if created else "already registered"
        print(f"{action} {entry['id']}: {entry['path']}")
    return 0


def command_check(_: argparse.Namespace) -> int:
    errors = run_checks()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("career harness checks passed")
    return 0


def command_build_resume(args: argparse.Namespace) -> int:
    config = load_config()
    input_path = args.input or REPOSITORY_ROOT / config["resume"]["master"]
    output_path = args.output or REPOSITORY_ROOT / config["resume"]["pdf_output"]
    result = build_resume(input_path, output_path)
    print(f"built resume: {result['pdf']} ({result['pages']} pages)")
    return 0


def command_build_portfolio(args: argparse.Namespace) -> int:
    config = load_config()
    outline_path = args.outline or REPOSITORY_ROOT / "drafts" / "portfolio" / "outline.yaml"
    html_path = args.output or REPOSITORY_ROOT / config["portfolio"]["source"]
    build_result = build_portfolio(outline_path, html_path)
    print(f"built portfolio HTML: {build_result['output']}")
    if not args.no_render:
        pdf_path = REPOSITORY_ROOT / config["portfolio"]["pdf_output"]
        render_result = render_portfolio(html_path, pdf_path=pdf_path)
        print(f"rendered portfolio PDF: {render_result['pdf']}")
    return 0


def command_deploy(_: argparse.Namespace) -> int:
    config = load_config()
    result = build_site(
        REPOSITORY_ROOT / config["portfolio"]["source"],
        REPOSITORY_ROOT / config["portfolio"]["dist"],
    )
    print(f"built deploy directory: {result['output']} ({result['assets']} assets)")
    return 0


def command_preview(args: argparse.Namespace) -> int:
    command_deploy(args)
    config = load_config()
    dist = REPOSITORY_ROOT / config["portfolio"]["dist"]
    handler = lambda *handler_args, **handler_kwargs: http.server.SimpleHTTPRequestHandler(
        *handler_args, directory=str(dist), **handler_kwargs
    )
    server = http.server.ThreadingHTTPServer((args.host, args.port), handler)
    print(f"previewing http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="harness", description="Career Harness CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Prepare directories and agent adapters")
    init_parser.set_defaults(handler=lambda _: (initialize(), 0)[1])

    ingest_parser = subparsers.add_parser("ingest", help="Ingest immutable local sources")
    ingest_parser.add_argument("paths", nargs="+", type=Path)
    ingest_parser.set_defaults(handler=command_ingest)

    check_parser = subparsers.add_parser("check", help="Run integrated quality gates")
    check_parser.set_defaults(handler=command_check)

    build_parser_command = subparsers.add_parser("build", help="Build outputs")
    build_subparsers = build_parser_command.add_subparsers(dest="artifact", required=True)
    resume_parser = build_subparsers.add_parser("resume")
    resume_parser.add_argument("--input", type=Path)
    resume_parser.add_argument("--output", type=Path)
    resume_parser.set_defaults(handler=command_build_resume)
    portfolio_parser = build_subparsers.add_parser("portfolio")
    portfolio_parser.add_argument("--outline", type=Path)
    portfolio_parser.add_argument("--output", type=Path)
    portfolio_parser.add_argument("--no-render", action="store_true")
    portfolio_parser.set_defaults(handler=command_build_portfolio)

    preview_parser = subparsers.add_parser("preview", help="Build and preview portfolio site")
    preview_parser.add_argument("--host", default="127.0.0.1")
    preview_parser.add_argument("--port", type=int, default=8000)
    preview_parser.set_defaults(handler=command_preview)

    deploy_parser = subparsers.add_parser("deploy", help="Build GitHub Pages directory")
    deploy_parser.set_defaults(handler=command_deploy)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
