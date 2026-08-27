# 포트폴리오 v4 · A 방향(편집 스플릿) 전면 적용 기록

## 메타

- 작성일: 2026-08-27
- 대상 산출물: `portfolio/heewung-song-portfolio-v4.html` (신규)
- 원본: `portfolio/heewung-song-portfolio-v3.html` (변경 없음, 그대로 유지)
- 범위: 30장 전체
- 선행 설계: `docs/plans/2026-08-25-portfolio-v3-structure-design.md`
- 사실 기준: `resume/product-engineer.md`

## 배경

v3는 슬라이드마다 `rail → head → 콘텐츠 블록` 단일 컬럼 스택 구조였다. 레이아웃 방향 시안 세 가지(A 편집 스플릿 · B 대시보드 그리드 · C 타임라인 스파인)를 비교한 뒤 **A 편집 스플릿**을 채택했다.

A 방향의 정의:

- 좌측 = 서사 컬럼(헤드라인 · claim · support)
- 우측 = 증거 패널(도식 · 카드 · 지표 · 화면)
- 두 컬럼 사이 헤어라인 디바이더
- 표지에만 쓰던 그라디언트 배경(`stage-bg`)을 전 슬라이드에 적용

## 확정된 편집 원칙

- **v3는 건드리지 않는다.** v4는 v3를 복사해 만든 별도 산출물이다.
- 문구·수치·경계 문장은 v3 그대로 유지한다. 이번 작업은 레이아웃 변경만 다룬다.
- 기존 컴포넌트 CSS는 수정하지 않는다. 새 `.split` 블록만 추가하고, 좁은 컬럼 대응은 모디파이어로 처리한다.
- 콘텐츠 밀도에 따라 두 비율을 쓴다.
  - `.split` — 좌 1.25fr / 우 1fr. 서사 주도형.
  - `.split.split-ev` — 좌 0.75fr / 우 1.6fr. 다이어그램 주도형.
- 2컬럼을 위해 split 슬라이드의 `.slide-inner` 최대 폭을 61rem → 80rem으로 넓힌다.
- 모바일(`@media`)에서는 1컬럼으로 해제하고 디바이더를 없앤다.

## 슬라이드별 비율 배정

| 비율 | 슬라이드 |
|---|---|
| `.split` (서사 주도) | 2 about · 24 ch4-what · 26 ch4-analytics · 27 ch4-qa · 29 ch4-result |
| `.split.split-ev` (증거 주도) | 3 map · 4–23 (ch1·ch2·ch3 전체) · 25 ch4-arch · 28 ch4-manual |
| 자체 레이아웃 유지 | 1 hero · 30 closing (배경 + 디바이더만 적용) |

## 예외 처리

- **2 about**: 경력 타임라인과 2컬럼 방법론 그리드를 모두 우측에 넣으면 세로로 3499px까지 넘쳤다. 경력 타임라인만 우측에 두고, 방법론 그리드는 split 아래 전체 폭 밴드(`.split-below`)로 내렸다.
- **19 ch3-what**: 채널 카드 2열(`chatbot-entry`)이 좁은 컬럼에서 글자 단위로 눌려 세로 1열로 스택했다.
- **26 ch4-analytics**: 자동 분배 시 좌측이 헤드라인만 남아 비었다. "왜 지표 계산을 코드가 소유하나" 설명 블록을 좌측으로 옮겨 균형을 맞췄다.
- **한국어 줄바꿈**: split 내부 텍스트에 `word-break: keep-all`과 `overflow-wrap: break-word`를 적용해 단어 중간 분리를 막았다.

## 작업 중 발견한 함정

- `.split-layout .slide-inner { max-width: 80rem }`(특이도 0,2,0)이 기존 슬라이드별 override
  `.ch2[data-slide="ch2-what"] .slide-inner`(0,4,0)에 밀려 적용되지 않았다.
  `.slide.split-layout[data-slide] .slide-inner`로 특이도를 맞추고 선언 순서를 뒤로 두어 해결했다.
- 좁은 컬럼용 모디파이어(`.dayline-v`, `.vis-board-v`)를 원본 정의보다 **앞에** 선언하면 무시된다.
  `.dayline.dayline-v` 형태로 특이도를 올려 선언 순서 의존을 없앴다.

## 검증

- 정적: 30장 유지, HTML 태그 균형, JavaScript parse 통과.
- 화면(1600×900): 30장 전부 뷰포트 안에 들어옴(최대 800px). 가로 오버플로 0.
- 눌림 검사: 폭 70px 미만에서 3줄 이상 감기는 텍스트 노드를 전 슬라이드에서 자동 탐지해 수정.
  남은 탐지 결과는 오탐(`.ask-time` 시각 칩 — `line-height:1` 칩이 말풍선 높이만큼 늘어난 것)이다.
- 모바일(375×812): 1컬럼 해제 확인.

## 남은 것

- `run` 시 상대 경로 이미지가 프리뷰 스냅샷에서 로드되지 않는다. 브라우저에서 파일을 직접 열면 정상이다.
- v3와 v4 중 무엇을 정본으로 삼을지는 미정. 정해지면 `README.md`와 `docs/workflow.md`의 대표 산출물 표기를 맞춘다.
