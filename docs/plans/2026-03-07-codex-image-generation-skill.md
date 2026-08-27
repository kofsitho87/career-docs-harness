# Shared Agent Image Generation Skill Plan

**Goal:** Keep one project-local image generation skill that all supported agents can use without duplicating the Gemini implementation.

**Architecture:** Store the skill instructions, UI metadata, dotenv configuration, and Python implementation together under `.agents/skills/image-generation/`. Agent-specific skill copies are not maintained.

**Tech Stack:** Markdown skill files, Python 3.11, `uv`, Gemini API via `google-genai`, dotenv

## Files

- `.agents/skills/image-generation/SKILL.md`
- `.agents/skills/image-generation/agents/openai.yaml`
- `.agents/skills/image-generation/scripts/generate_image.py`
- `.agents/skills/image-generation/scripts/.env.example`
- `.agents/skills/image-generation/scripts/.env` (local secret, ignored by Git)

## Workflow

1. Keep `generate_image.py` as the single Gemini implementation.
2. Have `SKILL.md` invoke it with `uv run` and document the shared `.env` location.
3. Document `.agents/skills/` as the repository's common skill root in `AGENTS.md`, `CLAUDE.md`, `README.md`, and `docs/workflow.md`.
4. Remove agent-specific skill copies after comparing their contents and migrating unique resources.

## Validation

```bash
test -f .agents/skills/image-generation/SKILL.md
test -f .agents/skills/image-generation/agents/openai.yaml
test -f .agents/skills/image-generation/scripts/generate_image.py
test -f .agents/skills/image-generation/scripts/.env.example
rg -n "GEMINI_API_KEY|generate_image.py" .agents/skills/image-generation
```

The validation does not call the Gemini API or print the secret value.
