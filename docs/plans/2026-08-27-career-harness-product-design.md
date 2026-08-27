# Career Harness Product Design

## 1. 목적

이 저장소를 완성된 개인 이력서·포트폴리오 보관소에서, 사용자가 GitHub 템플릿을 복제해 자신의 자료를 넣으면 AI와 함께 한국어 마스터 이력서와 슬라이드형 포트폴리오를 만들 수 있는 제품형 하네스로 확장한다.

하네스는 특정 AI 제품에 종속되지 않는다. `AGENTS.md`, 저장소 기반 메모리, 공통 스킬, 결정적 검증 도구를 정본으로 두고 Codex, Claude Code, Cursor가 같은 사실과 작업 규칙을 사용하게 한다.

## 2. 인터뷰로 확정한 제품 결정

- 한 저장소는 사용자 한 명만 관리한다.
- 배포 형태는 GitHub Template Repository를 기본으로 한다.
- 사용자는 기존 이력서, LinkedIn, 경력기술서, 프로젝트 문서, GitHub 등 어떤 소스도 제공할 수 있다.
- 로그인된 브라우저에서 LinkedIn과 기타 웹 프로필을 직접 읽는 흐름을 지원한다.
- 기본 언어는 한국어다.
- 마스터 이력서는 Markdown이 정본이며 PDF로 변환할 수 있어야 한다.
- 맞춤 이력서는 마스터 이력서에서 파생한다.
- 포트폴리오는 슬라이드형 HTML이며 전용 설계·디자인 스킬이 담당한다.
- 포트폴리오는 약 10장을 기본 목표로 하되 사용자 경력과 프로젝트 수에 따라 7~15장 범위에서 조절한다.
- 포트폴리오는 여러 테마 중 선택할 수 있어야 한다.
- Chromium·Playwright 기반 PDF와 시각 검증 의존성을 허용한다.
- 로컬 미리보기와 GitHub Pages 배포를 기본 지원한다.
- AI는 저장소 메모리를 자동 갱신한다.

## 3. 제품 정의

> 다양한 경력 자료를 불변 원본으로 수집하고, AI가 출처 기반 커리어 메모리를 자동 구축한 뒤, 검증된 사실로 한국어 마스터 이력서와 테마형 슬라이드 포트폴리오를 생성·검증·배포하는 멀티 에이전트 호환 GitHub 하네스.

## 4. 핵심 원칙

### 4.1 원본·메모리·산출물 분리

```text
sources/ -> memory/ -> drafts/ -> resume|case-studies|portfolio/
```

- `sources/`는 사용자가 제공한 불변 원본이다.
- `memory/`는 AI가 원본에서 추출하고 정규화한 영구 기억이다.
- `drafts/`는 승인 전 구조·전략·초안이다.
- 최종 산출물은 검증된 메모리에서만 사실을 가져온다.

### 4.2 자동 메모리와 출처 추적

AI는 메모리를 자동 갱신할 수 있다. 대신 모든 사실은 출처와 상태를 가져야 한다.

- `verified`: 명시적 원본으로 확인됨
- `inferred`: 여러 자료를 바탕으로 추론됨
- `unverified`: 출처가 부족함
- `conflicted`: 서로 다른 원본이 충돌함

충돌한 값은 덮어쓰지 않고 `memory/conflicts.yaml`에 기록한다. 사용자가 직접 수정한 값은 자동 추론보다 우선한다.

### 4.3 마스터 우선

`resume/master.md`가 모든 맞춤 이력서의 상위 원본이다. 맞춤 이력서는 내용의 우선순위, Summary, 키워드, 분량만 바꿀 수 있고 새로운 사실을 만들 수 없다.

### 4.4 한곳에서 관리하는 에이전트 규칙

- 공통 운영 계약: `AGENTS.md`
- 공통 스킬: `.agents/skills/`
- 공통 설정: `harness.yaml`
- 플랫폼별 파일은 정본을 참조하는 얇은 어댑터로만 유지한다.

## 5. 목표 디렉터리

