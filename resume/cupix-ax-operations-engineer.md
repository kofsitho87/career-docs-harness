# 송희웅

**지원 포지션: 큐픽스 AX Operations Engineer**

- 연락처: +82-10-3098-2011
- 이메일: [kofsitho@naver.com](mailto:kofsitho@naver.com)
- GitHub: [https://github.com/kofsitho87](https://github.com/kofsitho87)
- LinkedIn: [https://www.linkedin.com/in/kofsitho](https://www.linkedin.com/in/kofsitho)
- Tech Blog: [https://kofsitho87.github.io/my-tech-blog/](https://kofsitho87.github.io/my-tech-blog/)
- AX Case Study: [AIU 업무지원 Agent 시각 사례](../output/pdf/cupix-ax-aiu-case-study.pdf) · [Interactive HTML](../portfolio/cupix-ax-aiu-case-study.html)

## Professional Summary

9년 이상의 개발 경험을 바탕으로 현업의 복잡한 업무를 구조화하고, LLM·사내 데이터·업무 시스템을 연결해 실제 운영 가능한 AI workflow로 만드는 AI Product Engineer입니다.

최근에는 병원 Voice AI 제품의 설계·개발·운영을 리드하는 동시에, AIU 제품과 운영 정보를 Web·Slack에서 질의하고 통화 데이터를 분석할 수 있는 사내 업무지원 Multi-Agent를 구축했습니다. 빠른 PoC에 머무르지 않고 요구사항 정의, 시스템 연동, 권한·개인정보 설계, 테스트, 배포와 운영 개선까지 책임지는 데 강점이 있습니다.

## Core Competencies

- AX / Workflow Automation: 업무 흐름 구조화, API·데이터 파이프라인 연동, 운영 대시보드, 설정 기반 workflow, 사용자·AI 매뉴얼
- AI Agent / LLM: OpenAI API, Deep Agents, LangGraph, LangChain, AG-UI, RAG, Tool Calling, Multi-Agent Orchestration, LLM Evaluation
- Backend / Data: Python, TypeScript, Bun, Node.js, FastAPI, MySQL, PostgreSQL, Redis, Kafka, RabbitMQ, Qdrant
- Enterprise Integration: Slack, Web, 사내 DB, Computer Use, MCP/plugin tool bridge, Object Storage
- Governance / Operations: Role·Claim 기반 접근 제어, SELECT-only 데이터 도구, 개인정보 비식별화, HITL, 감사 로그, CI와 회귀 테스트
- Infra / DevOps: AWS ECS Fargate, Kubernetes, Docker, GitHub Actions, Terraform, CloudWatch, Auto Scaling

## Experience

### 와이즈에이아이

**AI 엔지니어 / AI 프로덕트 팀장**
2025.03 - 현재

현업의 병원 운영 절차를 AI workflow로 구조화하고, 실시간 통화 시스템부터 사내 업무지원 Agent, 데이터 분석과 운영 인프라까지 엔드투엔드로 구축했습니다.

#### 사내 AIU 업무지원 Multi-Agent 및 AX 자동화 플랫폼

2026.08 - 현재

AIU 제품과 운영 정보를 여러 사내 시스템에서 찾아야 하는 반복 업무를 줄이기 위해, OpenBot 기반의 사내 업무지원 AI Agent를 설계·구축했습니다.

- 기존 AIU Agent를 Bun·TypeScript 기반 Deep Agents 아키텍처로 마이그레이션하고 Web과 Slack에서 동일하게 사용할 수 있는 AG-UI Agent runtime으로 통합했습니다.
- 최상위 Supervisor가 요청을 분류하고 인바운드 통화, 아웃바운드 통화, Agent Admin, HQ/SVC 네 전문 Agent에 위임하도록 설계해 각 제품의 데이터·업무·권한 경계를 분리했습니다.
- 5개 사내 시스템에 흩어진 사용자·AI 매뉴얼 322개를 Google Cloud OKF v0.2 지식 번들로 통합했습니다. 역할·claim·문서 분류를 기준으로 본문을 읽기 전에 접근 범위를 제한하고, Supervisor의 원본 문서 직접 접근을 차단했습니다.
- 인바운드·아웃바운드 통화 검색, 병원별 운영 현황, 예약 전환율과 상담원 연결 지표를 자연어로 조회할 수 있는 SELECT-only MySQL Tool을 구현했습니다. 날짜·병원·업무 결과 필터와 운영 지표 계산 규칙을 코드로 명시했습니다.
- 민감한 통화 검토는 최대 5건의 명시적 후보만 읽도록 제한하고 전화번호·주민번호·이메일을 비식별화했습니다. parameter binding, SSL 인증서 검증과 raw transcript 비노출 원칙으로 사내 데이터 접근의 안전 경계를 구축했습니다.
- 서명된 사용자 실행 정보만 Agent가 수락하도록 하고, 브라우저·파일·plugin 작업은 OpenBot의 정책 평가, 감사 로그와 Human-in-the-Loop를 통과하도록 연결했습니다.
- Docker Compose 환경에 서비스를 통합하고 지식 manifest, 권한 격리, AG-UI 응답, DB 조회와 첨부 처리를 검증하는 37개 자동화 테스트를 구성했습니다.

기술: TypeScript, Bun, Deep Agents, LangGraph, LangChain, AG-UI, OpenAI API, MySQL, Slack, Docker, Google Cloud OKF v0.2

#### 병원 Voice AI 업무 자동화 제품 구축 및 운영

2025.03 - 현재

병원의 반복적인 예약 확인·안내·상담 업무를 AI가 실제 전화망에서 처리하도록 제품과 운영 workflow를 설계·개발했습니다.

- 병원별 운영시간, DTMF 메뉴, 예약 처리, 상담원 연결과 종료 정책을 `flow_config`와 `auto` / `transfer` / `leave_memo` 설정으로 분리해, 병원 정책 변경을 애플리케이션 코드와 독립적으로 반영할 수 있게 했습니다.
- 아웃바운드 Voice AI를 단독으로 구축해 100개 이상의 병원에 도입하고, 일 평균 2,000건·누적 96,000건 이상의 실시간 AI 통화를 처리했습니다.
- OpenAI Realtime API와 SIP를 결합해 기존 STT→LLM→TTS 구조의 약 900ms 응답 지연을 약 300ms로 줄이고, 예약 CRUD와 병원 정보 검색을 한 통화 안에서 처리하도록 구현했습니다.
- Self-hosted LiveKit 환경에서 환자·AI·상담원의 음성 권한, DTMF 수락, 상담원 대기열, 재시도·메모 fallback을 관리하는 Single-Room Warm Transfer를 구축했습니다.
- 운영 중 발견한 무응답, 자동응답기, Agent 전환 race condition과 외부 API 장애를 재현 가능한 상태·이벤트로 구조화하고 회귀 테스트와 fallback 경로로 전환했습니다.
- 단위 테스트, text-only Agent 평가, 환자 시뮬레이션, 실제 전화망 테스트를 결합한 4단계 검증 체계를 구축하고 개인정보가 없는 합성 데이터와 mock Tool로 운영 부작용을 차단했습니다.

기술: Python, LiveKit Agents, OpenAI Realtime API, SIP, Kafka, RabbitMQ, Qdrant, Pydantic, AWS ECS Fargate, Kubernetes, Docker

#### 통화 데이터 파이프라인 및 운영 지표 자동화

2026

- 실시간 통화 서비스와 후처리를 Kafka로 분리하고, 대화·Tool event·녹음·latency metric을 정규화하는 멱등 Consumer를 구축했습니다.
- 원본 event를 업무별 시도와 통화별 최종 결과로 변환하는 Analytics v2를 설계해 예약 완료, 상담원 연결, 이탈과 실패 원인을 운영 KPI로 집계할 수 있게 했습니다.
- 업무 완료는 결정론적 event로 계산하고 요청 의도와 응답 품질만 LLM으로 평가해 `task_completion`, `routing_correctness`, `response_quality` 지표로 분리했습니다.
- 환자 transcript와 식별 정보는 내부 저장소에 유지하고 비민감 집계값만 Langfuse에 전송해 개인정보 보호와 평가 추세 분석을 양립시켰습니다.

기술: Python, Kafka, PostgreSQL, Langfuse, LLM Evaluation, Pydantic, Object Storage

#### 병원 고객상담 AI Agent 및 운영 대시보드

2025.03 - 2025.05

- 병원별 지식 조회, 개인정보 수집과 상담원 연결 준비가 섞인 업무를 LangGraph 상태 기반 workflow로 구조화했습니다.
- 병원 웹사이트 데이터를 수집·정제하고 Qdrant 검색과 연결해 운영시간, 방문 안내, 의료진과 진료 정보를 근거 기반으로 제공했습니다.
- FastAPI API 서버, 검색 시스템, Next.js 운영 대시보드와 AWS ECS Fargate 배포를 하나의 서비스로 구축했습니다.

기술: Python, FastAPI, LangGraph, LangChain, Qdrant, PostgreSQL, Redis, Next.js, AWS ECS Fargate, GitHub Actions, Terraform

---

### 투썬월드

**소프트웨어 엔지니어**
2019.03 - 2025.02

- BM25·임베딩·cross-encoder reranking을 결합한 비자 문서 RAG 시스템을 구축하고 캐싱을 적용해 빈번한 질의의 응답 시간을 80% 단축했습니다.
- 크롤링·전처리·분류·검증·번역 데이터 파이프라인을 비동기·멀티스레드 구조로 개발해 처리 속도를 300% 개선하고 데이터 정확도 95% 이상을 유지했습니다.
- Next.js 15 백오피스와 다국어 채용공고 관리 기능을 구축하고 Claude 기반 자동 번역을 운영 workflow에 통합했습니다.
- OpenAI Realtime API와 LiveKit 기반 AI 면접, 이력서 기반 자기소개서 첨삭, CrewAI 평가·점수화 기능을 개발했습니다.
- 15명 규모의 교육 플랫폼에서 프론트엔드 성능을 개선해 Lighthouse 점수를 65점에서 91점으로 높였습니다.

기술: TypeScript, Next.js, React, Vue, Node.js, MongoDB, AWS, OpenAI, Gemini, LiveKit, CrewAI, LangSmith

### 투미유

**소프트웨어 엔지니어**
2017.10 - 2018.12

- 영어회화 학습 서비스의 Swift iOS 앱과 Laravel 백엔드를 개발하고 AWS 인프라를 운영했습니다.

기술: Swift, PHP, Laravel, Redis, Docker, AWS

### 예스콜닷컴

**웹 개발자**
2014.12 - 2016.02

- 반응형 웹 빌더와 쇼핑몰 플랫폼의 프론트엔드·백엔드, 결제, 관리자 기능, SEO와 소셜 연동을 구현했습니다.

기술: JavaScript, jQuery, AngularJS, PHP, MySQL

## Open Source & Community

- LangChain-OpenTutorial Core Contributor (2025.02)
- LiveKit Agent 기반 AI 영어 선생님 프로젝트 제작 및 지피터스 사례 발표 (2024.10)

## Education

### 대진대학교

- 철학과 졸업
- 2006.03 - 2013.08

## Language

- 영어: 일상 회화
