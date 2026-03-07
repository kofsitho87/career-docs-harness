# Hospital Customer Support Agent PPT Images Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** `case-studies/hospital-customer-support-agent.md`를 기반으로 16:9 PPT 스타일 이미지 2장을 생성해 포트폴리오용 시각 자산으로 저장한다.

**Architecture:** 케이스 스터디 문서를 그대로 옮기지 않고, 핵심 메시지를 두 장으로 압축한다. 첫 장은 프로젝트 개요와 서비스 아키텍처를, 두 번째 장은 상담 흐름과 핵심 설계 의사결정을 중심으로 구성하고, 실제 생성은 `.codex/skills/image-generation/scripts/generate-image` 래퍼를 사용한다.

**Tech Stack:** Markdown source document, local Codex `image-generation` skill, Gemini image wrapper, repository `assets/` folder

---

## Plan Notes

- Source file: `case-studies/hospital-customer-support-agent.md`
- Output style: clean enterprise PPT, Korean labels, 16:9 landscape
- Visual tone: white or very light background, restrained teal/blue accents, technical and credible, not poster-like
- Avoid: dark background, purple gradients, stock-photo people, tiny illegible labels, cluttered diagrams

## Slide Split

### Slide 1: Overview + Architecture

- Title: `병원 고객상담 AI Agent`
- Subtitle: `복잡한 병원 문의를 상태 기반 상담 흐름과 데이터 조회 구조로 처리한 AI 상담 시스템`
- Meta block:
  - 기간 `2025.03 - 2025.05`
  - 소속 `와이즈에이아이`
  - 역할 `핵심 아키텍트 + 일부 구현`
- Core message:
  - 단순 FAQ가 아니라 실제 상담 흐름으로 처리
  - LangGraph 기반 상담 플로우와 상태 모델
  - 병원별 지식 조회 + API/검색/대시보드/배포 경계
- Architecture nodes:
  - User inquiry
  - LangGraph consultation engine
  - `primary_assistant`
  - `customer_interaction`
  - `extract_personal_info`
  - `tools`
  - Qdrant search
  - FastAPI / LangGraph SDK API
  - Next.js monitoring dashboard
  - AWS ECS Fargate deployment

### Slide 2: Flow + Design Decisions

- Title: `Consultation Flow + Design Decisions`
- Subtitle: `상담 흐름 분리, 병원별 지식 응답, 운영 가능한 서비스 경계`
- Left flow:
  - 일반 문의 처리
  - 개인정보 수집 후 원래 질문 복귀
  - 상담원 연결 준비
- Right decision blocks:
  - 상태 기반 워크플로우
  - 병원별 검색 기반 응답
  - 서비스 경계와 운영 구조
- Bottom takeaway:
  - AI 제품의 복잡도는 모델보다 절차와 시스템 경계에서 더 크게 생긴다

## Prompt Spec

- Format: one clean presentation slide, 16:9 landscape
- Style: modern enterprise PPT, Korean text, sharp typography, white or very light background, restrained teal/blue accents
- Tone: product-engineering portfolio, technical and credible, healthcare-adjacent but not sterile or corporate-stock
- Composition:
  - clear title block
  - one dominant central diagram
  - 3-5 compact supporting info blocks
  - generous whitespace
- Avoid:
  - poster composition
  - website screenshot look
  - cartoon illustrations
  - long paragraph text
  - purple-heavy palettes

## Generation Prompt: Slide 1

```text
Create a polished 16:9 presentation slide image in Korean for a technical portfolio case study. The slide title is "병원 고객상담 AI Agent". Add the subtitle "복잡한 병원 문의를 상태 기반 상담 흐름과 데이터 조회 구조로 처리한 AI 상담 시스템". Use a clean white or very light background with restrained teal and blue accents, premium enterprise presentation typography, and a structured layout that looks like a real product engineering or architecture PPT slide.

Include a compact meta section with "기간 2025.03 - 2025.05", "소속 와이즈에이아이", and "역할 핵심 아키텍트 + 일부 구현". In the center, show a clear architecture diagram: User Inquiry flows into a LangGraph consultation engine, then branches into primary_assistant, customer_interaction, extract_personal_info, and tools. Connect those to Qdrant search, FastAPI plus LangGraph SDK API, a Next.js monitoring dashboard, and AWS ECS Fargate deployment. Add three short callout cards for "상태 기반 상담 흐름", "병원별 지식 조회", and "운영 가능한 서비스 경계".

The image should feel legible, balanced, and credible for a senior engineer portfolio. Use Korean labels where appropriate. Do not make it look like a poster, infographic, or website screenshot.
```

