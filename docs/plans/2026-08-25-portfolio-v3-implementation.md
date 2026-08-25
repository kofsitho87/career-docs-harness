# 포트폴리오 v3 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 설계 문서의 4챕터·22장 구조를 `portfolio/heewung-song-portfolio-v3.html` 한 파일로 구현한다.

**Architecture:** v2의 셸(CSS 시스템·메뉴·네비게이션 JS)을 그대로 들어 올려 재사용하고, 슬라이드 본문만 새로 쓴다. v2는 지우지 않고 남긴다. 슬라이드는 기존 컴포넌트 클래스(`.lay`, `.node`, `.blk`, `.fig`, `.gate` 등)로 조립하며 새 CSS는 꼭 필요할 때만 추가한다.

**Tech Stack:** 단일 HTML 파일, 인라인 CSS/JS, IBM Plex Sans KR·Mono·Manrope(Google Fonts), html-to-image(CDN), 이미지는 `../assets/` 상대 경로.

**Spec:** `docs/plans/2026-08-25-portfolio-v3-structure-design.md`

## Global Constraints

- 슬라이드 총 22장. 구성은 오프닝·지도 3 / 챕터1 5 / 챕터2 5 / 챕터3 3 / 챕터4 5 / 클로징 1.
- 챕터는 넷이며 번호는 `1`~`4`. 하위 번호(`1-1` 형식)를 쓰지 않는다.
- 모든 챕터가 `① 무엇인가 → ② 기능별로 깊게 → ③ 결과와 한계` 3단을 따른다. ①③은 각 1장 고정.
- 사실은 `resume/product-engineer.md`를 기준으로 한다. 설계 문서에 없는 수치·기능·사건을 새로 만들지 않는다.
- ①에는 위키 용어(`Configuration boundary` 등)를 그대로 쓰지 않는다. ②③에서는 `UNSOUND_COMMIT`, `ZSET` 같은 실제 이름을 쓴다.
- 소유 범위는 역할 라벨과 한 줄로만 적는다. 기능별로 누가 만들었는지 쪼개지 않는다.
- 회사명(Cupix 등)과 지원 직무 문구를 넣지 않는다.
- 측정하지 않은 성과(절감 시간, 확산률)를 주장하지 않는다.
- 16:9 기준 `font-size: clamp(11px, min(1.094vw, 1.944vh), 24px)` 루트 스케일을 유지한다. 보조 문구도 `--t-meta`(13.3px @1080p) 아래로 내려가지 않는다.
- 다크·라이트 테마 모두에서 읽혀야 한다. 색은 v2의 CSS 변수만 쓴다.
- 이미지는 `assets/`에 있는 것만 쓴다. 새 이미지를 만들지 않는다.

---

## File Structure

| 파일 | 책임 |
|---|---|
| `portfolio/heewung-song-portfolio-v3.html` (신규) | 전체 산출물. 셸 + 22장 |
| `portfolio/heewung-song-portfolio-v2.html` (수정 없음) | 셸 추출 원본이자 대조 기준 |
| `docs/plans/2026-08-25-portfolio-v3-structure-design.md` (참조) | 슬라이드별 내용 명세 |
| `resume/product-engineer.md` (참조) | 사실 기준 |

v2의 줄 구성은 다음과 같다. 셸 추출에 그대로 쓴다.

- `1`–`824`: `<!DOCTYPE>`부터 `</style>`까지. head + CSS 전체
- `825`–`840`: `<body>`, skip 링크, progress 바, 메뉴
- `841`: `<div class="deck">`
- `842`–`2335`: 슬라이드 28장 (v3에서는 버린다)
- `2336`–`2347`: `</div>`(deck) · `</main>` · `<nav>`(이전/다음 버튼과 counter)
- `2349`–`2474`: `<script>`부터 `</html>`까지. 네비게이션·테마·카운터·PNG 저장

`2343`의 counter 초기값이 `1 / 28`로 하드코딩돼 있다. v3에서 `1 / 22`로 고쳐야 한다.

### 사용 가능한 이미지

| 파일 | 배치 |
|---|---|
| `inbound-call-flow-config.png` | 챕터1 ① 또는 ② |
| `inbound-warm-transfer-flow.png` | 챕터1 ② 상담원 연결 |
| `cupix-ax-operations-screen.png` | 챕터2 ③ 모니터 |
| `cupix-ax-analytics-screen.png` | 챕터2 ③ 진단 |
| `customer-support-chat-flow.png`, `customer-support-chat-step1.png`, `customer-support-chat-step2.png`, `customer-support-chat-complete.png` | 챕터3 ② 상담 흐름 |
| `aiu-web-knowledge-answer.png`, `aiu-slack-knowledge-answer.jpg`, `aiu-web-evidence-attachment.png` | 챕터4 ① 또는 ② |

