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

### 3. Multi-Agent Voice AI 설계

- 단일 Agent 한계 → Multi-Agent 전환 (Before/After)
- TriageCoordinator / BookingAgent / InfoAgent 역할
- Agent 전환 플로우 + 컨텍스트 전달
- 예약 플로우 (AgentTask 멀티턴)
- Qdrant 벡터 DB 기반 정보 검색
- OpenAI Realtime API (900ms → 300ms)
- 실전 예외 처리 (ARS, 무응답, 상담원 Fallback, Human 예약 모드)
- 프롬프트 시스템 + Developer 메시지 카탈로그

### 4. 통화 분석 파이프라인

- 왜 필요한가 (STT 오류, 결과 파악)
- 3단계 비동기 파이프라인 (Gemini 교정 → trustcall 분석 → 요약)
- Ghost Message + DTMF 처리
- LLM + Hard Rules 하이브리드
- 비즈니스 로직 연동 (예약 모드별 분기)

### 5. 프로덕션 인프라

- AWS ECS Fargate DEV/QA/PROD 3환경
- Multi-AZ 고가용성
- 시간 기반 + 메트릭 기반 Auto Scaling
- Secrets Manager, CloudWatch 모니터링

### 6. 기술 스택 & 성과 요약

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