## Generation Prompt: Slide 2

```text
Create a polished 16:9 presentation slide image in Korean for a technical portfolio case study. The slide title is "Consultation Flow + Design Decisions". Add the subtitle "상담 흐름 분리, 병원별 지식 응답, 운영 가능한 서비스 경계". Use the same visual language as a premium enterprise PPT slide: white or very light background, restrained teal and blue accents, sharp presentation typography, and a clean grid layout.

On the left, show a simplified consultation flow with three paths: "일반 문의 처리", "개인정보 수집 후 원래 질문 복귀", and "상담원 연결 준비". Use concrete mini examples such as asking weekend clinic hours, collecting name and phone number before resuming a pending implant question, and preparing a human handoff only after required info is present. On the right, show three design decision panels labeled "LangGraph 상태 기반 워크플로우", "병원별 검색 기반 응답", and "API·검색·대시보드·배포 경계". At the bottom, add a concise takeaway in Korean: "AI 제품의 복잡도는 모델보다 절차와 시스템 경계에서 더 크게 생긴다".

The result must feel like a real strategy or architecture slide for a technical portfolio, not an illustration poster. Keep text brief and highly legible.
```

### Task 1: Lock slide scope and filenames

**Files:**
- Reference: `case-studies/hospital-customer-support-agent.md`
- Create: `docs/plans/2026-03-07-hospital-customer-support-agent-ppt-images.md`

**Step 1: Confirm the two-slide split fits the source**

Run: `sed -n '1,240p' case-studies/hospital-customer-support-agent.md`
Expected: the document naturally separates into overview/architecture and flow/design-decision sections.

**Step 2: Fix output filenames**

- `assets/hospital-customer-support-agent-ppt-overview.png`
- `assets/hospital-customer-support-agent-ppt-flow.png`

**Step 3: Keep the deck scope single-purpose**

Run: `rg -n "LangGraph|Qdrant|FastAPI|Next.js|ECS Fargate|pending_question|customer_interaction|상담원 연결" case-studies/hospital-customer-support-agent.md`
Expected: all required slide anchors exist in the source file.

### Task 2: Finalize prompt spec and prompt text

**Files:**
- Modify: `docs/plans/2026-03-07-hospital-customer-support-agent-ppt-images.md`

**Step 1: Verify the prompt spec covers slide style and legibility**

Run: `rg -n "16:9|white|teal|blue|website screenshot|poster|cartoon" docs/plans/2026-03-07-hospital-customer-support-agent-ppt-images.md`
Expected: layout, style, and avoidance rules are all present.

**Step 2: Verify both generation prompts include all required content anchors**

Run: `rg -n "primary_assistant|customer_interaction|extract_personal_info|Qdrant|FastAPI|Next.js|AWS ECS Fargate|개인정보 수집 후 원래 질문 복귀|AI 제품의 복잡도는 모델보다 절차와 시스템 경계에서 더 크게 생긴다" docs/plans/2026-03-07-hospital-customer-support-agent-ppt-images.md`
Expected: both architecture and flow prompts contain the required source concepts.

### Task 3: Verify image-generation readiness

**Files:**
- Check: `.codex/skills/image-generation/SKILL.md`
- Check: `.codex/skills/image-generation/scripts/generate-image`
- Check: `.claude/skills/image_generation/scripts/.env`

**Step 1: Verify the Codex image-generation workflow**

Run: `sed -n '1,220p' .codex/skills/image-generation/SKILL.md`
Expected: the workflow says to verify `GEMINI_API_KEY`, rewrite the prompt in English, choose aspect ratio, and use the wrapper script.

**Step 2: Verify the generation wrapper is executable**

Run: `test -x .codex/skills/image-generation/scripts/generate-image`
Expected: exit status `0`.

**Step 3: Verify the API key is configured without printing it**

Run: `test -f .claude/skills/image_generation/scripts/.env && rg -q '^GEMINI_API_KEY=' .claude/skills/image_generation/scripts/.env`
Expected: exit status `0`.

### Task 4: Generate the overview architecture slide

