# Resume Rewrite Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rewrite the existing resume into a cleaner, ATS-friendly document targeted at a senior full-stack / AI-capable product engineer role.

**Architecture:** Preserve the factual career history from the original resume, but reorganize it around a tighter summary, grouped core skills, and outcome-oriented experience bullets. Compress lower-signal sections, elevate links and recent impact, and standardize wording for consistency.

**Tech Stack:** Markdown, ATS-friendly resume structure, Korean professional writing

---

### Task 1: Define the rewrite structure

**Files:**
- Create: `docs/plans/2026-03-07-resume-rewrite.md`
- Modify: `resume.md`
- Create: `resume-product-engineer.md`

**Step 1: Identify the target role and key message**

Use the approved positioning: `시니어 풀스택/AI 가능한 프로덕트 엔지니어`.

**Step 2: Lock the new section order**

Use this order:
- Header with contact and links
- Professional Summary
- Core Competencies
- Experience
- Education
- Open Source / Additional
- Language

**Step 3: Decide what to compress**

Compress:
- Old or low-signal miscellaneous items
- Long narrative project descriptions
- Redundant skill mentions

**Step 4: Decide what to emphasize**

Emphasize:
- End-to-end product delivery
- AI feature implementation in production
- Frontend + backend + infra ownership
- Measurable performance and delivery outcomes

### Task 2: Draft the new resume file

**Files:**
- Modify: `resume.md`
- Create: `resume-product-engineer.md`

**Step 1: Write a stronger summary**

Replace aspiration-driven wording with evidence-driven positioning.

**Step 2: Rewrite recent experience**

Rewrite WiseAI and TwoSunWorld so each project highlights:
- product/problem context
- direct ownership
- technologies used
- outcome or measurable impact

**Step 3: Rebuild the skills section**

Group skills into:
- Frontend
- Backend
- AI / LLM
- Data / Search
- Infrastructure / DevOps

**Step 4: Trim supporting sections**

Keep only the strongest supporting items that reinforce the target role.

### Task 3: Review and polish

**Files:**
- Review: `resume-product-engineer.md`

**Step 1: Check consistency**

Verify naming, capitalization, and technology labels are consistent.

**Step 2: Check ATS readability**

Ensure the document uses standard headings, plain text links, and no decorative structure.

**Step 3: Check message alignment**

Verify the resume reads first as a senior product engineer, and second as someone with strong AI implementation experience.
