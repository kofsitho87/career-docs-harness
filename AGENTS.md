# Career Harness Agent Contract

## Purpose

This repository is a single-user, Korean-first career-document harness. It turns immutable career sources into provenance-backed memory, a Markdown master resume, tailored resumes, case studies, and a slide-based HTML portfolio.

All supported coding agents must follow this file as the canonical operating contract. Platform-specific instruction files are generated adapters and must not duplicate or override these rules.

## Canonical Configuration

- Product settings: `harness.yaml`
- Source manifest: `sources/manifest.yaml`
- Working state: `memory/state.yaml`
- Canonical skills: `.agents/skills/`
- User onboarding: `START_HERE.md`
- Product design: `docs/plans/2026-08-27-career-harness-product-design.md`
- Implementation plan: `docs/plans/2026-08-27-career-harness-implementation.md`

When paths or settings disagree, prefer `harness.yaml` for product configuration and this file for agent behavior.

## Information Authority

Use this order when deciding what is true:

1. The user's latest explicit correction or instruction.
2. Immutable originals and captured snapshots under `sources/`.
3. Provenance-backed facts under `memory/`.
4. Target-specific strategy under `targets/`.
5. Drafts under `drafts/`.
6. Final outputs under `resume/`, `case-studies/`, and `portfolio/`.
7. Historical design and implementation records under `docs/plans/`.

Final outputs are not independent fact sources. When an output conflicts with `sources/` or verified `memory/`, correct the memory flow first and then regenerate or update the output.

## Required Read Order

At the beginning of a new task:

1. Read `harness.yaml`.
2. Read `memory/state.yaml`.
3. Read the minimum relevant memory files.
4. Read the relevant guide, plan, template, and skill only when the task requires them.
5. Inspect the current output only after understanding its upstream facts and strategy.

For a new user whose state is `not_started`, read `START_HERE.md` and begin with source intake rather than drafting an output.

## Directory Responsibilities

- `sources/`: immutable user-provided files and authentication-free web snapshots.
- `memory/`: AI-maintained durable career memory with provenance and status.
- `targets/`: job descriptions, company research, and target-specific strategy.
- `drafts/`: outlines, strategies, and unapproved intermediate work.
- `templates/`: reusable resume and portfolio structures with no personal facts.
- `resume/`: master and tailored resume outputs.
- `case-studies/`: final project case studies.
- `portfolio/html/`: editable slide-portfolio source.
- `portfolio/pdf/`: generated portfolio PDFs.
- `portfolio/assets/`: portfolio and case-study visual evidence.
- `portfolio/dist/`: generated deployment output; never edit it directly.
- `.agents/skills/`: canonical reusable workflows shared across agents.
- `scripts/`: deterministic ingestion, build, validation, preview, and deployment tools.
- `docs/guides/`: reusable writing and operating guidance.
- `docs/plans/`: historical or active design and implementation context, not facts.

## Source Handling

- Never edit files under `sources/` as part of normalization or writing work.
- Record every ingested source in `sources/manifest.yaml` with its type, location, capture time when relevant, and content hash.
- Logged-in browser sessions may be used to read LinkedIn or other authorized pages.
- Never save cookies, tokens, passwords, browser profiles, or authenticated session state in the repository.
- Store only authentication-free text snapshots, metadata, and user-approved screenshots.
- Record substantive user interview answers under `sources/interviews/` before using them as verified memory provenance.
- Project repository paths and GitHub URLs may be read to create immutable snapshots under `sources/projects/`; never edit the source repository or store its Git credentials.
- Repository structure, documentation, manifests, and history are evidence context. Do not infer the user's ownership or business impact without interview or source confirmation.
- Do not infer career achievements from repository activity counts alone.

## Automatic Memory Policy

The AI may update `memory/` without asking for approval on every edit. Every automatic change must preserve traceability.

### Allowed automatic updates

- Normalize company, role, project, technology, and date formatting.
- Merge equivalent facts that point to compatible sources.
- Add source references and confidence/status metadata.
- Add newly discovered experience, project, claim, and evidence candidates.
- Update `memory/state.yaml` and append a concise entry to `memory/changelog.md`.

### Required safeguards

- Use only `verified`, `inferred`, `unverified`, or `conflicted` as fact status values.
- Never silently overwrite conflicting dates, titles, metrics, ownership, or visibility.
- Record unresolved conflicts in `memory/conflicts.yaml`.
- Preserve direct user corrections over automated extraction and inference.
- Do not promote an inferred or unverified fact to verified without an explicit source.
- Do not place conflicted facts in final outputs.
- Every quantitative or high-impact public claim must link to one or more source references.

## Resume Workflow

- `resume/master.md` is the canonical resume output once the product migration reaches that phase.
- Tailored resumes must be derived from the master resume and verified memory.
- Tailoring may change summary, ordering, emphasis, keywords, and length.
- Tailoring may not introduce new companies, roles, dates, metrics, projects, or skills without first updating memory.
- The default language is Korean unless `harness.yaml` or the user requests otherwise.
- Keep Markdown as the editable source and generate PDF through the build tool.
- Validate ATS structure, repetition, dates, links, text extraction, and page layout before completion.

## Case Study Workflow

- Read the relevant project memory and claims before editing a case study.
- Separate problem, constraints, decisions, implementation, personal contribution, evidence, results, and lessons.
- Make ownership boundaries explicit; do not present team or later work as the user's own contribution.
- Store reusable visual evidence under `portfolio/assets/` and reference it with valid relative paths.

## Portfolio Workflow

- Build a portfolio outline before editing HTML.
- Target 10 slides by default and remain within the configured 7–15 range.
- Do not add filler slides to reach the target count.
- Give each slide one primary communication goal.
- Connect important slide claims and evidence to stable IDs from memory.
- Use a configured theme rather than inventing an unrelated visual system per run.
- Edit source under `portfolio/html/`; never edit `portfolio/dist/` directly.
- After source changes, rebuild the portfolio PDF and deployment output.
- Validate slide count, 16:9 rendering, overflow, missing assets, contrast, links, PDF page size, and text extraction.

## Planning and Change Scope

- Read relevant plans before structural or architectural changes.
- Keep historical plans accurate as records; do not rewrite old implementation history to pretend removed artifacts still exist.
- Add or update design and implementation plans before a substantial new subsystem.
- Preserve unrelated user changes in a dirty worktree.
- Do not delete, move, publish, or expose personal career data unless the task explicitly authorizes it.
- Keep real candidate data out of the template baseline; use `examples/sample-candidate/` for product tests.

## Validation and Completion

Run the narrowest relevant checks while working and the integrated check when it becomes available.

An output task is complete only when:

- used facts have acceptable status and provenance;
- unresolved conflicts do not leak into the output;
- dates, metrics, roles, and technologies agree across outputs;
- local links and referenced assets exist;
- sensitive-information checks pass or approved values are allowlisted;
- requested Markdown, PDF, HTML, and deployment artifacts build successfully;
- generated outputs are not treated as editable source;
- `memory/state.yaml` reflects the new phase and pending questions.

## Multi-Agent Portability

- `AGENTS.md` is the only canonical behavior document.
- `.agents/skills/` is the only canonical project skill directory.
- `CLAUDE.md` and Cursor rule files are thin generated adapters.
- Run `uv run python scripts/setup_agents.py` to create or repair adapters.
- Run `uv run python scripts/setup_agents.py --check` to detect adapter drift.
- Never copy the full contents of this file into an adapter.
