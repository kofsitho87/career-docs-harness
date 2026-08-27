# AGENTS.md

## 저장소 목적

이 저장소는 이력서와 포트폴리오를 작성, 정리, 개선하기 위한 작업 공간이다. 단순히 최종 결과물만 보관하는 곳이 아니라, 사실 기준 문서, 작성 가이드, 설계/계획 문서, 최종 산출물, 보조 자산을 함께 관리하는 harness로 사용한다.

## 핵심 디렉터리와 역할

- `resume/`: 현재 정본 이력서이자 사실 기준 문서를 보관한다.
- `docs/guides/`: 재사용 가능한 작성 가이드. 문체, 구조, 성과 표현 원칙을 확인할 때 본다.
- `docs/plans/`: 설계 문서와 구현 계획. 특정 결과물이나 케이스 스터디가 어떤 의도로 작성됐는지 파악할 때 사용한다.
- `case-studies/`: 개별 프로젝트 기반 케이스 스터디 문서를 보관한다.
- `portfolio/html/`: 직접 편집하는 포트폴리오 HTML 원본을 보관한다.
- `portfolio/pdf/`: 제출과 공유에 사용하는 포트폴리오 PDF를 보관한다.
- `portfolio/assets/`: 포트폴리오와 케이스 스터디에 쓰는 이미지와 시각 자료를 보관한다.
- `portfolio/dist/`: Cloudflare Pages 배포 시 생성되는 사이트 결과물이다. Git에는 포함하지 않는다.
- `.agents/skills/`: 에이전트별 중복 없이 공통으로 사용하는 로컬 스킬을 보관한다.

## 현재 대표 산출물

- `resume/product-engineer.md`
- `case-studies/outbound-voice-agent.md`
- `portfolio/html/heewung-song-portfolio.html`
- `portfolio/pdf/heewung-song-portfolio-v4.pdf`
- `portfolio/assets/heewung-song-infographic.png`

## 우선 읽기 순서

1. `README.md`로 저장소 목적과 구조를 빠르게 파악한다.
2. `resume/product-engineer.md`로 사실 기준 데이터와 현재 정본 이력서를 함께 확인한다.
3. `docs/guides/resume-guide.md`로 작성 원칙을 확인한다.
4. `case-studies/outbound-voice-agent.md`를 읽어 현재 대표 케이스 스터디를 파악한다.
5. `docs/workflow.md`를 읽어 현재 저장소의 작업 흐름과 주의사항을 확인한다.
6. 특정 결과물을 수정할 때는 관련 `docs/plans/` 문서를 함께 확인한다.

## 작업 원칙

- 사실 변경은 먼저 `resume/product-engineer.md`에 반영한다.
- 표현 개선은 `docs/guides/resume-guide.md`를 확인한 뒤 최종 산출물에 적용한다.
- 프로젝트 케이스 스터디 문서를 수정할 때는 관련 `docs/plans/` 설계 문서를 함께 확인한다.
- 설계나 구조 변경 전에는 관련 `docs/plans/` 문서를 먼저 확인한다.
- 이미지나 시각 자산은 문서 구조와 메시지가 정리된 뒤 마지막 단계에서 다룬다.
- 포트폴리오 HTML은 `portfolio/html/`에서 직접 수정하고 `portfolio/dist/`의 파일은 직접 편집하지 않는다.
- 대표 포트폴리오 HTML을 수정하면 `scripts/build_portfolio_pdf.py`로 `portfolio/pdf/heewung-song-portfolio-v4.pdf`를 다시 만들고, `scripts/build_portfolio_site.sh`로 `portfolio/dist/`를 다시 빌드한다.
- HTML에서 포트폴리오 자산을 참조할 때는 형제 디렉터리 기준의 `../assets/` 상대 경로를 사용한다.
- 케이스 스터디에서 포트폴리오 자산을 참조할 때는 `../portfolio/assets/` 상대 경로를 사용한다.
- 최종 산출물을 수정할 때는 사실 기준 문서와 모순이 없는지 항상 확인한다.

## 수정 우선순위

### 1. 사실 수정

경력, 수치, 기간, 기술 스택, 역할 같은 사실 정보는 먼저 `resume/product-engineer.md`를 고친다.

### 2. 가이드 확인

문장 압축, 성과 표현, 이력서 구조 조정은 `docs/guides/resume-guide.md`를 기준으로 판단한다.

### 3. 결과물 반영

이력서는 `resume/product-engineer.md`, 프로젝트 케이스 스터디는 `case-studies/[프로젝트명].md`, 종합 포트폴리오 HTML은 `portfolio/html/`에 반영한다.

### 4. 보조 문서 정리

구조나 흐름이 바뀌면 `README.md`, `AGENTS.md`, `CLAUDE.md`, `docs/workflow.md`, 관련 `docs/plans/` 문서도 함께 맞춘다.

## 주의사항

- `docs/plans/`는 최종 결과물이 아니라 설계/계획 문서다.
- 계획 문서명과 실제 산출물 파일명은 다를 수 있으므로, 수정 대상이 설계 문서인지 최종 결과물인지 먼저 구분한다.
- 현재 아웃바운드 보이스 에이전트 케이스 스터디를 수정할 때는 `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`를 함께 참고한다.
- 인바운드 보이스 에이전트 케이스 스터디를 수정할 때는 `docs/plans/2026-03-07-inbound-voice-agent-portfolio-design.md`를 함께 참고한다.
- 일부 계획 문서에는 현재 저장소에 없는 참고 자료가 남아 있을 수 있으므로, 실제 작업 근거는 현재 저장소 안의 문서와 산출물을 우선한다.
- 경로를 변경한 경우에는 `README.md`, `docs/workflow.md`, 문서 내부 링크를 함께 점검한다.
- 루트 `assets/`, `output/`, `dist/`는 더 이상 사용하지 않는다. 포트폴리오 관련 파일은 `portfolio/` 아래의 역할별 디렉터리에 둔다.
- `portfolio/dist/`는 재생성 가능한 배포 산출물이므로 source-of-truth로 취급하지 않는다.
- `.omx`, `.omc` 같은 런타임 상태 경로나 이전 구조의 흔적이 보여도, 사실 기준 문서나 최종 산출물보다 우선하지 않는다.
- 이 저장소는 문서 하네스이므로, 새 작업을 시작할 때도 가능하면 사실 기준 문서 -> 가이드 -> 결과물 순서를 유지한다.
