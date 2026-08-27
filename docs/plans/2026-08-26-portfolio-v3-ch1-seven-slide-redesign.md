# 포트폴리오 v3 챕터 1 · 7장 재설계 작업 기록

## 메타

- 작성일: 2026-08-26
- 대상 산출물: `portfolio/heewung-song-portfolio-v3.html`
- 대상 범위: CH 01 병원 전화 Voice AI
- 목적: 기존 9장을 7장으로 재구성하고, 각 장의 내용 합의·구현·검증 상태를 한 문서에서 추적한다.
- 선행 설계: `docs/plans/2026-08-25-portfolio-v3-structure-design.md`
- 사실 기준: `resume/product-engineer.md`

## 작업 상태 정의

각 장은 아래 네 단계를 모두 만족해야 완료로 본다.

1. **내용 확정**: 헤드라인, 핵심 메시지, 포함·제외 범위를 사용자와 합의했다.
2. **구현**: 대상 HTML과 필요한 CSS를 수정했다.
3. **정적 검증**: `git diff --check`, JavaScript parse, 필수 문구와 HTML 구조 검사를 통과했다.
4. **화면 확인**: 실제 브라우저에서 16:9 화면을 확인하고 필요 시 사용자 피드백을 반영했다.

## 확정된 편집 원칙

- CH 01은 아래 7개 헤드라인을 그대로 사용한다.
- 별도의 `문제와 해결 방식` 장은 두지 않는다. 프로젝트 문제와 자동화 범위는 1장과 4장에 분산한다.
- 6개 언어 지원은 이번 CH 01의 핵심 메시지와 성과 카드에서 제외한다.
- 회사 홈페이지 이미지는 아웃바운드 중심이고 마케팅 범위가 넓으므로 1장 본문에 직접 사용하지 않는다.
- 2장과 3장은 `전체 시스템 → LiveKit 영역 확대`의 연속된 줌 구조로 만든다.
- LiveKit Server/SFU와 LiveKit Agents/Agent job은 같은 프로세스처럼 표현하지 않는다.
- 참조 아키텍처의 권장 topology를 실제 운영 구현으로 주장하지 않는다.
- 예약 Commit은 EMR 최종 확정이 아니라 예약 신청 기록이라는 경계를 유지한다.
- 인바운드 Dynamic Booking v3와 아웃바운드 레거시 예약 경로의 성숙도 차이를 명시한다.
- 통화 관측과 품질 평가는 CH 02에서 전담한다. CH 01의 6장은 인·아웃바운드가 공유하는 상담원 연결 대기줄을 비기술적인 언어로 설명한다.

## 최종 7장 구성과 진행 상태

| 장 | 헤드라인 | 대상 섹션 | 내용 확정 | 구현 | 정적 검증 | 화면 확인 |
|---:|---|---|:---:|:---:|:---:|:---:|
| 1 | 인/아웃바운드 Voice Call Agent | `ch1-what` | [x] | [x] | [x] | [x] |
| 2 | 전체 시스템 아키텍처 | `ch1-scale` | [x] | [x] | [x] | [x] |
| 3 | LiveKit 기반 실시간 음성 처리 | `ch1-arch` | [x] | [x] | [x] | [x] |
| 4 | 안전한 Tool Calling 기반 예약 처리 | `ch1-booking` | [x] | [x] | [x] | [x] |
| 5 | Warm Transfer 기반 상담 연속성 | `ch1-modes` | [x] | [x] | [x] | [x] |
| 6 | 상담원 연결 요청을 순서대로 처리합니다 | `ch1-queue` | [x] | [x] | [x] | [x] |
| 7 | 성과와 배운 점 | `ch1-result` | [x] | [x] | [x] | [x] |

상태 해석:

- 1~7장은 사용자 화면 확인까지 완료했다.

## 장별 완료 체크리스트

### 1장 · 인/아웃바운드 Voice Call Agent

