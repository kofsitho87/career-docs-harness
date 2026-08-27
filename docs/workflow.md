# Career Harness Workflow

## 1. Authority

```text
사용자 최신 교정
-> sources 불변 원본
-> provenance-backed memory
-> target 전략
-> drafts
-> 최종 산출물
```

최종 이력서와 포트폴리오는 새로운 사실의 원본이 아니다. 충돌이 발견되면 memory를 먼저 수정하고 산출물을 다시 만든다.

## 2. Initialize

```bash
uv sync
./scripts/harness init
./scripts/harness check
```

`init`은 기존 사용자 데이터를 덮어쓰지 않고 필요한 디렉터리와 에이전트 어댑터를 준비한다.

## 3. Collect Sources

로컬 파일:

```bash
./scripts/harness ingest sources/files/FILE
```

로그인된 웹 페이지:

1. 사용자가 접근 권한을 가진 브라우저 세션에서 텍스트를 읽는다.
2. 쿠키·토큰·세션 상태를 저장하지 않는다.
3. 인증정보 없는 텍스트를 등록한다.

```bash
uv run python -m scripts.lib.ingest_web_snapshot \
  --url "https://example.com/profile" \
  --title "Profile" \
  --input /tmp/profile.txt
```

GitHub:

```bash
uv run python -m scripts.lib.ingest_github USERNAME
```

인터뷰 답변:

```bash
uv run python -m scripts.lib.record_interview \
  --topic "..." \
  --question "..." \
  --answer "..."
```

## 4. Build Memory

1. `$career-intake`로 sources와 기존 memory를 비교한다.
2. 이미 확인된 내용은 다시 묻지 않는다.
3. 사용자 답변을 interview source로 기록한다.
4. `$career-memory`로 stable ID, source refs, status를 포함해 병합한다.
5. 자동 충돌은 덮어쓰지 않고 `memory/conflicts.yaml`에 둔다.
6. `memory/changelog.md`와 `memory/state.yaml`을 갱신한다.

```bash
uv run python -m scripts.lib.validate_memory
```

## 5. Master Resume

1. blocking conflict를 해결하거나 해당 사실을 제외한다.
2. `$master-resume`으로 `resume/master.md`를 만든다.
3. visible public claim은 verified 상태와 source refs를 가져야 한다.
4. 중요한 bullet 옆에 claim ID HTML comment를 둔다.
5. PDF를 빌드한다.

```bash
./scripts/harness build resume
```

## 6. Targeted Resume

```text
targets/<slug>/job-description.md
targets/<slug>/strategy.md
resume/tailored/<slug>.md
```

`$targeted-resume`은 마스터의 Summary, 순서, 강조, 키워드, 분량만 바꾼다. 새로운 경력 사실은 memory와 master에 먼저 반영한다.

## 7. Portfolio

1. `$career-portfolio`로 narrative와 대표 프로젝트를 결정한다.
2. `drafts/portfolio/outline.yaml`을 먼저 만든다.
3. 슬라이드별 purpose, claim IDs, evidence IDs를 검증한다.
4. editorial, minimal, technical 중 테마를 선택한다.
5. HTML과 PDF를 빌드한다.

```bash
./scripts/harness build portfolio
```

렌더 결과는 `tmp/pdfs/portfolio/`의 PNG와 contact sheet에서 확인한다. 생성된 `portfolio/dist/`는 직접 편집하지 않는다.

## 8. Review

`$career-review`는 기본적으로 산출물을 다시 쓰지 않고 P0–P3 findings를 보고한다.

- P0: credential, privacy, fabricated fact, serious attribution
- P1: wrong date/metric/title, conflicted claim, broken required artifact
- P2: weak evidence, unclear ownership, ATS/relevance, visual readability
- P3: wording and polish

수정을 요청받은 경우에도 source와 memory를 먼저 고친다.

## 9. Check, Preview, Deploy

```bash
./scripts/harness check
./scripts/harness preview
./scripts/harness deploy
```

GitHub Actions는 unit tests, Ruff, memory schema, adapters, integrated quality gates를 실행한다. main의 `portfolio/html/index.html`이 준비되면 GitHub Pages artifact를 배포한다.

## 10. Completion

- 모든 중요한 사실이 허용된 status와 provenance를 가진다.
- unresolved conflict가 final output에 없다.
- 마스터와 맞춤 이력서가 같은 사실을 사용한다.
- HTML·Markdown 로컬 링크와 이미지가 유효하다.
- 공개 연락처는 allowlist에 있다.
- 이력서 PDF는 A4, 포트폴리오 PDF는 16:9다.
- PDF 텍스트와 링크가 살아 있다.
- 포트폴리오 PNG와 contact sheet에 clipping·overflow가 없다.
- `memory/state.yaml`에 완료 단계와 남은 질문이 반영된다.
