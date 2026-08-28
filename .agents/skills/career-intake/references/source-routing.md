# Source Routing

| Source | Action | Stored result |
|---|---|---|
| PDF, DOCX, Markdown, TXT, HTML | `uv run python -m scripts.lib.ingest_files PATH` | Original plus `sources/extracted/` text |
| LinkedIn or logged-in profile | Read with authorized browser, save plain text, then `ingest_web_snapshot` | `sources/web/` Markdown snapshot |
| Public GitHub profile | `uv run python -m scripts.lib.ingest_github USERNAME` | Sanitized `sources/github/` JSON |
| Local Git project | `./scripts/harness ingest-project /path/to/repository` | Docs/tree/history snapshot under `sources/projects/` |
| GitHub project URL | `./scripts/harness ingest-project https://github.com/owner/repository` | Temporary clone followed by the same project snapshot |
| Project with `openwiki/` | Default `--openwiki auto`; use `required` for strict or `off` to skip | OpenWiki CLI briefing and wiki pages before Git fallback |
| User interview answer | `uv run python -m scripts.lib.record_interview ...` | `sources/interviews/` Markdown snapshot |
| Screenshot | Put the approved original under `sources/screenshots/`, then ingest it | Manifest entry without extracted text |

Before using a source, confirm its ID exists in `sources/manifest.yaml`. Use only the manifest ID in memory `source_refs`.

Never store cookies, tokens, browser profiles, private GitHub payloads, or temporary authenticated page state.

Project snapshots exclude source-code bodies by default. Add `--include-code` only when implementation details are needed; even then, only tracked text files within the configured count and size limits are captured. Repository metadata never proves the candidate's personal role or impact by itself.

OpenWiki runs only inside a temporary clone and uses `openwiki code -p` for a one-shot briefing. It never initializes or updates the user's original wiki. Auto mode falls back to existing wiki Markdown; required mode fails when OpenWiki cannot run.