- [x] 프로젝트를 인바운드와 아웃바운드의 두 방향으로 정의
- [x] 아웃바운드: 예약 확인·안내 전화 자동 발신
- [x] 인바운드: 예약 신청·조회, 병원 안내, 상담원 연결·메모 접수
- [x] 기간·역할·담당 범위 표시
- [x] 6개 언어와 성과 수치 제거
- [x] 회사 홈페이지 이미지 대신 CSS 기반 양방향 도식 사용
- [x] 사용자 화면 확인 완료

### 2장 · 전체 시스템 아키텍처

- [x] Telephony → LiveKit Platform → AI·업무 시스템의 전체 경계 표현
- [x] LiveKit SIP, Server/SFU, AgentServer/Per-call Job을 하나의 확대 대상 그룹으로 표시
- [x] Egress/S3, OpenTelemetry/Langfuse, Kafka/Analysis 경로 분리
- [x] Kafka를 실시간 통화와 분석의 장애 격리 경계로 표시
- [x] 다음 장의 LiveKit 확대와 연결
- [x] 사용자 화면 확인 완료

### 3장 · LiveKit 기반 실시간 음성 처리

- [x] LiveKit Transport와 Agent Compute 분리
- [x] PSTN → SIP → Server/SFU 흐름 표현
- [x] Room, Caller·AI Agent·Consultant·Egress와 Track 구조 표현
- [x] AgentServer → Per-call Job → AgentSession 실행 모델 표현
- [x] VAD/Turn → STT → LLM·Tool → TTS pipeline 표현
- [x] 발화 중단 처리와 Egress 녹음 경계 표시
- [x] 사용자 화면 확인 완료

### 4장 · 안전한 Tool Calling 기반 예약 처리

- [x] Tool 실행 전 `action_mode_handler` 정책 분기 합의
- [x] `auto / transfer / leave_memo` 세 경로 합의
- [x] 인바운드 `Search → Stage → Confirm → Commit` 확대 구성 합의
- [x] 모델이 아닌 코드가 확인 문구를 생성하는 경계 합의
- [x] `UNSOUND_COMMIT` 탐지와 대표 장애 사례 포함 합의
- [x] 아웃바운드 레거시 경로의 성숙도 차이 표시 합의
- [x] HTML·CSS 구현
- [x] 정적 검증
- [x] 사용자 화면 확인 완료

### 5장 · Warm Transfer 기반 상담 연속성

- [x] AI 상담에서 인간 상담원 연결이 필요한 당위성 표현
- [x] 병원 정책·자동화 경계·상담 맥락 유지의 세 이유 표현
- [x] 인·아웃바운드 → AI 1차 상담 → 인간 상담원 연결 흐름 표현
- [x] 연결 대상 없음·Warm 연결 실패 → Leave Memo → 병원 후속 연락 표현
- [x] Cold Transfer와 Warm Transfer 비교 카드 구성
- [x] LiveKit 공식 Warm Transfer의 사용자 경험 5단계 참고
- [x] 공식 private consultation room 예제와 custom `SingleRoomWarmTransferTask`의 구현 차이 명시
- [x] 실제 Agent Admin Warm Transfer 성공 화면을 구현 증거로 선택
- [x] `STARTED → QUEUED → DTMF 수락 → SUCCESS → AI 브리핑` 구간만 캡처
- [x] 환자명·상담원 번호를 불투명 마스킹하고 원본 임시 파일 삭제
- [x] OCR로 원래 환자명·전화번호가 남지 않았는지 확인
- [x] HTML·CSS 구현
- [x] 정적 검증
- [x] 사용자 화면 확인

### 6장 · 상담원 연결 요청을 순서대로 처리합니다

