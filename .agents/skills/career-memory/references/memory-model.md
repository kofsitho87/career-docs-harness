# Career Memory Model

## Stable IDs

Use lowercase kebab-case IDs with a type prefix.

- `experience-company-role`
- `project-short-name`
- `claim-short-impact`
- `evidence-short-description`
- `conflict-field-hash`

Do not change an ID because wording improves.

## Source References

Every source reference must match an ID in `sources/manifest.yaml`. A source reference establishes provenance, not automatically the truth of every interpretation.

## Memory Responsibilities

- `candidate.md`: identity, public contact, positioning, preferences summary
- `preferences.yaml`: language, tone, length, portfolio theme and visual preferences
- `timeline.yaml`: chronological experience, project, education, and activity entries
- `experience/`: company- and role-level facts
- `projects/`: problem, constraints, ownership, decisions, implementation, results, technologies
- `claims.yaml`: reusable public or restricted career statements
- `evidence.yaml`: documents, URLs, repositories, images, screenshots, metrics
- `conflicts.yaml`: unresolved and explicitly resolved disagreements
- `decisions.md`: user-approved strategic decisions
- `changelog.md`: automatic memory mutations
- `state.yaml`: workflow phase and pending questions

## Merge Decisions

- Equivalent value plus new source: merge source refs and retain the stronger supported status.
- Empty existing value plus sourced incoming value: add it.
- Automated disagreement: preserve the existing value, mark the record conflicted, and add an open conflict.
- Incoming direct user correction: apply it and add a resolved conflict noting that the user value won.
- Existing user-edited value versus automated extraction: preserve the user value and record the rejected alternative.

Use `scripts.lib.memory_merge` for collection merges when the input already has structured records.

## Changelog Entry

Record what changed and which stable IDs were affected. Do not copy sensitive source contents into the changelog.
