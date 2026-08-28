# Career Harness 시작하기

이 저장소는 기존 경력 자료를 바탕으로 AI와 함께 한국어 마스터 이력서와 슬라이드형 HTML 포트폴리오를 만드는 제품형 하네스다.

## 처음 시작하는 순서

1. GitHub에서 이 저장소를 템플릿으로 사용해 새 저장소를 만든다.
2. `uv run python scripts/setup_agents.py`를 실행해 Claude Code와 Cursor 어댑터를 준비한다.
3. 기존 이력서, 경력기술서, 프로젝트 문서, 인증서, 스크린샷을 `sources/files/` 또는 `sources/screenshots/`에 넣는다. 수행한 프로젝트의 GitHub URL이나 로컬 Git 경로가 있다면 `ingest-project`로 먼저 등록한다.
4. LinkedIn이나 웹 프로필을 읽어야 한다면 로그인된 브라우저를 준비한다. 인증정보와 쿠키는 저장소에 저장하지 않는다.
5. AI에게 다음과 같이 요청한다.

```text
$career-intake를 사용해 이 저장소의 커리어 인터뷰를 시작해줘.
sources/의 자료를 먼저 확인하고, 이미 확인된 내용은 다시 묻지 마.
```

6. AI는 `$career-memory`로 `memory/`를 자동 갱신하고 출처가 충돌하거나 부족한 내용만 질문한다.
7. 메모리가 준비되면 `$master-resume`으로 `resume/master.md`를 생성한다.
8. 마스터 이력서를 기준으로 포트폴리오 outline, 테마, 슬라이드 HTML을 만든다.
9. 공개할 이메일·전화번호·URL을 `privacy.allowlist.yaml`에 등록한다.
10. `./scripts/harness check`로 전체 결과를 검사한다.

어댑터가 정본과 일치하는지는 다음 명령으로 확인한다.

```bash
uv run python scripts/setup_agents.py --check
```

## 현재 사용할 수 있는 수집·검증 명령

`sources/files/`에 넣은 PDF, DOCX, Markdown, TXT, HTML을 추출하고 manifest에 등록한다.

```bash
uv run python -m scripts.lib.ingest_files sources/files/FILE
```

브라우저에서 읽은 인증정보 없는 텍스트 스냅샷을 등록한다.

```bash
uv run python -m scripts.lib.ingest_web_snapshot \
  --url "https://example.com/profile" \
  --title "Profile" \
  --input /tmp/profile.txt
```

공개 GitHub 프로필과 공개 저장소 메타데이터를 수집한다.

```bash
uv run python -m scripts.lib.ingest_github USERNAME
```

현재 manifest와 memory가 스키마·출처 규칙을 지키는지 검사한다.

```bash
uv run python -m scripts.lib.validate_memory
```

## 통합 명령

```bash
./scripts/harness init
./scripts/harness ingest sources/files/FILE
./scripts/harness ingest-project /path/to/project
./scripts/harness ingest-project https://github.com/owner/repository
./scripts/harness check
./scripts/harness build resume
./scripts/harness build portfolio
./scripts/harness preview
./scripts/harness deploy
```

GitHub Actions는 push와 pull request에서 품질 검사를 실행하고, `portfolio/html/index.html`이 준비된 main 브랜치에서는 GitHub Pages 배포본을 생성한다.

## 자료를 넣는 위치

```text
sources/files/        PDF, DOCX, Markdown, TXT, HTML
sources/web/          LinkedIn 등 웹 페이지의 인증정보 없는 스냅샷
sources/github/       GitHub 프로필과 저장소 요약
sources/projects/     프로젝트 Git 저장소의 문서·tree·history snapshot
sources/interviews/   AI 인터뷰에서 사용자가 직접 확인한 답변
sources/screenshots/  프로젝트와 성과를 설명하는 이미지
```

`sources/`의 파일은 불변 원본이다. AI는 원본을 수정하지 않고 `memory/`에 구조화된 사실과 출처를 기록한다.

## 메모리 상태

- `verified`: 원본에서 명시적으로 확인됨
- `inferred`: 원본을 바탕으로 합리적으로 추론됨
- `unverified`: 출처가 부족함
- `conflicted`: 원본 간 값이 충돌함

`conflicted` 사실은 해결되기 전까지 최종 이력서와 포트폴리오에 사용할 수 없다.

## 기본 산출물

```text
resume/master.md              한국어 마스터 이력서 정본
resume/master.pdf             제출용 PDF
portfolio/html/index.html     슬라이드형 포트폴리오 HTML
portfolio/pdf/portfolio.pdf   포트폴리오 PDF
portfolio/dist/               GitHub Pages 배포 결과
```

## 현재 개발 상태

GitHub Template 기준 기능이 구현되어 있다. source 수집, 자동 memory, 커리어 스킬, Markdown 이력서 A4 PDF, 3개 테마 슬라이드 포트폴리오, 시각 QA, 통합 CLI, GitHub Actions·Pages와 합성 end-to-end 테스트를 사용할 수 있다. 상세 설계와 검증 범위는 `docs/plans/2026-08-27-career-harness-implementation.md`를 따른다.