```text
.
├── START_HERE.md
├── AGENTS.md
├── CLAUDE.md
├── harness.yaml
├── sources/
│   ├── files/
│   ├── web/
│   ├── github/
│   ├── screenshots/
│   └── manifest.yaml
├── memory/
│   ├── candidate.md
│   ├── preferences.yaml
│   ├── timeline.yaml
│   ├── experience/
│   ├── projects/
│   ├── claims.yaml
│   ├── evidence.yaml
│   ├── conflicts.yaml
│   ├── decisions.md
│   ├── changelog.md
│   └── state.yaml
├── targets/
├── drafts/
│   ├── resume/
│   └── portfolio/
├── templates/
│   ├── resume/
│   └── portfolio/
│       ├── base/
│       └── themes/
│           ├── editorial/
│           ├── minimal/
│           └── technical/
├── resume/
│   ├── master.md
│   ├── master.pdf
│   └── tailored/
├── case-studies/
├── portfolio/
│   ├── html/
│   ├── pdf/
│   ├── assets/
│   └── dist/
├── .agents/skills/
├── scripts/
├── tests/
└── .github/workflows/
```

## 6. 사용자 여정

1. GitHub 템플릿을 복제한다.
2. `START_HERE.md`를 읽고 하네스를 초기화한다.
3. 기존 경력 자료를 `sources/`에 넣는다.
4. AI에게 커리어 인터뷰를 요청한다.
5. AI가 로컬 파일과 로그인된 브라우저의 웹 프로필을 읽는다.
6. AI가 `memory/`를 자동 구축하고 충돌·누락을 인터뷰한다.
7. 검증된 사실로 `resume/master.md`를 만든다.
8. 포트폴리오 outline과 테마를 정한 뒤 슬라이드 HTML을 만든다.
9. 링크·자산·주장·개인정보·레이아웃을 검사한다.
10. PDF와 사이트를 빌드하고 로컬 미리보기 또는 GitHub Pages로 배포한다.

## 7. 메모리 모델

### 7.1 후보자 메모리

`memory/candidate.md`는 이름, 연락처, 포지셔닝, 목표 역할, 언어, 지역·근무 선호를 관리한다.

### 7.2 경력과 프로젝트

`memory/experience/`와 `memory/projects/`는 사람에게 읽기 쉬운 Markdown과 구조화된 YAML frontmatter를 함께 사용한다.

### 7.3 주장 장부

`memory/claims.yaml`은 이력서와 포트폴리오에서 사용할 수 있는 성과·역할 주장을 관리한다. 각 항목은 ID, 문장, 프로젝트, 상태, 출처, 공개 범위, 허용 산출물을 가진다.

### 7.4 증거 장부

`memory/evidence.yaml`은 문서, URL, GitHub 저장소, 이미지, 스크린샷을 주장과 연결한다. 브라우저 인증 정보와 쿠키는 저장소에 기록하지 않는다.

### 7.5 상태와 변경 기록

- `state.yaml`: 현재 단계, 완료 작업, 대기 질문
- `conflicts.yaml`: 충돌한 사실
- `changelog.md`: AI의 메모리 갱신 이력
- `decisions.md`: 사용자와 확정한 전략·표현 결정

## 8. 스킬 구성

### 8.1 career-intake

다양한 원본을 읽고 경력 타임라인, 프로젝트, 성과, 기술, 누락 질문을 추출한다. 로그인된 브라우저 수집은 기존 `agent-browser`를 사용하되 결과는 `sources/web/`에 스냅샷으로 남긴다.

### 8.2 career-memory

원본과 인터뷰 답변을 메모리 스키마로 정규화하고 출처·신뢰도·충돌·변경 기록을 관리한다.

### 8.3 master-resume

검증된 메모리로 한국어 마스터 이력서를 작성하고 ATS, 중복, 성과 표현, 분량을 점검한다.

### 8.4 targeted-resume

채용공고와 마스터 이력서를 비교해 `resume/tailored/`에 맞춤 이력서를 파생한다.

### 8.5 career-portfolio

