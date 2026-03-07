# Hospital Customer Support Agent Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** `agent-service-guide.md`와 인터뷰 내용을 바탕으로 신규 케이스 스터디 `case-studies/hospital-customer-support-agent.md`를 작성한다.

**Architecture:** 먼저 기존 사실 기준 문서와 참고 가이드를 다시 대조해 문서에 들어갈 확정 사실만 추린다. 그다음 설계 문서에서 승인된 구조대로 섹션 초안을 순서대로 작성하고, 마지막에 사실 일관성, 톤, 링크, 파일명 정합성을 점검한다.

**Tech Stack:** Markdown, local repository docs, existing case study structure

---

### Task 1: 근거 문서 재확인 및 문서 골격 고정

**Files:**
- Read: `resume/product-engineer.md`
- Read: `docs/guides/resume-guide.md`
- Read: `docs/plans/2026-03-07-hospital-customer-support-agent-design.md`
- Read: `/Users/heewungsong/Desktop/Wise-Ai/langgraph-customer-support-agent/langgraph_app/data/docs/agent-service-guide.md`
- Create: `case-studies/hospital-customer-support-agent.md`

**Step 1: 사실 근거를 다시 확인한다**

Run: `sed -n '1,220p' resume/product-engineer.md`
Expected: 와이즈에이아이의 `병원 고객상담 AI Agent 시스템 설계 및 배포` 항목이 보인다.

**Step 2: 작성 원칙을 다시 확인한다**

Run: `sed -n '1,220p' docs/guides/resume-guide.md`
Expected: 성과 과장 금지, 구조 중심 서술, 명확한 동사 사용 원칙이 보인다.

**Step 3: 설계 문서에서 승인된 섹션 구조를 확인한다**

Run: `sed -n '1,240p' docs/plans/2026-03-07-hospital-customer-support-agent-design.md`
Expected: `프로젝트 개요`, `문제 정의`, `핵심 설계 의사결정`, `시스템 동작 방식`, `내가 기여한 부분`, `회고` 구조가 확인된다.

**Step 4: 새 문서의 헤더와 섹션 골격을 만든다**

```md
# Hospital Customer Support Agent

> 병원 고객 문의를 구조적으로 처리하기 위해 상담 흐름, 지식 조회, 운영 구조를 함께 설계한 AI 상담 시스템

---

## 프로젝트 개요

## 문제 정의

## 핵심 설계 의사결정

## 시스템 동작 방식

## 내가 기여한 부분

## 회고
```

**Step 5: 골격만 작성된 파일을 확인한다**

Run: `sed -n '1,120p' case-studies/hospital-customer-support-agent.md`
Expected: 제목, 한 줄 요약, 6개 상위 섹션만 있는 초안이 보인다.

### Task 2: 프로젝트 개요와 문제 정의 초안 작성

**Files:**
- Modify: `case-studies/hospital-customer-support-agent.md`
- Read: `/Users/heewungsong/Desktop/Wise-Ai/langgraph-customer-support-agent/langgraph_app/data/docs/agent-service-guide.md`

**Step 1: 프로젝트 개요 문단과 메타 테이블을 작성한다**

```md
## 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 역할 | 핵심 아키텍트 + 일부 구현 |
| 기간 | 2025.03 - 2025.05 |
| 소속 | 와이즈에이아이 |

이 프로젝트는 병원·클리닉 고객 문의를 자동으로 응대하는 AI 상담 에이전트 시스템이다. 핵심은 단순 FAQ 응답기가 아니라 병원별 지식 조회, 개인정보 수집, 상담 흐름 전환을 하나의 대화 맥락 안에서 처리할 수 있는 구조를 설계한 점이다.
```

**Step 2: 문제 정의 섹션을 작성한다**

```md
## 문제 정의

- 병원 문의는 기관별 정보 차이와 절차 차이 때문에 공통 답변 템플릿만으로 처리하기 어렵다.
- 상담 도중 개인정보 수집이 필요해도 사용자의 원래 질문 흐름은 유지되어야 한다.
- 실제 운영 가능한 상담 시스템이 되려면 답변 생성만이 아니라 지식 데이터, 도구 실행, 배포 구조가 함께 설계되어야 했다.
```

**Step 3: 표현 과장이 없는지 점검한다**

Run: `rg -n "정확도|가용성|향상|개선" case-studies/hospital-customer-support-agent.md`
Expected: 근거 없는 정량 성과 표현이 없거나, 있더라도 이력서 근거와 일치한다.

### Task 3: 핵심 설계 의사결정 섹션 작성

**Files:**
- Modify: `case-studies/hospital-customer-support-agent.md`
- Read: `/Users/heewungsong/Desktop/Wise-Ai/langgraph-customer-support-agent/langgraph_app/data/docs/agent-service-guide.md`

**Step 1: 상담 흐름 분리 설계를 작성한다**

```md
### 1. 상담 흐름을 역할별 상태 전이로 분리

- 일반 문의, 개인정보 수집, 도구 실행을 하나의 응답 흐름에 섞지 않고 역할별로 나눴다.
- `primary_assistant`, `customer_interaction`, `extract_personal_info`, `tools`로 흐름을 구분해 복잡한 상담에서도 상태 제어가 가능하도록 만들었다.
- 이 구조 덕분에 개인정보 수집이 필요해도 대화 맥락을 잃지 않고 다음 단계로 복귀할 수 있었다.
```

**Step 2: 병원별 지식 조회 설계를 작성한다**

