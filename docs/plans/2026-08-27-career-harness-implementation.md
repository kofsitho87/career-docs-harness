# Career Harness Product Implementation Plan

## Goal

현재 개인 이력서·포트폴리오 저장소를 보존하면서, 새 사용자가 GitHub 템플릿으로 복제해 원본 수집부터 메모리, 마스터 이력서, 슬라이드 포트폴리오, 검증, GitHub Pages 배포까지 수행할 수 있는 제품형 하네스를 단계적으로 구현한다.

## Architecture

`sources -> memory -> drafts -> outputs`의 단방향 데이터 흐름을 정본으로 한다. `AGENTS.md`와 `.agents/skills/`는 플랫폼 공통 규칙이며 플랫폼별 파일은 어댑터로만 유지한다. Python 3.11과 `uv`를 기본 런타임으로 사용하고 PDF·시각 검증에는 Playwright를 사용한다.

## Implementation Principles

- 현재 개인 산출물은 예제 데이터로 분리하기 전까지 삭제하거나 덮어쓰지 않는다.
- 각 단계는 독립적으로 검증 가능해야 한다.
- 원본 `sources/`는 불변으로 취급한다.
- 자동 메모리는 모든 변경에 출처와 상태를 남긴다.
- 스킬을 만들거나 수정할 때는 `skill-creator` 지침과 검증기를 사용한다.
- 사용자-facing 명령은 최종적으로 `scripts/harness` 하나로 모은다.

---

## Phase 1. Product Foundation

### Task 1. Add product configuration and onboarding

**Files**

- Create: `harness.yaml`
- Create: `START_HERE.md`
- Modify: `README.md`

**Work**

1. 기본 언어, 단일 사용자, 마스터 이력서, 포트폴리오 형식, 테마, 메모리 자동 갱신, 배포 대상을 설정한다.
2. 사용자가 템플릿 복제 후 자료를 넣고 AI 인터뷰를 시작하는 단일 온보딩 경로를 작성한다.
3. README에서 개인 산출물 설명과 제품 사용 설명을 구분한다.

**Validation**

```bash
test -f harness.yaml
test -f START_HERE.md
rg -n "language|memory|portfolio|github_pages" harness.yaml
```

### Task 2. Add sources and memory skeleton

**Files**

- Create: `sources/manifest.yaml`
- Create: `sources/files/.gitkeep`
- Create: `sources/web/.gitkeep`
- Create: `sources/github/.gitkeep`
- Create: `sources/screenshots/.gitkeep`
- Create: `memory/candidate.md`
- Create: `memory/preferences.yaml`
- Create: `memory/timeline.yaml`
- Create: `memory/claims.yaml`
- Create: `memory/evidence.yaml`
- Create: `memory/conflicts.yaml`
- Create: `memory/decisions.md`
- Create: `memory/changelog.md`
- Create: `memory/state.yaml`
- Create: `memory/experience/.gitkeep`
- Create: `memory/projects/.gitkeep`
- Create: `targets/.gitkeep`
- Create: `drafts/resume/.gitkeep`
- Create: `drafts/portfolio/.gitkeep`

**Work**

1. 각 파일에 완성된 개인 사실 대신 스키마와 빈 기본값만 둔다.
2. 상태는 `not_started`, `in_progress`, `needs_review`, `complete`를 사용한다.
3. 출처 상태는 `verified`, `inferred`, `unverified`, `conflicted`를 사용한다.

**Validation**

```bash
find sources memory targets drafts -maxdepth 2 -type f | sort
rg -n "verified|inferred|unverified|conflicted" memory
```

---

## Phase 2. Agent Contract and Portability

### Task 3. Rewrite AGENTS.md as a product operating contract

**Files**

- Modify: `AGENTS.md`
- Modify: `CLAUDE.md`
- Create: `.cursor/rules/career-harness.mdc`
- Create: `scripts/setup_agents.py`

**Work**

1. 사실 권한 순서, 메모리 자동 갱신, 충돌 처리, 마스터 우선, 승인·완료 조건을 정의한다.
2. 플랫폼별 파일은 `AGENTS.md`를 복제하지 않고 참조하거나 생성되게 한다.
3. 지원 플랫폼별 어댑터가 정본과 drift하지 않는지 검사한다.

**Validation**

```bash
uv run python scripts/setup_agents.py --check
rg -n "sources/|memory/|resume/master.md" AGENTS.md
```