---

## 슬라이드 인벤토리

| # | `data-slide` | 챕터 | 내용 | Task |
|---|---|---|---|---|
| 1 | `hero` | — | 히어로 · 중심 메시지 · 4챕터 맵 | 2 |
| 2 | `about` | — | 일하는 방식 · 커리어 타임라인 | 2 |
| 3 | `map` | — | 챕터 지도 · 클릭 이동 | 2 |
| 4 | `ch1-what` | 1 | ① 병원 전화 Voice AI란 | 3 |
| 5 | `ch1-booking` | 1 | ② 신규 예약 | 3 |
| 6 | `ch1-transfer` | 1 | ② 상담원 연결 | 3 |
| 7 | `ch1-directions` | 1 | ② 두 방향의 차이 | 3 |
| 8 | `ch1-result` | 1 | ③ 결과와 한계 | 3 |
| 9 | `ch2-what` | 2 | ① 대화분석이란 | 4 |
| 10 | `ch2-transcribe` | 2 | ② 전사 보완 | 4 |
| 11 | `ch2-resolution` | 2 | ② 통화 결과 판정 | 4 |
| 12 | `ch2-semantic` | 2 | ② 의미 QA | 4 |
| 13 | `ch2-result` | 2 | ③ 이걸로 무엇을 하는가 | 4 |
| 14 | `ch3-what` | 3 | ① 챗봇이란 | 5 |
| 15 | `ch3-flow` | 3 | ② 상담 한 번의 흐름 | 5 |
| 16 | `ch3-result` | 3 | ③ 결과와 한계 | 5 |
| 17 | `ch4-what` | 4 | ① AIU란 · 소유 경계 | 6 |
| 18 | `ch4-manual` | 4 | ② 매뉴얼 답변 | 6 |
| 19 | `ch4-analytics` | 4 | ② 통화 조회·전환율 | 6 |
| 20 | `ch4-qa` | 4 | ② 통화 QA | 6 |
| 21 | `ch4-result` | 4 | ③ 결과와 한계 | 6 |
| 22 | `closing` | — | 반복되는 방식 | 7 |

---

## Task 1: 셸 추출과 22장 프레임

v2의 CSS·메뉴·JS를 그대로 옮기고, 내용이 빈 슬라이드 22개를 만든다. 이 태스크가 끝나면 좌우 키로 22장을 넘길 수 있고 테마 토글이 동작한다.

**Files:**
- Create: `portfolio/heewung-song-portfolio-v3.html`
- Read: `portfolio/heewung-song-portfolio-v2.html:1-841`, `:2336-2474`

**Interfaces:**
- Consumes: 없음
- Produces: `.slide[data-slide]` 22개, `.slide-inner` 래퍼, `.rail` 4챕터 트랙, `showSlide(n)` / `cycleTheme()` / `downloadImage()` 전역 함수, CSS 변수 전체(`--t-*`, `--panel`, `--r` 등)와 컴포넌트 클래스

- [ ] **Step 1: 셸 세 조각을 추출해 합친다**

```bash
cd /Users/heewungsong/Desktop/Dan/career-docs-harness
V2=portfolio/heewung-song-portfolio-v2.html
V3=portfolio/heewung-song-portfolio-v3.html
sed -n '1,841p' "$V2" > "$V3"
printf '\n      <!-- SLIDES -->\n\n' >> "$V3"
sed -n '2336,2474p' "$V2" >> "$V3"
wc -l "$V3"
```

기대: 983줄 안팎. `<div class="deck">`까지가 앞부분, `</div>` · `</main>` · `<nav>` · `<script>`가 뒷부분이다.

경계를 반드시 눈으로 확인한다. `2336`은 deck을 닫는 `</div>`이고 `2337`은 `</main>`이다. `2346`에서 자르면 `<nav>` 중간이 잘려 HTML이 깨진다.

- [ ] **Step 2: 제목과 챕터 클래스를 v3에 맞춘다**