```md
### 2. 병원별 지식 조회를 데이터 기반 응답 구조로 설계

- 기관 소개, 운영 시간, 방문 안내, 의료진, 진료·시술, 증명서, 이벤트 정보는 병원마다 달랐다.
- 공통 프롬프트만으로는 운영 가능한 품질을 만들기 어렵다고 판단해 병원별 지식 데이터를 조회하는 구조를 중심에 두었다.
- 이 프로젝트의 본질은 FAQ 챗봇이 아니라 병원별 데이터에 따라 응답이 달라지는 상담 시스템이었다.
```

**Step 3: 운영 가능한 서비스 경계 설계를 작성한다**

```md
### 3. 운영 가능한 서비스 경계를 함께 설계

- 상담 엔진만 구현해서는 서비스가 완성되지 않기 때문에 API 서버, 검색 시스템, 운영 대시보드, 배포 구조를 함께 설계했다.
- LangGraph 기반 상담 엔진과 지식 수집/검색, 운영 API, 모니터링 대시보드, AWS ECS Fargate 배포를 하나의 제품 구조로 연결했다.
- 이를 통해 실험용 데모가 아니라 실제 운영 가능한 상담 서비스 기반을 만들 수 있었다.
```

**Step 4: 섹션 흐름을 확인한다**

Run: `sed -n '1,220p' case-studies/hospital-customer-support-agent.md`
Expected: 세 가지 설계 의사결정이 `왜 필요했는가 -> 어떻게 설계했는가 -> 무엇이 가능해졌는가` 흐름으로 읽힌다.

### Task 4: 시스템 동작 방식과 기여 범위 작성

**Files:**
- Modify: `case-studies/hospital-customer-support-agent.md`
- Read: `/Users/heewungsong/Desktop/Wise-Ai/langgraph-customer-support-agent/langgraph_app/data/docs/agent-service-guide.md`

**Step 1: 대표 시나리오 3개를 작성한다**

```md
## 시스템 동작 방식

### 일반 문의 처리

1. 사용자의 질문을 받는다.
2. 일반 상담 흐름에서 답변 가능 여부를 판단한다.
3. 필요하면 병원별 지식 조회를 수행한다.
4. 조회 결과를 바탕으로 답변을 구성한다.

### 개인정보 수집 후 상담 복귀

1. 상담 진행에 필요한 개인정보가 부족한지 판단한다.
2. 이름, 휴대전화번호, 생년월일을 수집하고 정규화한다.
3. 저장이 끝나면 보관해 둔 원래 질문으로 돌아간다.

### 상담원 연결 준비

1. 사용자가 연결을 원하면 현재 수집 정보와 외부 사용자 상태를 함께 확인한다.
2. 필요한 정보가 충분하면 다음 연결 단계로 넘긴다.
3. 부족하면 다시 필요한 정보를 안내한다.
```

**Step 2: 기여 범위 섹션을 작성한다**

```md
## 내가 기여한 부분

- 전체 상담 아키텍처와 상태 전이 구조를 설계했다.
- 병원별 지식 조회와 개인정보 수집/복귀 흐름의 핵심 설계를 주도했다.
- 서비스가 운영 가능한 형태가 되도록 API, 검색, 대시보드, 배포 구조의 큰 경계를 설계했다.
- 일부 핵심 구간은 직접 구현해 설계가 실제 동작으로 이어지도록 만들었다.
```

**Step 3: 회고 섹션 초안을 작성한다**

```md
## 회고

이 프로젝트를 통해 상담형 AI 제품은 답변 생성 능력만으로 완성되지 않는다는 점을 분명히 배웠다. 상태 관리, 병원별 데이터 품질, 개인정보 수집 절차, 운영 구조가 함께 맞물려야 실제 서비스가 된다. 이 경험은 복잡한 도메인 문제를 제품 구조와 시스템 구조로 동시에 풀어내는 역량을 보여준다.
```

### Task 5: 사실 일관성과 문서 품질 검증

**Files:**
- Review: `case-studies/hospital-customer-support-agent.md`
- Read: `resume/product-engineer.md`
- Read: `case-studies/outbound-voice-agent.md`

**Step 1: 이력서와 사실이 충돌하지 않는지 확인한다**

Run: `rg -n "2025.03|와이즈에이아이|LangGraph|Qdrant|FastAPI|ECS Fargate" case-studies/hospital-customer-support-agent.md resume/product-engineer.md`
Expected: 기술, 기간, 소속, 핵심 표현이 이력서와 모순되지 않는다.

**Step 2: 기존 케이스 스터디와 톤 차이를 확인한다**

Run: `sed -n '1,220p' case-studies/outbound-voice-agent.md`
Expected: 새 문서도 개요가 빠르게 읽히고, 본문은 문제와 설계 중심으로 전개되어 톤이 크게 어긋나지 않는다.

**Step 3: 최종 문서를 처음부터 끝까지 다시 읽는다**

Run: `sed -n '1,260p' case-studies/hospital-customer-support-agent.md`
Expected: 기술 나열보다 문제, 설계 판단, 시스템 동작, 기여 범위가 먼저 보인다.

**Step 4: 필요하면 README 또는 workflow 참조 추가 여부를 판단한다**

Run: `rg -n "hospital-customer-support-agent" README.md docs/workflow.md`
Expected: 기존 색인에 새 문서를 추가해야 하는지 판단할 수 있다.

**Step 5: 사용자 요청에 따라 커밋은 생략한다**

커밋 단계는 이번 작업에서 수행하지 않는다.