---

## Phase 3. Source Ingestion and Memory Engine

### Task 4. Define source manifest and memory schemas

**Files**

- Create: `pyproject.toml`
- Create: `schemas/harness.schema.json`
- Create: `schemas/source-manifest.schema.json`
- Create: `schemas/preferences.schema.json`
- Create: `schemas/timeline.schema.json`
- Create: `schemas/claims.schema.json`
- Create: `schemas/evidence.schema.json`
- Create: `schemas/conflicts.schema.json`
- Create: `scripts/lib/schema.py`

**Work**

1. 필수 필드, ID 규칙, 날짜 형식, 상태 enum을 정의한다.
2. source reference는 파일 경로 또는 URL, 캡처 시간, 해시를 가진다.
3. 사용자 수정값을 보호할 수 있는 provenance 필드를 둔다.

### Task 5. Implement file ingestion

**Files**

- Create: `scripts/lib/ingest_files.py`
- Create: `scripts/lib/source_manifest.py`
- Create: `tests/test_ingest_files.py`
- Create: `tests/fixtures/sources/`

**Work**

1. PDF, DOCX, Markdown, TXT, HTML의 텍스트를 추출한다.
2. 원본 해시와 메타데이터를 manifest에 기록한다.
3. 원본 파일을 수정하지 않는다.
4. 동일 파일 중복 수집을 방지한다.

### Task 6. Support browser and GitHub sources

**Files**

- Modify: `.agents/skills/agent-browser/SKILL.md` only when product-specific routing is required
- Create: `docs/guides/web-source-capture.md`
- Create: `scripts/lib/ingest_web_snapshot.py`
- Create: `scripts/lib/ingest_github.py`

**Work**

1. 로그인된 브라우저로 LinkedIn을 읽고 인증정보 없이 스냅샷을 저장한다.
2. URL, 수집 시각, 해시, 추출 범위를 manifest에 기록한다.
3. GitHub 프로필, 공개 저장소, README, 공개 기여를 보조 증거로 수집한다.

### Task 7. Implement memory validation and merge

**Files**

- Create: `scripts/lib/memory_merge.py`
- Create: `scripts/lib/validate_memory.py`
- Create: `tests/test_memory_merge.py`
- Create: `tests/test_validate_memory.py`

**Work**

1. 출처가 같은 사실은 병합한다.
2. 상충하는 날짜·직책·수치는 conflict로 분기한다.
3. 사용자 직접 수정값을 우선한다.
4. 모든 자동 변경을 changelog에 기록한다.

---

## Phase 4. Career Skills

### Task 8. Create career-intake skill

**Files**

- Create: `.agents/skills/career-intake/SKILL.md`
- Create: `.agents/skills/career-intake/references/interview.md`
- Create: `.agents/skills/career-intake/references/source-routing.md`
- Create: `.agents/skills/career-intake/agents/openai.yaml`
- Create: `scripts/lib/record_interview.py`
- Create: `sources/interviews/.gitkeep`

**Behavior**

- 원본을 먼저 읽는다.
- 이미 확인된 내용을 다시 묻지 않는다.
- 한 번에 필요한 질문만 묻는다.
- 답변을 memory 후보로 구조화한다.
- 중단 후 `state.yaml`에서 재개한다.

### Task 9. Create career-memory skill

**Files**

- Create: `.agents/skills/career-memory/SKILL.md`
- Create: `.agents/skills/career-memory/references/memory-model.md`
- Create: `.agents/skills/career-memory/agents/openai.yaml`

**Behavior**

- 자동 메모리 수정
- 출처와 상태 기록
- 충돌 보존
- 사용자 수정 우선
- changelog 갱신

### Task 10. Create master-resume and targeted-resume skills

**Files**

- Create: `.agents/skills/master-resume/`
- Create: `.agents/skills/targeted-resume/`
- Create: `templates/resume/master.md`
- Create: `templates/resume/tailored.md`

**Behavior**

- 한국어 마스터 이력서 우선
- 맞춤 이력서는 마스터에서만 파생
- verified 주장만 사용
- ATS, 가독성, 중복, 분량 검사

### Task 11. Create career-review skill

**Files**

- Create: `.agents/skills/career-review/`

**Behavior**

- 작성과 독립된 검토
- 사실·수치·기간 일치
- 과장·모호한 기여 탐지
- 링크·자산·개인정보·레이아웃 확인