`<title>`은 그대로 두되, CSS의 챕터 색 정의에서 `ch5`를 제거하고 `ch4`까지만 남긴다. v2에서 `.ch1`과 `.ch4`만 별도 정의돼 있으므로 실제 수정 대상은 챕터 강조색을 쓰는 규칙뿐이다. 다음으로 확인한다.

```bash
grep -n "ch5\|\.ch4\|\.ch1" portfolio/heewung-song-portfolio-v3.html | head -20
```

`ch5` 선택자가 있으면 지운다. 없으면 이 스텝은 확인만 하고 넘어간다.

이어서 counter 초기값을 고친다. v2에서 `1 / 28`로 하드코딩돼 있다.

```bash
sed -i '' 's|>1 / 28<|>1 / 22<|' portfolio/heewung-song-portfolio-v3.html
grep -n "1 / 22" portfolio/heewung-song-portfolio-v3.html
```

한 줄이 잡혀야 한다.

- [ ] **Step 3: 빈 슬라이드 22개를 삽입한다**

`<!-- SLIDES -->` 자리에 아래 패턴을 22번 반복해 넣는다. `data-slide` 값과 챕터 클래스는 위 인벤토리 표를 따른다. 첫 장에만 `active`를 붙인다.

```html
      <!-- ============ 04 · CH1 ① 무엇인가 ============ -->
      <section class="slide ch1" data-slide="ch1-what">
        <div class="slide-inner">
          <div class="rail an">
            <span class="rail-ch">CH 01</span><span class="rail-name">병원 전화 Voice AI</span>
            <span class="rail-track"><i class="on"></i><i></i><i></i><i></i></span>
            <span class="rail-layer" data-l="what">무엇인가</span>
          </div>
          <div class="head an d1">
            <h2>PLACEHOLDER — Task 2~7에서 채운다</h2>
          </div>
        </div>
      </section>
```

`.rail-track`의 `<i>`는 **4개**다. v2는 5챕터라 5개였다. 현재 챕터 위치에만 `class="on"`을 준다. 오프닝·지도·클로징 슬라이드에는 `.rail`을 넣지 않는다.

- [ ] **Step 4: 로컬 서버를 띄우고 브라우저로 연다**

```bash
python3 -m http.server 8899 --directory /Users/heewungsong/Desktop/Dan/career-docs-harness
```

백그라운드로 실행한 뒤 `http://localhost:8899/portfolio/heewung-song-portfolio-v3.html`을 브라우저 도구로 연다.

- [ ] **Step 5: 네비게이션을 확인한다**

브라우저에서 확인할 것:
1. 우하단 카운터가 `1 / 22`로 표시된다
2. 오른쪽 화살표 키를 21번 눌러 마지막 장까지 간다. 카운터가 `22 / 22`가 된다
3. 메뉴 → 테마 토글이 dark/light/system을 순환하고 배경색이 바뀐다
4. 콘솔에 에러가 없다

카운터가 22가 아니면 슬라이드 수를 세어 맞춘다.

- [ ] **Step 6: 커밋**

```bash
git add portfolio/heewung-song-portfolio-v3.html
git commit -m "chore: v3 셸과 22장 프레임 추가"
```

---

## Task 2: 오프닝 3장

**Files:**
- Modify: `portfolio/heewung-song-portfolio-v3.html` — `data-slide="hero"`, `"about"`, `"map"`

**Interfaces:**
- Consumes: Task 1의 프레임과 컴포넌트 클래스
- Produces: `.hero-map-row` 4개(챕터당 하나), `.map-row[onclick]` 4개 — 각 `showSlide()` 호출로 챕터 첫 장으로 이동

- [ ] **Step 1: 히어로를 쓴다**

v2의 `data-slide="1"`(`:844-880`) 마크업을 뼈대로 삼되 챕터 맵을 **4줄**로 줄인다. v2는 5줄이었다.

| 번호 | 제목 | 부제 |
|---|---|---|
| 01 | 병원 전화 Voice AI | 거는 전화와 받는 전화를 하나의 시스템으로 |
| 02 | 통화 관측과 평가 | 수천 건의 결과를 다시 듣지 않고 재구성 |
| 03 | 챗봇 고객상담 | 웹과 카카오의 1차 응대 |
| 04 | AIU 사내 업무지원 | 같은 방식을 동료의 업무로 |

중심 메시지와 `.hero-stats` 수치는 v2에서 그대로 가져온다. 단 통화 수치는 **아웃바운드 550,000 + 인바운드 70,000 = 620,000**을 합산 표기한다. 근거는 `resume/product-engineer.md`.

