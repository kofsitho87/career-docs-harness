# Inbound Voice AI Agent 포트폴리오 설계

## 메타

- 작성일: 2026-03-07
- 타겟: 채용 담당자/면접관
- 형식: 마크다운 (한국어)
- 핵심: 아웃바운드 후속편으로서의 발전 스토리 + 설계 판단 깊이
- 관계: `case-studies/outbound-voice-agent.md`의 시리즈 후속편

## 설계 원칙

- 아웃바운드 포트폴리오에서 이미 설명한 호출 수명주기와 공통 Voice pipeline은 반복하지 않음
- 인바운드만의 기술적 도전과 의사결정에 집중
- 수치 성과 없이 설계 깊이로 승부
- 최종적으로 아웃바운드 문서와 하나로 합칠 수 있는 구조

## 핵심 강조점

1. **SingleAgent + flow_config** — 하나의 Context 안에서 병원마다 다른 콜 플로우를 설정으로 제어
2. **Dynamic Booking v3** — 기준정보·검색·스테이징·명시적 동의·신청 접수 경계
3. **공용 Redis FIFO Warm Transfer** — 상담 자원 점유와 실시간 상태·실패 복구

## 섹션 구조

### 1. 프로젝트 개요

- 한 줄 소개: 병원 인바운드 전화를 AI가 자동 응대하는 실시간 음성 AI 시스템
- 기간: 2025 - 현재
- 아웃바운드와의 관계 (1-2줄)
- 전체 시스템 아키텍처 다이어그램
- 기술 스택 테이블

### 2. 프로젝트 배경

- 아웃바운드 → 인바운드 확장 동기
- 인바운드만의 도전 과제: 동적 콜 플로우, 상담원 연결 복잡성, 병원별 설정 분리

### 3. SingleAgent와 설정 기반 Call Flow

- 문제: 병원마다 다른 전화 응대 시나리오
- SingleAgent + 노드 그래프 설계
- 5가지 노드 타입 (condition, greeting, agent, action, exit)
- DTMF 방식 vs 자유대화 방식 이중 지원
- `agent` 노드는 별도 Agent handoff가 아니라 요청 전달·Tool 진입 경계
- 병원별 설정 분리 (BusinessData, AgentsConfig, WorkflowConfig)
- client-scoped Call Context API를 시작 시 주입하고 no-knowledge fallback
- 다이어그램 + 예시

### 4. Dynamic Booking v3와 행동 제어

- 환자 식별·선택적 보험 확인·진료과/의료진 기준정보 로드
- 실시간 일정 검색 → 정확한 후보 스테이징 → 정형 확인 질문 → 명시적 동의
- 검색 결과만으로 Commit 금지, 동의 일시와 staging mismatch 차단
- EMR 즉시 확정이 아닌 예약 신청 정보 기록
- `action_mode_handler`: 예약 작업별 auto/transfer/leave_memo 분기

### 5. 상담원 연결: 공용 Redis FIFO Warm Transfer

- Transfer 상태 흐름 다이어그램
- 인바운드·아웃바운드 공용 병원별 FIFO와 trunk occupancy lock
- ZSET/HASH current snapshot + 비식별 Redis Stream notification
- queued/waiting_for_trunk/dialing/briefing/connected/retrying 상태
- AI briefing + 상담원 DTMF 수락, 120/240/360초 대기 재확인
- TIMEOUT/ERROR/VOICEMAIL 재시도, DECLINED 중단, leave_memo fallback
- 성공 시 양측 disconnect와 점유 종료 모니터링
- Cold Transfer vs Warm Transfer 판단 기준

### 6. 테스트와 운영 복구

- 단위 테스트 → LiveKit text eval → 환자 시뮬레이션 → 오디오·전화망의 4단계 검증
- Dynamic Booking entry/earliest-offer 회귀 테스트
- Egress recording anchor와 조기 종료 race 테스트
- Redis queue·실시간 상태·subscriber 테스트
- Worker process 격리, OOM 메모리 산정, prewarm·Pod 수용량 기준

통화 분석은 별도 Chapter 04에서 Analytics v2·Semantic·Langfuse 구조로 다룬다.

### 7. 기술적 의사결정 요약

- 주요 판단을 테이블로 정리 (문제 → 선택 → 결과)

## 아웃바운드 포트폴리오와의 역할 분담

| 주제 | 아웃바운드에서 상세 | 인바운드에서 상세 |
|------|-------------------|-----------------|
| 호출 수명주기 소유권 | O | SIP 수신 이후 runtime만 설명 |
| 단계형 Voice pipeline / 레이턴시 | O | 설정값과 interruption 차이만 설명 |
| 병원 정보 Grounding | FAQ 주입 | Call Context 주입과 no-knowledge fallback |
| flow_config 노드 그래프 | - | O (핵심) |
| action_mode_handler | - | O |
| 안전한 예약 신청 | 접수 흐름 | Dynamic Booking v3 상세 |
| Warm/Cold Transfer | 공용 FIFO 개요 | 상태·점유·실패 복구 상세 |
| 통화 분석 | Kafka 분리 개요 | Chapter 04로 이동 |

## 참고 자료

- `case-studies/outbound-voice-agent.md`: 아웃바운드 포트폴리오 (시리즈 선행편)
- 인바운드 프로젝트 소스: README.md, docs/flow-config.md, docs/agent-tool-guide.md
- 인바운드 분석 파이프라인: conversation_analysis/README.md, conversation_analysis/docs/data-schema.md
