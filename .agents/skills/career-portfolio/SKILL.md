---
name: career-portfolio
description: Design and build a provenance-backed slide HTML career portfolio from verified memory and the master resume. Use for portfolio narrative, outline, theme selection, HTML generation, PDF rendering, and visual QA; do not start with page styling before the outline is approved.
metadata:
  short-description: Build a verified slide career portfolio
---

# Career Portfolio

Turn verified career evidence into a concise slide narrative before choosing layout details.

## Preconditions

1. Read `harness.yaml`, `memory/state.yaml`, `resume/master.md`, relevant projects, claims, evidence, and preferences.
2. Run `uv run python -m scripts.lib.validate_memory`.
3. Read [narrative architecture](references/narrative-architecture.md) and [slide patterns](references/slide-patterns.md) before writing the outline.
4. Read [evidence design](references/evidence-design.md) when slides use screenshots, diagrams, or operational proof.

## Outline First

1. Choose one professional positioning and the smallest representative project set.
2. Create `drafts/portfolio/outline.yaml` using the configured 7–15 slide range and target of 10.
3. Give every slide one purpose and connect important statements to claim/evidence IDs.
4. Validate the outline before HTML generation.
5. Do not add filler slides to reach the target count.

## Design and Build

1. Choose `editorial`, `minimal`, or `technical` from candidate preferences and audience. Read [design system](references/design-system.md) for theme boundaries.
2. Read [content density](references/content-density.md) before selecting slide layouts.
3. Build from the shared runtime and theme tokens:

```bash
uv run python -m scripts.lib.build_portfolio \
  --outline drafts/portfolio/outline.yaml \
  --output portfolio/html/index.html
```

4. Keep reusable evidence under `portfolio/assets/`; never embed credentials or restricted material.

## Verify

Read [visual QA](references/visual-qa.md), then run static validation, render slides, inspect the contact sheet, and verify the PDF. Do not treat a successful build as visual approval.

```bash
uv run python -m scripts.lib.validate_slides portfolio/html/index.html
uv run python -m scripts.lib.render_portfolio --input portfolio/html/index.html
```

Update the outline or source, not `portfolio/dist/`, when a problem is found.
