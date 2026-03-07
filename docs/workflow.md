# 워크플로우 문서

이 저장소는 이력서와 포트폴리오를 만들고 다듬기 위한 작업 공간이다. 핵심은 사실 기준 문서를 보존하고, 가이드와 설계 문서를 참고해 최종 산출물을 점진적으로 개선하는 것이다.

## 1. 저장소를 보는 기준

### 1.1 사실 기준 문서 (source-of-truth)

이 범주의 문서는 실제 경력, 프로젝트, 기술, 성과를 정리한 기준 데이터다. 표현 방식은 바뀔 수 있어도 사실 자체를 가장 우선해서 유지해야 한다.

- `resume/product-engineer.md`: 현재 정본이자 경력, 프로젝트, 기술 스택, 활동 이력을 관리하는 사실 기준 이력서

실무 원칙:

- 새로운 경력이나 프로젝트 사실을 추가할 때는 먼저 이 범주의 문서를 갱신한다.
- 최종 이력서나 포트폴리오에서 표현을 줄이거나 재구성하더라도, 근거는 항상 이 범주에서 가져온다.

### 1.2 가이드와 계획 문서 (guidelines and plans)

이 범주의 문서는 무엇을 어떻게 쓸지 정하는 기준과 설계 문서다. 사실 데이터 자체를 담기보다는, 어떤 관점으로 문서를 편집할지 안내한다.

- `docs/guides/resume-guide.md`: 이력서 구조, 문체, 성과 표현, ATS 대응 등 재사용 가능한 작성 가이드
- `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`: 아웃바운드 보이스 에이전트 포트폴리오의 구성과 강조 포인트를 정리한 설계 문서
- `docs/plans/`: 저장소 문서화나 산출물 정리를 위한 작업 계획 문서 모음

실무 원칙:

- 새 문서를 쓰기 전에 먼저 가이드와 설계 문서를 확인해 톤, 구조, 강조 지점을 맞춘다.
- 설계 문서는 최종 산출물과 동일하지 않을 수 있으므로, 초안 작성 시 실제 파일명과 연결 관계를 별도로 확인한다.

### 1.3 최종 산출물 (final outputs)

이 범주의 문서는 외부에 보여주기 위한 현재 결과물이다. 지원용 이력서, 프로젝트 케이스 스터디, 필요 시 시각 자료가 여기에 해당한다.

- `resume/product-engineer.md`: 현재 메인 이력서 산출물이자 사실 기준 문서
- `case-studies/outbound-voice-agent.md`: 아웃바운드 Voice AI Agent 케이스 스터디
- `case-studies/inbound-voice-agent.md`: 인바운드 Voice AI Agent 케이스 스터디
- `assets/heewung-song-infographic.png`: 이력서와 함께 사용할 수 있는 시각 자료

실무 원칙:

- 이 범주의 문서는 직접 배포하거나 제출할 수 있는 상태를 목표로 관리한다.
- 표현을 수정할 때는 사실 기반 원문과 가이드 문서에 어긋나지 않는지 먼저 확인한다.

### 1.4 로컬 스킬과 런타임 상태 (local skills and runtime state)

이 범주는 문서 자체보다 작업 보조 수단과 로컬 실행 흔적에 해당한다. 현재 저장소 안에서 확인 가능한 항목은 이미지 자산 생성 스킬과 스크립트이며, 런타임 상태 경로는 로컬 환경에서 생성될 수 있는 부가 요소로 본다. 이 범주는 최종 산출물의 근거 문서로 취급하지 않는다.

- `.claude/skills/image_generation/SKILL.md`: 로컬 이미지 생성 워크플로우 설명
- `.claude/skills/image_generation/scripts/generate_image.py`: 이미지 생성 스크립트
- `.omx`, `.omc`: 로컬에서 생성될 수 있는 런타임 상태나 로그용 무시 대상 경로

실무 원칙:

- 이 범주는 문서 작업을 보조하지만, 이력이나 프로젝트 사실의 source-of-truth는 아니다.
- 런타임 상태 경로는 저장소의 핵심 문서 체계라기보다 로컬 작업 중 생성될 수 있는 운영 보조 요소로만 다룬다.

## 2. 실제 작업 순서

이 저장소의 기본 흐름은 아래 순서를 따른다.

### 2.1 사실 자료 수집

먼저 경력, 프로젝트, 기술 스택, 수치 성과 같은 사실 정보를 모은다.

- 기본 시작점은 `resume/product-engineer.md`다.
- 새 프로젝트를 문서화할 때도 먼저 사실, 역할, 기간, 성과, 사용 기술을 정리한다.

### 2.2 작성 및 설계 기준 정의

다음으로 어떤 메시지와 구조로 보여줄지 정한다.