- [ ] **Step 2: 일하는 방식을 쓴다**

v2의 `data-slide="2"`(`:882-983`)를 거의 그대로 옮긴다. 커리어 타임라인, 4단계 일하는 방식, End-to-end product scope가 모두 v3에서도 유효하다. 변경할 것은 없다.

- [ ] **Step 3: 챕터 지도를 쓴다**

v2의 `data-slide="toc"`(`:1035-1074`)를 4행으로 줄인다. 각 행은 챕터가 답하는 질문 하나와 대표 증거를 담는다.

| 챕터 | 질문 | 증거 | 장수 |
|---|---|---|---|
| 01 | 병원의 전화 업무를 AI가 대신할 수 있는가? | flow_config 설정 · stage-before-commit 예약 · 공용 FIFO 상담원 연결 | 5 slides |
| 02 | 수천 건의 통화를 사람이 다시 듣지 않고 판정할 수 있는가? | 전사 보완 · 배타적 resolution · 근거 기반 의미 QA | 5 slides |
| 03 | 검색·개인정보·중단이 섞인 상담을 상태로 관리할 수 있는가? | 결정론적 4단 게이트 · pending_question 복귀 | 3 slides |
| 04 | 같은 방식을 사내 업무로 옮길 수 있는가? | 범위 나눈 전문가 · SELECT-only 조회 · 실행 권한 분리 | 5 slides |

각 행에 `onclick="showSlide(N)"`을 붙인다. N은 인벤토리 표의 슬라이드 번호(4, 9, 14, 17)다.

- [ ] **Step 4: 브라우저로 3장을 확인한다**

1. 1~3장을 넘기며 잘림이나 겹침이 없는지 본다
2. 지도의 4행을 각각 클릭해 4·9·14·17장으로 이동하는지 확인한다
3. 라이트 테마로 바꿔 같은 3장을 다시 본다

- [ ] **Step 5: 커밋**

```bash
git add portfolio/heewung-song-portfolio-v3.html
git commit -m "feat: v3 오프닝 3장"
```

---

## Task 3: 챕터 1 — 병원 전화 Voice AI (5장)

내용 명세는 설계 문서의 `### 1 · 병원 전화 Voice AI (확정)` 절을 따른다. 그 절의 표와 문장이 이 태스크의 사양이다.

**Files:**
- Modify: `portfolio/heewung-song-portfolio-v3.html` — `ch1-what`, `ch1-booking`, `ch1-transfer`, `ch1-directions`, `ch1-result`

**Interfaces:**
- Consumes: Task 1의 `.rail`, `.lay`, `.node`, `.blk`, `.gate`, `.fig`, `.metric` 클래스
- Produces:
  - `.flow` 가로 4단계 + 받침 한 줄 패턴 — 챕터 2~4의 ①이 같은 문법을 재사용한다
  - **②의 세 겹 고정 패턴** — 아래 Step 2에서 확정하며 이후 모든 ② 슬라이드가 그대로 따른다

**②의 세 겹 시각 규약 (이 태스크에서 확정, 이후 전 챕터 고정)**

설계 문서의 시각 방향에 따라 ②는 항상 같은 자리에 같은 종류의 블록을 놓는다. 독자가 세 번째 블록을 보면 실패 사례임을 학습해야 한다.

```html
<div class="sec-h"><h3 class="cap cap-own ko">무엇을 하는가</h3></div>
<!-- 한 문장. 사용자에게 무엇이 일어나는지 -->

<div class="sec-h"><h3 class="cap cap-bound ko">어떻게 만들었나</h3></div>
<!-- .flow / .gates / .states 중 하나로 구조를 그린다 -->

<div class="sec-h"><h3 class="cap cap-edge ko">뭐가 깨졌나</h3></div>
<!-- .bul 목록. 각 항목은 사건 하나 -->
```

`cap-own` / `cap-bound` / `cap-edge` 세 색을 이 순서로 고정한다. 세 번째 겹이 실패가 아니라 **의도적으로 그은 경계**인 슬라이드(챕터 4의 통화 QA)에서는 제목만 `뭘 하지 않기로 했나`로 바꾸고 `cap-edge`는 유지한다.

- [ ] **Step 1: ① 무엇인가를 쓴다**

설계 문서의 번역표 다섯 줄을 **가로 4단계 흐름 + 받치는 한 줄**로 그린다. 위키 용어를 쓰지 않는다.

