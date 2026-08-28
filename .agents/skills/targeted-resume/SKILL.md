---
name: targeted-resume
description: Derive a company- or role-specific Markdown resume from the canonical master resume and a saved target job description. Use for tailoring emphasis and keywords; never use it to introduce facts absent from verified memory and the master resume.
metadata:
  short-description: Tailor the master resume to a target role
---

# Targeted Resume

Create a relevance-focused derivative while keeping the master resume and career memory authoritative.

## Preconditions

1. Resolve a target slug under `targets/` and require its `job-description.md`.
2. Read `resume/master.md`, verified memory, preferences, and [tailoring guidance](references/tailoring.md).
3. If the master resume is absent or stale relative to memory, use `$master-resume` first.
4. Run memory validation before writing.

## Tailor

1. Extract responsibilities, required capabilities, preferred capabilities, domain context, and exact standard terminology.
2. Create or update `targets/<slug>/strategy.md` with match, evidence, gaps, selected projects, and keyword plan.
3. Start from `templates/resume/tailored.md` and the master resume.
4. Change only summary, ordering, emphasis, keyword wording, selected bullets, and length.
5. Save to `resume/tailored/<slug>.md`.

## Guardrails

- Do not change company, title, dates, metrics, ownership, or technology depth to resemble the job description.
- Do not include a keyword unless verified memory shows real use or knowledge at the stated level.
- Do not hide a material gap by implying adjacent experience is identical.
- Keep claim ID trace comments for retained or rewritten high-impact statements.
- Do not modify `resume/master.md` merely to improve one target unless the improvement is genuinely universal.

Finish by comparing the derivative with the master and verified memory, then record only target-specific decisions under `targets/<slug>/`.
