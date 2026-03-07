# Inbound Voice AI Agent 포트폴리오 설계

## 메타

- 작성일: 2026-03-07
- 타겟: 채용 담당자/면접관
- 형식: 마크다운 (한국어)
- 핵심: 아웃바운드 후속편으로서의 발전 스토리 + 설계 판단 깊이
- 관계: `case-studies/outbound-voice-agent.md`의 시리즈 후속편

## 설계 원칙

- 아웃바운드 포트폴리오에서 이미 설명한 내용(Multi-Agent 분리 동기, OpenAI Realtime API, Qdrant 벡터 검색)은 반복하지 않음
- 인바운드만의 기술적 도전과 의사결정에 집중
- 수치 성과 없이 설계 깊이로 승부
- 최종적으로 아웃바운드 문서와 하나로 합칠 수 있는 구조

## 핵심 강조점

1. **flow_config 노드 그래프 설계** — 병원마다 다른 콜 플로우를 코드 변경 없이 JSON 설정으로 동적 제어
2. **Warm/Cold Transfer 재시도 + 모니터링** — 상담원 연결의 실전 복잡성 처리

## 섹션 구조

### 1. 프로젝트 개요

- 한 줄 소개: 병원 인바운드 전화를 AI가 자동 응대하는 실시간 음성 AI 시스템
- 기간: 1달
- 아웃바운드와의 관계 (1-2줄)
- 전체 시스템 아키텍처 다이어그램
- 기술 스택 테이블

### 2. 프로젝트 배경

- 아웃바운드 → 인바운드 확장 동기
- 인바운드만의 도전 과제: 동적 콜 플로우, 상담원 연결 복잡성, 병원별 설정 분리

### 3. flow_config: 동적 콜 플로우 설계 (핵심)

- 문제: 병원마다 다른 전화 응대 시나리오
- SupervisorAgent + 노드 그래프 설계
- 5가지 노드 타입 (condition, greeting, agent, action, exit)
- DTMF 방식 vs 자유대화 방식 이중 지원
- 병원별 설정 분리 (BusinessData, AgentsConfig)
- 다이어그램 + 예시

### 4. 에이전트 계층과 행동 제어

- Multi-Agent 구조 (아웃바운드 대비 SupervisorAgent 추가)
- action_mode_handler 데코레이터: 도구별 auto/transfer/leave_memo 동적 분기
- Agent 간 handoff 규약 (user_request 전달)

### 5. 상담원 연결: Warm/Cold Transfer (핵심)

- Transfer 상태 흐름 다이어그램
- Warm Transfer 3회 재시도 + 상태별 분기 (TIMEOUT, ERROR, VOICEMAIL → 재시도 / DECLINED → 중단)
- 성공 시 양측 disconnect 모니터링
- Briefing Text 자동 생성
- Fallback: leave_memo 분기
- Cold Transfer vs Warm Transfer 판단 기준

### 6. 통화 분석 파이프라인

- 아웃바운드에서 배운 것: LLM + Hard Rules → 구조화된 로그를 정교하게 설계하면 LLM 분류 불필요
- Kafka 기반 비동기 파이프라인 흐름: 정규화 → 분류 → 전사 → Playback 계산 → 요약 → DB 저장
- 100% 규칙 기반 분류: developer 태그 파싱으로 24개 boolean 메타데이터 추출
- 상담원 대화 전사: Warm Transfer 성공 후 오디오 전사, consultant role 삽입
- Playback Segment: 메시지별 오디오 재생 구간 서버 계산

### 7. 기술적 의사결정 요약

- 주요 판단을 테이블로 정리 (문제 → 선택 → 결과)

## 아웃바운드 포트폴리오와의 역할 분담

| 주제 | 아웃바운드에서 상세 | 인바운드에서 상세 |
|------|-------------------|-----------------|
| Multi-Agent 분리 동기 | O (Before/After) | 가볍게 언급, SupervisorAgent 추가만 설명 |
| OpenAI Realtime API / 레이턴시 | O | 언급하지 않음 |
| Qdrant 벡터 검색 | O | 언급하지 않음 |
| flow_config 노드 그래프 | - | O (핵심) |
| action_mode_handler | - | O |
| Warm/Cold Transfer | 간단히 | O (핵심) |
| 통화 분석: LLM + Hard Rules | O | 발전 스토리로 언급 |
| 통화 분석: 규칙 기반 분류 | - | O |
| 통화 분석: 상담원 대화 전사 | - | O |
| ARS 감지 / 무응답 처리 | O | 언급하지 않음 |

## 참고 자료

- `case-studies/outbound-voice-agent.md`: 아웃바운드 포트폴리오 (시리즈 선행편)
- 인바운드 프로젝트 소스: README.md, docs/flow-config.md, docs/agent-tool-guide.md
- 인바운드 분석 파이프라인: conversation_analysis/README.md, conversation_analysis/docs/data-schema.md
