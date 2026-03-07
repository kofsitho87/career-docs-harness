# Codex Image Generation Skill Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the existing Claude-only image generation skill available to Codex inside this repository without duplicating the Gemini image generation logic.

**Architecture:** Create a project-local Codex skill under `.codex/skills/` that mirrors the intent of the existing Claude skill and reuses the existing Python script in `.claude/skills/image_generation/scripts/`. Add a repository-scoped `AGENTS.md` entry so future Codex sessions can discover and trigger the local skill consistently.

**Tech Stack:** Markdown skill files, project-scoped AGENTS instructions, Python 3.11, `uv`, Gemini API via `google-genai`, dotenv

---

### Task 1: Create the Codex skill scaffold

**Files:**
- Check: `.claude/skills/image_generation/SKILL.md`
- Create: `.codex/skills/image-generation/SKILL.md`
- Create: `.codex/skills/image-generation/agents/openai.yaml`

**Step 1: Write the failing validation check**

Run:

```bash
test -f .codex/skills/image-generation/SKILL.md
```

Expected: command exits with status `1` because the Codex skill does not exist yet.

**Step 2: Draft the Codex SKILL.md frontmatter and workflow**

Write `.codex/skills/image-generation/SKILL.md` with:

```md
---
name: image-generation
description: Generate images from user requests inside this repository. Use when the user asks for an image, illustration, mockup, diagram, or visual asset, and route generation through the local Gemini script.
metadata:
  short-description: Generate images with the local Gemini workflow
---

# Image Generation

Use this skill when the user wants a new image asset for documents, presentations, diagrams, mockups, or other visual outputs in this repository.

## Inputs to identify

- subject
- style
- usage context
- required text or labels
- target output path if the user already gave one

## Workflow

1. Clarify only one missing requirement when the request is too vague.
2. Rewrite the request into a concrete English prompt.
3. Choose an aspect ratio based on use case.
4. Pick a short kebab-case filename.
5. Run `uv run .claude/skills/image_generation/scripts/generate_image.py ...`
6. Report the saved file path and offer one concise revision loop.

## Aspect ratio defaults

- `16:9` for diagrams, slides, document figures
- `9:16` for mobile mockups
- `1:1` for icons or square graphics
- `4:3` for general images
- `3:4` for posters or vertical layouts

## Validation

If generation fails because `GEMINI_API_KEY` is missing, tell the user to add it to `.claude/skills/image_generation/scripts/.env`.
```

**Step 3: Add the UI metadata file**

Write `.codex/skills/image-generation/agents/openai.yaml` with:

```yaml
display_name: Image Generation
short_description: Generate repository images with the local Gemini script
default_prompt: Generate an image for this project using the local image-generation skill.
```

**Step 4: Run validation to verify the scaffold exists**

Run:

```bash
test -f .codex/skills/image-generation/SKILL.md && test -f .codex/skills/image-generation/agents/openai.yaml
```

Expected: command exits with status `0`.

**Step 5: Commit**

```bash
git add .codex/skills/image-generation/SKILL.md .codex/skills/image-generation/agents/openai.yaml
git commit -m "feat: add codex image generation skill scaffold"
```

### Task 2: Add a Codex-friendly execution wrapper instead of duplicating the Python implementation

**Files:**
- Check: `.claude/skills/image_generation/scripts/generate_image.py`
- Create: `.codex/skills/image-generation/scripts/generate-image`
- Test: `.codex/skills/image-generation/SKILL.md`

**Step 1: Write the failing execution check**

Run:

```bash
test -x .codex/skills/image-generation/scripts/generate-image
```

Expected: command exits with status `1` because the wrapper does not exist yet.

**Step 2: Write the minimal wrapper script**

Create `.codex/skills/image-generation/scripts/generate-image`:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"

