from __future__ import annotations

from scripts.lib.cli import build_parser


def test_cli_exposes_product_commands() -> None:
    parser = build_parser()
    assert parser.parse_args(["init"]).command == "init"
    assert parser.parse_args(["ingest", "sources/files/profile.md"]).command == "ingest"
    project_args = parser.parse_args(["ingest-project", "/tmp/project"])
    assert project_args.command == "ingest-project"
    assert project_args.openwiki == "auto"
    assert parser.parse_args(
        ["ingest-project", "/tmp/project", "--openwiki", "required"]
    ).openwiki == "required"
    assert parser.parse_args(["check"]).command == "check"
    assert parser.parse_args(["build", "resume"]).artifact == "resume"
    assert parser.parse_args(["build", "portfolio", "--no-render"]).artifact == "portfolio"
    assert parser.parse_args(["preview"]).command == "preview"
    assert parser.parse_args(["deploy"]).command == "deploy"
