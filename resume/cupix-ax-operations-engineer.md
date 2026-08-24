# 송희웅

**지원 포지션: 큐픽스 AX Operations Engineer**

- 연락처: +82-10-3098-2011
- 이메일: [kofsitho@naver.com](mailto:kofsitho@naver.com)
- GitHub: [https://github.com/kofsitho87](https://github.com/kofsitho87)
- LinkedIn: [https://www.linkedin.com/in/kofsitho](https://www.linkedin.com/in/kofsitho)
- Tech Blog: [https://kofsitho87.github.io/my-tech-blog/](https://kofsitho87.github.io/my-tech-blog/)
- AX Case Study: [AIU 업무지원 Agent 시각 사례](../output/pdf/cupix-ax-aiu-case-study.pdf) · [Interactive HTML](../portfolio/cupix-ax-aiu-case-study.html) · [Career Story](../portfolio/cupix-ax-career-story.html)

## Professional Summary

9년 이상의 백엔드·내부 시스템 경험을 바탕으로, 현업의 반복 업무를 LLM·사내 데이터·업무 도구와 연결해 실제로 쓰이는 AI workflow로 만드는 AX Operations Engineer입니다. Make·Zapier·n8n 같은 로우코드 자동화 대신, 백엔드 코드로 더 유연하고 견고한 자동화 파이프라인을 직접 설계·구현해왔습니다.

최근에는 착수 3주 만에 운영·HQ/SVC가 여러 시스템에서 찾던 제품 매뉴얼과 운영 데이터를 Web·Slack에서 질의할 수 있는 사내 업무지원 Agent를 구축하고, 권한·개인정보·감사 로그 경계를 코드 수준에서 명확히 했습니다. 병원 Voice AI에서는 설정 기반 운영 정책 설계부터 예외 처리, 운영 KPI 관리까지 책임지며 PoC를 프로덕션 운영으로 옮겼습니다.

## Core Competencies

- AX / Workflow Automation: 업무 흐름 구조화, 문서 검색 자동화, 자연어 운영 조회, API·데이터 파이프라인 연동, 설정 기반 정책, 사용자·AI 매뉴얼 정비, 로우코드 툴(Make/Zapier/n8n) 대비 코드 기반 커스텀 자동화
- AI Agent / LLM: OpenAI API, Deep Agents, AG-UI, LangGraph, RAG, Tool Calling
- Backend / Data: Python, TypeScript, Bun, Node.js, FastAPI, MySQL, PostgreSQL, Kafka, Qdrant
- Enterprise Integration: Slack, Web, 사내 DB, Computer Use
- Governance / Operations: Role·Claim 기반 접근 제어, SELECT-only 데이터 도구, 개인정보 비식별화, HITL, 감사 로그, CI와 회귀 테스트
- Infra / DevOps: AWS ECS Fargate, Kubernetes, Docker, GitHub Actions, Terraform, CloudWatch, Auto Scaling



## Experience



### 와이즈에이아이

**AI 엔지니어 / AI 프로덕트 팀장**
2025.03 - 현재

운영·HQ/SVC의 반복 조회를 사내 Agent로 줄이고, 병원 예약·안내 업무를 설정 기반 AI workflow로 구조화해 배포와 운영 개선까지 책임졌습니다.

#### 사내 AIU 업무지원 Multi-Agent 및 AX 자동화

2026.08 - 현재

운영·HQ/SVC가 AIU 사용법, 통화 운영, 화면 설정, 운영 지표를 여러 시스템에서 찾던 반복 업무를 줄이기 위해 사내 업무지원 Agent를 설계·구축했습니다. 2026.08에 착수해 3주 만에 지식 통합, 권한 경계, Web·Slack 런타임과 자동화 테스트까지 1차 운영 가능한 상태로 만들었습니다.

- 현업이 제품별 화면과 데이터 저장소를 외우지 않도록, 기존 AIU Agent를 Web·Slack에서 같은 방식으로 쓰는 AG-UI runtime으로 통합했습니다.
- 5개 사내 시스템의 사용자 매뉴얼과 AI Playbook 322개를 Google Cloud OKF(사내 지식 관리 프레임워크) 지식 번들로 통합하고, 역할·claim 기준으로 본문 접근을 제한해 문서 검색 범위를 안전하게 제한했습니다.
- 최상위 Supervisor가 인바운드·아웃바운드·Agent Admin·HQ/SVC 요청을 나누고, 각 하위 Agent가 자신의 도메인 데이터·업무·권한 경계만 사용하도록 구성했습니다.
- 통화 검색, 병원별 운영 현황, 예약 전환율, 상담원 연결 지표를 자연어로 조회하는 SELECT-only MySQL Tool을 만들고 지표 계산 규칙을 코드로 명시했습니다.
- Docker Compose로 서비스를 묶고 지식 manifest, 권한 격리, 응답, DB 조회, 첨부 처리에 대한 자동화를 구성했습니다.

기술: Deep Agents, AG-UI, Google Cloud OKF

#### 병원 Voice AI 운영 workflow 구축

2025.03 - 현재

병원의 반복적인 예약 확인·안내·상담 업무를, 병원별 정책을 코드 배포 없이 바꿀 수 있는 운영 workflow로 설계하고 실제 전화망에서 운영했습니다.

- 병원별 운영시간, DTMF, 예약 처리, 상담원 연결, 종료 정책을 `flow_config`와 `auto` / `transfer` / `leave_memo` 설정으로 분리했습니다.
- 아웃바운드 Voice AI를 단독 구축해 300개 이상 병원에 도입하고, 일 평균 2,500건·누적 55만 건 이상의 통화를 처리했습니다.
- 무응답, 자동응답기, Agent 전환 충돌, 외부 API 장애를 재현 가능한 상태·이벤트로 정리하고 회귀 테스트와 fallback 경로로 전환했습니다.
- 단위 테스트, text-only Agent 평가, 시뮬레이션, 실제 전화망 테스트를 4단계로 묶고 개인정보 없는 합성 데이터와 mock Tool로 운영 부작용을 차단했습니다.

기술: Python, LiveKit Agents, OpenAI Realtime API, SIP, AWS ECS Fargate

#### 통화 운영 지표 자동화 및 내부 리포팅

2026

- 실시간 통화와 후처리를 Kafka로 분리하고, 업무 시도·최종 결과를 예약 완료, 상담원 연결, 이탈, 실패 원인 KPI로 집계했습니다.
- 업무 완료는 결정론적 event로 계산하고 요청 의도와 응답 품질만 LLM으로 평가해 운영 지표와 품질 지표를 분리했습니다.
- 환자 transcript와 식별 정보는 내부에 유지하고 비민감 집계값만 Langfuse로 보내 개인정보를 보호하면서 추세 분석도 함께 가능하게 했습니다.

기술: Python, Kafka, PostgreSQL, Langfuse

#### 병원 고객상담 workflow 및 운영 대시보드

2025.03 - 2025.05

- 병원별 지식 조회, 개인정보 수집, 상담원 연결이 섞인 상담 업무를 LangGraph 상태 기반 workflow로 구조화했습니다.
- 병원 웹사이트 데이터를 검색 가능한 지식으로 만들어 운영시간, 방문 안내, 의료진 정보를 근거 기반으로 답하게 했습니다.
- FastAPI 서버, 검색 시스템, Next.js 운영 대시보드를 AWS ECS Fargate로 묶어 상담 로직을 운영 도구로 배포했습니다.

기술: Python, FastAPI, LangGraph, Qdrant, Next.js, AWS ECS Fargate

---



### 투썬월드

**소프트웨어 엔지니어**
2019.03 - 2025.02

- BM25·임베딩·cross-encoder reranking을 결합한 비자 문서 RAG를 구축하고 캐싱을 적용해 빈번한 질의 응답 시간을 80% 단축했습니다.
- 크롤링·전처리·검증·번역 파이프라인을 비동기·멀티스레드로 만들어 처리 속도를 300% 개선하고 데이터 정확도 95% 이상을 유지했습니다. Slack/Email 알림과 메트릭 대시보드로 운영 모니터링 체계를 구축했습니다.
- Next.js 15 백오피스와 다국어 채용공고 관리를 구축하고 Claude 기반 자동 번역을 운영 workflow에 통합했습니다.

기술: TypeScript, Next.js, Node.js, OpenAI, Claude, Slack

### 투미유

**소프트웨어 엔지니어**
2017.10 - 2018.12

- 영어회화 학습 서비스의 Swift iOS 앱과 Laravel 백엔드를 개발하고 AWS 인프라를 운영했습니다.

기술: Swift, Laravel, AWS

### 예스콜닷컴

**웹 개발자**
2014.12 - 2016.02

- 반응형 웹 빌더와 쇼핑몰 플랫폼의 프론트엔드·백엔드, 결제, 관리자 기능, SEO와 소셜 연동을 구현했습니다.

기술: JavaScript, AngularJS, PHP, MySQL

## Open Source & Community

- LangChain-OpenTutorial Core Contributor (2025.02)
- LiveKit Agent 기반 AI 영어 선생님 프로젝트 제작 및 지피터스 사례 발표 (2024.10)



## Education



### 대진대학교

- 철학과 졸업
- 2006.03 - 2013.08



## Language

- 영어: 일상 회화
