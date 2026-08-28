---
name: master-resume
description: Create or revise the Korean Markdown master resume from verified career memory and reusable claims. Use when the user requests the canonical resume; do not use for a company-specific tailored version or before blocking memory conflicts are resolved.
metadata:
  short-description: Write the canonical Korean master resume
---

# Master Resume

Create the broadest useful resume for the candidate's target role family while keeping every factual statement traceable.

## Preconditions

1. Read `harness.yaml`, `memory/state.yaml`, candidate, preferences, timeline, experience, projects, claims, and evidence.
2. Read `docs/guides/resume-guide.md` and [resume strategy](references/resume-strategy.md).
3. Run:

```bash
uv run python -m scripts.lib.validate_memory
```

Do not draft around a blocking date/title conflict. Omit optional unverified material rather than fabricating or silently promoting it.

## Draft

1. Establish one clear professional identity from verified recent experience.
2. Select public verified claims that demonstrate scope, decisions, ownership, and outcomes.
3. Follow `templates/resume/master.md`; preserve standard ATS section names.
4. Keep recent experience detailed and compress older experience.
5. Group production-used skills by category and show important skills in experience context.
6. Add hidden Markdown comments with relevant claim IDs near high-impact bullets so review can trace them without affecting rendered output.
7. Write the configured master path, normally `resume/master.md`.

## Verify

- Every number, date, title, technology, and ownership statement matches memory.
- Summary uses evidence, not aspirations.
- Bullets make the candidate's action and result explicit.
- Repetition and unrelated history are removed.
- The default language and tone follow preferences.
- Update `memory/state.yaml` only after the Markdown master is ready for review.

PDF generation belongs to the resume build pipeline, not this writing skill.
