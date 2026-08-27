# Outbound Voice Agent PPT Image Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Generate a single 16:9 PPT-style summary image from `case-studies/outbound-voice-agent.md` using the repository's local `image-generation` skill.

**Architecture:** Use the existing portfolio case study as the only content source, compress it into one slide-worthy visual hierarchy, and run the local Gemini script with `uv run .agents/skills/image-generation/scripts/generate_image.py`. Save the exported image under `portfolio/assets/` so it remains a reusable portfolio artifact inside this repository.

**Tech Stack:** Markdown source document, local Codex skill, Gemini image generation script, repository assets folder

## Plan Notes

- Title: 병원 아웃바운드 Voice AI Agent
- Subtitle: 병원 예약 확인·안내 전화를 AI가 자동 발신하고 분석하는 실시간 음성 AI 시스템
- Hero metrics:
  - 총 통화 성공 96,000건+
  - 일 평균 통화 2,000건/일
  - 도입 병원 100개+
  - 응답 레이턴시 300ms
  - 지원 언어 6개
- Core structure:
  - Trigger: RabbitMQ message
  - Runtime: LiveKit multi-agent voice system
  - Agents: TriageCoordinator / BookingAgent / InfoAgent
  - Downstream: Booking API, Qdrant, analysis pipeline, S3
- Value props:
  - 단일 Agent에서 Multi-Agent로 분리
  - 예약/정보/전환을 역할 기반으로 라우팅
  - 실시간 음성 처리와 통화 후 비동기 분석 결합

## Prompt Spec

- Format: one clean presentation slide, 16:9 landscape
- Style: modern enterprise PPT, Korean text, sharp typography, white or very light background, restrained teal/blue accents
- Composition:
  - top-left title and subtitle
  - top-right compact KPI cards
  - center architecture flow diagram
  - bottom three feature blocks for Multi-Agent, Realtime API, Analysis Pipeline
- Tone: production-grade AI platform, credible and technical, not cartoonish
- Avoid: clutter, tiny illegible text, stock-photo people, purple gradients, dark backgrounds

## Generation Prompt

```text
Create a polished 16:9 presentation slide image in Korean for a technical portfolio case study. The slide title is "병원 아웃바운드 Voice AI Agent". Add the subtitle "병원 예약 확인·안내 전화를 AI가 자동 발신하고 분석하는 실시간 음성 AI 시스템". Use a clean white background with restrained teal and blue enterprise accents, modern presentation typography, and a structured layout that looks like a real investor or product engineering PPT slide.

Show five KPI cards: "총 통화 성공 96,000건+", "일 평균 통화 2,000건/일", "도입 병원 100개+", "응답 레이턴시 300ms", "지원 언어 6개". In the center, show a simplified architecture diagram flowing from RabbitMQ trigger to LiveKit multi-agent server, then to BookingAgent, InfoAgent, Booking API, Qdrant, analysis pipeline, and S3. At the bottom, show three concise feature panels labeled "Multi-Agent Routing", "Realtime Voice", and "Call Analysis Pipeline".

The result must feel like a premium technical presentation slide, legible, balanced, and suitable for a resume portfolio. Use Korean labels where appropriate. Do not make it look like a poster or a website screenshot.
```

## Generation Readiness Checks

- Verify `.agents/skills/image-generation/SKILL.md` requires checking `GEMINI_API_KEY`, English prompt translation, aspect ratio selection, and wrapper execution.
- Verify `.agents/skills/image-generation/scripts/generate_image.py` exists.
- Verify `.agents/skills/image-generation/scripts/.env` contains `GEMINI_API_KEY=` without printing the secret.

---

### Task 1: Lock the content scope for the slide

**Files:**
- Check: `case-studies/outbound-voice-agent.md`
- Reference: `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`
- Create: `docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md`

**Step 1: Re-read the portfolio source for the top slide-worthy signals**

Run:

```bash
sed -n '1,260p' case-studies/outbound-voice-agent.md
```

Expected: confirm the slide should center on the project title, role, period, 5 key metrics, architecture summary, and 3 technical differentiators.

**Step 2: Extract the content that must survive compression**

Write this working content block into the plan notes section before generating:

