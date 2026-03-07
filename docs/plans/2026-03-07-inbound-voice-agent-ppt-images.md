# Inbound Voice Agent PPT Images Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Generate two 16:9 PPT-style slide images from `case-studies/inbound-voice-agent.md` using the repository's local `image-generation` skill.

**Architecture:** Use the inbound portfolio document as the single content source, compress it into a matched two-slide visual set, and run the local Gemini wrapper through `.codex/skills/image-generation/scripts/generate-image`. Save both exported images under `assets/` as reusable portfolio artifacts.

**Tech Stack:** Markdown source document, local Codex image-generation skill, Gemini wrapper script, repository assets folder

---

### Task 1: Lock slide scope and filenames

**Files:**
- Reference: `case-studies/inbound-voice-agent.md`
- Reference: `docs/plans/2026-03-07-inbound-voice-agent-portfolio-design.md`
- Reference: `docs/plans/2026-03-07-inbound-voice-agent-ppt-images-design.md`
- Create: `docs/plans/2026-03-07-inbound-voice-agent-ppt-images.md`

**Step 1: Confirm the two-slide split**

Run: `sed -n '1,260p' case-studies/inbound-voice-agent.md`
Expected: the first slide maps to system architecture, and the second slide maps to `flow_config` plus transfer design.

**Step 2: Fix output filenames**

- `assets/inbound-voice-agent-ppt-architecture.png`
- `assets/inbound-voice-agent-ppt-flow-transfer.png`

**Step 3: Keep the deck scope single-purpose**

Run: `rg -n "SupervisorAgent|flow_config|Warm/Cold Transfer|DTMF|Qdrant|Kafka|AWS S3" case-studies/inbound-voice-agent.md`
Expected: all required anchors exist in the source file.

### Task 2: Define prompts for both slides

**Files:**
- Modify: `docs/plans/2026-03-07-inbound-voice-agent-ppt-images.md`

**Step 1: Define prompt spec**

- Format: one clean presentation slide, 16:9 landscape
- Style: modern enterprise PPT, Korean text, sharp typography, white or very light background, restrained teal/blue accents
- Tone: production-grade healthcare AI platform, credible and technical
- Avoid: clutter, poster composition, dark backgrounds, purple gradients, cartoon illustrations, tiny text

**Step 2: Define prompt for architecture slide**

Create an English generation prompt that includes:

- title `병원 인바운드 Voice AI Agent`
- subtitle about AI handling inbound hospital calls
- SIP inbound to LiveKit Agent Server flow
- SupervisorAgent routing to Booking Agent, Info Agent, Triage Coordinator
- downstream systems Booking API, Qdrant, Kafka, AWS S3
- three short value callouts

**Step 3: Define prompt for flow/transfer slide**

Create an English generation prompt that includes:

- title `flow_config + Warm Transfer`
- subtitle about config-driven call flow and transfer control
- left-side node graph with `condition`, `greeting`, `agent`, `action`, `exit`
- right-side transfer state flow with approval, cold transfer, warm transfer, retry, leave memo
- small callouts for config-driven routing, retry logic, `action_mode_handler`

### Task 3: Verify generation readiness

**Files:**
- Check: `.codex/skills/image-generation/SKILL.md`
- Check: `.codex/skills/image-generation/scripts/generate-image`
- Check: `.claude/skills/image_generation/scripts/.env`

**Step 1: Verify the wrapper is executable**

Run: `test -x .codex/skills/image-generation/scripts/generate-image`
Expected: exit status `0`.

**Step 2: Verify the API key is configured without printing it**

Run: `test -f .claude/skills/image_generation/scripts/.env && rg -q '^GEMINI_API_KEY=' .claude/skills/image_generation/scripts/.env`
Expected: exit status `0`.

### Task 4: Generate the architecture slide

**Files:**
- Create: `assets/inbound-voice-agent-ppt-architecture.png`

**Step 1: Run the generator**

Run the local image-generation wrapper with a 16:9 prompt for the architecture slide.

**Step 2: Verify the file exists**

Run: `ls -l assets/inbound-voice-agent-ppt-architecture*`
Expected: generated image is present.

### Task 5: Generate the flow/transfer slide

**Files:**
- Create: `assets/inbound-voice-agent-ppt-flow-transfer.png`

**Step 1: Run the generator**

Run the local image-generation wrapper with a 16:9 prompt for the flow/transfer slide.

**Step 2: Verify the file exists**

Run: `ls -l assets/inbound-voice-agent-ppt-flow-transfer*`
Expected: generated image is present.

### Task 6: Validate outputs for one revision pass

**Files:**
- Check: `assets/inbound-voice-agent-ppt-architecture.png`
- Check: `assets/inbound-voice-agent-ppt-flow-transfer.png`

**Step 1: Inspect both outputs against the design**

Confirm:

- shared visual language
- readable Korean title text
- clearly legible main diagrams
- distinct message between slide 1 and slide 2

**Step 2: If one image misses, revise only that image once**

Tighten the prompt around the missing element and regenerate the single image.
