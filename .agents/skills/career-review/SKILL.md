---
name: career-review
description: Independently review career memory, resumes, case studies, or portfolio content for factual consistency, provenance, ownership clarity, relevance, privacy, and output quality. Use for audits and pre-release review; report findings without rewriting unless fixes are explicitly requested.
metadata:
  short-description: Audit career outputs before release
---

# Career Review

Review independently from the writing workflow. Lead with actionable findings and evidence, not a rewritten document.

## Scope

Identify the requested artifact and read its upstream sources in authority order: `sources/`, verified `memory/`, target strategy, then the output. Read [review checklist](references/review-checklist.md) for the relevant artifact type.

## Deterministic Checks

Run the available checks before judgment-based review:

```bash
uv run python -m scripts.lib.validate_memory
uv run python scripts/setup_agents.py --check
```

Add artifact-specific build, link, asset, PDF, and visual checks when those tools exist.

## Review Rules

- Trace every important metric, date, title, technology, and ownership statement.
- Treat conflicted memory as blocking when it appears in output.
- Distinguish the candidate's work from team, vendor, open-source, or later work.
- Flag unsupported causal language even when the underlying metric is real.
- Check relevance and readability separately from factual correctness.
- Do not introduce new claims while suggesting wording improvements.

## Report

Order findings by severity:

- `P0`: privacy, credential, fabricated fact, or serious attribution risk
- `P1`: wrong date/metric/title, conflicted claim, broken required artifact, or misleading ownership
- `P2`: weak evidence, unclear contribution, ATS/relevance issue, repetition, or visual readability problem
- `P3`: minor wording, consistency, or polish

For each finding, name the artifact location, explain the impact, and cite the upstream fact or missing provenance. If there are no actionable findings, say so and list the checks performed.
