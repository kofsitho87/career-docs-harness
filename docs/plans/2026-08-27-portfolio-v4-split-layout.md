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
- **레이아웃은 한 틀을 고집하지 않는다.** 콘텐츠 밀도에 따라 세 모드 중 하나를 고른다.
  - `.split` — 좌 1.25fr / 우 1fr. 서사 주도형.
  - `.split.split-ev` — 좌 0.75fr / 우 1.6fr. 증거 주도형이되 폭이 덜 필요한 장.
  - `.lead` + `.lead-body` — 상단 서사 밴드(헤드라인 좌 / claim·support 우, 헤어라인으로 분리) + 그 아래 전체 폭 증거. 다이어그램·스크린샷이 폭을 실제로 필요로 하는 장.
- 2컬럼과 전체 폭 증거를 위해 `.slide-inner` 최대 폭을 61rem → 80rem으로 넓힌다.
- 모바일(`@media`)에서는 1컬럼으로 해제하고 디바이더를 없앤다.

## 슬라이드별 비율 배정

| 모드 | 슬라이드 |
|---|---|
| `.split` (서사 주도 2컬럼) | 2 about · 24 ch4-what · 26 ch4-analytics · 27 ch4-qa · 29 ch4-result |
| `.split.split-ev` (증거 주도 2컬럼) | 3 map · 4 ch1-what · 14 ch2-resolution · 15 ch2-semantic · 18 ch2-result · 25 ch4-arch |
| `.lead` + `.lead-body` (상단 밴드 + 전체 폭 증거) | 5 ch1-scale · 6 ch1-arch · 7 ch1-booking · 8 ch1-modes · 9 ch1-queue · 10 ch1-result · 11 ch2-what · 12 ch2-transcribe · 13 ch2-flags · 16 ch2-monitor · 17 ch2-diagnose · 19 ch3-what · 20 ch3-architecture · 21 ch3-flow · 22 ch3-knowledge · 23 ch3-result · 28 ch4-manual |
| 자체 레이아웃 유지 | 1 hero · 30 closing (배경 + 디바이더만 적용) |

`.lead`로 옮긴 기준은 **증거가 폭을 실제로 필요로 하는가**다. 2컬럼에서 증거 패널은 816px였는데, `.lead`에서는 1291px를 받는다.
해당 장들은 7트랙 파이프라인(11), 중첩 그리드 아키텍처 다이어그램(6·20), 실제 운영 화면 스크린샷(13·16·17·28)처럼 좁은 컬럼에서 라벨이 글자 단위로 감기거나 화면이 읽을 수 없게 작아지던 것들이다.
CH 03(19·20·21·22·23)은 다섯 장 모두 다중 트랙 보드라 전부 `.lead`로 옮겼다. 예를 들어 19의 결과 카드는 2컬럼에서 폭 171px라 제목이 전부 두 줄로 감겼는데, `.lead`에서는 한 줄에 들어간다.

## 예외 처리

- **2 about**: 경력 타임라인과 2컬럼 방법론 그리드를 모두 우측에 넣으면 세로로 3499px까지 넘쳤다. 경력 타임라인만 우측에 두고, 방법론 그리드는 split 아래 전체 폭 밴드(`.split-below`)로 내렸다.
- **19 ch3-what**: 처음에는 좁은 컬럼 대응으로 채널 카드를 세로 1열로 스택했으나, `.lead`로 옮겨 폭을 확보하면서 원래의 2열 배치로 되돌렸다.
- **26 ch4-analytics**: 자동 분배 시 좌측이 헤드라인만 남아 비었다. "왜 지표 계산을 코드가 소유하나" 설명 블록을 좌측으로 옮겨 균형을 맞췄다.
- **28 ch4-manual**: `.lead`로 옮길 때 질문 말풍선이 증거 뒤로 밀렸다. 밴드 위로 되돌려 `말풍선 → 헤드라인 → 증거` 순서를 지켰다.
- **한국어 줄바꿈**: split 내부 텍스트에 `word-break: keep-all`과 `overflow-wrap: break-word`를 적용해 단어 중간 분리를 막았다.

## 작업 중 발견한 함정

- `.split-layout .slide-inner { max-width: 80rem }`(특이도 0,2,0)이 기존 슬라이드별 override
  `.ch2[data-slide="ch2-what"] .slide-inner`(0,4,0)에 밀려 적용되지 않았다.
  `.slide.split-layout[data-slide] .slide-inner`로 특이도를 맞추고 선언 순서를 뒤로 두어 해결했다.
- 좁은 컬럼용 모디파이어(`.dayline-v`, `.vis-board-v`)를 원본 정의보다 **앞에** 선언하면 무시된다.
  `.dayline.dayline-v` 형태로 특이도를 올려 선언 순서 의존을 없앴다.
- **아이콘 박스가 `<span>`이라 생긴 v3 이월 버그**: `.chatbot-outcome span`·`.chatbot-core span`(특이도 0,1,1)이
  `.chatbot-outcome-icon`·`.chatbot-core-icon`(0,1,0)의 `display: grid`를 덮어써서 박스가 block이 됐고,
  아이콘이 박스 정중앙이 아니라 위쪽에 붙어 있었다(19장, 세로 10px 어긋남).
  `.chatbot-outcome span.chatbot-outcome-icon` 형태로 특이도를 올려 grid·중앙 정렬을 복구했다.
  같은 증상을 전 슬라이드에서 자동 탐지했고, 다른 곳의 어긋남은 아이콘 박스가 아닌 컨테이너라 손대지 않았다.

## 검증

- 정적: 30장 유지, HTML 태그 균형, JavaScript parse 통과.
- 화면(1600×900): 30장 전부 뷰포트 안에 들어옴(최대 800px). 가로 오버플로 0.
- 눌림 검사: 폭 70px 미만에서 3줄 이상 감기는 텍스트 노드를 전 슬라이드에서 자동 탐지해 수정.
  남은 탐지 결과는 오탐(`.ask-time` 시각 칩 — `line-height:1` 칩이 말풍선 높이만큼 늘어난 것)이다.
- 모바일(375×812): 1컬럼 해제 확인.
- 아이콘 중앙 정렬: 아이콘 박스와 그 안 SVG의 중심 좌표 차이를 전 슬라이드에서 측정. 19장은 세로 10px 어긋남 → 0px.

## 정본 표기

2026-08-27, **v4를 현재 대표 종합 포트폴리오로 확정**했다. `README.md`와 `docs/workflow.md`의 대표 산출물 표기를 v4로 옮기고, v3는 "v4 이전의 구조 정본"으로 내렸다.
사실(경력·수치·기간·기술 스택)을 고칠 때는 v3와 v4를 함께 맞춘다.

## 남은 것

- `run` 시 상대 경로 이미지가 프리뷰 스냅샷에서 로드되지 않는다. 브라우저에서 파일을 직접 열면 정상이다.
- `output/pdf/` 빌드는 아직 v3 기준이다. v4로 PDF를 다시 뽑을지는 미정.