```html
<div class="flow">
  <div class="node node-own"><b>규칙을 받는다</b><span>병원마다 다른 설정을 통화 시작 때</span></div><span class="arw">&rarr;</span>
  <div class="node"><b>대화를 진행한다</b><span>설정대로</span></div><span class="arw">&rarr;</span>
  <div class="node"><b>처리를 정한다</b><span>AI · 사람 연결 · 메모</span></div><span class="arw">&rarr;</span>
  <div class="node"><b>결과를 넘긴다</b><span>통화 종료 후 분석으로</span></div>
</div>
<div class="note note-edge"><strong>민감한 내용은 밖으로 내보내지 않는다</strong> · 네 단계 전체를 관통하는 규칙입니다.</div>
```

기능 다섯(병원 지식 답변·신규 예약 신청·예약 조회·예약 변경·예약 취소)과 상담원 연결을 `.chips`로 나열한다. 규모(6개 언어, action mode 3종)와 안 하는 것 두 줄을 `.blk`에 넣는다.

- [ ] **Step 2: ② 신규 예약을 쓴다**

`.gates` 컴포넌트로 `search → stage → commit`을 그린다. v2의 `data-slide="8"`(`:1334-1382`)이 같은 패턴을 쓰므로 참고한다.

깨진 것 세 가지와 잡는 법(`UNSOUND_COMMIT`)을 설계 문서 표 그대로 넣는다. 성숙도 차이 한 줄을 `.note`로 붙인다. **아웃바운드가 인바운드와 같은 수준이라고 쓰지 않는다.**

- [ ] **Step 3: ② 상담원 연결을 쓴다**

`.states` 컴포넌트로 `queued → waiting_for_trunk → dialing → briefing → connected`를 그린다. ZSET/HASH/Stream 세 구조를 `.blk` 세 개로 나눈다. 깨진 것 네 가지를 `.bul` 목록으로 넣는다. `assets/inbound-warm-transfer-flow.png`를 `.fig`로 붙인다.

- [ ] **Step 4: ② 두 방향의 차이를 쓴다**

설계 문서의 4행 비교표를 `.lay lay-2`로 좌우 배치한다. 깨진 것 세 가지(AMD race condition, 늦은 STT, DTMF provenance 누수)를 번호 목록으로 넣고, 동시성 상한 한 줄을 `.note`로 붙인다.

- [ ] **Step 5: ③ 결과와 한계를 쓴다**

- 검증 4단계를 `.flow`로: `단위 테스트 → text-only Agent 평가 → 환자 시뮬레이션 → 오디오·전화망`
- 수치를 `.metrics`로 방향별 분리: 아웃바운드 550,000+ / 일 2,500 / 300+ 병원, 인바운드 70,000+ / 일 1,500
- 한계 세 가지를 `.bul bul-deny`로

- [ ] **Step 6: 브라우저로 5장을 확인한다**

1. 4~8장을 넘기며 각 장이 한 화면에 들어가는지 본다. 세로 스크롤이 생기면 내용을 줄인다
2. 이미지가 깨지지 않는지 확인한다
3. 라이트 테마에서 다시 본다
4. 1280x720으로 창을 줄여 같은 5장을 본다

- [ ] **Step 7: 사실을 대조한다**

```bash
grep -n "550,000\|70,000\|2,500\|1,500\|300+" portfolio/heewung-song-portfolio-v3.html
grep -n "550,000\|70,000\|2,500\|1,500\|300" resume/product-engineer.md
```

두 결과의 수치가 일치해야 한다. 어긋나면 이력서를 기준으로 v3를 고친다.

- [ ] **Step 8: 커밋**

```bash
git add portfolio/heewung-song-portfolio-v3.html
git commit -m "feat: v3 챕터1 병원 전화 Voice AI 5장"
```

---

## Task 4: 챕터 2 — 통화 관측과 평가 (5장)

내용 명세는 설계 문서의 `### 2 · 통화 관측과 평가 (확정)` 절을 따른다.

**Files:**
- Modify: `portfolio/heewung-song-portfolio-v3.html` — `ch2-what`, `ch2-transcribe`, `ch2-resolution`, `ch2-semantic`, `ch2-result`

**Interfaces:**
- Consumes: Task 3이 만든 `.flow` ① 문법
- Produces: `.figs` 2열 스크린샷 배치 — 챕터 3·4가 재사용한다

- [ ] **Step 1: ① 대화분석이란을 쓴다**

