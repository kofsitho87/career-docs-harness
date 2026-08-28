---
name: career-memory
description: Normalize source-backed career facts into durable repository memory while preserving user edits, provenance, and conflicts. Use after source ingestion, interview answers, or user corrections; do not use it as a final resume-writing workflow.
metadata:
  short-description: Maintain provenance-backed career memory
---

# Career Memory

Convert sources and explicit user corrections into durable memory without silently resolving disagreement.

## Workflow

1. Read `harness.yaml`, `sources/manifest.yaml`, `memory/state.yaml`, and the affected memory files.
2. Read [memory model](references/memory-model.md) before adding a new record type or changing structure.
3. Run the baseline validator:

```bash
uv run python -m scripts.lib.validate_memory
```

4. Locate the exact source IDs supporting the update. Record a substantive interview answer with `scripts.lib.record_interview` if it is not already a source.
5. Reuse stable IDs for the same experience, project, claim, and evidence. Merge compatible facts and source refs.
6. Preserve direct user edits. Record incompatible automated values in `memory/conflicts.yaml` instead of overwriting them.
7. Update affected memory, `memory/changelog.md`, and `memory/state.yaml` in the same change.
8. Run validation again and report unresolved blocking conflicts.

## Status Rules

- `verified`: explicitly supported by a source or recorded user answer
- `inferred`: reasonable synthesis that remains distinguishable from source text
- `unverified`: candidate fact with insufficient support
- `conflicted`: incompatible values remain unresolved

Only verified public claims are eligible for final resume and portfolio copy. Inferred material may guide interview questions or positioning drafts but must not be presented as settled fact.
