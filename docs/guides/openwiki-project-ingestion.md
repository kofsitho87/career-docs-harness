# OpenWiki Project Ingestion Guide

## 1. OpenWiki란 무엇인가

[OpenWiki](https://github.com/langchain-ai/openwiki)는 코드베이스나 개인 knowledge source를 AI가 읽고, 사람과 에이전트가 함께 사용할 수 있는 연결된 Markdown wiki로 생성·유지하는 CLI다. Career Harness 구현·테스트 기준 버전은 OpenWiki v0.4.0이다.

OpenWiki에는 두 가지 모드가 있다.

| 모드 | 입력 | 출력 | 대표 명령 |
|---|---|---|---|
| `code` | 현재 Git repository와 tests | repository의 `openwiki/` | `openwiki code --init` |
| `personal` | 연결된 개인 knowledge sources | `~/.openwiki/wiki` | `openwiki personal --init` |

Career Harness는 이 중 **code mode의 repository-local `openwiki/`만 사용**한다.

code wiki에는 보통 다음과 같은 문서가 만들어진다.

- `openwiki/quickstart.md`
- `openwiki/architecture/`
- `openwiki/concepts/`
- `openwiki/workflows/`
- `openwiki/operations/`
- `openwiki/integrations/`
- `openwiki/testing/`
- `openwiki/INSTRUCTIONS.md`
- `openwiki/.claims/`의 grounded claim state

OpenWiki v0.4.0은 Open Knowledge Format(OKF) 형태의 wiki와 grounded claims를 사용한다. Grounded claim은 architecture, behavior, invariant, workflow 같은 중요한 설명을 repository의 versioned evidence와 연결하기 위한 정보다.

## 2. Career Harness가 OpenWiki를 사용하는 이유

일반적인 project ingestion은 Git tree, README, manifest, commit metadata를 빠르게 수집할 수 있지만, 대규모 프로젝트의 의미를 직접 설명하지는 못한다.

OpenWiki가 있으면 다음 정보가 이미 구조화되어 있을 가능성이 높다.

- 프로젝트 목적과 시스템 경계
- 주요 component와 책임
- 데이터 흐름과 핵심 workflow
- 운영·배포·테스트 방식
- integration과 외부 의존성
- 보안과 실패 처리 invariant
- 해당 설명을 뒷받침하는 source evidence

Career Harness는 이를 이력서와 포트폴리오 작성을 위한 **프로젝트 이해 source**로 사용한다. OpenWiki 설명이 있더라도 다음 정보는 자동 확정하지 않는다.

- 사용자가 직접 구현한 범위
- 프로젝트 이전 상태와 사용자가 변경한 부분
- 팀과 사용자의 ownership 경계
- 사용자가 내린 기술 결정
- 사용자의 기여로 발생한 성과
- 외부 공개 가능 여부

이 정보는 `$career-intake`가 사용자에게 질문하고 interview source로 기록한다.

## 3. 사전 준비

### 설치

OpenWiki는 Node.js 22 이상이 필요하다.

```bash
npm install -g openwiki
```

설치 확인:

```bash
command -v openwiki
openwiki --help
```

일부 비대화형 terminal에서는 bare `openwiki`나 `openwiki --help`가 interactive UI를 열면서 raw-mode 오류를 낼 수 있다. Career Harness는 interactive UI를 사용하지 않고 `openwiki code -p` one-shot 실행만 사용한다.

### Provider와 model

OpenWiki CLI는 사용자가 설정한 provider와 model을 사용한다. 초기 설정이 없다면 원본 프로젝트에서 OpenWiki 안내에 따라 provider를 설정한다.

CLI briefing 생성에는 선택한 provider의 모델 사용량과 비용이 발생할 수 있다. Career Harness는 API key, OAuth token, provider 설정을 복사하거나 manifest에 기록하지 않는다.

## 4. OpenWiki 생성과 업데이트 책임

Career Harness는 원본 project의 wiki를 자동 생성하거나 갱신하지 않는다.

처음 wiki를 만들 때 원본 프로젝트에서 실행한다.

```bash
cd /path/to/project
openwiki code --init
```

기존 wiki를 최신 source에 맞게 갱신한다.

```bash
cd /path/to/project
openwiki code --update
```

업데이트가 끝난 다음 Career Harness에서 프로젝트를 ingestion한다.

```bash
cd /path/to/career-harness
./scripts/harness ingest-project /path/to/project
```

이 책임을 분리하는 이유:

- `--init`은 기존 generated wiki와 claims를 다시 만들 수 있다.
- `--update`는 프로젝트의 tracked documentation을 변경할 수 있다.
- provider 실행은 시간과 비용이 발생할 수 있다.
- Career Harness의 source ingestion은 원본 project를 수정하지 않아야 한다.

## 5. 하네스 내부 실행 흐름

기본 `auto` 모드의 순서는 다음과 같다.

```text
project path 또는 GitHub URL
→ Git repository 확인
→ openwiki/ 감지
→ 임시 Git clone 생성
→ 원본 openwiki/를 임시 clone에 복사
→ 임시 clone에서 openwiki code -p 실행
→ project briefing 수집
→ openwiki/**/*.md 수집
→ Git tree·docs·manifest·history 수집
→ sources/projects/ snapshot 생성
→ sources/manifest.yaml 등록
```

OpenWiki CLI에는 다음 목적의 one-shot prompt가 전달된다.

- Purpose
- Architecture
- Core Workflows
- Key Modules
- Data and Integrations
- Testing and Operations
- Security Boundaries
- Questions About Personal Contribution

CLI는 임시 clone에서만 실행된다. 원본 프로젝트의 `openwiki/`, source, Git state는 변경하지 않는다.

## 6. OpenWiki 모드 선택

### `auto` — 기본 권장

```bash
./scripts/harness ingest-project /path/to/project
```

또는 명시적으로:

```bash
./scripts/harness ingest-project /path/to/project --openwiki auto
```

| 상태 | 동작 |
|---|---|
| `openwiki/` 없음 | 일반 Git snapshot 사용 |
| wiki 있음 + CLI 성공 | CLI briefing과 wiki Markdown 우선 사용 |
| wiki 있음 + CLI 없음·실패 | 기존 wiki Markdown으로 fallback |
| wiki 있음 + 일부 page가 민감정보 패턴 포함 | 해당 page 제외 |

대부분의 프로젝트에서 이 모드를 권장한다.

### `required` — OpenWiki 품질 게이트

```bash
./scripts/harness ingest-project /path/to/project --openwiki required
```

다음 조건을 모두 만족해야 한다.

- project에 `openwiki/`가 존재
- `openwiki` CLI 설치
- provider·model 실행 가능
- CLI briefing 생성 성공

하나라도 실패하면 snapshot을 만들지 않는다. 프로젝트 설명을 반드시 최신 OpenWiki에 의존해야 할 때 사용한다.

### `off` — OpenWiki 제외

```bash
./scripts/harness ingest-project /path/to/project --openwiki off
```

`openwiki/`가 있어도 CLI와 wiki를 모두 무시하고 일반 Git snapshot만 만든다.

다음 경우 유용하다.

- provider 비용을 사용하지 않으려는 경우
- wiki가 오래됐고 신뢰할 수 없는 경우
- Git tree와 문서 snapshot만 비교하려는 경우
- OpenWiki 실행 문제를 진단하는 경우

## 7. GitHub URL과 OpenWiki

```bash
./scripts/harness ingest-project https://github.com/owner/repository
```

GitHub URL ingestion은 `gh repo clone`을 우선 사용하고, 사용할 수 없으면 `git clone`을 사용한다. `openwiki/`가 GitHub repository에 commit되어 있어야 clone에서 감지할 수 있다.

로컬에만 있고 Git에 추적되지 않는 wiki는 GitHub URL ingestion에서 사용할 수 없다. 이 경우 로컬 경로를 직접 전달한다.

```bash
./scripts/harness ingest-project /local/path/to/repository
```

## 8. OpenWiki와 코드 본문 옵션

OpenWiki가 있어도 기본 snapshot에는 임의의 source-code 본문을 추가하지 않는다. OpenWiki wiki와 일반 문서·manifest만으로 프로젝트 이해가 충분한지 먼저 확인한다.

구현 세부사항을 함께 분석해야 한다면:

```bash
./scripts/harness ingest-project /path/to/project \
  --openwiki auto \
  --include-code \
  --max-code-files 30
```

최종 snapshot 우선순위:

```text
OpenWiki CLI briefing
→ OpenWiki Markdown pages
→ tracked file tree
→ README·docs·manifest
→ recent commit metadata
→ bounded source-code content
```

## 9. 생성되는 source와 metadata

snapshot:

```text
sources/projects/<project>-<commit>-openwiki-<mode>-<digest>.md
```

manifest에는 다음 OpenWiki metadata가 기록된다.

```yaml
openwiki_mode: auto
openwiki_detected: true
openwiki_cli_used: true
openwiki_pages: 12
openwiki_cli_error: null
```

CLI fallback이 발생하면 `openwiki_cli_used`는 `false`이고 오류 요약이 기록된다. 오류가 credential과 유사하면 상세 내용은 저장하지 않는다.

## 10. 원본 보호와 보안

- OpenWiki CLI는 임시 clone에서만 실행한다.
- 원본 checkout에서 `init`, `update`, chat을 실행하지 않는다.
- 임시 clone은 ingestion 종료 후 삭제한다.
- `~/.openwiki` provider 설정은 복사하지 않는다.
- API key, private key, GitHub token, AWS key 패턴이 있는 briefing·page는 저장하지 않는다.
- `.env`, credential, password, secret, token 파일은 일반 project snapshot에서도 제외한다.
- OpenWiki error가 credential처럼 보이면 세부 오류를 생략한다.

## 11. 권장 커리어 인터뷰

OpenWiki ingestion 이후 다음과 같이 요청한다.

```text
$career-intake를 사용해 방금 등록한 project_repository source를 분석해줘.

OpenWiki가 설명한 architecture와 workflow를 바탕으로 다음 항목 중
source만으로 확인할 수 없는 내용만 질문해줘.

- 내가 직접 설계하거나 구현한 module
- 프로젝트 이전 상태와 내가 변경한 부분
- 팀과 내 ownership 경계
- 가장 중요한 기술 결정과 tradeoff
- 운영 규모와 측정 가능한 결과
- 공개 가능한 evidence
```

답변은 `sources/interviews/`에 verified source로 기록한 뒤 memory에 반영한다.

## 12. 문제 해결

### `OpenWiki required but project has no openwiki/ directory`

원본 프로젝트에서 wiki를 생성하거나 `auto`·`off` 모드를 사용한다.

```bash
cd /path/to/project
openwiki code --init
```

### `openwiki CLI is not installed`

```bash
npm install -g openwiki
```

설치 후 새 terminal에서 `command -v openwiki`로 확인한다.

### provider 또는 model 오류

원본 프로젝트에서 OpenWiki 자체 명령을 먼저 실행해 provider 설정을 확인한다.

```bash
cd /path/to/project
openwiki code -p "Summarize this project"
```

Career Harness에서는 `auto`를 사용하면 기존 wiki page로 fallback할 수 있다.

### wiki가 오래됨

```bash
cd /path/to/project
openwiki code --update
```

업데이트 commit 또는 working tree를 확인한 다음 다시 ingestion한다.

### CLI 실행 비용을 피하고 싶음

```bash
./scripts/harness ingest-project /path/to/project --openwiki off
```

### fallback 여부 확인

`sources/manifest.yaml`에서 다음 값을 확인한다.

```yaml
openwiki_detected: true
openwiki_cli_used: false
openwiki_cli_error: "..."
```

## 13. FAQ

### OpenWiki가 있으면 모든 코드를 하네스가 읽는가?

OpenWiki CLI는 임시 clone의 repository와 기존 wiki를 사용해 briefing을 만든다. Career Harness snapshot에는 OpenWiki briefing과 Markdown wiki를 저장하며, 일반 source-code 본문은 `--include-code`가 없으면 포함하지 않는다.

### Career Harness가 OpenWiki wiki를 최신화하는가?

아니다. 하네스는 원본 불변 계약을 지킨다. wiki 생성·업데이트는 사용자가 원본 프로젝트에서 명시적으로 수행한다.

### OpenWiki grounded claim이 곧 내 경력 claim인가?

아니다. OpenWiki grounded claim은 코드베이스의 architecture와 behavior를 repository evidence에 연결한다. 사용자의 개인 기여와 성과는 별도 인터뷰와 경력 source가 필요하다.

### `auto`와 `required` 중 무엇을 써야 하는가?

일반적으로 `auto`를 사용한다. OpenWiki 실행 실패를 허용하면 안 되는 검증된 대표 프로젝트에서만 `required`를 사용한다.