파이프라인 전경을 `.flow flow-v` 또는 `.stack`으로 한 장에 그린다.

```
입력 → 중복 확인 → 정규화 → 전사 보완 → 요약 → 발행 → 저장 → 결정론적 분석 → 의미 분석 → 점수
```

실시간과 Kafka로 분리돼 있다는 점, 통화 중에는 아무것도 바꾸지 않는다는 점을 `.blk`와 `.note`로 넣는다.

- [ ] **Step 2: ② 전사 보완을 쓴다**

상담원 연결 이후 AI가 대화에서 빠져 기록이 끊긴다는 문제를 먼저 그린다. 녹음 크롭 → Gemini 구조화 전사 → 순서 보존 병합을 `.flow`로. 깨진 것 세 가지(앵커 어긋남, 짧거나 무음인 오디오, 녹음 가용성 지연)를 `.bul`로. `recording_started_at` 앵커 한 줄을 `.note`로.

- [ ] **Step 3: ② 통화 결과 판정을 쓴다**

`events → attempts → rollup` 3층을 `.flow`로. 배타적 resolution 7단계 우선순위를 `.gates` 또는 번호 목록으로. 깨진 것 네 가지를 `.bul`로.

- [ ] **Step 4: ② 의미 QA를 쓴다**

핵심 문장을 `.claim`으로 올린다.

> AI가 "목요일 오후 가능합니다"라고 말한 것을 근거로 환자가 목요일을 원했다고 판정하던 문제

근거 turn index 필수와 sanitizer 거부를 `.blk`로. 민감정보 경계와 두 테스트(`test_main_kafka_payload.py`, `test_semantic_layer_boundary.py`)를 `.note note-own`으로 한 줄씩.

- [ ] **Step 5: ③ 이걸로 무엇을 하는가를 쓴다**

두 화면을 `.figs`로 나란히 놓는다.

| 이미지 | 라벨 | 캡션 |
|---|---|---|
| `../assets/cupix-ax-operations-screen.png` | Monitor | 응대 성공률·셀프 처리율·예약 전환율과 인사말 전·중·후로 나눈 초기 이탈 |
| `../assets/cupix-ax-analytics-screen.png` | Diagnose | 시도 단위로 분해한 손실 지점과 개선 담당 주체 |

운영 도구(버전 기반 백필, 리포트 시점 임계값 조정) 한 줄과 한계 세 가지를 넣는다.

- [ ] **Step 6: 브라우저로 5장을 확인하고 커밋**

Task 3의 Step 6과 같은 절차로 9~13장을 본다. 통과하면 커밋한다.

```bash
git add portfolio/heewung-song-portfolio-v3.html
git commit -m "feat: v3 챕터2 통화 관측과 평가 5장"
```

---

## Task 5: 챕터 3 — 챗봇 고객상담 (3장)

내용 명세는 설계 문서의 `### 3 · 챗봇 고객상담 (확정)` 절을 따른다.

**Files:**
- Modify: `portfolio/heewung-song-portfolio-v3.html` — `ch3-what`, `ch3-flow`, `ch3-result`

**Interfaces:**
- Consumes: Task 3·4의 `.flow` ① 문법, Task 4의 `.figs`
- Produces: 없음

- [ ] **Step 1: ① 챗봇이란을 쓴다**

용도·역할을 `.claim`과 `.support`로. 기능 여섯(병원 지식 답변·예약 안내·개인정보 수집·상담원 연결 신청·진료 이미지 제공·의료 범위 차단)을 `.chips`로. 안 하는 것 두 줄을 `.bul bul-deny`로.

**예약을 직접 실행한다고 쓰지 않는다.** UI를 열어줄 뿐이다.

- [ ] **Step 2: ② 상담 흐름을 쓴다**

결정론적 게이트 순서를 `.flow flow-v`로 세로 배치한다.

```
개인정보 미수집?  → 지식 조회를 건너뛰고 수집부터
FAQ 우선          → 등록된 답변을 그대로 (엄격 검증 통과 시)
직접 fact data    → 병원 기준정보에서 즉답
예약 가드         → 의도 분류 후 UI 열기
의료 범위 게이트  → 진단·처방은 여기서 차단
↓ 전부 미해당
LLM 팀 실행
```

`pending_question` 복귀를 이 장의 하이라이트로 `.blk blk-own`에 넣는다. 동의 카드 중복 사건을 `.note`로 한 줄. `assets/customer-support-chat-flow.png`를 `.fig`로 붙인다.