```md
- Title: 병원 아웃바운드 Voice AI Agent
- Subtitle: 병원 예약 확인·안내 전화를 AI가 자동 발신하고 분석하는 실시간 음성 AI 시스템
- Hero metrics:
  - 총 통화 성공 96,000건+
  - 일 평균 통화 2,000건/일
  - 도입 병원 100개+
  - 응답 레이턴시 300ms
  - 지원 언어 6개
- Core structure:
  - Trigger: RabbitMQ message
  - Runtime: LiveKit multi-agent voice system
  - Agents: TriageCoordinator / BookingAgent / InfoAgent
  - Downstream: Booking API, Qdrant, analysis pipeline, S3
- Value props:
  - 단일 Agent에서 Multi-Agent로 분리
  - 예약/정보/전환을 역할 기반으로 라우팅
  - 실시간 음성 처리와 통화 후 비동기 분석 결합
```

**Step 3: Validate the slide scope stays single-slide**

Run:

```bash
rg -n "총 통화 성공|일 평균 통화|도입 병원 수|응답 레이턴시|지원 언어" case-studies/outbound-voice-agent.md
```

Expected: matches exist for the five headline metrics and no extra section is required to understand the summary image.

**Step 4: Commit**

```bash
git add docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md
git commit -m "docs: add outbound voice agent ppt image plan"
```

### Task 2: Define the visual direction and generation prompt

**Files:**
- Modify: `docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md`
- Reference: `case-studies/outbound-voice-agent.md`

**Step 1: Write the prompt-spec section in the plan**

Add this exact prompt spec to the plan:

```md
## Prompt Spec

- Format: one clean presentation slide, 16:9 landscape
- Style: modern enterprise PPT, Korean text, sharp typography, white or very light background, restrained teal/blue accents
- Composition:
  - top-left title and subtitle
  - top-right compact KPI cards
  - center architecture flow diagram
  - bottom three feature blocks for Multi-Agent, Realtime API, Analysis Pipeline
- Tone: production-grade AI platform, credible and technical, not cartoonish
- Avoid: clutter, tiny illegible text, stock-photo people, purple gradients, dark backgrounds
```

**Step 2: Rewrite the prompt into concrete English for Gemini**

Add this exact generation prompt to the plan:

```text
Create a polished 16:9 presentation slide image in Korean for a technical portfolio case study. The slide title is "병원 아웃바운드 Voice AI Agent". Add the subtitle "병원 예약 확인·안내 전화를 AI가 자동 발신하고 분석하는 실시간 음성 AI 시스템". Use a clean white background with restrained teal and blue enterprise accents, modern presentation typography, and a structured layout that looks like a real investor or product engineering PPT slide.

Show five KPI cards: "총 통화 성공 96,000건+", "일 평균 통화 2,000건/일", "도입 병원 100개+", "응답 레이턴시 300ms", "지원 언어 6개". In the center, show a simplified architecture diagram flowing from RabbitMQ trigger to LiveKit multi-agent server, then to BookingAgent, InfoAgent, Booking API, Qdrant, analysis pipeline, and S3. At the bottom, show three concise feature panels labeled "Multi-Agent Routing", "Realtime Voice", and "Call Analysis Pipeline".

The result must feel like a premium technical presentation slide, legible, balanced, and suitable for a resume portfolio. Use Korean labels where appropriate. Do not make it look like a poster or a website screenshot.
```

**Step 3: Validate the prompt includes all mandatory elements**

Run:

```bash
rg -n "16:9|KPI|RabbitMQ|LiveKit|Multi-Agent Routing|Realtime Voice|Call Analysis Pipeline" docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md
```

Expected: every required layout and content anchor is present in the plan.

**Step 4: Commit**

```bash
git add docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md
git commit -m "docs: define prompt for outbound voice agent slide"
```

### Task 3: Verify the image-generation path before invoking Gemini

**Files:**
- Check: `.agents/skills/image-generation/SKILL.md`
- Check: `.agents/skills/image-generation/scripts/generate_image.py`
- Check: `.agents/skills/image-generation/scripts/.env`

**Step 1: Verify the Codex image-generation skill instructions**