---

## Phase 5. Resume Build Pipeline

### Task 12. Build Markdown resume to PDF

**Files**

- Create: `scripts/lib/build_resume.py`
- Create: `templates/resume/resume.css`
- Create: `tests/test_build_resume.py`

**Work**

1. Markdown을 HTML로 변환한다.
2. Chromium으로 A4 PDF를 생성한다.
3. 페이지 수, 링크, 텍스트 추출, overflow를 검증한다.

---

## Phase 6. Portfolio Skill and Themes

### Task 13. Create career-portfolio skill

**Files**

- Create: `.agents/skills/career-portfolio/SKILL.md`
- Create: `.agents/skills/career-portfolio/references/narrative-architecture.md`
- Create: `.agents/skills/career-portfolio/references/slide-patterns.md`
- Create: `.agents/skills/career-portfolio/references/content-density.md`
- Create: `.agents/skills/career-portfolio/references/evidence-design.md`
- Create: `.agents/skills/career-portfolio/references/design-system.md`
- Create: `.agents/skills/career-portfolio/references/visual-qa.md`
- Create: `.agents/skills/career-portfolio/agents/openai.yaml`

**Behavior**

1. 메모리와 마스터 이력서를 읽는다.
2. 포지셔닝과 대표 프로젝트를 정한다.
3. 7~15장 범위의 outline을 먼저 만든다.
4. 슬라이드마다 claim/evidence ID를 연결한다.
5. 테마를 선택하고 HTML을 구현한다.
6. contact sheet와 PDF를 검토한다.

### Task 14. Add base slide runtime and themes

**Files**

- Create: `templates/portfolio/base/index.html`
- Create: `templates/portfolio/base/presentation.js`
- Create: `templates/portfolio/base/components.css`
- Create: `templates/portfolio/themes/editorial/theme.css`
- Create: `templates/portfolio/themes/minimal/theme.css`
- Create: `templates/portfolio/themes/technical/theme.css`
- Create: `schemas/portfolio-outline.schema.json`

**Work**

- CSS token 기반 테마
- 키보드 탐색
- 16:9 화면·인쇄
- 반응형 미리보기
- accessible labels와 alt text

### Task 15. Add portfolio visual QA

**Files**

- Create: `scripts/lib/render_portfolio.py`
- Create: `scripts/lib/validate_slides.py`
- Create: `scripts/lib/create_contact_sheet.py`
- Create: `tests/test_portfolio_build.py`

**Validation**

- 1920x1080 렌더링
- overflow·누락 자산·빈 슬라이드
- PDF 페이지 수와 크기
- 텍스트 추출과 링크
- 테마별 snapshot

---

## Phase 7. Unified CLI and Quality Gates

### Task 16. Create scripts/harness

**Files**

- Create: `scripts/harness`
- Create: `scripts/lib/cli.py`

**Commands**

```text
init
ingest
check
build resume
build portfolio
preview
deploy
```

### Task 17. Add integrated checks

**Files**

- Create: `scripts/lib/validate_claims.py`
- Create: `scripts/lib/validate_links.py`
- Create: `scripts/lib/validate_assets.py`
- Create: `scripts/lib/scan_sensitive_info.py`

`./scripts/harness check`는 스키마, 메모리, 주장, 링크, 자산, 개인정보, Markdown, PDF, HTML 검사를 모두 실행한다.

---

## Phase 8. GitHub Template and Deployment

### Task 18. Add GitHub Actions

**Files**

- Create: `.github/workflows/check.yml`
- Create: `.github/workflows/deploy-pages.yml`

**Work**

- PR과 push에서 하네스 검사
- `portfolio/dist/` 빌드
- GitHub Pages 배포
- 인증정보 없이 동작

### Task 19. Separate personal example data

**Files**

- Create: `examples/sample-candidate/`
- Move or transform current personal content only after explicit review
- Update: `.gitignore`
- Update: `README.md`

**Work**

1. 제품 템플릿에 실제 개인정보가 기본값으로 남지 않게 한다.
2. 현재 저장소의 완성 산출물은 예제 또는 별도 브랜치로 보존한다.
3. 템플릿 초기화 후 빈 사용자 상태가 되게 한다.

---

## Phase 9. End-to-End Product Test

### Task 20. Test a clean user journey

**Scenario**

