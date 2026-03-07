# 송희웅

![Infographic](../assets/heewung-song-infographic.png)

- 연락처: +82-10-3098-2011
- 이메일: [kofsitho@naver.com](mailto:kofsitho@naver.com)
- GitHub: [https://github.com/kofsitho87](https://github.com/kofsitho87)
- LinkedIn: [https://www.linkedin.com/in/kofsitho](https://www.linkedin.com/in/kofsitho)
- Tech Blog: [https://medium.com/@kofsitho](https://medium.com/@kofsitho)

## Professional Summary

9년 이상의 경력을 가진 시니어 소프트웨어 엔지니어입니다. 프론트엔드, 백엔드, 인프라를 아우르며 제품을 설계하고 출시해 왔고, 최근에는 병원 아웃바운드 Voice AI 시스템을 단독으로 설계·개발·운영하며 100개 병원에 도입, 일 2,000건의 실시간 AI 통화를 처리하는 프로덕션 서비스를 구축했습니다.

Multi-Agent 아키텍처 설계, OpenAI Realtime API 기반 실시간 음성 처리, LLM 기반 통화 분석 파이프라인 등 AI 애플리케이션의 설계부터 프로덕션 운영까지 엔드투엔드 오너십에 강점이 있습니다. LangChain 오픈소스 Core Contributor로도 활동했습니다.

## Core Competencies

- Frontend: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, TanStack Query, Vue, Vuetify
- Backend: Python, FastAPI, Node.js
- AI / LLM: OpenAI Realtime API, Claude API, LangGraph, LangChain, RAG, trustcall, LangSmith
- Voice AI & Telephony: LiveKit Agents, SIP Trunk, WebRTC, STT/TTS
- Data / Search: PostgreSQL, MySQL, Redis, MongoDB, Qdrant, hybrid search (Dense + Sparse), OpenAI Embeddings, BM25, cross-encoder reranking
- Infra / DevOps: AWS ECS Fargate, ECR, ALB, VPC, S3, Secrets Manager, CloudWatch, Docker, Auto Scaling, Multi-AZ, GitHub Actions, Terraform

## Experience

### 와이즈에이아이

**AI 엔지니어 / 팀장**  
2025.03 - 현재


| 지표      | 수치           |
| ------- | ------------ |
| 총 통화 성공 | 96,000건+     |
| 일 평균 통화 | 2,000건/일     |
| 도입 병원 수 | 100개+        |
| 지원 언어   | 4개 (한/영/중/일) |


#### 병원 아웃바운드 Voice AI Agent 설계 및 운영

병원의 예약 확인·안내 전화를 AI가 자동으로 발신하고, 통화 종료 후 대화 내용을 자동으로 교정·분석·요약하는 실시간 음성 AI 에이전트 시스템을 설계·개발·운영했습니다.

- 단일 Agent(프롬프트 200줄, 도구 14개)의 도구 오호출·지시사항 누락 한계를 분석하고, TriageCoordinator(의도 분류) / BookingAgent(예약 처리) / InfoAgent(정보 안내)로 3개 Agent를 분리하는 Multi-Agent 아키텍처를 설계했습니다. Agent당 프롬프트 40-50줄, 도구 3-6개로 축소해 도구 오호출률을 현저히 감소시키고 유지보수성을 향상시켰습니다.
- OpenAI Realtime API를 도입해 기존 STT→LLM→TTS 파이프라인(~900ms) 대비 ~300ms로 응답 레이턴시를 대폭 감소시켰습니다. SIP 트렁크를 통한 실제 전화망 연동으로 아웃바운드 콜 자동 발신을 구현했습니다.
- 예약 CRUD 도구(진료과→의사→날짜→시간→확인)의 순차 플로우와 Qdrant 벡터 DB 기반 병원 정보 검색 도구(5개 카테고리, 토픽별 메타데이터 필터링)를 설계했습니다.
- 자동응답기(ARS) 감지(3중 조건 검증), 사용자 무응답 감지(2회 확인 후 자동 종료), 상담원 연결 Fallback(SIP Transfer / 메시지 수집 분기) 등 실전 예외 처리 로직을 구현했습니다.
- Gemini 2.5 Pro 멀티모달로 원본 오디오와 텍스트를 비교해 STT 오류를 교정하고, Ghost Message(가짜 발화 인식) 자동 제거 및 DTMF 메시지 삭제 방지 예외 처리를 구현했습니다.
- trustcall + Claude Sonnet / GPT-4.1로 15개 메타데이터를 자동 추출하는 분석 단계를 구현했습니다. Pydantic 스키마 + JSON Patch 방식으로 안정적 구조화 출력을 달성했습니다.
- LLM 판단 결과를 로그 기반 규칙으로 보정하는 LLM + Hard Rules 하이브리드 판단 체계를 구현해 분석 일관성과 정확도를 향상시켰습니다.
- RabbitMQ 기반으로 통화 서비스와 분석 서비스를 완전 분리해 독립 스케일링 및 장애 격리를 달성했습니다.
- AWS ECS Fargate 기반 DEV / QA / PROD 3환경 분리 운영, Multi-AZ 구성으로 고가용성을 확보했습니다.
- 한국 병원 운영시간에 맞춘 시간 기반 스케일링(07:50 시작→09:30 용량 증가→21:30 중지)과 CPU/Memory 메트릭 기반 동적 스케일링(최대 20 태스크)을 설계해 비용을 최적화했습니다.
- AWS Secrets Manager(API 키 9개), VPC + 보안 그룹 네트워크 격리, CloudWatch JSON 구조화 로그 모니터링 체계를 구축했습니다.

기술: Python, LiveKit Agents, OpenAI Realtime API, Google Gemini Live, SIP, Qdrant, RabbitMQ, Gemini 2.5 Pro, Claude Sonnet, GPT-4.1, trustcall, LangChain, Pydantic, AWS ECS Fargate, S3, Secrets Manager, CloudWatch, Docker, VPC, Auto Scaling

#### 병원 고객상담 AI Agent 시스템 설계 및 배포

의료기관 고객 상담 자동화를 위한 AI Agent 시스템을 설계하고, 백엔드 API부터 검색 시스템, 운영 대시보드까지 구축했습니다.

- LangGraph 기반 대화 상태 관리와 멀티스텝 워크플로우를 설계 했습니다.
- 병원 웹사이트 데이터를 자동 수집하고 6개 토픽으로 분류·구조화하는 추출 파이프라인을 개발했습니다. TrustCall 기반 스키마 추출로 90% 이상의 정보 추출 정확도를 달성했습니다.
- FastAPI + LangGraph SDK 기반 비동기 API 서버를 설계하고 API 응답 속도를 70% 개선했습니다.
- Qdrant 기반 하이브리드 검색 시스템과 Next.js 15 기반 Agent 모니터링 대시보드를 구축했습니다.

기술: Python, FastAPI, LangGraph, LangChain, TrustCall, Crawl4ai, Qdrant, PostgreSQL, Redis, Next.js 15, CopilotKit, shadcn/ui, LangSmith

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