- [ ] **Step 3: ③ 결과와 한계를 쓴다**

채널 확장(웹 → 카카오·음성)을 한 줄. 소유 범위를 **한 줄로만** — "이후 팀이 확장할 수 있는 초기 그래프와 서비스 경계를 구축했다." 한계 세 가지를 `.bul bul-deny`로.

- [ ] **Step 4: 브라우저로 3장을 확인하고 커밋**

14~16장을 본다. 통과하면 커밋한다.

```bash
git add portfolio/heewung-song-portfolio-v3.html
git commit -m "feat: v3 챕터3 챗봇 고객상담 3장"
```

---

## Task 6: 챕터 4 — AIU 사내 업무지원 (5장)

내용 명세는 설계 문서의 `### 4 · AIU 사내 업무지원 (확정)` 절을 따른다.

**Files:**
- Modify: `portfolio/heewung-song-portfolio-v3.html` — `ch4-what`, `ch4-manual`, `ch4-analytics`, `ch4-qa`, `ch4-result`

**Interfaces:**
- Consumes: Task 3·4·5의 컴포넌트 문법 전체
- Produces: 없음

- [ ] **Step 1: ① AIU란을 쓴다**

이 챕터는 정의가 곧 경계다. 소유 경계를 그림으로 그린다.

```html
<div class="flow">
  <div class="node node-mute"><b>동료</b><span>웹 · Slack</span></div><span class="arw">&rarr;</span>
  <div class="node node-bound"><b>OpenBot</b><span>신원 · 권한 · 실행 · 감사</span></div><span class="arw">&rarr;</span>
  <div class="node node-own"><b>AIU</b><span>추론하고 답한다</span></div>
</div>
<div class="note note-edge"><strong>AIU는 효과를 직접 실행하지 않습니다</strong> · 실행이 필요하면 OpenBot으로 되돌려 보냅니다.</div>
```

기능 여섯을 `.chips`로. 안 하는 것 세 가지(스스로 실행하지 않음·지식은 읽기 전용·DB는 SELECT만)를 `.bul bul-deny`로.

- [ ] **Step 2: ② 매뉴얼 답변을 쓴다**

Supervisor가 매뉴얼을 직접 못 읽는다는 것을 그림으로. 네 전문 Agent와 각자의 소스 범위를 `.lanes` 또는 `.grid-2`로.

| 전문 Agent | 읽을 수 있는 소스 |
|---|---|
| `inbound-agent` | 인바운드 |
| `agent-admin-agent` | Agent Admin |
| `outbound-agent` | 아웃바운드 |
| `hq-svc-agent` | AIU HQ · AIU SVC |

깨진 것 두 가지(접근 거부를 문서 없음으로 답하던 문제, 매니페스트 문서 수 불일치)를 `.bul`로. 문서 322개 규모를 `.metric`으로. `assets/aiu-web-knowledge-answer.png`를 `.fig`로.

- [ ] **Step 3: ② 통화 조회·전환율을 쓴다**

SELECT-only 경계를 `.blk blk-bound`로. 결과에서 제외하는 것(이름·전화번호·transcript·녹음·raw payload)을 `.bul bul-deny`로 명시. 깨진 것 세 가지를 `.bul`로.

지표 정의를 코드가 소유한다는 요지를 `.claim`으로 올린다.

- [ ] **Step 4: ② 통화 QA를 쓴다**

제한 네 가지(ID 1~5건, 패턴 마스킹, 턴당 1,200자, 앞뒤 60개)를 `.gates`로. 경계 세 줄(untrusted data, 재진술 필수, 독립 검증 주장 금지)을 `.bul bul-deny`로.

이 슬라이드는 세 번째 겹이 실패가 아니라 경계다. Task 3의 시각 규약대로 제목만 `뭘 하지 않기로 했나`로 바꾸고 `cap-edge` 색은 유지한다.

마지막 줄을 `.note note-own`으로 강조한다. 할 수 있는 것과 주장할 수 있는 것을 구분한다.

- [ ] **Step 5: ③ 결과와 한계를 쓴다**

- 규모를 `.metrics`로: 소스 5개 · 문서 322개 · 전문 Agent 4개 · 계약 테스트 45개
- 속도 한 줄: 2026.08 착수 후 3주 만에 1차 운영 가능
- 한계 세 가지. **1번(단일 full-access 인증 경계)을 빼지 않는다.** 미완성을 완성처럼 쓰지 않은 기록이다

