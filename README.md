# Career Harness

Career Harness는 사용자가 기존 이력서, LinkedIn, 경력기술서, 프로젝트 문서, GitHub 자료를 넣으면 AI와 함께 한국어 마스터 이력서와 슬라이드형 HTML 포트폴리오를 만드는 GitHub Template Repository다.

원본, AI 메모리, 초안, 최종 산출물을 분리하고 모든 중요한 경력 주장에 provenance를 연결한다. Codex, Claude Code, Cursor는 동일한 `AGENTS.md`, `memory/`, `.agents/skills/`를 사용한다.

## Quick Start

```bash
uv sync
./scripts/harness init
```

자료를 추가한다.

```text
sources/files/        PDF, DOCX, Markdown, TXT, HTML
sources/web/          인증정보 없는 웹 스냅샷
sources/github/       공개 GitHub 메타데이터
sources/interviews/   사용자 인터뷰 답변
sources/screenshots/  승인된 이미지 증거
```

AI에게 요청한다.

```text
$career-intake를 사용해 sources를 먼저 읽고 커리어 인터뷰를 시작해줘.
이미 확인된 내용은 다시 묻지 마.
```

자세한 온보딩은 `START_HERE.md`를 따른다.

## Data Flow

```text
sources/ -> memory/ -> drafts/ -> resume|case-studies|portfolio/
```

- `sources/`: 수정하지 않는 사용자 원본과 스냅샷
- `memory/`: AI가 자동 관리하는 출처 기반 커리어 메모리
- `targets/`: 채용공고와 맞춤 전략
- `drafts/`: outline, 전략, 승인 전 초안
- `resume/`: Markdown 마스터·맞춤 이력서와 PDF
- `case-studies/`: 프로젝트 케이스 스터디
- `portfolio/`: HTML, PDF, 시각 자산, 배포 결과

## Canonical Files

- `AGENTS.md`: 멀티 에이전트 운영 계약
- `harness.yaml`: 제품 설정
- `sources/manifest.yaml`: 원본 manifest
- `memory/state.yaml`: 사용자 작업 상태
- `.agents/skills/`: 공통 스킬 정본
- `privacy.allowlist.yaml`: 공개 연락처 허용 목록

Claude Code와 Cursor 어댑터는 정본을 복제하지 않는다.

```bash
uv run python scripts/setup_agents.py
uv run python scripts/setup_agents.py --check
```

## Skills

- `career-intake`: source 분석과 집중 인터뷰
- `career-memory`: 자동 메모리, provenance, 충돌 보존
- `master-resume`: 한국어 마스터 이력서
- `targeted-resume`: 마스터 기반 맞춤 이력서
- `career-review`: 사실·출처·개인정보·품질 감사
- `career-portfolio`: outline, 3개 테마, 슬라이드 HTML·PDF·시각 QA
- `agent-browser`: 로그인된 웹 자료 읽기
- `visualize`: 범용 HTML 시각화

## CLI

```bash
./scripts/harness init
./scripts/harness ingest sources/files/FILE
./scripts/harness check
./scripts/harness build resume
./scripts/harness build portfolio
./scripts/harness preview
./scripts/harness deploy
```

개별 모듈 명령과 인터뷰 기록 방법은 `START_HERE.md`와 `docs/workflow.md`에 있다.

## Resume

- 정본: `resume/master.md`
- 맞춤 이력서: `resume/tailored/<target>.md`
- PDF: `resume/master.pdf`
- 템플릿: `templates/resume/`

Markdown을 semantic HTML로 변환하고 Chromium으로 A4 PDF를 생성한다. 페이지 수, A4 크기, 링크, 텍스트 추출, 가로 overflow를 검사한다.

## Portfolio

- outline: `drafts/portfolio/outline.yaml`
- HTML: `portfolio/html/index.html`
- PDF: `portfolio/pdf/portfolio.pdf`
- 자산: `portfolio/assets/`
- 배포본: `portfolio/dist/`

기본 목표는 10장이며 자료에 따라 7~15장으로 조정한다. 모든 테마는 같은 semantic HTML과 컴포넌트를 사용한다.

- `editorial`: 서사와 증거의 균형
- `minimal`: 절제된 기업·컨설팅 스타일
- `technical`: 시스템·아키텍처 중심

렌더러는 1920×1080 PNG, contact sheet, 16:9 PDF를 만들고 overflow, 페이지 수, 크기, 텍스트 추출을 검사한다.

## Quality Gates

```bash
uv run pytest -q
uv run ruff check scripts tests
./scripts/harness check
```

통합 검사는 다음을 다룬다.

- YAML·JSON Schema와 source refs
- conflicted·비공개·출처 없는 claim
- 깨진 로컬 링크와 이미지
- alt text
- 비밀 키와 non-allowlisted 연락처
- 에이전트 adapter drift
- 포트폴리오 slide IDs와 memory IDs

## Synthetic End-to-End Test

`examples/sample-candidate/`는 실제 개인정보가 없는 합성 후보자다.

```bash
uv run python -m scripts.e2e_sample
```

이 명령은 A4 이력서 PDF, 10장 포트폴리오 PDF, 슬라이드 PNG, contact sheet, 정적 사이트와 검증 보고서를 `tmp/pdfs/e2e-sample/`에 생성한다.

## CI and Deployment

- `.github/workflows/check.yml`: push·PR 품질 검사
- `.github/workflows/deploy-pages.yml`: `portfolio/html/index.html`이 있을 때 GitHub Pages 배포
- `./scripts/harness preview`: 로컬 정적 사이트 미리보기

GitHub Pages가 기본 배포 대상이며 Cloudflare Pages는 선택적 어댑터로 확장할 수 있다.

## Design and Implementation

- 제품 설계: `docs/plans/2026-08-27-career-harness-product-design.md`
- 구현 계획·상태: `docs/plans/2026-08-27-career-harness-implementation.md`
- 사용자·AI 작업 흐름: `docs/workflow.md`