exec uv run "$ROOT_DIR/.claude/skills/image_generation/scripts/generate_image.py" "$@"
```

**Step 3: Make the wrapper executable**

Run:

```bash
chmod +x .codex/skills/image-generation/scripts/generate-image
```

Expected: no output and exit status `0`.

**Step 4: Update the Codex skill instructions to use the wrapper**

Replace the run step in `.codex/skills/image-generation/SKILL.md` so it tells Codex to execute:

```bash
.codex/skills/image-generation/scripts/generate-image \
  --prompt "..." \
  --name "..." \
  --output "..." \
  --aspect 16:9
```

Also add one sentence explaining that the wrapper intentionally reuses the existing Claude-side Python script so there is only one Gemini implementation to maintain.

**Step 5: Run validation to verify the wrapper is executable**

Run:

```bash
test -x .codex/skills/image-generation/scripts/generate-image
```

Expected: command exits with status `0`.

**Step 6: Commit**

```bash
git add .codex/skills/image-generation/SKILL.md .codex/skills/image-generation/scripts/generate-image
git commit -m "feat: add codex wrapper for image generation"
```

### Task 3: Add repository-level skill discovery instructions

**Files:**
- Create: `AGENTS.md`
- Modify: `README.md`
- Check: `.codex/skills/image-generation/SKILL.md`

**Step 1: Write the failing discovery check**

Run:

```bash
rg -n "image-generation|.codex/skills/image-generation" AGENTS.md README.md
```

Expected: no match for the new Codex skill path yet.

**Step 2: Create a repository-scoped AGENTS.md**

Write `AGENTS.md` with:

```md
# AGENTS.md

## Project Notes

- This repository contains a project-local Codex skill at `.codex/skills/image-generation/`.
- Use that skill when the user asks for an image, diagram, mockup, illustration, or other generated visual asset for this repository.
- The Codex skill intentionally reuses `.claude/skills/image_generation/scripts/generate_image.py` as the single image generation implementation.
- When the skill is used, verify `GEMINI_API_KEY` is present in `.claude/skills/image_generation/scripts/.env` before claiming generation is ready.
```

**Step 3: Update README.md**

Add one bullet under the repository structure section:

```md
- `.codex/skills/image-generation/`: Codex-compatible local image generation skill that reuses the shared Gemini script
```

**Step 4: Run validation to verify discovery text exists**

Run:

```bash
rg -n "image-generation|.codex/skills/image-generation" AGENTS.md README.md
```

Expected: matches in both `AGENTS.md` and `README.md`.

**Step 5: Commit**

```bash
git add AGENTS.md README.md
git commit -m "docs: document codex image generation skill"
```

### Task 4: Verify end-to-end readiness without calling the Gemini API

**Files:**
- Check: `.codex/skills/image-generation/SKILL.md`
- Check: `.codex/skills/image-generation/scripts/generate-image`
- Check: `.claude/skills/image_generation/scripts/.env.example`
- Check: `.claude/skills/image_generation/scripts/generate_image.py`

**Step 1: Verify the skill references the wrapper, not the Python script directly**

Run:

```bash
rg -n "generate-image|generate_image.py|GEMINI_API_KEY" .codex/skills/image-generation/SKILL.md
```

Expected: references the wrapper path and the env var guidance.

**Step 2: Verify the wrapper points at the shared implementation**

Run:

```bash
sed -n '1,80p' .codex/skills/image-generation/scripts/generate-image
```

Expected output includes:

```bash
exec uv run "$ROOT_DIR/.claude/skills/image_generation/scripts/generate_image.py" "$@"
```

**Step 3: Verify local prerequisites are discoverable**

Run:

```bash
rg -n "GEMINI_API_KEY" .claude/skills/image_generation/scripts/.env.example .claude/skills/image_generation/scripts/generate_image.py
```

Expected: one match in `.env.example` and one or more matches in `generate_image.py`.

**Step 4: Verify the new files are tracked**

Run:

```bash
git status --short
```

Expected: only the intended new or modified files appear.

**Step 5: Final commit**

```bash
git add AGENTS.md README.md .codex/skills/image-generation
git commit -m "feat: enable codex image generation skill in repo"
```
