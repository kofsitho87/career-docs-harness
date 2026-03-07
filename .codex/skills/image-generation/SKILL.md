---
name: image-generation
description: Generate repository images with the local Gemini workflow. Use when the user asks for an image, illustration, diagram, mockup, or other visual asset for this project.
metadata:
  short-description: Generate project images with the local Gemini script
---

# Image Generation

Use this skill when the user wants a new image asset for this repository.

## Identify

- subject
- style
- usage context
- required text labels
- output path if already specified

Ask at most one clarifying question when the request is too vague.

## Workflow

1. Verify `.claude/skills/image_generation/scripts/.env` has `GEMINI_API_KEY` before claiming generation is ready.
2. Rewrite the request as a concrete English prompt.
3. Choose an aspect ratio for the intended output.
4. Pick a short kebab-case filename.
5. Run `.codex/skills/image-generation/scripts/generate-image` so Codex reuses the existing Claude-side Gemini implementation instead of maintaining a duplicate script.
6. Return the saved file path and offer one concise revision pass.

## Run

```bash
.codex/skills/image-generation/scripts/generate-image \
  --prompt "..." \
  --name "..." \
  --output "..." \
  --aspect 16:9
```

## Aspect Ratio Defaults

- `16:9` for diagrams, slides, and document figures
- `9:16` for mobile mockups
- `1:1` for icons or square graphics
- `4:3` for general images
- `3:4` for posters or vertical layouts

## Validation

If generation fails because `GEMINI_API_KEY` is missing, tell the user to add it to `.claude/skills/image_generation/scripts/.env`.
