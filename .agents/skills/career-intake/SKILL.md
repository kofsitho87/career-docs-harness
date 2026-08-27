---
name: career-intake
description: Collect and resume a candidate's career intake from repository sources and focused interviews. Use when onboarding a new user, importing new career material, or continuing an incomplete intake; do not use to draft final resumes or portfolios.
metadata:
  short-description: Build career intake from sources and interviews
---

# Career Intake

Build enough provenance-backed input for career memory without asking the user to repeat facts already present in the repository.

## Start

1. Read `harness.yaml`, `memory/state.yaml`, and `sources/manifest.yaml`.
2. If the state is `not_started`, read `START_HERE.md`.
3. Inspect existing sources and the minimum relevant files under `memory/`.
4. Read [source routing](references/source-routing.md) when sources still need ingestion.
5. Read [interview guidance](references/interview.md) before asking career questions.

## Source First

- Ingest unregistered local material before interviewing.
- Use the logged-in browser only for pages the user is authorized to access.
- Store authentication-free snapshots, never browser state or credentials.
- Treat GitHub activity as evidence context, not an achievement by itself.
- Do not edit originals under `sources/`.

## Interview Loop

1. Compare sources with candidate, preferences, timeline, experience, projects, claims, and evidence memory.
2. Rank gaps that block a useful master resume: identity/contact, target roles, dates/titles, representative projects, personal contribution, results, and public evidence.
3. Ask at most three related questions in one turn. Prefer one question when it can unlock several facts.
4. Record each substantive answer as an interview source before marking derived memory verified:

```bash
uv run python -m scripts.lib.record_interview \
  --topic "..." \
  --question "..." \
  --answer "..."
```

5. Use `$career-memory` to merge the answer and its source ID into memory.
6. Update `memory/state.yaml` with completed areas and remaining questions.

## Stop Condition

Intake is ready for a master-resume draft when the career timeline has no blocking date/title conflict, at least one representative project has clear personal contribution, and public claims have usable provenance. Leave optional gaps in `pending_questions`; do not prolong the interview for completeness alone.