- [x] 인·아웃바운드 요청이 병원별 하나의 대기줄을 공유하는 개념 표현
- [x] 먼저 온 통화부터 상담원에게 연결하는 흐름 표현
- [x] 재시도해도 원래 순서를 유지하는 규칙 표현
- [x] 환자가 통화를 종료하면 대기줄에서 제거하는 흐름 표현
- [x] 한 상담원 회선에 여러 통화를 동시에 연결하지 않는 원칙 표현
- [x] 연결 성공·장기 대기·Leave Memo fallback의 세 결과 표현
- [x] ZSET·HASH·Stream·Redis key·TTL 등 저장 구현 상세 제거
- [x] HTML·CSS 구현
- [x] 정적 검증
- [x] 사용자 화면 확인

### 7장 · 성과와 배운 점

- [x] 양방향 운영 규모 `620,000+`, `4,000건/일`, `300개+` 표시
- [x] Analytics v2 고정 기간 `2026-08-13~26 PROD` 범위 표시
- [x] AI 단독 처리율 7.4% 표시
- [x] 예약 조회·취소·신청·변경 요청 완료율 표시
- [x] 업무별 수치는 시도 단위이며 전체 통화와 합산하지 않는 경계 표시
- [x] 예약 신청·변경·취소 지표가 EMR 최종 상태를 뜻하지 않는 경계 표시
- [x] 포트폴리오 화면에서는 퍼센트만 남기고 분자·분모 상세 건수 제거
- [x] `귀인 실패율` 등 어려운 분석 용어 제거
- [x] 배운 점을 쉬운 문장 세 개로 재작성
- [x] HTML·CSS 구현
- [x] 정적 검증
- [x] 사용자 화면 확인

## 기존 9장과 새 7장의 매핑

| 기존 섹션 | 처리 계획 | 새 장 |
|---|---|---:|
| `ch1-what` | 전면 수정 완료 | 1 |
| `ch1-scale` | 전체 시스템 아키텍처로 전면 수정 완료 | 2 |
| `ch1-arch` | LiveKit 확대 구조로 전면 수정 완료 | 3 |
| `ch1-start` | 핵심 내용을 2·3장에 통합하고 삭제 완료 | - |
| `ch1-booking` | 정책 분기와 안전한 예약 처리로 전면 수정 | 4 |
| `ch1-routing` | 정책 분기를 4·5장에 통합하고 삭제 완료 | - |
| `ch1-modes` | Warm Transfer 중심으로 전면 수정 | 5 |
| `ch1-queue` | 인·아웃바운드 공용 상담원 대기줄의 개념 설명으로 전면 수정 | 6 |
| `ch1-result` | 운영 규모·현재 처리 결과·쉬운 표현의 배운 점으로 전면 수정 | 7 |

## 전체 완료 전 정리 체크리스트

- [x] `ch1-start` 삭제
- [x] `ch1-routing` 삭제 후 CH 01이 정확히 7장인지 확인
- [x] 챕터 지도에서 CH 01 장수를 7장으로 수정
- [x] 전체 덱 장수와 이전 `showSlide()` 인덱스 수정
- [ ] 내비게이션·키보드·터치·프린트 동작 확인
- [ ] 다크·라이트 테마 확인
- [ ] 1920×1080, 일반 노트북, 모바일 세로 화면 확인
- [x] 사실 기준 문서에 Analytics v2 고정 기간 지표 추가
- [x] `README.md`, `docs/workflow.md`, 선행 구조 설계 문서의 장수와 구조 갱신
- [ ] PDF를 다시 생성하고 16:9 페이지·링크·잘림 확인

## 근거 자료

