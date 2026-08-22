# 송희웅

## Experience Sample

### 와이즈에이아이

**AI 엔지니어 / AI 프로덕트 팀장**  
2025.03 - 현재

병원 Voice AI 제품을 1인 설계·개발·운영하거나 핵심 아키텍트로 리드하며, 실시간 통화 시스템부터 상담 구조, 분석 파이프라인, 운영 인프라까지 엔드투엔드로 구축했습니다.


| 지표      | 수치                     |
| ------- | ---------------------- |
| 총 통화 성공 | 62만 건+ (아웃바운드 55만+ · 인바운드 7만+) |
| 일 평균 통화 | 4,000건/일 (아웃바운드 2,500 · 인바운드 1,500) |
| 도입 병원 수 | 300개+                  |
| 지원 언어   | 6개 (한/영/중/일/스페인어/베트남어) |


#### 병원 아웃바운드 Voice AI Agent 설계 및 운영

2025.03 - 현재

- OpenAI Realtime API와 SIP 트렁크를 결합한 실시간 아웃바운드 콜 시스템을 설계·구현해 병원 예약 확인·안내 통화를 자동화했습니다.
- 단일 Agent의 한계를 분석하고 `TriageCoordinator` / `BookingAgent` / `InfoAgent` 기반 Multi-Agent 구조로 재설계해 운영 안정성과 유지보수성을 높였습니다.
- STT→LLM→TTS 개별 호출을 단일 Realtime 파이프라인으로 통합해 응답 레이턴시를 약 900~1200ms 수준으로 유지했고, 예약 CRUD 멀티턴 플로우와 Qdrant 기반 정보 검색을 한 통화 안에서 연결했습니다.
- 자동응답기 감지, 무응답 종료, 상담원 연결 fallback, STT 교정, Ghost Message 제거, trustcall 기반 메타데이터 추출까지 포함한 프로덕션 운영 구조를 구축했습니다.
- 사용기술: Python, LiveKit Agents, OpenAI Realtime API, SIP, RabbitMQ, Qdrant, Gemini 2.5 Pro, Claude Sonnet, GPT-4.1, trustcall, Pydantic, AWS ECS Fargate, S3, Secrets Manager, CloudWatch, Docker, VPC, Auto Scaling

#### 병원 인바운드 Voice AI Agent 설계

2025

- 병원마다 다른 전화 응대 시나리오를 코드 수정 없이 제어하기 위해 `flow_config` 기반 노드 그래프 아키텍처를 설계했습니다.
- `SupervisorAgent`를 추가해 콜 플로우 제어와 실제 응답 에이전트를 분리했고, DTMF IVR과 자유대화 플로우를 동일 엔진에서 처리할 수 있게 만들었습니다.
- `action_mode_handler` 패턴으로 `auto` / `transfer` / `leave_memo` 분기를 설정 기반으로 제어하고, Warm/Cold Transfer 및 재시도 구조까지 포함해 상담원 연결 경계를 제품 수준으로 정리했습니다.
- Kafka 기반 비동기 분석 파이프라인으로 정규화, 규칙 기반 메타데이터 추출, 상담원 대화 전사, 요약 저장 흐름을 분리했습니다.
- 사용기술: Python, LiveKit Agents, OpenAI Realtime API, SIP, Kafka, Qdrant, Gemini 2.5 Pro, GPT-4.1, Pydantic, AWS ECS Fargate, S3, Docker

#### 병원 고객상담 AI Agent 시스템 아키텍처 설계 및 배포

2025.03 - 2025.05

- 단순 FAQ 응답기가 아니라 병원별 지식 조회, 개인정보 수집, 상담원 연결 준비를 하나의 흐름으로 다루는 상담 시스템 아키텍처를 주도했습니다.
- LangGraph 기반으로 `primary_assistant`, `customer_interaction`, `extract_personal_info`, `tools` 흐름과 상태 전이 구조를 설계해 절차가 섞인 상담을 안정적으로 처리할 수 있게 했습니다.
- 병원 웹사이트 데이터를 수집·구조화하고 Qdrant 기반 조회 구조를 연결해 병원별 운영시간, 방문 안내, 의료진, 진료·시술 정보를 응답에 반영했습니다.
- FastAPI + LangGraph SDK 기반 API 서버, 검색 시스템, Next.js 운영 대시보드, AWS ECS Fargate 배포 구조를 하나의 서비스 경계로 설계해 운영 가능한 제품 형태로 연결했습니다.
- 사용기술: Python, FastAPI, LangGraph, LangChain, trustcall, Crawl4ai, Qdrant, PostgreSQL, Redis, Next.js 15, LangSmith, AWS ECS Fargate, ALB, VPC, ECR, GitHub Actions, Docker, Terraform

