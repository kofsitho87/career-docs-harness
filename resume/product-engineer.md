# 송희웅

![Infographic](../assets/heewung-song-infographic.png)

- 연락처: +82-10-3098-2011
- 이메일: [kofsitho@naver.com](mailto:kofsitho@naver.com)
- GitHub: [https://github.com/kofsitho87](https://github.com/kofsitho87)
- LinkedIn: [https://www.linkedin.com/in/kofsitho](https://www.linkedin.com/in/kofsitho)
- Tech Blog: [https://kofsitho87.github.io/my-tech-blog/](https://kofsitho87.github.io/my-tech-blog/)
- Medium: [https://medium.com/@kofsitho](https://medium.com/@kofsitho)

## Professional Summary

9년 이상의 경력을 가진 시니어 소프트웨어 엔지니어입니다. 프론트엔드, 백엔드, 인프라를 아우르며 제품을 설계하고 출시해 왔고, 최근에는 병원 인바운드·아웃바운드 Voice AI 제품을 엔드투엔드로 개발·운영하고 있습니다. 아웃바운드 시스템을 단독으로 구축해 300개 병원에 도입하고 일 평균 2,500건의 실시간 AI 통화를 처리했습니다.

Self-hosted LiveKit 기반 실시간 음성 처리, 안전한 Tool Calling과 AgentTask 설계, 상담원 전환, Kafka 기반 통화 분석과 LLM 평가 등 AI 애플리케이션의 설계부터 프로덕션 운영까지 엔드투엔드 오너십에 강점이 있습니다. LangChain 오픈소스 Core Contributor로도 활동했습니다.

## Core Competencies

- Frontend: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, TanStack Query, Vue, Vuetify
- Backend: Python, FastAPI, Node.js, Kafka, RabbitMQ
- AI / LLM: OpenAI Realtime API, Claude API, LangGraph, LangChain, RAG, trustcall, LangSmith, Langfuse, LLM Evaluation
- Voice AI & Telephony: LiveKit Agents, Self-hosted LiveKit, SIP Trunk, WebRTC, STT/TTS, DTMF, AMD, Warm/Cold Transfer
- Data / Search: PostgreSQL, MySQL, Redis, MongoDB, Qdrant, hybrid search (Dense + Sparse), OpenAI Embeddings, BM25, cross-encoder reranking
- Infra / DevOps: AWS ECS Fargate, Kubernetes, ECR, ALB, VPC, S3, Secrets Manager, CloudWatch, Docker, Auto Scaling, Multi-AZ, GitHub Actions, Terraform

## Experience

### 와이즈에이아이

**AI 엔지니어 / AI 프로덕트 팀장**  
2025.03 - 현재

병원 Voice AI 제품을 1인 설계·개발·운영하거나 핵심 아키텍트로 리드하며, 실시간 통화 시스템부터 상담 구조, 분석 파이프라인, 운영 인프라까지 엔드투엔드로 구축했습니다.

| 지표 | 수치 |
|------|------|
| 총 통화 성공 | 62만 건+ (아웃바운드 55만+ · 인바운드 7만+) |
| 일 평균 통화 | 4,000건/일 (아웃바운드 2,500 · 인바운드 1,500) |
| 도입 병원 수 | 300개+ |
| 지원 언어 | 6개 (한/영/중/일/스페인어/베트남어) |

#### 사내 AIU 업무지원 Multi-Agent 및 AX 자동화 플랫폼 구축

2026.08 - 현재

AIU 제품과 운영 정보를 여러 사내 시스템에서 찾아야 하는 반복 업무를 줄이기 위해, OpenBot 기반의 사내 업무지원 AI Agent를 설계·구축했습니다.

- Web과 Slack에서 AIU 제품 사용법, 인바운드·아웃바운드 통화 운영, Agent Admin, HQ/SVC 업무를 질의할 수 있도록 기존 AIU Agent를 Bun·TypeScript 기반 Deep Agents 아키텍처로 마이그레이션했습니다.
- 최상위 Supervisor가 요청 도메인을 판별하고 `inbound-agent`, `agent-admin-agent`, `outbound-agent`, `hq-svc-agent` 네 전문 Agent에 위임하도록 구성해 서로 다른 제품·데이터·권한 경계를 분리했습니다.
- 5개 사내 시스템의 사용자·AI 매뉴얼 322개를 Google Cloud OKF v0.2 지식 번들로 통합하고, source manifest와 frontmatter의 역할·claim·분류 정보를 기준으로 검색 전에 접근 범위를 제한하는 read-only 지식 backend를 구현했습니다.
- 인바운드·아웃바운드 통화 검색과 전환율·운영 지표 분석을 위한 SELECT-only MySQL Tool을 구현했습니다. 사용자 입력은 parameter binding으로 분리하고 SSL 인증서 검증, 조회 한도, transcript 비식별화와 근거 turn 제한을 적용했습니다.
- AG-UI를 통해 Web·Slack 실행을 하나의 Agent runtime으로 연결하고, 서명된 run assertion, OpenBot의 Computer Use·plugin 정책, 감사 로그와 Human-in-the-Loop 경계를 유지하도록 통합했습니다.
- Docker Compose 실행 환경과 지식 manifest·권한 격리·AG-UI 응답·DB 조회·첨부 처리 등을 검증하는 37개 자동화 테스트를 구성했습니다.

기술: TypeScript, Bun, Deep Agents, LangGraph, LangChain, AG-UI, OpenAI API, MySQL, Slack, Docker, Google Cloud OKF v0.2

#### 병원 아웃바운드 Voice AI Agent 설계 및 운영

2025 - 현재

병원의 예약 확인·안내 전화를 AI가 자동 발신하고, 통화 종료 후 전사 교정·구조화 분석·요약까지 비동기로 처리하는 실시간 Voice AI 시스템을 설계·개발·운영했습니다.

- 단일 Agent의 프롬프트 과대화와 도구 오호출 문제를 분석해 `TriageCoordinator` / `BookingAgent` / `InfoAgent`로 분리된 Multi-Agent 아키텍처를 설계했습니다.
- OpenAI Realtime API와 SIP 트렁크를 결합해 실제 전화망 기반 아웃바운드 콜 시스템을 구현했습니다. STT→LLM→TTS 개별 호출을 단일 Realtime 파이프라인으로 통합해 응답 레이턴시를 약 900~1200ms 수준으로 유지하며 자연스러운 실시간 대화 경험을 만들었습니다.
- 예약 CRUD를 멀티턴 대화 플로우로 설계하고, Qdrant 기반 병원 정보 검색 도구를 붙여 예약 처리와 병원 안내를 한 통화 안에서 이어지도록 만들었습니다.
- 자동응답기 3중 조건 감지, 사용자 무응답 종료, 상담원 연결 및 메시지 수집 fallback 등 프로덕션 예외 처리 로직을 구축해 실제 운영 환경에서의 실패 케이스를 흡수했습니다.
- Gemini 2.5 Pro 멀티모달 기반 STT 교정, Ghost Message 제거, DTMF 보존 예외 처리, trustcall 기반 메타데이터 추출을 포함한 통화 분석 파이프라인을 구현했습니다.
- RabbitMQ로 통화 처리와 분석 처리를 분리하고, AWS ECS Fargate DEV/QA/PROD 3환경, Multi-AZ, 시간 기반 + 메트릭 기반 오토스케일링(최대 20 태스크), Secrets Manager, CloudWatch 구조화 로그 체계를 설계해 운영 안정성과 비용 효율을 함께 확보했습니다.
- 외부 발신 오케스트레이터와 LiveKit Agent 사이의 통화 수명주기를 event-driven 방식으로 재설계했습니다. Participant listener 등록 후 현재 상태를 다시 확인하는 `subscribe-then-snapshot`, 계층화된 timeout, 실제 SIP 연결 이후의 녹음·분석 callback 등록으로 연결 race와 잘못된 후처리를 방지했습니다.
- AMD 판별 중 시작된 발화가 Agent 전환 후 완료되며 설정 인사말 대신 LLM 응답을 생성하던 race condition을 메트릭 타임라인으로 추적했습니다. 생성이 금지된 최종 Task에서 `StopResponse`를 강제하고 회귀 테스트를 추가해 결정적 인사말 경계를 보호했습니다.

기술: Python, LiveKit Agents, OpenAI Realtime API, LiveKit AMD, SIP, voxBridge, RabbitMQ, Qdrant, Gemini 2.5 Pro, Claude Sonnet, GPT-4.1, trustcall, Pydantic, AWS ECS Fargate, S3, Secrets Manager, CloudWatch, Docker, VPC, Auto Scaling

#### 병원 인바운드 Voice AI Agent 구축 및 운영

2025 - 현재

환자가 병원에 전화해 예약 조회·신청·변경·취소, 병원 정보 안내, 상담원 연결을 처리할 수 있는 Self-hosted LiveKit 기반 인바운드 Voice AI 시스템을 구축·운영하고 있습니다.

- `AgentServer` / `AgentSession` / `SingleAgent` 런타임과 `flow_config` 기반 노드 그래프를 결합했습니다. 병원별 운영시간, DTMF 메뉴, 자유대화, 상담원 연결과 종료 정책을 코드 배포 없이 설정으로 제어하도록 만들었습니다.
- 하나의 `SingleAgent`가 통화 Context를 유지하고 예약·DTMF·상담원 연결 업무를 `AgentTask`에 위임하는 Supervisor Pattern을 구현했습니다. Task가 typed result를 반환하도록 해 업무 완료, 이탈, 상담원 요청과 통화 종료의 제어권을 명확히 분리했습니다.
- 예약 조회·신청·변경·취소 흐름에서 LLM은 대화를 담당하고 코드는 병원 기준 정보, 실시간 일정, 후보 스테이징과 최종 동의 대상을 검증하도록 설계했습니다. 병원별 `auto` / `transfer` / `leave_memo` 정책을 공통 코드에서 분기해 잘못된 Tool 실행과 상태 변경을 방지했습니다.
- Self-hosted LiveKit 환경에 `SingleRoomWarmTransferTask`를 구현했습니다. 환자·AI·상담원의 오디오 구독 권한, DTMF 수락, FIFO 상담원 대기열, 재시도·AI 복귀·메모 fallback과 연결 종료까지 상태 머신으로 관리했습니다.
- VAD, endpointing, turn detection, interruption과 preemptive generation을 조정하고 STT·LLM·TTS·Tool·E2E 지표를 분리해 관측했습니다. 결정적 안내와 되돌리기 어려운 Tool 구간에는 별도 interruption guardrail을 적용했습니다.
- 단위 테스트, LiveKit text-only Agent 평가, 로컬 환자 시뮬레이션, 오디오·실제 전화망 검증으로 이어지는 4단계 테스트 체계를 구축했습니다. 외부 예약·연결·종료 Tool을 mock 처리하고 운영 장애를 회귀 시나리오로 전환했습니다.
- LiveKit Worker의 통화별 프로세스 격리와 Kubernetes Pod 수용량을 분석해 prewarm·메모리·동시 Job·graceful drain을 함께 다루는 동시 통화 확장 및 장애 복구 기준을 정리했습니다.

기술: Python, LiveKit Agents, Self-hosted LiveKit, SIP, STT/LLM/TTS, DTMF, Kafka, Qdrant, GPT-4.1, Pydantic, Kubernetes, S3, Docker, pytest

#### Voice AI 통화 분석 및 Privacy-safe LLM 평가 파이프라인

2026

실시간 통화와 분석 부하를 분리하면서도 한 통화의 업무 결과와 품질을 재구성할 수 있는 Kafka 기반 후처리·평가 파이프라인을 구축했습니다.

- 대화 transcript, 구조화 Agent event, 녹음과 단계별 latency metric을 Kafka로 전달하고, `room_name` 기준 멱등 처리와 재처리가 가능한 Consumer를 구현해 분석 장애가 실시간 통화에 영향을 주지 않도록 분리했습니다.
- 상담원 연결 이후의 녹음 구간을 잘라 전사를 보완하고, 원본 event를 업무별 시도와 통화별 최종 resolution으로 정규화하는 Analytics v2를 설계했습니다. 실패를 단계·유형·개선 주체로 분류해 운영 KPI에서 원인까지 추적할 수 있게 했습니다.
- 업무 완료는 결정론적 event로, 요청 의도와 응답 품질은 근거 turn을 포함한 Semantic 분석으로 평가했습니다. `task_completion`, `routing_correctness`, `response_quality`를 버전이 있는 Langfuse session score로 발행하도록 구현했습니다.
- 환자 transcript·임상 정보·식별 정보는 로컬 저장소에 유지하고 비민감 집계값만 Langfuse로 전송했습니다. 통화·점수·평가 버전 기반 idempotency key와 hard-cap 규칙으로 개인정보 경계와 재평가 일관성을 확보했습니다.

기술: Python, Kafka, PostgreSQL, LLM Evaluation, Langfuse, Pydantic, Object Storage

#### 역할 기반 사용자·AI 매뉴얼 및 코드 동기화 체계 구축

2026

- Google Cloud Open Knowledge Format v0.2를 기반으로 사용자 매뉴얼과 AI용 Playbook·Policy·State Model을 하나의 지식 번들로 설계하고, 역할·claim·위험도·근거 source를 frontmatter 계약으로 정의했습니다.
- 인증된 역할과 claim으로 본문 로드 전에 문서 접근 범위를 줄이는 resolver, 코드 capability와 문서를 연결하는 catalog, 두 매뉴얼이 공유하는 Git 동기화 marker를 구현했습니다.
- source drift, 깨진 링크, capability coverage, HITL 확인 정책과 공개·비공개 문서 경계를 검사하는 deterministic checker와 CI를 구축했습니다. 현재 문서 내용은 사람 검토가 진행 중인 draft로 관리하고 있습니다.

기술: Google Cloud OKF v0.2, Python, Markdown, YAML, GitHub Actions

#### 병원 고객상담 AI Agent 시스템 아키텍처 설계 및 배포

2025.03 - 2025.05

의료기관 고객 상담 자동화를 위해, 단순 FAQ 응답기가 아니라 병원별 지식 조회와 개인정보 수집, 상담원 연결 준비를 하나의 흐름으로 다루는 상담 시스템 아키텍처를 주도했습니다.

- LangGraph 기반으로 `primary_assistant`, `customer_interaction`, `extract_personal_info`, `tools` 흐름을 분리하고, `pending_question`, `collected_info` 같은 상태를 명시적으로 관리해 절차가 섞인 상담을 안정적으로 처리할 수 있게 설계했습니다.
- 병원 웹사이트 데이터를 수집·구조화해 검색 가능한 지식 레이어를 만들고, Qdrant 기반 조회 구조를 통해 병원별 운영시간, 방문 안내, 의료진, 진료·시술 정보를 상담 응답에 연결했습니다.
- FastAPI + LangGraph SDK 기반 비동기 API 서버, 검색 시스템, Next.js 운영 대시보드, AWS ECS Fargate 배포 구조를 하나의 서비스 경계로 설계해 상담 로직이 프로토타입이 아니라 운영 가능한 제품으로 이어지도록 만들었습니다.
- 상담원 연결 시 필요한 개인정보 수집과 원래 질문 복귀 흐름을 분리해, 사용자가 같은 맥락을 반복 설명하지 않아도 되도록 상담 UX와 운영 절차를 함께 정리했습니다.

기술: Python, FastAPI, LangGraph, LangChain, trustcall, Crawl4ai, Qdrant, PostgreSQL, Redis, Next.js 15, LangSmith, AWS ECS Fargate, ALB, VPC, ECR, GitHub Actions, Docker, Terraform

---

### 투썬월드

**소프트웨어 엔지니어**
2019.03 - 2025.02 (6년)

교육 및 AI 기반 서비스에서 웹 제품 개발과 신규 기능 구현을 담당했습니다. 서비스 기획 의도를 제품 기능으로 구체화하고, 프론트엔드 구현부터 데이터 처리, AI 기능 실험까지 폭넓게 수행했습니다.

#### RAG 비자 챗봇 시스템 설계 및 개발

2024.02 - 2024.04

- 비자 관련 문서를 마크다운으로 전처리하고, 벡터 데이터베이스 기반의 검색 가능한 지식베이스로 재구성했습니다.
- BM25 키워드 검색과 임베딩 기반 시맨틱 검색을 결합한 하이브리드 검색 아키텍처를 설계했습니다. 키워드 검색(Recall) → 시맨틱 검색(Precision) → cross-encoder reranker(최종 순위)로 이어지는 3단계 파이프라인을 구현했습니다.
- 청킹 전략(512 tokens, overlap 50), 인덱싱 방식, 메타데이터 구조를 최적화하고 캐싱 레이어를 도입해 빈번한 질의의 응답 시간을 80% 단축했습니다.
- LangSmith 트레이싱과 사용자 피드백 수집을 적용해 검색 품질을 지속적으로 모니터링하고 A/B 테스트를 통해 검색 파라미터를 최적화했습니다.

#### 크롤링 및 데이터 수집·처리 파이프라인 설계

2024.06 - 2024.07

- 대규모 데이터 수집을 위한 크롤링, 전처리, 분류, 검증, 번역 파이프라인을 설계하고 구현했습니다.
- 비동기 처리와 멀티스레딩 병렬화를 적용해 크롤링 처리 속도를 300% 개선했습니다.
- 데이터 검증 및 정합성 확인을 자동화해 데이터 정확도 95% 이상을 유지하는 파이프라인을 구축했습니다.
- JSONL 기반 구조화 로그, Slack/Email 실시간 알림, 성능 메트릭 대시보드를 구성해 운영 모니터링 체계를 만들었습니다.

#### AI 면접 데모 및 AI 자기소개서 첨삭 기능 개발

2024.11

- OpenAI Realtime API와 LiveKit Agent를 활용해 음성 기반 AI 면접 PoC를 개발했습니다.
- 이력서 업로드 기반 자기소개서 AI 첨삭 기능을 구현했습니다.
- CrewAI를 활용해 면접 대화 내용 기반 평가 및 점수화 기능을 구현했습니다.

#### 백오피스 애플리케이션 개발

2024.09 - 2024.11

- Next.js 15 기반 백오피스 애플리케이션을 구축하고, 다국어 채용 공고 관리 기능을 개발했습니다.
- Claude 기반 자동 번역 기능을 서비스 운영 흐름에 통합했습니다.

#### 한국어 교육 플랫폼 개발

2023.09 - 2024.01 | 15명 규모 프로젝트

- Next.js 14, TypeScript, Tailwind CSS, shadcn/ui 기반 반응형 웹 UI를 구현했습니다.
- REST API 연동을 통해 강의 콘텐츠 제공과 학습 진행 상태 추적 기능을 개발했습니다.
- OpenAI, Gemini 기반 프롬프트 실험을 통해 한국어 학습용 콘텐츠 생성 기능을 개발했습니다.
- 프론트엔드 성능을 최적화해 Lighthouse 점수를 65점에서 91점으로 개선했습니다 (페이지 로딩 속도 40% 향상).

#### 공맵 멘토링 플랫폼

2023.04 - 2023.08

- 해외 교육 과정(SAT, IB, AP, A-Level) 준비생을 위한 온라인 멘토링 플랫폼을 설계하고 개발했습니다.
- 학습 요구사항과 멘토 전문성을 반영한 매칭 알고리즘을 구현했습니다.
- 입시 정보, 대학 리소스, 에세이 가이드를 통합 제공하는 제품 흐름을 설계했습니다.

기술: TypeScript, Next.js, React, Vue, Vuetify, Pinia, TanStack Query, MongoDB, AWS, OpenAI, Gemini, LiveKit, CrewAI, LangSmith

---

### 투미유

**소프트웨어 엔지니어**
2017.10 - 2018.12 (1년 3개월)

- 영어회화 학습 서비스 "투덥"의 iOS 앱과 백엔드를 개발했습니다.
- Swift 기반 iOS 앱 개발, Laravel 기반 서버 개발, AWS 인프라 운영을 담당했습니다.

기술: Swift, PHP, Laravel, Redis, Docker, AWS (EC2, ELB, S3, RDS), FFmpeg

---

### 예스콜닷컴

**웹 개발자**
2014.12 - 2016.02 (1년 3개월)

- 반응형 웹 빌더 "DUBUPLUS"와 쇼핑몰 제작 플랫폼의 프론트엔드·백엔드를 개발했습니다.
- 결제 시스템, 관리자 모듈, SEO 최적화, 소셜 연동 기능을 구현했습니다.

기술: JavaScript, jQuery, AngularJS, PHP, MySQL

## Education

### 대진대학교

- 철학과 졸업
- 2006.03 - 2013.08

## Open Source & Community

### LangChain-OpenTutorial Core Contributor

2025.02

- LangChain 공식 튜토리얼 오픈소스 프로젝트에 참여해 Core Contributor로 등록되었습니다.
- [https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial)

### 지피터스 AI 프로덕트 사례 발표

2024.10

- LiveKit Agent 기반 AI 영어 선생님 프로젝트를 제작하고 커뮤니티에서 사례를 발표했습니다.
- [사례발표 1](https://www.gpters.org/chatbot/post/ai-roleplaying-conversation-application-qnoe9TQDzZv9lQM) | [사례발표 2](https://www.gpters.org/chatbot/post/ai-roleplaying-conversation-application-iF1DFPjzxXdvSlm)

## Language

- 영어: 일상 회화