**Files:**
- Create: `assets/hospital-customer-support-agent-ppt-overview.png`
- Reference: `docs/plans/2026-03-07-hospital-customer-support-agent-ppt-images.md`

**Step 1: Run the generator for slide 1**

Run:

```bash
.codex/skills/image-generation/scripts/generate-image \
  --prompt "Create a polished 16:9 presentation slide image in Korean for a technical portfolio case study. The slide title is '병원 고객상담 AI Agent'. Add the subtitle '복잡한 병원 문의를 상태 기반 상담 흐름과 데이터 조회 구조로 처리한 AI 상담 시스템'. Use a clean white or very light background with restrained teal and blue accents, premium enterprise presentation typography, and a structured layout that looks like a real product engineering or architecture PPT slide. Include a compact meta section with '기간 2025.03 - 2025.05', '소속 와이즈에이아이', and '역할 핵심 아키텍트 + 일부 구현'. In the center, show a clear architecture diagram: User Inquiry flows into a LangGraph consultation engine, then branches into primary_assistant, customer_interaction, extract_personal_info, and tools. Connect those to Qdrant search, FastAPI plus LangGraph SDK API, a Next.js monitoring dashboard, and AWS ECS Fargate deployment. Add three short callout cards for '상태 기반 상담 흐름', '병원별 지식 조회', and '운영 가능한 서비스 경계'. The image should feel legible, balanced, and credible for a senior engineer portfolio. Use Korean labels where appropriate. Do not make it look like a poster, infographic, or website screenshot." \
  --name "hospital-customer-support-agent-ppt-overview" \
  --output "assets" \
  --aspect 16:9
```

Expected: a generated slide image is saved under `assets/`.

**Step 2: Verify the file exists**

Run: `ls -l assets/hospital-customer-support-agent-ppt-overview*`
Expected: a matching output file is present.

### Task 5: Generate the flow and design-decision slide

**Files:**
- Create: `assets/hospital-customer-support-agent-ppt-flow.png`
- Reference: `docs/plans/2026-03-07-hospital-customer-support-agent-ppt-images.md`

**Step 1: Run the generator for slide 2**

Run:

```bash
.codex/skills/image-generation/scripts/generate-image \
  --prompt "Create a polished 16:9 presentation slide image in Korean for a technical portfolio case study. The slide title is 'Consultation Flow + Design Decisions'. Add the subtitle '상담 흐름 분리, 병원별 지식 응답, 운영 가능한 서비스 경계'. Use the same visual language as a premium enterprise PPT slide: white or very light background, restrained teal and blue accents, sharp presentation typography, and a clean grid layout. On the left, show a simplified consultation flow with three paths: '일반 문의 처리', '개인정보 수집 후 원래 질문 복귀', and '상담원 연결 준비'. Use concrete mini examples such as asking weekend clinic hours, collecting name and phone number before resuming a pending implant question, and preparing a human handoff only after required info is present. On the right, show three design decision panels labeled 'LangGraph 상태 기반 워크플로우', '병원별 검색 기반 응답', and 'API·검색·대시보드·배포 경계'. At the bottom, add a concise takeaway in Korean: 'AI 제품의 복잡도는 모델보다 절차와 시스템 경계에서 더 크게 생긴다'. The result must feel like a real strategy or architecture slide for a technical portfolio, not an illustration poster. Keep text brief and highly legible." \
  --name "hospital-customer-support-agent-ppt-flow" \
  --output "assets" \
  --aspect 16:9
```

Expected: a generated slide image is saved under `assets/`.

**Step 2: Verify the file exists**

Run: `ls -l assets/hospital-customer-support-agent-ppt-flow*`
Expected: a matching output file is present.

### Task 6: Validate output quality and allow one revision pass

**Files:**
- Check: `assets/hospital-customer-support-agent-ppt-overview.png`
- Check: `assets/hospital-customer-support-agent-ppt-flow.png`

**Step 1: Inspect both slides against acceptance criteria**

Confirm:

- the two slides share one visual language
- Korean titles are readable
- the main architecture and flow structures are legible
- slide 1 and slide 2 have clearly different messages
- layout looks like a real presentation slide, not a poster

**Step 2: If one slide misses, revise only that prompt once**

Tighten the missing requirement, regenerate the single slide, and keep the other slide unchanged.

**Step 3: User-request note**

This task intentionally skips commit steps unless the user later asks for git actions.

