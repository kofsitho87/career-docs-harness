# 송희웅

Infographic

- 연락처: +82-10-3098-2011
- 이메일: [kofsitho@naver.com](mailto:kofsitho@naver.com)
- GitHub: [https://github.com/kofsitho87](https://github.com/kofsitho87)
- LinkedIn: [https://www.linkedin.com/in/kofsitho](https://www.linkedin.com/in/kofsitho)
- Tech Blog: [https://kofsitho87.github.io/my-tech-blog/](https://kofsitho87.github.io/my-tech-blog/)
- Medium: [https://medium.com/@kofsitho](https://medium.com/@kofsitho)
- Portfolio: [종합 포트폴리오](../portfolio/html/heewung-song-portfolio.html)

## Professional Summary

10년+ 경력의 소프트웨어 엔지니어로, 최근에는 AI 제품의 설계와 운영을 맡고 있습니다. 병원 300곳에 도입된 아웃바운드 Voice AI를 엔드투엔드로 구축했고, 지금은 하루 4,000건 규모의 인바운드·아웃바운드 AI 통화를 운영합니다. 같은 방식을 통화 분석과 사내 업무지원 AI로 넓히고 있습니다.

Self-hosted LiveKit 기반 실시간 음성 처리, 안전한 Tool Calling과 AgentTask 설계, 상담원 전환, Kafka 기반 통화 분석과 LLM 평가 등 AI 애플리케이션의 설계부터 프로덕션 운영까지 엔드투엔드 오너십에 강점이 있습니다. LangChain 오픈소스 Core Contributor로도 활동했습니다.

## Core Competencies

- Frontend: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, TanStack Query
- Backend: Python, FastAPI, Node.js, Kafka, RabbitMQ
- AI / LLM: OpenAI Realtime API, Claude API, LangGraph, LangChain, RAG, trustcall, LangSmith, Langfuse, LLM Evaluation
- Voice AI & Telephony: LiveKit Agents, Self-hosted LiveKit, SIP Trunk, WebRTC, STT/TTS, DTMF, AMD, Warm/Cold Transfer
- Data / Search: PostgreSQL, MySQL, Redis, MongoDB, Qdrant, hybrid search (Dense + Sparse), OpenAI Embeddings, BM25, cross-encoder reranking
- Infra / DevOps: AWS ECS Fargate, ECR, ALB, VPC, S3, Secrets Manager, CloudWatch, Docker, Auto Scaling, Multi-AZ, GitHub Actions, Terraform



## Experience



### 와이즈에이아이

**AI 엔지니어 / AI 프로덕트 팀장**  
2025.03 - 현재

병원 Voice AI 제품을 1인 설계·개발·운영하거나 핵심 아키텍트로 리드하며, 실시간 통화 시스템부터 상담 구조, 분석 파이프라인, 운영 인프라까지 엔드투엔드로 구축했습니다.


| 지표      | 수치                                  |
| ------- | ----------------------------------- |
| 총 통화 성공 | 62만 건+ (아웃바운드 55만+ · 인바운드 7만+)      |
| 일 평균 통화 | 4,000건/일 (아웃바운드 2,500 · 인바운드 1,500) |
| 도입 병원 수 | 300개+                               |
| 지원 언어   | 6개 (한/영/중/일/스페인어/베트남어)              |

인바운드 운영 실측 (2026-04-20 ~ 08-25 prod, 통화 70,654건 기준):

| 지표                | 수치                                            |
| ----------------- | --------------------------------------------- |
| AI 단독 완결 통화       | 5,056건 · 응대 시간 146.4시간 · 평균 104.3초             |
| 메모 접수             | 12,074건 성사 (시도 16,911건, 71.4%)                 |
| 예약 요청 처리 성공률      | 8.48% → 25.08% (2026-05 → 08 MTD, +16.6%p)     |
| 백엔드 귀인 실패율        | 8.54% → 0.34% (2026-05 → 08 MTD, −8.2%p)       |
| `UNSOUND_COMMIT`  | 18건 / 예약 시도 24,647건 = 0.073%                   |
| 확인 가능한 warm 연결    | 513건 / 2,899건 = 17.7%                          |
| 확인 불가 cold 전환     | 15,798건 (성사 집계에서 제외)                           |
| 활성 병원 · 활동 유지율    | 130곳 (2026-08 MTD) · 91.1% (2026-07 기준)        |

인바운드 Analytics v2 운영 스냅샷 (2026-08-13 ~ 08-26 prod, 분석 완료 통화 20,151건 기준):

| 지표 | 수치 |
| --- | --- |
| AI 단독 처리율 | 7.4% · 1,482 / 20,151건 (상담원 연결·메모 접수 없이 완료) |
| 예약 조회 요청 완료율 | 91.0% · 694 / 763건 |
| 예약 취소 요청 완료율 | 36.6% · 146 / 399건 |
| 예약 신청 요청 완료율 | 16.8% · 535 / 3,192건 |
| 예약 변경 요청 완료율 | 10.5% · 233 / 2,209건 |

업무별 완료율은 해당 업무의 시도 단위 결과이며 전체 통화 수치와 합산하지 않는다. 예약 신청의 완료는 신청 정보 기록을 뜻하며 EMR 최종 확정이 아니다. 예약 변경·취소 완료율도 요청 흐름의 완료를 뜻하며 실제 EMR 예약 상태 변경·취소 수치로 해석하지 않는다.

146.4시간은 AI가 수행한 응대 시간이며 절감된 인건비가 아니다. 수동 처리 시간과 후처리 데이터가 없어 절감분은 계산할 수 없다. 활성 고객 구성이 기간 중 크게 달라져 월별 변화를 제품 성능 변화로 귀속할 수 없다.




#### 사내 AIU 업무지원 Multi-Agent 및 AX 자동화 플랫폼 구축

2026.08 - 현재

AIU 제품과 운영 정보를 여러 사내 시스템에서 찾아야 하는 반복 업무를 줄이기 위해, OpenBot 기반의 사내 업무지원 AI Agent를 설계·구축했습니다. 2026.08 착수 후 3주 만에 지식 통합, 권한 경계, Web·Slack 런타임과 자동화 테스트를 갖춘 1차 운영 가능 상태로 만들었습니다.

- Web과 Slack에서 AIU 제품 사용법, 인바운드·아웃바운드 통화 운영, Agent Admin, HQ/SVC 업무를 질의할 수 있도록 기존 AIU Agent를 Bun·TypeScript 기반 Deep Agents 아키텍처로 마이그레이션했습니다.
- 최상위 Supervisor가 요청을 `inbound-agent`, `agent-admin-agent`, `outbound-agent`, `hq-svc-agent` 네 stateless 전문 Agent에 위임하도록 구성했습니다. Supervisor의 원본 source 접근은 차단하고 각 전문 Agent에 선언된 source path와 Tool만 허용해 제품·데이터 경계를 분리했습니다.
- 5개 source의 사용자 매뉴얼과 AI용 Playbook·Policy·State Model 322개를 Google Cloud OKF v0.2 번들로 통합했습니다. read-only virtual backend와 catalog가 source manifest, 실제 문서 수, frontmatter 접근 metadata와 screenshot 경로를 시작 시 검증하도록 구현했습니다.
- 현재 인증 경계는 OpenBot이 검증한 AIU Web·Slack run을 신뢰하는 단일 full-access 정책이며, 메시지 텍스트로 권한을 만들 수 없게 했습니다. 세밀한 사용자별 role/claim 집행은 아직 완성된 기능으로 주장하지 않고, Supervisor와 전문 Agent 사이의 source isolation을 실제 강제 경계로 유지했습니다.
- 인바운드·아웃바운드 저장 통화 검색과 운영 지표를 자연어로 조회하는 SELECT-only MySQL Tool을 구현했습니다. parameter binding, SSL 인증서 검증, 날짜·환경 enum과 hard limit을 적용하고 기본 결과에서 이름·전화번호·transcript·녹음·raw payload를 제외했습니다.
- 민감 통화 QA는 명시적으로 선택한 최대 5건·120 turn만 읽고 전화번호·이름·패턴형 식별자를 가렸습니다. transcript를 untrusted data로 표시하고 근거 turn index만 남겨 원문과 개인정보가 최종 답변에 재노출되지 않도록 제한했습니다.
- AG-UI를 통해 Web·Slack을 하나의 runtime으로 연결하고 하위 Agent의 내부 JSON·중첩 event를 숨긴 채 Supervisor 최종 답변만 노출했습니다. Surface-owned Tool은 OpenBot으로 돌려보내고 deployment Tool은 active run과 callback credential을 확인한 뒤 OpenBot이 실행하도록 권한을 유지했습니다.
- 매뉴얼 screenshot과 생성 이미지는 대화 상태 밖에 저장하고 HMAC 또는 난수 기반의 짧은 수명 URL로 전달했습니다. OpenBot의 Computer Use·plugin·감사·HITL 정책과 결합해 Agent가 임의의 외부 사이트나 변경 작업을 직접 소유하지 않게 했습니다.
- 지식 manifest·source 격리·AG-UI 최종 응답·SELECT-only DB·비식별 통화 검토·Tool ownership·서명 attachment를 검증하는 45개 AIU unit/contract test를 구성했습니다.

기술: TypeScript, Bun, Deep Agents, LangGraph, LangChain, AG-UI, OpenBot, OpenAI GPT-5.6 Luna, Gemini, MySQL, Zod, Slack, Docker, Google Cloud OKF v0.2, Markdown, YAML

#### 병원 아웃바운드 Voice AI Agent 설계 및 운영

2025 - 현재

병원의 예약 확인·안내 전화를 실제 전화망에서 자동 발신하고, 병원별 통화 목적·정책·예외를 설정으로 제어하며 통화 종료 후 분석까지 비동기로 처리하는 Voice AI 시스템을 설계·개발·운영했습니다.

- voxBridge가 Room·SIP 발신 수명주기를 소유하고 Agent가 `sip.callStatus=active`를 기다리도록 책임을 분리했습니다. Participant listener를 먼저 등록한 뒤 현재 상태를 다시 읽는 `subscribe-then-snapshot`, 계층화된 timeout과 단일 cleanup 소유권으로 중복 발신과 Room 정리 race를 방지했습니다.
- AMD 판정 전에는 무발화 `FakeAgent`, 사람 또는 불확실 판정 뒤에는 하나의 `SingleAgent`를 활성화했습니다. `condition`·`greeting`·`agent`·`action`·`exit` 노드로 구성한 `flow_config`와 통화 목적 계약으로 DTMF, 예약, 정보 안내, 상담원 연결과 종료를 코드 배포 없이 조합했습니다.
- AWS Streaming STT, OpenAI LLM과 Gemini fallback, Google Streaming TTS를 결합하고 preemptive LLM·TTS를 적용했습니다. STT 지연, Turn Detection, LLM TTFT, TTS TTFB, Playback과 E2E latency를 분리해 관측하며 속도와 Tool 제어·감사 가능성을 함께 관리했습니다.
- 신규 예약은 생년월일 DTMF 확인, 진료과 조회, 일정 선택과 확인을 `ScheduleSelectionTask`로 분리하고 진료과·의료진 변경 시 해당 단계로 되돌아가는 재선택을 최대 3회 허용했습니다. 선택 결과는 부분 갱신이 아니라 스냅샷 교체로 기록해 통화 종료 시점에 불완전한 신청 정보가 남지 않게 했습니다. 통화 중 EMR 예약을 즉시 확정하지 않고 완전한 예약 신청 정보를 기록한 뒤 병원 확인 전 상태임을 명확히 안내했으며, 변경·취소는 정책에 따라 상담원 연결 또는 메모 접수로 전달했습니다.
- 병원 FAQ는 통화 시작 시 기관별 활성 목록을 조회해 프롬프트에 주입하고, 등록된 답변 범위 밖에서는 추정하지 않도록 제한했습니다. 답변 매칭 결과를 구조화 이벤트로 기록해 정보 안내 성공 여부를 후처리에서 재현할 수 있게 했습니다.
- warm/cold transfer, 인바운드·아웃바운드 공용 Redis FIFO, trunk 점유권, AI 브리핑과 상담원 DTMF 수락, 대기 재확인·재시도·수신자 이탈·메모 fallback을 하나의 상태 모델로 관리하고 상태 변경을 Redis Stream으로 발행했습니다.
- 통화 transcript와 `extra.agent_event` 구조화 이벤트를 Kafka로 분석 Consumer에 전달했습니다. 상담원 연결 이후 녹음 구간을 Gemini로 보완 전사하고, 결정론적 이벤트 분류와 trustcall 기반 의미 분석·요약을 결합해 결과·이탈·전환 상태를 재구성했습니다.
- AMD 판별 중 시작된 발화가 Agent 전환 후 완료되며 설정 인사말 대신 LLM 응답을 생성하던 race condition을 메트릭 타임라인으로 추적했습니다. 생성이 금지된 `FakeAgent`와 `GreetingDtmfTask`에서 `StopResponse`를 강제하고 회귀 테스트를 추가해 결정적 인사말 경계를 보호했습니다.
- Tokyo ECS Fargate와 Korea Kubernetes 배포 경로, S3 녹음, Kafka 기반 후처리, 구조화 로그와 자동화 테스트를 운영해 실시간 통화와 분석 장애를 분리했습니다.

기술: Python, LiveKit Agents, LiveKit AMD, AWS Streaming STT, OpenAI GPT-5.4-mini, Gemini 2.5 Flash Lite, Google TTS, SIP, voxBridge, Kafka, Redis, AgentTask, trustcall, Gemini 2.5 Pro, GPT-5.6 Luna, AWS ECS Fargate, Kubernetes, S3, Docker

#### 병원 인바운드 Voice AI Agent 구축 및 운영

2025 - 현재

환자가 병원에 전화해 예약 조회·신청·변경·취소, 병원 정보 안내와 상담원 연결을 처리할 수 있는 Self-hosted LiveKit 기반 인바운드 Voice AI 시스템을 구축·운영하고 있습니다.

- `AgentServer` / `AgentSession` / `SingleAgent` 런타임과 `condition`·`greeting`·`agent`·`action`·`exit` 노드로 구성한 `flow_config`를 결합했습니다. 병원별 운영시간, DTMF·자유대화, 업무 진입, 연결과 종료 정책을 코드 배포 없이 설정으로 제어했습니다.
- 하나의 `SingleAgent`가 통화 Context를 유지하고 예약·DTMF·상담원 연결 업무를 한정된 `AgentTask`에 위임하도록 설계했습니다. `agent` 노드는 별도 Agent handoff가 아니라 요청 전달 또는 Tool 강제 호출 경계로 사용하고, Task의 typed result로 완료·이탈·상담원 요청의 제어권을 회수했습니다.
- AWS Streaming STT, GPT-5.4-mini와 Gemini fallback, Google Streaming TTS를 결합하고 preemptive LLM·TTS를 적용했습니다. STT 지연, Turn Detection, LLM TTFT, TTS TTFB, Playback과 E2E latency를 분리해 관측하고 결정적 안내·Tool 구간에는 별도 interruption guardrail을 적용했습니다.
- Dynamic Booking v3에서 환자 식별과 선택적 보험 확인, 병원별 진료과·의료진 기준정보, 실시간 일정 검색, 후보 스테이징과 명시적 동의를 분리했습니다. 검색 결과만으로 확인 질문을 만들거나 의료진을 임의 확정하지 못하게 하고, 동의 일시가 현재 스테이징과 다르면 Commit을 차단했습니다. Commit은 EMR 확정이 아니라 완전한 예약 신청 정보 기록으로 제한했습니다.
- 병원 정보는 통화 시작 시 client-scoped Call Context API에서 압축된 근거를 가져와 프롬프트에 주입했습니다. Context 조회 실패는 통화를 중단시키지 않고 지식 없는 상태로 폴백하며, 발화 매칭 결과를 `INFO_LOOKUP` 구조화 이벤트로 기록했습니다.
- 예약 작업별 `auto` / `transfer` / `leave_memo` 정책과 신규 예약의 의료진 선택·본인확인·진료과 표시 방식, 변경·취소의 당일 허용, 메모 수집 범위를 typed workflow 설정으로 분리했습니다.
- Self-hosted LiveKit 환경에 `SingleRoomWarmTransferTask`를 구현하고 인바운드·아웃바운드 공용 Redis FIFO, trunk 점유권, AI 브리핑, 상담원 DTMF 수락, 대기 재확인·재시도·수신자 이탈·메모 fallback을 상태 머신으로 관리했습니다. ZSET/HASH를 현재 상태의 기준으로, 비식별 Redis Stream을 구독 알림으로 사용했습니다.
- 단위 테스트, LiveKit text-only Agent 평가, 로컬 환자 시뮬레이션, 오디오·실제 전화망 검증으로 이어지는 4단계 테스트 체계를 구축했습니다. Dynamic Booking, 녹음 anchor, Warm Transfer queue·실시간 상태와 운영 장애를 회귀 테스트로 전환했습니다.
- LiveKit Worker의 통화별 프로세스 격리와 Kubernetes Pod OOM을 분석해 VAD·Turn Detector·idle prewarm·active job의 메모리 비용을 분리하고, Pod 수용량·graceful drain·동시 통화 확장 기준을 정리했습니다.

기술: Python, LiveKit Agents, Self-hosted LiveKit, SIP, AWS Streaming STT, OpenAI GPT-5.4-mini, Gemini 2.5 Flash Lite, Google TTS, DTMF, AgentTask, Kafka, Redis, MySQL, Pydantic, Kubernetes, S3, Docker, pytest

#### Voice AI 통화 분석 및 Privacy-safe LLM 평가 파이프라인

2026

실시간 통화와 분석 부하를 분리하면서도 한 통화의 업무 결과와 품질을 재구성할 수 있는 Kafka 기반 후처리·평가 파이프라인을 구축했습니다.

- 대화 transcript, 구조화 Agent event, 녹음과 단계별 latency metric을 Kafka로 전달하고, `room_name` 기준 멱등 처리와 재처리가 가능한 Consumer를 구현해 분석 장애가 실시간 통화에 영향을 주지 않도록 분리했습니다.
- 구조화된 developer event를 규칙으로 파싱해 예약 12개, 정보 문의 1개, 상담원 연결·메모 10개, 통화 종료 5개의 `InboundConversationMetadata` boolean 플래그로 분류했습니다. 한 통화에서 여러 활동 플래그가 동시에 참이 될 수 있으며, 이 상세 분류와 Analytics v2의 업무별 시도·통화당 대표 결과를 서로 다른 분석층으로 분리했습니다.
- 상담원 연결 이후의 녹음 구간을 잘라 전사를 보완하고, 원본 event를 업무별 시도와 통화별 최종 resolution으로 정규화하는 Analytics v2를 설계했습니다. 실패를 단계·유형·개선 주체로 분류해 운영 KPI에서 원인까지 추적할 수 있게 했습니다.
- 업무 완료는 결정론적 event로, 요청 의도와 응답 품질은 근거 turn을 포함한 Semantic 분석으로 평가했습니다. `task_completion`, `routing_correctness`, `response_quality`를 버전이 있는 Langfuse session score로 발행하도록 구현했습니다.
- 환자 transcript·임상 정보·식별 정보는 로컬 저장소에 유지하고 비민감 집계값만 Langfuse로 전송했습니다. 통화·점수·평가 버전 기반 idempotency key와 hard-cap 규칙으로 개인정보 경계와 재평가 일관성을 확보했습니다.

기술: Python, Kafka, PostgreSQL, LLM Evaluation, Langfuse, Pydantic, Object Storage

#### 병원 고객상담 AI Agent 아키텍처 및 제품 기반 구축

2025.03 - 2026.03

의료기관 고객 상담을 단순 FAQ 응답이 아니라 병원별 지식 조회, 개인정보 수집, 예약 안내와 상담원 연결 준비가 상태를 공유하는 LangGraph 제품으로 설계하고 주요 기능을 구현했습니다. 이후 팀이 Harness·Kakao 채널로 확장할 수 있는 초기 그래프와 서비스 경계를 구축했습니다.

- `primary_assistant`, `customer_interaction`, `extract_personal_info`, `tools`의 역할을 분리하고 `pending_question`, `collected_info`, `is_personal_info_saved`, `current_node`를 상태로 관리했습니다. 개인정보 수집이 끝난 뒤 원래 질문으로 복귀하게 해 절차 중에도 사용자가 같은 맥락을 반복하지 않도록 설계했습니다.
- 기관 소개·운영시간·방문 안내·의료진·진료·시술·증명서·이벤트를 병원별 Fact Data로 구조화하고, Qdrant Dense+Sparse Hybrid Search와 typed knowledge Tool로 연결했습니다. 의료 서비스 별칭·의료진·이미지 응답을 분리해 검색 결과를 채널 응답으로 변환했습니다.
- FastAPI gateway가 LangGraph SDK의 thread·run을 호출하고, Thread ID 재사용으로 대화 상태와 개인정보를 이어가도록 구현했습니다. Batch 요청은 Semaphore로 동시성을 제한하고 LangGraph API·PostgreSQL·Redis·FastAPI를 Docker로 묶어 독립 실행 가능한 서비스 경계를 만들었습니다.
- 웹·Voice·Kakao 등 채널별 응답 규칙과 다국어 메시지, 개인정보 동의 버튼, 예약 안내 경로를 설정으로 분리하고 상담 종료 시 대화 로그를 외부 API에 저장하도록 연결했습니다.
- 이후 팀이 추가한 `harness_agent`는 내가 설계한 기존 상담 노드와 상태를 team wrapper로 감싸고, `current_node`의 legacy 값을 유지한 채 허용 전이·도구 루프 감시·fast/full controller를 추가했습니다. 초기 상태 모델과 API 경계가 제품 확장을 수용한 구조적 근거를 확인했습니다.
- 2025년 5월 상용 출시 후 300개 이상 병원에서 운영 중입니다(2026.08 기준). GA4 퍼널(activeUsers) 기준 누적 상담 시작 사용자 7,464명 중 2,987명(40%)이 예약 또는 상담원 연결 단계로 진입했고, 812명(시작 대비 10.9%)이 예약 완료까지 도달했습니다. 챗봇 경유 예약은 전체 예약 21,343건의 약 4%(점유율 3.8%)입니다.

기술: Python, FastAPI, LangGraph, LangGraph SDK, LangChain, Qdrant Hybrid Search, FastEmbed, PostgreSQL, Redis, trustcall, LangSmith, Docker, AWS Elastic Beanstalk, ECR

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