Run:

```bash
sed -n '1,220p' .agents/skills/image-generation/SKILL.md
```

Expected: the workflow explicitly says to verify `GEMINI_API_KEY`, translate the request into English, pick an aspect ratio, and run the shared script.

**Step 2: Verify the generation script is executable**

Run:

```bash
test -f .agents/skills/image-generation/scripts/generate_image.py
```

Expected: command exits with status `0`.

**Step 3: Verify the Gemini API key is configured without printing it**

Run:

```bash
test -f .agents/skills/image-generation/scripts/.env && rg -q '^GEMINI_API_KEY=' .agents/skills/image-generation/scripts/.env
```

Expected: command exits with status `0`.

**Step 4: Commit**

```bash
git add docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md
git commit -m "docs: add generation readiness checks"
```

### Task 4: Generate the first PPT-style slide image

**Files:**
- Create: `portfolio/assets/outbound-voice-agent-ppt-slide.png`
- Reference: `docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md`

**Step 1: Run the generator with the planned prompt**

Run:

```bash
uv run .agents/skills/image-generation/scripts/generate_image.py \
  --prompt "Create a polished 16:9 presentation slide image in Korean for a technical portfolio case study. The slide title is '병원 아웃바운드 Voice AI Agent'. Add the subtitle '병원 예약 확인·안내 전화를 AI가 자동 발신하고 분석하는 실시간 음성 AI 시스템'. Use a clean white background with restrained teal and blue enterprise accents, modern presentation typography, and a structured layout that looks like a real investor or product engineering PPT slide. Show five KPI cards: '총 통화 성공 96,000건+', '일 평균 통화 2,000건/일', '도입 병원 100개+', '응답 레이턴시 300ms', '지원 언어 6개'. In the center, show a simplified architecture diagram flowing from RabbitMQ trigger to LiveKit multi-agent server, then to BookingAgent, InfoAgent, Booking API, Qdrant, analysis pipeline, and S3. At the bottom, show three concise feature panels labeled 'Multi-Agent Routing', 'Realtime Voice', and 'Call Analysis Pipeline'. The result must feel like a premium technical presentation slide, legible, balanced, and suitable for a resume portfolio. Use Korean labels where appropriate. Do not make it look like a poster or a website screenshot." \
  --name "outbound-voice-agent-ppt-slide" \
  --output "assets" \
  --aspect 16:9
```

Expected: a new image file is saved under `portfolio/assets/` and the tool prints the final saved path.

**Step 2: Verify the output file exists**

Run:

```bash
ls -l portfolio/assets/outbound-voice-agent-ppt-slide*
```

Expected: at least one generated image file is present.

**Step 3: Commit**

```bash
git add portfolio/assets/outbound-voice-agent-ppt-slide.png
git commit -m "feat: add outbound voice agent ppt slide image"
```

### Task 5: Run one focused revision pass if the first image misses

**Files:**
- Modify: `docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md`
- Update: `portfolio/assets/outbound-voice-agent-ppt-slide.png`

**Step 1: Inspect the first output against the acceptance criteria**

Run:

```bash
printf "%s\n" \
  "1. title/subtitle legible" \
  "2. five KPI cards visible" \
  "3. center architecture readable" \
  "4. bottom three panels present" \
  "5. overall feel is PPT slide, not poster"
```

Expected: review checklist is available before deciding whether a revision is required.

**Step 2: If needed, append one revision prompt in the plan**

Use one of these minimal deltas only:

```text
Make the layout less poster-like and more like a consulting presentation slide with stronger grid alignment and smaller decorative elements.
```

```text
Increase Korean text legibility, enlarge the title and KPI labels, and simplify the architecture diagram so it reads clearly at slide scale.
```

**Step 3: Re-run the generator once**

Run the same command from Task 4 with the selected revision sentence appended to the prompt.

Expected: one improved replacement image is saved and the workflow stops after this single revision pass.

**Step 4: Commit**

```bash
git add docs/plans/2026-03-07-outbound-voice-agent-ppt-image.md portfolio/assets/outbound-voice-agent-ppt-slide.png
git commit -m "refactor: refine outbound voice agent slide image"
```
