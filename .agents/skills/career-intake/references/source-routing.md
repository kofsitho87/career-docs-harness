# Source Routing

| Source | Action | Stored result |
|---|---|---|
| PDF, DOCX, Markdown, TXT, HTML | `uv run python -m scripts.lib.ingest_files PATH` | Original plus `sources/extracted/` text |
| LinkedIn or logged-in profile | Read with authorized browser, save plain text, then `ingest_web_snapshot` | `sources/web/` Markdown snapshot |
| Public GitHub profile | `uv run python -m scripts.lib.ingest_github USERNAME` | Sanitized `sources/github/` JSON |
| User interview answer | `uv run python -m scripts.lib.record_interview ...` | `sources/interviews/` Markdown snapshot |
| Screenshot | Put the approved original under `sources/screenshots/`, then ingest it | Manifest entry without extracted text |

Before using a source, confirm its ID exists in `sources/manifest.yaml`. Use only the manifest ID in memory `source_refs`.

Never store cookies, tokens, browser profiles, private GitHub payloads, or temporary authenticated page state.