- `resume/product-engineer.md`
- `case-studies/outbound-voice-agent.md`
- `case-studies/inbound-voice-agent.md`
- `docs/plans/2026-03-07-outbound-voice-agent-portfolio-design.md`
- `docs/plans/2026-03-07-inbound-voice-agent-portfolio-design.md`
- `docs/plans/2026-08-25-portfolio-v3-structure-design.md`
- `/Users/heewungsong/Desktop/Wise-Ai/Outbound-Agent-Project/inbound-agent/docs/livekit-technology-stack-and-infrastructure.md`
- `/Users/heewungsong/Desktop/Wise-Ai/Outbound-Agent-Project/inbound-agent/openwiki/inbound/transfers.md`
- `assets/agent-admin-warm-transfer-evidence.png`
- `https://ai.wiseai.co.kr/platform/aiu`
- `https://ai.wiseai.co.kr/event/target-event/6-1`
- `https://docs.livekit.io/telephony/features/transfers/cold/`
- `https://docs.livekit.io/telephony/features/transfers/warm/`

## 작업 로그

### 2026-08-26 · 1차

- 1장 `ch1-what`을 인·아웃바운드 양방향 프로젝트 소개로 전면 수정했다.
- 2장 `ch1-scale`을 전체 시스템 아키텍처로 전면 수정했다.
- 3장 `ch1-arch`를 LiveKit Transport와 Agent Compute 확대 구조로 전면 수정했다.
- 4장 `ch1-booking`에 action mode 정책 gate와 인바운드 Dynamic Booking v3의 `Search → Stage → Confirm → Commit`을 결합했다.
- 4장에 세 가지 실제 실패 사례, `UNSOUND_COMMIT`, EMR 확정 경계와 아웃바운드 성숙도 차이를 반영했다.
- 사용자가 1~4장 화면을 확인했다.
- 기존 `ch1-start` 슬라이드를 삭제하고, 현재 8장 기준으로 챕터 지도 장수와 CH 02~04 이동 인덱스를 조정했다.
- 5장 `ch1-modes`를 상담원 연결의 당위성, 인·아웃바운드 공통 흐름, Leave Memo 보완 경로, Cold/Warm 비교 중심으로 전면 수정했다.
- Agent Admin의 실제 Warm Transfer 성공 구간을 캡처해 환자명·전화번호를 불투명 마스킹하고 5장에 구현 증거로 삽입했다.
- 비식별 이미지에 OCR 검사를 실행해 원래 환자명과 전화번호가 검출되지 않음을 확인하고, 민감정보가 담긴 임시 원본 파일은 삭제했다.
- 6장 `ch1-queue`에서 ZSET·HASH·Stream과 Redis 내부 구조를 제거하고, 동시 요청이 하나의 대기줄에서 순서대로 상담원에게 연결되는 개념 도식으로 교체했다.
- 6장의 역할을 통화 분석 루프에서 공용 상담원 대기줄 설명으로 변경하고, 통화 분석은 CH 02에서 전담하도록 구조를 정리했다.
- Analytics v2의 2026-08-13~26 PROD 스냅샷을 사실 기준 이력서에 먼저 추가했다.
- 7장 `ch1-result`에서 백엔드 귀인 실패율과 기술 중심 검증 목록을 제거하고, AI 단독 처리율과 예약 업무별 요청 완료율을 쉬운 표현으로 반영했다.
- 배운 점을 `AI는 대화하고, 중요한 결정은 코드가 확인합니다`, `AI가 해결하지 못해도 환자 요청은 남아야 합니다`, `통화를 단계별로 기록해 막힌 곳부터 고쳤습니다`로 확정했다.
- 사용자 확인 후 7장의 AI 단독 처리율과 업무별 완료율 카드에서 분자·분모 상세 건수를 제거하고 퍼센트만 남겼다. 상세 건수는 사실 기준 이력서에 검증 근거로 유지했다.
- 기존 `ch1-routing`을 삭제해 CH 01을 정확히 7장으로 줄였다.
- CH 01 완료 시점에는 전체 덱이 24장이었고 CH 02·03·04 시작 인덱스는 11·16·19였다. 이후 CH 02가 8장, CH 03이 5장으로 확장된 현재 전체 덱은 29장, 시작 인덱스는 11·19·24다.
- JavaScript parse, 필수 문구 검사, `section`·`article`·`div` 구조 균형, `git diff --check`를 통과했다.
