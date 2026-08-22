# 송희웅

## Experience Sample

### 와이즈에이아이

2025.03 - 현재 | AI 엔지니어 / AI 프로덕트 팀장

- 병원 Voice AI 제품의 실시간 통화 시스템, 상담 구조, 분석 파이프라인, 운영 인프라를 설계·개발·운영
- 총 통화 성공 62만 건+ (아웃바운드 55만+·인바운드 7만+), 일 평균 4,000건 (아웃바운드 2,500·인바운드 1,500), 도입 병원 300개+, 지원 언어 6개

#### 병원 아웃바운드 Voice AI Agent 설계 및 운영

2025.03 - 현재

- 병원의 예약 확인·안내 전화를 AI가 자동 발신하고, 통화 종료 후 전사 교정·구조화 분석·요약까지 비동기로 처리하는 실시간 Voice AI 시스템 설계·개발·운영
- 단일 Agent 구조를 `TriageCoordinator` / `BookingAgent` / `InfoAgent`로 분리한 Multi-Agent 아키텍처 설계
- OpenAI Realtime API와 SIP 트렁크를 결합해 실제 전화망 기반 아웃바운드 콜 시스템 구현, STT→LLM→TTS를 단일 파이프라인으로 통합해 응답 레이턴시 약 900~1200ms 수준 유지
- 예약 CRUD 멀티턴 플로우, Qdrant 기반 병원 정보 검색, 자동응답기 감지, 무응답 종료, 상담원 연결 fallback 등 운영 로직 구현
- Gemini 2.5 Pro 기반 STT 교정, Ghost Message 제거, trustcall 기반 메타데이터 추출, RabbitMQ 기반 분석 파이프라인 분리 구축
- 사용기술: Python, LiveKit Agents, OpenAI Realtime API, SIP, RabbitMQ, Qdrant, Gemini 2.5 Pro, Claude Sonnet, GPT-4.1, trustcall, Pydantic, AWS ECS Fargate, S3, Secrets Manager, CloudWatch, Docker, VPC, Auto Scaling

#### 병원 인바운드 Voice AI Agent 설계

2025

- 환자가 병원에 전화했을 때 병원별 시나리오를 코드 변경 없이 제어할 수 있는 인바운드 Voice AI 시스템 설계
- `flow_config` 기반 노드 그래프 아키텍처로 DTMF IVR과 자유대화 플로우를 동일 엔진에서 처리하도록 설계
- `SupervisorAgent`를 추가해 콜 플로우 제어와 응답 에이전트의 책임 분리
- `action_mode_handler` 패턴으로 `auto` / `transfer` / `leave_memo` 분기를 설정 기반으로 제어
- Warm/Cold Transfer, 재시도, 연결 실패 fallback, Kafka 기반 비동기 분석 파이프라인 구조 설계
- 사용기술: Python, LiveKit Agents, OpenAI Realtime API, SIP, Kafka, Qdrant, Gemini 2.5 Pro, GPT-4.1, Pydantic, AWS ECS Fargate, S3, Docker

#### 병원 고객상담 AI Agent 시스템 아키텍처 설계 및 배포

2025.03 - 2025.05

- 병원별 지식 조회, 개인정보 수집, 상담원 연결 준비를 하나의 흐름으로 다루는 상담 시스템 아키텍처 주도
- LangGraph 기반으로 `primary_assistant`, `customer_interaction`, `extract_personal_info`, `tools` 흐름과 상태 관리 구조 설계
- 병원 웹사이트 데이터를 수집·구조화하고 Qdrant 기반 조회 구조를 연결해 병원별 응답 체계 구축
- FastAPI + LangGraph SDK 기반 API 서버, 검색 시스템, Next.js 운영 대시보드, AWS ECS Fargate 배포 구조를 하나의 서비스 경계로 설계
- 상담원 연결 전 개인정보 수집과 원래 질문 복귀 흐름을 분리해 상담 UX와 운영 절차 정리
- 사용기술: Python, FastAPI, LangGraph, LangChain, trustcall, Crawl4ai, Qdrant, PostgreSQL, Redis, Next.js 15, LangSmith, AWS ECS Fargate, ALB, VPC, ECR, GitHub Actions, Docker, Terraform

