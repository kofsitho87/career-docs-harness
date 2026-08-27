# AIU 업무지원 Agent 포트폴리오 확장 설계

**작성일:** 2026-08-24
**대상:** `portfolio/html/heewung-song-portfolio-v1.html` Chapter 05

## 문제 정의

현재 Chapter 05는 프로젝트 개요, Multi-Agent/지식 계약, 거버넌스의 3장으로만 구성돼 있다. 실제 `OpenBot/agent-aiu` 구현에는 AG-UI surface 경계, 전문 Agent source 격리, 다섯 지식 source, SELECT-only 통화 분석, 비식별 통화 검토, OpenBot Tool ownership과 signed attachment 같은 독립적인 설계 증거가 있으나 포트폴리오에서 거의 보이지 않는다.

## 중심 메시지

> 흩어진 운영 지식을 답하는 Agent가 아니라, 근거·데이터·실행 권한을 분리한 사내 업무 런타임을 만들었다.

## 사실 기준

- Bun/TypeScript + Deep Agents 기반 AIU Supervisor
- 4개 stateless specialist: inbound, outbound, Agent Admin, HQ/SVC
- 5개 OKF source, Markdown 문서 322개
- AIU 전용 unit/contract test 45개
- Web·Slack 공통 AG-UI runtime
- SELECT-only MySQL 검색·집계와 최대 5건의 비식별 통화 QA
- OpenBot이 Computer Use·plugin·HITL·감사와 실행 권한을 소유
- 현재 verified AIU caller는 동일 full-access identity를 사용한다. 세밀한 사용자별 role/claim 권한 집행은 완료된 기능으로 표현하지 않는다.

## 슬라이드 구성

1. Chapter 개요 — 문제, 기간, 5→1, 322문서, 4 specialist, 45 test
2. 업무 언어로 묻는 네 가지 질문 — inbound/outbound/Admin/HQ·SVC 도메인
3. Supervisor와 AG-UI 경계 — source를 읽지 않는 Supervisor, 최종 답변만 surface에 노출
4. 지식 계약 — 5개 source별 문서 수, manifest/frontmatter/screenshot 검증, read-only backend
5. SELECT-only 운영 분석 — parameter binding, SSL, hard limit, PII 비노출, 최대 5건 QA
6. OpenBot 실행·첨부·정직한 범위 — Tool ownership, run assertion, signed assets, 45 tests, 미측정 성과와 현재 access 범위

## 시각 방향

기존 `운영 시스템 블루프린트` 톤을 유지한다. 각 슬라이드는 하나의 계약을 보여주는 구조로 만들고, 기능 목록보다 `요청 → 위임 → 근거 → 안전한 실행/전달`의 경계를 시각화한다.

## 완료 기준

- AIU가 Chapter 말미의 짧은 부록이 아니라 독립적인 AX 대표 사례로 읽힌다.
- 코드로 강제되는 경계와 문서상 정책을 혼동하지 않는다.
- 기존 3장을 6장으로 확장하되 각 장이 중복 없이 하나의 질문에 답한다.
- 데스크톱·모바일·다크/라이트 테마에서 오버플로 없이 표시된다.
