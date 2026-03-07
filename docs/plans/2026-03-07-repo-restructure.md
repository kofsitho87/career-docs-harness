# Repository Restructure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reorganize the repository into a clearer harness structure with separate locations for source documents, guides, final outputs, and assets.

**Architecture:** Move the current resume, portfolio, origin source, guide, and infographic asset into function-based directories without rewriting their substantive content. After moving files, update all known internal references so the new structure remains self-consistent.

**Tech Stack:** Markdown, repository structure, file reference maintenance

---

### Task 1: Create the target directory structure

**Files:**
- Create: `resume/`
- Create: `case-studies/`
- Create: `assets/`
- Create: `docs/source/`
- Create: `docs/guides/`

**Step 1: Create the final-output directories**

Create:
- `resume/`
- `case-studies/`
- `assets/`

**Step 2: Create the document-support directories**

Create:
- `docs/source/`
- `docs/guides/`

**Step 3: Verify the intended structure**

Confirm that the repository now has clear destinations for:
- final resume output
- final portfolio output
- assets
- source-of-truth docs
- reusable guides

### Task 2: Move the main content files into the new structure

**Files:**
- Move: `dan-resume-product-engineer.md` -> `resume/product-engineer.md`
- Move: `projects/portfolio-outbound-voice-agent.md` -> `case-studies/outbound-voice-agent.md`
- Move: `heewung-song-infographic.png` -> `assets/heewung-song-infographic.png`
- Move: `docs/origin-resume.md` -> `docs/source/origin-resume.md`
- Move: `docs/resume-guidelines/resume-guide.md` -> `docs/guides/resume-guide.md`

**Step 1: Move the final outputs**

Move the current resume and portfolio deliverables into:
- `resume/product-engineer.md`
- `case-studies/outbound-voice-agent.md`

**Step 2: Move the shared source and guide docs**

Move the baseline resume and reusable guide into:
- `docs/source/origin-resume.md`
- `docs/guides/resume-guide.md`

**Step 3: Move the infographic asset**

Move the infographic into:
- `assets/heewung-song-infographic.png`

### Task 3: Update internal references to the new paths

**Files:**
- Modify: `README.md`
- Modify: `docs/workflow.md`
- Modify: `resume/product-engineer.md`
- Modify: `docs/plans/2026-03-07-repo-documentation.md`

**Step 1: Update README references**

Change references to:
- `resume/product-engineer.md`
- `case-studies/outbound-voice-agent.md`
- `assets/heewung-song-infographic.png`
- `docs/source/origin-resume.md`
- `docs/guides/resume-guide.md`

**Step 2: Update workflow references**

Change references to the same new paths and keep the explanatory structure intact.

**Step 3: Update in-file asset references**

In `resume/product-engineer.md`, update the infographic image link to the new relative asset path.

**Step 4: Update the repository-documentation implementation plan**

Update any checked file paths in `docs/plans/2026-03-07-repo-documentation.md` so the plan reflects the new structure.

### Task 4: Review the restructured repository for consistency

**Files:**
- Review: `README.md`
- Review: `docs/workflow.md`
- Review: `resume/product-engineer.md`
- Review: `docs/plans/2026-03-07-repo-documentation.md`

**Step 1: Search for stale paths**

Search for remaining references to:
- `dan-resume-product-engineer.md`
- `projects/portfolio-outbound-voice-agent.md`
- `heewung-song-infographic.png`
- `docs/origin-resume.md`
- `docs/resume-guidelines/resume-guide.md`

**Step 2: Verify moved files exist**

Confirm the new files exist at:
- `resume/product-engineer.md`
- `case-studies/outbound-voice-agent.md`
- `assets/heewung-song-infographic.png`
- `docs/source/origin-resume.md`
- `docs/guides/resume-guide.md`

**Step 3: Check documentation accuracy**

Ensure `README.md` and `docs/workflow.md` describe the new structure correctly and do not mention the old layout as current state.