1. 빈 템플릿 복제
2. 샘플 이력서·프로젝트 문서 투입
3. 원본 수집과 메모리 생성
4. 인터뷰 재개
5. 한국어 마스터 이력서 Markdown·PDF 생성
6. 세 테마 중 하나로 약 10장 포트폴리오 생성
7. PDF와 local preview 생성
8. GitHub Pages 배포 준비
9. Codex, Claude Code, Cursor에서 동일 규칙 확인

**Completion Criteria**

- 한 명령 검사가 통과한다.
- 핵심 주장에 source reference가 있다.
- 충돌 사실이 최종 산출물로 새지 않는다.
- 마스터와 맞춤 이력서 간 사실이 일치한다.
- HTML과 PDF에 깨진 링크·자산·overflow가 없다.
- 플랫폼별 에이전트가 같은 메모리와 스킬을 사용한다.

## Current Execution Point

Phase 1~11을 구현했다. 제품 설정·온보딩·메모리와 source engine, OpenWiki-first 로컬·GitHub 프로젝트 repository snapshot, 멀티 에이전트 계약, 커리어 스킬, Markdown 이력서 A4 PDF, `career-portfolio`와 3개 테마, 슬라이드 PNG·contact sheet·PDF QA, 통합 CLI와 품질 게이트, GitHub Actions·Pages, 합성 후보자 end-to-end 테스트가 준비됐다. 개인 산출물과 과거 개인 작업 계획은 `main`에 보존하고 제품 브랜치에서는 제거해 GitHub Template 기준선을 정리했다.

---

## Phase 10. Project Repository Ingestion

### Task 21. Ingest local and GitHub project repositories

**Files**

- Create: `sources/projects/.gitkeep`
- Create: `scripts/lib/ingest_project.py`
- Create: `tests/test_ingest_project.py`
- Modify: `harness.yaml`, source schemas, `scripts/lib/cli.py`
- Modify: `career-intake` source routing, `README.md`, `START_HERE.md`, `docs/workflow.md`

**Work**

1. 로컬 Git 경로와 GitHub URL을 입력받는다.
2. 원본 저장소를 수정하지 않고 tracked tree, 주요 문서·manifest, Git metadata를 snapshot한다.
3. 코드 본문은 기본 제외하고 `--include-code`에서만 안전 제한과 secret 검사를 적용한다.
4. snapshot을 `sources/projects/`와 manifest에 `project_repository` source로 기록한다.
5. repository 내용에서 역할·성과를 자동 추론하지 않고 intake 인터뷰로 확인한다.

**Validation**

```bash
./scripts/harness ingest-project /path/to/repository
./scripts/harness ingest-project https://github.com/owner/repository
uv run pytest -q tests/test_ingest_project.py
```

**Status:** Complete. Local repositories and GitHub URLs share the same immutable snapshot pipeline. Tests cover source-repository immutability, duplicate ingestion, docs-only defaults, safe code inclusion, sensitive-file exclusion, and temporary GitHub clone routing.

---

## Phase 11. OpenWiki-First Project Ingestion

### Task 22. Prefer OpenWiki when a project wiki exists

**Files**

- Modify: `scripts/lib/ingest_project.py`, CLI, schemas, harness settings
- Modify: `career-intake`, `README.md`, `START_HERE.md`, `docs/workflow.md`
- Extend: `tests/test_ingest_project.py`

**Work**

1. 프로젝트 루트의 `openwiki/`를 감지한다.
2. 원본 checkout을 보호하기 위해 임시 clone과 wiki copy를 만든다.
3. `openwiki code -p`로 career-oriented project briefing을 비대화형 생성한다.
4. briefing과 `openwiki/**/*.md`를 snapshot의 최우선 섹션으로 포함한다.
5. `auto|required|off` 모드와 fallback/error semantics를 제공한다.

**Validation**

- OpenWiki가 없는 저장소는 기존 snapshot과 동일하게 동작한다.
- auto mode는 CLI failure에서 wiki Markdown으로 fallback한다.
- required mode는 missing wiki·CLI failure를 거부한다.
- OpenWiki runner는 원본 경로가 아닌 임시 clone을 받는다.
- snapshot metadata는 detected/used/pages/error 상태를 기록한다.

**Status:** Complete against the installed official OpenWiki v0.4.0 CLI contract. The harness uses `openwiki code -p` only in an isolated temporary clone and never runs init/update against the user's checkout.