- 이력서 작성 원칙은 `docs/guides/resume-guide.md`를 기준으로 삼는다.
- 특정 프로젝트 케이스 스터디 문서는 관련 설계 문서를 함께 본다.
- 아웃바운드 보이스 에이전트 케이스 스터디는 `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`를 참고한다.
- 인바운드 보이스 에이전트 케이스 스터디는 `docs/plans/2026-03-07-inbound-voice-agent-portfolio-design.md`를 참고한다.

### 2.3 최종 문서 작성 또는 개선

기준이 정리되면 실제 산출물을 작성하거나 다듬는다.

- 이력서 작업은 `resume/product-engineer.md`를 중심으로 진행한다.
- 프로젝트 케이스 스터디 작업은 `case-studies/outbound-voice-agent.md`를 중심으로 진행한다.
- 이 단계에서는 내용을 압축하거나 재배치할 수 있지만, 사실 왜곡 없이 사실 기준 문서를 바탕으로 수정해야 한다.

### 2.4 필요 시 보조 자산 생성

문서 이해를 돕기 위한 이미지나 다이어그램이 필요하면 마지막 단계에서 생성한다.

- 로컬 이미지 생성 흐름은 `.claude/skills/image_generation/SKILL.md`와 관련 스크립트를 따른다.
- 보조 자산은 문서의 핵심 내용을 대체하는 것이 아니라, 이미 정리된 내용을 더 잘 전달하기 위한 수단으로 사용한다.

## 3. 현재 저장소 기준 운영 메모

현재 상태를 기준으로 작업할 때 아래 사항을 알고 있어야 한다.

### 3.1 계획 문서명과 실제 산출물 파일명이 다를 수 있다

설계 문서는 주제 기준으로 이름이 붙어 있고, 실제 결과 문서는 목적에 맞는 별도 파일명을 사용할 수 있다.

- 케이스 스터디 설계 문서: `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`
- 실제 케이스 스터디 산출물: `case-studies/outbound-voice-agent.md`
- 저장소 문서화 설계 문서: `docs/plans/2026-03-07-repo-documentation-design.md`
- 저장소 문서화 구현 계획: `docs/plans/2026-03-07-repo-documentation.md`
- 실제 문서화 결과 파일: `README.md`, `docs/workflow.md`

따라서 작업자는 "계획 문서를 수정하는지", "최종 산출물을 수정하는지"를 항상 구분해야 한다.

### 3.2 현재 프로젝트 케이스 스터디는 2건 정리되어 있다

현재 저장소에서 정리된 프로젝트 케이스 스터디는 2건이다.

- `case-studies/outbound-voice-agent.md`: 아웃바운드 Voice AI Agent
- `case-studies/inbound-voice-agent.md`: 인바운드 Voice AI Agent (아웃바운드의 시리즈 후속편)

추가 프로젝트를 확장하려면 먼저 사실 자료를 정리하고, 필요한 경우 별도 설계 문서를 만든 뒤 `case-studies/` 아래 케이스 스터디 문서를 늘리는 방식이 적절하다.

### 3.3 일부 설계 문서의 참고 자료는 현재 저장소에 없다

케이스 스터디 설계 문서에는 현재 저장소에 없는 참고 자료들이 함께 언급되어 있다. 따라서 설계 문서에 적힌 모든 배경 자료가 실제로 저장소 안에 존재한다고 가정하면 안 된다.

현재 확인되지 않는 참고 자료:

- `docs/Livkit Agent/outbound_agent_architecture_final.md`
- `docs/blog/livekit-hospital-voice-agent.md`
- `docs/blog/call-analysis-pipeline-ko.md`
- `docs/infra/server-infrastructure.md`
- `docs/dev/Human 예약 플로우 요약.md`
- `docs/dev/prompt_and_tools_review.md`
- `docs/dev/developer_message_catalog.md`
- `docs/image.png`

실무적으로는 다음처럼 다루는 것이 안전하다.

- 없는 참고 문서는 "외부 참고 또는 미반입 자료"로 간주한다.
- 최종 산출물 작성 시에는 현재 저장소에 있는 사실 문서와 실제 산출물을 우선 근거로 삼는다.
- 필요한 경우 누락 자료를 별도로 정리하거나, 설계 문서의 참고 목록을 현재 저장소 상태에 맞게 나중에 정비한다.

## 4. 권장 작업 방식

이 저장소에서 문서를 만들 때는 아래 기준을 유지하는 것이 좋다.

- 사실 업데이트는 먼저 사실 기준 문서에 반영한다.
- 표현 개선은 가이드와 설계 문서를 확인한 뒤 최종 산출물에 적용한다.
- 이미지 생성이나 시각 자산 제작은 문서 구조와 메시지가 정리된 뒤에 진행한다.
- 설계 문서에 있는 참고 자료가 실제로 존재하는지 항상 확인하고, 없는 자료를 전제로 문장을 쓰지 않는다.