포지셔닝, 프로젝트 선택, 슬라이드 outline, 주장·증거 연결, 테마 선택, HTML 구현, 시각 QA를 담당한다. 바로 HTML을 만들지 않고 `drafts/portfolio/outline.yaml`을 먼저 만든다.

### 8.6 career-review

작성과 독립된 검토 단계로 사실 일치, 과장, ATS, 개인정보, 링크, 자산, 슬라이드 밀도와 시각 결과를 검사한다.

## 9. 포트폴리오 설계

### 9.1 슬라이드 수

- 목표: 10장
- 최소: 7장
- 최대: 15장
- 한 슬라이드당 핵심 주장 하나
- 자료가 부족하면 억지로 장수를 채우지 않는다.

### 9.2 기본 구성

1. Cover
2. Professional positioning
3. Career map
4. Representative project
5. Problem and constraints
6. Architecture
7. Key technical decision
8. Evidence and results
9. Additional project or expansion
10. My role and closing

### 9.3 테마

- `editorial`: 서사와 증거의 균형
- `minimal`: 절제된 기업·컨설팅 스타일
- `technical`: 시스템 구조와 기술 설명 중심

테마는 HTML을 복제하지 않고 CSS 디자인 토큰과 컴포넌트 변형으로 구현한다.

## 10. 도구와 단일 진입점

사용자가 기억할 도구는 `scripts/harness` 하나로 제한한다.

```bash
./scripts/harness init
./scripts/harness ingest
./scripts/harness check
./scripts/harness build resume
./scripts/harness build portfolio
./scripts/harness preview
./scripts/harness deploy
```

내부 도구는 원본 추출, 메모리·주장·링크·자산·개인정보 검증, PDF 빌드, contact sheet 생성, 로컬 서버, GitHub Pages 배포를 담당한다.

## 11. 배포

- 기본: GitHub Pages
- 로컬: `portfolio/dist/` 미리보기 서버
- 선택: Cloudflare Pages 어댑터
- 배포 입력은 `portfolio/html/`과 필요한 자산이며 `portfolio/dist/`는 재생성 가능해야 한다.

## 12. 제품 안전성과 개인정보

- 인증 상태, 쿠키, 토큰은 Git에 저장하지 않는다.
- `sources/`의 원본은 자동 수정하지 않는다.
- 사용자가 명시한 공개 범위를 존중한다.
- 개인정보 검사는 기본 활성화하되 사용자의 공개 연락처는 allowlist로 관리한다.
- 출처 없는 수치와 경력은 최종 산출물에 포함하지 않는다.

## 13. MVP 범위

### 포함

- GitHub 템플릿과 한 명의 사용자
- 한국어 마스터 이력서 Markdown·PDF
- 파일·웹·GitHub 원본 수집
- 자동 메모리와 출처 추적
- 약 10장의 슬라이드 HTML·PDF
- editorial, minimal, technical 테마
- 로컬 미리보기와 GitHub Pages
- Codex, Claude Code, Cursor 공통 운영
- 한 명령 통합 검증

### 제외

- 여러 사용자 동시 관리
- 웹 기반 관리자 UI
- 채용 지원 자동 제출
- 비공개 계정 인증정보 저장
- 완전 자동 사실 충돌 해결
- 초기 MVP의 다국어 동시 생성

## 14. 성공 기준

- 새로운 사용자가 저장소 구조를 몰라도 `START_HERE.md`만으로 시작할 수 있다.
- 원본 투입 후 인터뷰를 중단하고 다시 이어갈 수 있다.
- 모든 핵심 주장에 출처 또는 명시적 상태가 있다.
- 마스터 이력서에서 맞춤 이력서를 안전하게 파생할 수 있다.
- 세 테마 중 하나로 슬라이드 포트폴리오를 생성할 수 있다.
- Markdown, PDF, HTML, 로컬 미리보기, GitHub Pages가 동일한 사실을 사용한다.
- 에이전트를 바꿔도 같은 메모리와 작업 규칙을 따른다.
- `./scripts/harness check`가 전체 품질 게이트를 실행한다.
