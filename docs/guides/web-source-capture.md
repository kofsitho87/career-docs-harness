# 웹 경력 자료 수집 가이드

로그인된 브라우저에서 LinkedIn 등 사용자가 접근 권한을 가진 경력 자료를 읽을 때 적용한다.

## 원칙

- 사용자가 이미 로그인한 브라우저 세션을 사용할 수 있다.
- 쿠키, 비밀번호, 토큰, 브라우저 프로필, 세션 상태는 저장소에 저장하지 않는다.
- 원본 페이지를 수정하거나 외부에 메시지를 보내지 않는다.
- 화면에서 확인한 텍스트와 사용자가 승인한 스크린샷만 수집한다.
- 수집 결과에는 URL과 캡처 시각을 기록한다.
- GitHub의 저장소 수, 스타, 커밋 수는 보조 맥락이며 그 자체를 경력 성과로 해석하지 않는다.

## LinkedIn 수집 흐름

1. `agent-browser` 또는 사용자의 로그인된 브라우저 제어 도구로 프로필을 연다.
2. 이름, headline, about, experience, education, skills, projects의 보이는 텍스트를 읽는다.
3. 인증정보를 제외한 텍스트를 임시 파일에 저장한다.
4. 다음 명령으로 불변 스냅샷과 manifest 항목을 만든다.

```bash
uv run python -m scripts.lib.ingest_web_snapshot \
  --url "https://www.linkedin.com/in/example" \
  --title "LinkedIn profile" \
  --input /tmp/linkedin-profile.txt
```

5. 스냅샷은 `sources/web/`, 구조화된 사실은 이후 `memory/`에 기록한다.

## GitHub 수집 흐름

`gh` CLI의 인증 상태는 로컬 환경에만 두고 공개 프로필과 공개 저장소 메타데이터만 저장한다.

```bash
uv run python -m scripts.lib.ingest_github USERNAME
```

비공개 저장소, 토큰, 이메일 가시성 우회, 조직 내부 데이터 수집은 기본 범위에 포함하지 않는다.