- [ ] **Step 6: 브라우저로 5장을 확인하고 커밋**

17~21장을 본다.

```bash
grep -n "322\|45개\|3주" portfolio/heewung-song-portfolio-v3.html
grep -n "322\|45개\|3주" resume/product-engineer.md
```

수치가 일치하면 커밋한다.

```bash
git add portfolio/heewung-song-portfolio-v3.html
git commit -m "feat: v3 챕터4 AIU 사내 업무지원 5장"
```

---

## Task 7: 클로징 1장

**Files:**
- Modify: `portfolio/heewung-song-portfolio-v3.html` — `closing`

**Interfaces:**
- Consumes: Task 2~6이 만든 챕터 전체
- Produces: 없음

- [ ] **Step 1: 반복되는 방식을 쓴다**

v2의 `data-slide="close"`(`:2261` 이후)를 뼈대로 삼되 4챕터에 맞춘다. 네 프로젝트를 관통하는 패턴을 쓴다.

- 업무를 먼저 이해하고 반복 판단을 찾는다
- 정책·권한·예외를 코드와 설정으로 고정해 모델의 추론과 분리한다
- 실제 도구·데이터·채널에 연결해 운영 가능한 상태까지 만든다
- 관측과 평가 결과를 다음 설계의 근거로 되돌린다

네 챕터가 각각 이 패턴의 어느 단계를 보여줬는지 한 줄씩 연결한다.

- [ ] **Step 2: 브라우저로 확인하고 커밋**

```bash
git add portfolio/heewung-song-portfolio-v3.html
git commit -m "feat: v3 클로징"
```

---

## Task 8: 전체 검증

**Files:**
- Modify: `portfolio/heewung-song-portfolio-v3.html` (수정이 필요한 경우만)

**Interfaces:**
- Consumes: 완성된 22장
- Produces: 없음

- [ ] **Step 1: 22장을 순서대로 넘기며 본다**

브라우저에서 1장부터 22장까지 넘긴다. 각 장에서 확인할 것:
1. 세로 스크롤이 생기지 않는다
2. 텍스트가 잘리거나 겹치지 않는다
3. 이미지가 모두 로드된다
4. 콘솔 에러가 없다

- [ ] **Step 2: 라이트 테마로 다시 본다**

테마를 light로 바꾸고 22장을 다시 넘긴다. 대비가 부족해 읽히지 않는 텍스트가 없어야 한다.

- [ ] **Step 3: 두 뷰포트에서 확인한다**

1280x720과 1920x1080에서 각각 몇 장을 표본으로 본다. 루트 스케일이 정상이면 두 해상도의 레이아웃이 동일해야 한다. 이어서 375px 폭으로 줄여 가로 넘침이 없는지 본다.

- [ ] **Step 4: 완료 기준을 대조한다**

설계 문서의 `## 완료 기준` 항목을 하나씩 확인한다.

- 각 챕터의 ① 한 장만 보고 그 시스템이 무엇인지 말할 수 있는가
- ②의 모든 슬라이드에 실패 사례 또는 의도적으로 그은 경계가 들어 있는가
- 인바운드와 아웃바운드가 한 시스템의 두 방향으로 읽히는가
- 관측 챕터에서 과정과 용도가 둘 다 드러나는가
- AIU 챕터에서 무엇을 하지 않기로 했는지 드러나는가
- 모든 챕터가 마지막에 못 하는 것을 명시하는가
- 네 챕터가 같은 3단 리듬을 유지하는가

미달 항목이 있으면 해당 슬라이드를 고치고 Step 1로 돌아간다.

- [ ] **Step 5: 금지 표현을 검사한다**

```bash
grep -n -i "cupix\|큐픽스\|지원\s*동기\|절감\|확산률" portfolio/heewung-song-portfolio-v3.html
```

결과가 비어 있어야 한다. 회사명·지원 직무 문구·측정하지 않은 성과가 없어야 한다.

- [ ] **Step 6: 보조 문서를 맞춘다**

`README.md`와 `docs/workflow.md`에서 대표 산출물 경로를 v3로 갱신한다. v2를 남길지 대체할지는 이 시점에 사용자에게 확인한다.

- [ ] **Step 7: 서버를 정리하고 커밋**

```bash
lsof -ti:8899 | xargs kill 2>/dev/null || true
git add -A
git commit -m "docs: v3 완성에 맞춰 보조 문서 갱신"
```
