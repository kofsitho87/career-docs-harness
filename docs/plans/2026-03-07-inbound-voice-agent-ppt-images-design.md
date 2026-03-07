# Inbound Voice Agent PPT Images Design

## Meta

- Date: 2026-03-07
- Source: `case-studies/inbound-voice-agent.md`
- Target: PPT/portfolio slide images
- Output count: 2
- Theme: matched slide pair

## Goal

`case-studies/inbound-voice-agent.md`의 핵심 내용을 PPT에 바로 넣을 수 있는 16:9 슬라이드 이미지 2장으로 압축한다. 한 장은 시스템 전체를 요약하고, 다른 한 장은 인바운드 프로젝트의 핵심 설계 난제를 시각적으로 설명한다.

## Chosen Direction

동일한 비주얼 시스템을 공유하는 2장 세트로 구성한다.

- 공통 스타일: 화이트 또는 매우 밝은 배경, teal/blue 포인트 컬러, 엔터프라이즈 발표자료 톤
- 공통 목적: 채용 포트폴리오에 바로 삽입 가능한 고해상도 슬라이드
- 공통 제약: 과도한 장식, 포스터형 레이아웃, 다크 배경, 작은 글자, 보라 계열 그라디언트는 피한다

## Image 1: System Architecture Summary

- Title: `병원 인바운드 Voice AI Agent`
- Subtitle: `환자 전화를 AI가 자동 응대하고 예약·안내·상담원 연결을 설정 기반으로 처리하는 실시간 음성 AI 시스템`
- Main visual:
  - SIP 인바운드 연결
  - LiveKit Agent Server
  - SupervisorAgent
  - Booking Agent / Info Agent / Triage Coordinator
  - Booking API / Qdrant / Kafka / AWS S3
  - 통화 분석 파이프라인
- Supporting callouts:
  - 설정 기반 콜 플로우
  - DTMF + 자유대화 이중 지원
  - 비동기 통화 분석 파이프라인

## Image 2: Core Design Deep Dive

- Title: `flow_config + Warm Transfer`
- Subtitle: `병원별 콜 플로우를 코드 변경 없이 제어하고 상담원 연결 상태를 정교하게 관리한 핵심 설계`
- Left visual:
  - `condition`, `greeting`, `agent`, `action`, `exit` 노드 기반 `flow_config`
  - DTMF 메뉴와 자유대화 모드가 같은 프레임 안에서 표현되도록 구성
- Right visual:
  - 상담원 번호 확인
  - 승인/거부
  - Cold Transfer
  - Warm Transfer
  - 재시도, 실패 fallback, leave memo
- Supporting callouts:
  - 병원별 시나리오를 JSON 설정으로 제어
  - Warm/Cold Transfer 분기와 재시도
  - `action_mode_handler` 기반 동적 행동 제어

## Visual Recommendation

가독성과 포트폴리오 적합성을 우선해 실제 제품/기술 소개 슬라이드처럼 구성한다.

- Layout: 좌상단 제목, 중앙 대형 구조도, 우측 또는 하단 요약 블록
- Tone: 신뢰감 있는 B2B 의료 AI 인프라 발표자료
- Text density: 이미지 자체만 봐도 핵심을 읽을 수 있을 정도로만 제한
- Consistency: 두 이미지 모두 같은 제목 스타일, 카드 스타일, 선/박스 스타일 사용

## Acceptance Criteria

- 두 이미지가 한 세트처럼 보인다.
- 첫 이미지는 시스템 전체 구조를 5초 안에 이해할 수 있다.
- 두 번째 이미지는 왜 이 프로젝트가 기술적으로 어려웠는지 전달한다.
- 한국어 제목과 핵심 레이블이 포함된다.
- PPT 슬라이드에 바로 넣을 수 있는 16:9 비율이다.
