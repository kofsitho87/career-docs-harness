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
- `docs/guides/job-search-protocol.md`: 원하는 포지션과 스펙을 바탕으로 적합한 채용공고를 찾기 위한 내부 검색 프로토콜
- `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`: 아웃바운드 보이스 에이전트 포트폴리오의 구성과 강조 포인트를 정리한 설계 문서
- `docs/plans/`: 저장소 문서화나 산출물 정리를 위한 작업 계획 문서 모음

실무 원칙:

- 새 문서를 쓰기 전에 먼저 가이드와 설계 문서를 확인해 톤, 구조, 강조 지점을 맞춘다.
- 설계 문서는 최종 산출물과 동일하지 않을 수 있으므로, 초안 작성 시 실제 파일명과 연결 관계를 별도로 확인한다.

### 1.3 최종 산출물 (final outputs)

이 범주의 문서는 외부에 보여주기 위한 현재 결과물이다. 지원용 이력서, 프로젝트 케이스 스터디, 필요 시 시각 자료가 여기에 해당한다.

- `resume/product-engineer.md`: 현재 메인 이력서 산출물이자 사실 기준 문서
- `portfolio/heewung-song-portfolio.html`: 반복 업무를 프로덕션 AI 시스템으로 전환해 온 다섯 프로젝트를 하나의 커리어 서사로 연결한 종합 포트폴리오
- `portfolio/heewung-song-portfolio-v2.html`: 위 포트폴리오의 디자인 개선 버전. 콘텐츠·수치·28장 구성은 동일하고 시각 위계와 레이아웃 언어만 재설계했다. 사실을 고칠 때는 두 파일을 함께 맞춘다.
- `portfolio/heewung-song-portfolio-v3.html`: 현재 대표 종합 포트폴리오. v2와 달리 다섯 챕터를 네 챕터·30장으로 재구성했다(오프닝 3장 + 병원 전화 Voice AI 7장 + 통화 분석 및 평가 8장 + 병원 고객상담 AI Agent 5장 + AIU 사내 업무지원 6장 + 클로징 1장). 인바운드·아웃바운드를 한 챕터의 두 방향으로 통합했고, CH 01은 프로젝트 소개 → 전체 시스템 → LiveKit 실시간 음성 → 안전한 예약 → Warm Transfer → 공용 대기줄 → 성과와 배운 점, CH 02는 분석 시스템 → 통화 복원 → 28개 규칙 분류 → 업무/통화 결과 → LLM 평가 → 현황 확인 → 문제 진단 → 운영 개선 순으로 전개된다. CH 01 작업 기록은 `docs/plans/2026-08-26-portfolio-v3-ch1-seven-slide-redesign.md`, CH 02 작업 기록은 `docs/plans/2026-08-26-portfolio-v3-ch2-eight-slide-redesign.md`다. CH 03은 `docs/plans/2026-08-26-portfolio-v3-ch3-redesign.md`에서 소개 → LangGraph 기반 상담 시스템 아키텍처 → 상태 기반 상담 흐름 → 병원별 지식 검색 → 운영 가능한 서비스 경계와 배운 점의 5장으로 구현했다. CH 04는 `docs/plans/2026-08-27-portfolio-v3-ch4-redesign.md`에서 사내 AX 프로젝트 소개 → 구조와 기술 → 하루 시나리오 세 장(성과 확인·통화 검토·문의 응대) → 확장 비전의 6장으로 구현했다.
- `case-studies/outbound-voice-agent.md`: 아웃바운드 Voice AI Agent 케이스 스터디
- `case-studies/inbound-voice-agent.md`: 인바운드 Voice AI Agent 케이스 스터디
- `case-studies/hospital-customer-support-agent.md`: 병원 고객상담 AI Agent 케이스 스터디
- `assets/heewung-song-infographic.png`: 이력서와 함께 사용할 수 있는 시각 자료
- `assets/hospital-customer-support-agent-ppt-overview.png`: 병원 고객상담 AI Agent 개요·아키텍처 시각 자료
- `assets/hospital-customer-support-agent-ppt-flow.png`: 병원 고객상담 AI Agent 흐름·설계 의사결정 시각 자료
- `assets/agent-admin-call-classification-evidence.png`: 실제 통화 상세의 규칙 기반 분류 카드에서 개인·병원·통화 식별정보를 제외한 CH 02 증거 이미지

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
- 채용공고 탐색 작업은 `docs/guides/job-search-protocol.md`를 기준으로 검색 입력값, 사이트별 탐색 순서, 적합도 판단 방식을 맞춘다.
- 특정 프로젝트 케이스 스터디 문서는 관련 설계 문서를 함께 본다.
- 아웃바운드 보이스 에이전트 케이스 스터디는 `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`를 참고한다.
- 인바운드 보이스 에이전트 케이스 스터디는 `docs/plans/2026-03-07-inbound-voice-agent-portfolio-design.md`를 참고한다.
- 병원 고객상담 AI Agent 케이스 스터디는 `docs/plans/2026-03-07-hospital-customer-support-agent-design.md`를 참고한다.

### 2.3 최종 문서 작성 또는 개선

기준이 정리되면 실제 산출물을 작성하거나 다듬는다.

- 이력서 작업은 `resume/product-engineer.md`를 중심으로 진행한다.
- 프로젝트 케이스 스터디 작업은 대상 문서에 맞는 `case-studies/*.md` 파일을 중심으로 진행한다.
- 종합 포트폴리오의 구조나 중심 메시지를 바꿀 때는 `docs/plans/2026-08-24-general-portfolio-narrative-design.md`를 기준으로 Voice AI, 통화 지표 자동화, AIU가 하나의 문제 해결 패턴으로 연결되는지 확인한다.
- 종합 포트폴리오의 AIU 업무지원 Agent 장을 수정할 때는 `docs/plans/2026-08-24-aiu-portfolio-expansion-design.md`를 기준으로 Supervisor·지식·운영 데이터·OpenBot 실행 경계가 분리되어 있는지 확인한다.
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

### 3.2 현재 프로젝트 케이스 스터디는 3건 정리되어 있다

현재 저장소에서 정리된 프로젝트 케이스 스터디는 3건이다.

- `case-studies/outbound-voice-agent.md`: 아웃바운드 Voice AI Agent
- `case-studies/inbound-voice-agent.md`: 인바운드 Voice AI Agent (아웃바운드의 시리즈 후속편)
- `case-studies/hospital-customer-support-agent.md`: 병원 고객상담 AI Agent

추가 프로젝트를 확장하려면 먼저 사실 자료를 정리하고, 필요한 경우 별도 설계 문서를 만든 뒤 `case-studies/` 아래 케이스 스터디 문서를 늘리는 방식이 적절하다.

## 4. 권장 작업 방식

이 저장소에서 문서를 만들 때는 아래 기준을 유지하는 것이 좋다.

- 사실 업데이트는 먼저 사실 기준 문서에 반영한다.
- 표현 개선은 가이드와 설계 문서를 확인한 뒤 최종 산출물에 적용한다.
- 이미지 생성이나 시각 자산 제작은 문서 구조와 메시지가 정리된 뒤에 진행한다.
