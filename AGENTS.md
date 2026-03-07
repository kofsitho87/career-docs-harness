# Agent.md

## 저장소 목적

이 저장소는 이력서와 포트폴리오를 작성, 정리, 개선하기 위한 작업 공간이다. 단순히 최종 결과물만 보관하는 곳이 아니라, 사실 기준 문서, 작성 가이드, 설계/계획 문서, 최종 산출물, 보조 자산을 함께 관리하는 harness로 사용한다.

## 핵심 디렉터리와 역할

- `docs/source/`: 사실 기준 문서. 경력, 프로젝트, 기술, 성과의 원본 근거를 보관한다.
- `docs/guides/`: 재사용 가능한 작성 가이드. 문체, 구조, 성과 표현 원칙을 확인할 때 본다.
- `docs/plans/`: 설계 문서와 구현 계획. 특정 결과물이 어떤 의도로 작성됐는지 파악할 때 사용한다.
- `resume/`: 현재 최종 이력서 산출물.
- `portfolio/`: 현재 최종 포트폴리오 산출물.
- `assets/`: 이미지와 시각 자료 자산.
- `.claude/skills/image_generation/`: 이미지 자산 제작에 쓰는 로컬 스킬과 스크립트.

## 현재 대표 산출물

- `resume/product-engineer.md`
- `portfolio/outbound-voice-agent.md`
- `assets/heewung-song-infographic.png`

## 우선 읽기 순서

1. `README.md`로 저장소 목적과 구조를 빠르게 파악한다.
2. `docs/source/origin-resume.md`로 사실 기준 데이터를 확인한다.
3. `docs/guides/resume-guide.md`로 작성 원칙을 확인한다.
4. `resume/product-engineer.md`와 `portfolio/outbound-voice-agent.md`를 읽어 현재 결과물을 파악한다.
5. `docs/workflow.md`를 읽어 현재 저장소의 작업 흐름과 주의사항을 확인한다.
6. 특정 결과물을 수정할 때는 관련 `docs/plans/` 문서를 함께 확인한다.

## 작업 원칙

- 사실 변경은 먼저 `docs/source/origin-resume.md`에 반영한다.
- 표현 개선은 `docs/guides/resume-guide.md`를 확인한 뒤 최종 산출물에 적용한다.
- 포트폴리오 문서를 수정할 때는 관련 `docs/plans/` 설계 문서를 함께 확인한다.
- 설계나 구조 변경 전에는 관련 `docs/plans/` 문서를 먼저 확인한다.
- 이미지나 시각 자산은 문서 구조와 메시지가 정리된 뒤 마지막 단계에서 다룬다.
- 최종 산출물을 수정할 때는 사실 기준 문서와 모순이 없는지 항상 확인한다.

## 수정 우선순위

### 1. 사실 수정

경력, 수치, 기간, 기술 스택, 역할 같은 사실 정보는 먼저 `docs/source/origin-resume.md`를 고친다.

### 2. 가이드 확인

문장 압축, 성과 표현, 이력서 구조 조정은 `docs/guides/resume-guide.md`를 기준으로 판단한다.

### 3. 결과물 반영

이력서는 `resume/product-engineer.md`, 포트폴리오는 `portfolio/outbound-voice-agent.md`에 반영한다.

### 4. 보조 문서 정리

구조나 흐름이 바뀌면 `README.md`, `Agent.md`, `docs/workflow.md`, 관련 `docs/plans/` 문서도 함께 맞춘다.

## 주의사항

- `docs/plans/`는 최종 결과물이 아니라 설계/계획 문서다.
- 계획 문서명과 실제 산출물 파일명은 다를 수 있으므로, 수정 대상이 설계 문서인지 최종 결과물인지 먼저 구분한다.
- 현재 아웃바운드 보이스 에이전트 포트폴리오를 수정할 때는 `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`를 함께 참고한다.
- 일부 계획 문서에는 현재 저장소에 없는 참고 자료가 남아 있을 수 있으므로, 실제 작업 근거는 현재 저장소 안의 문서와 산출물을 우선한다.
- 경로를 변경한 경우에는 `README.md`, `docs/workflow.md`, 문서 내부 링크를 함께 점검한다.
- `.omx`, `.omc` 같은 런타임 상태 경로나 이전 구조의 흔적이 보여도, 사실 기준 문서나 최종 산출물보다 우선하지 않는다.
- 루트에 `dan-resume-product-engineer.md` 같은 이전 구조의 파일이 남아 있더라도, 현재 정본 이력서는 `resume/product-engineer.md`다.
- 이 저장소는 문서 하네스이므로, 새 작업을 시작할 때도 가능하면 사실 기준 문서 -> 가이드 -> 결과물 순서를 유지한다.
