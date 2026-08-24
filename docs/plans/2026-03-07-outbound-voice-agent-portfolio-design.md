# Outbound Voice AI Agent 포트폴리오 설계

## 메타

- 작성일: 2026-03-07
- 타겟: 채용 담당자/면접관
- 형식: 마크다운 (한국어)
- 핵심: 깊이 있는 설명 + 보기 쉬운 구조

## 설계 원칙

- 상단 Executive Summary로 빠른 스캔
- 본문은 문제-해결 스토리텔링
- 다이어그램과 테이블로 가독성 확보
- K8s, VPC 네트워크 상세는 제외

## 섹션 구조

### 1. 프로젝트 개요 (Executive Summary)

- 한 줄 소개, 역할, 기간
- 핵심 지표 테이블
- 전체 시스템 아키텍처 다이어그램
- 기술 스택

### 2. 프로젝트 배경과 목표

- 병원 전화 업무 현실 (85% AI 처리 가능)
- 해결하려는 문제
- 목표

### 3. 아웃바운드 호출 수명주기와 업무 실행 구조

- voxBridge가 Room·SIP 발신을 소유하고 Agent가 `sip.callStatus=active`를 기다리는 책임 분리
- `subscribe-then-snapshot`, 계층화된 timeout, 연결 이후 녹음·AMD와 shutdown 분석 payload 경계
- `FakeAgent` → AMD → `SingleAgent` 전환
- `flow_config` 기반 condition/greeting/agent/action/exit 노드
- 하나의 `SingleAgent`가 Context를 유지하고 예약·DTMF·전환 업무를 AgentTask에 위임
- 통화 목적 계약과 금지 Tool, `auto` / `transfer` / `leave_memo` 정책
- FAQ API 목록을 시작 시 주입하고 등록된 근거 범위 안에서만 응답
- 구조화된 `extra.agent_event`와 레거시 문자열 fallback 구분

### 4. 안전한 예약 신청과 프로덕션 예외 처리

- 생년월일 확인 → 진료과 선택 → 실시간 일정 조회 → 후보 스테이징 → 최종 동의
- 예약은 EMR 즉시 확정이 아니라 병원 확인 전 신청 접수 상태
- 변경·취소는 상담원 연결 또는 메모 접수로 전달
- AMD 사람/기계 판정과 `StopResponse` 기반 첫 발화 race 방어
- Task·AMD·warm transfer와 충돌하지 않는 사용자 무응답 처리
- Redis 공용 FIFO warm transfer, trunk 점유권, 브리핑·DTMF 수락·재시도·메모 fallback

### 5. 통화 분석 파이프라인

- Kafka로 실시간 통화와 분석 Consumer 분리
- 상담원 연결 이후 녹음 구간 Gemini 보완 전사
- 구조화 이벤트 기반 결정론 분류 + trustcall 의미 분석
- GPT-5.6 Luna primary / Gemini 3.5 Flash fallback 분석·요약
- 통화 결과, 예약 신청, 연결·메모·이탈 상태 재구성

### 6. 프로덕션 인프라와 관측

- Tokyo ECS Fargate와 Korea Kubernetes 이중 배포 경로
- S3 녹음, Kafka 후처리, Redis warm-transfer 상태
- STT·Turn Detection·LLM·TTS·Playback·E2E latency 분리 관측
- 구조화 로그, 테스트 통화, 회귀 테스트

### 7. 기술 스택 & 성과 요약

## 참고 문서

아래 참고 문서 중 일부는 현재 저장소에 포함되어 있지 않을 수 있다. 실제 작성 시에는 `case-studies/outbound-voice-agent.md`, `docs/workflow.md`, 현재 저장소 안에 있는 사실 기준 문서를 우선 근거로 사용한다.

- docs/Livkit Agent/outbound_agent_architecture_final.md
- docs/blog/livekit-hospital-voice-agent.md
- docs/blog/call-analysis-pipeline-ko.md
- docs/infra/server-infrastructure.md
- docs/dev/Human 예약 플로우 요약.md
- docs/dev/prompt_and_tools_review.md
- docs/dev/developer_message_catalog.md
- docs/image.png
