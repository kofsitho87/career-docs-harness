# 이력서·포트폴리오 제작 워크스페이스

이 저장소는 이력서와 포트폴리오를 작성, 정리, 개선하기 위한 작업 공간입니다. 사실 기준 문서, 작성 가이드, 설계/계획 문서, 현재 산출물을 함께 두고 문서 제작 흐름을 관리합니다.

## 프로젝트 요약

- 목적: 이력서와 포트폴리오를 일관된 기준으로 제작하고 업데이트하기
- 성격: 최종 결과물만 모아둔 폴더가 아니라, 작성 근거와 중간 계획까지 함께 관리하는 문서 작업 저장소
- 구성: 사실 기준 문서, 작성 가이드, 계획 문서, 최종 산출물, 일부 로컬 보조 스킬이 함께 존재

## 현재 산출물

- `resume/product-engineer.md`: 현재 정본이자 사실 기준으로 사용하는 제품 엔지니어 이력서
- `resume/cupix-ax-operations-engineer.md`: 큐픽스 AX Operations Engineer 지원용 맞춤 이력서
- `portfolio/html/heewung-song-portfolio.html`: **현재 대표 종합 포트폴리오.** v4에서 버전 접미사를 제거한 정본이다. v3의 4개 챕터·30장 구성과 문구·수치를 그대로 두고 레이아웃 언어만 편집 스플릿으로 재설계했다. 좌측 서사 컬럼과 우측 증거 패널을 헤어라인으로 나누고, 표지에만 쓰던 그라디언트 배경을 전 슬라이드에 적용한다. 슬라이드마다 콘텐츠 밀도에 맞춰 세 가지 레이아웃 모드(서사 주도 2컬럼 · 증거 주도 2컬럼 · 상단 서사 밴드 + 전체 폭 증거)를 골라 쓴다. 작업 기록은 `docs/plans/2026-08-27-portfolio-v4-split-layout.md`다
- `portfolio/pdf/heewung-song-portfolio-v4.pdf`: **현재 대표 포트폴리오 PDF.** v4 30장을 16:9(1152×648pt) 벡터 PDF로 뽑았다. 화면 캡처를 이미지로 묶는 방식이 아니라 Chromium 인쇄 경로를 써서 텍스트가 선택되고 연락처·GitHub 링크가 살아 있다. 빌드는 `scripts/build_portfolio_pdf.py`
- `case-studies/outbound-voice-agent.md`: 아웃바운드 Voice AI Agent 케이스 스터디
- `case-studies/inbound-voice-agent.md`: 인바운드 Voice AI Agent 케이스 스터디
- `case-studies/hospital-customer-support-agent.md`: 병원 고객상담 AI Agent 케이스 스터디
- `portfolio/assets/heewung-song-infographic.png`: 이력서와 함께 쓰는 시각 자료 자산
- `portfolio/assets/hospital-customer-support-agent-ppt-overview.png`: 병원 고객상담 AI Agent 개요·아키텍처 슬라이드 이미지
- `portfolio/assets/hospital-customer-support-agent-ppt-flow.png`: 병원 고객상담 AI Agent 흐름·설계 의사결정 슬라이드 이미지
- `portfolio/assets/customer-support-chat-step1.png`, `portfolio/assets/customer-support-chat-complete.png`: 공개 개발 서비스에서 검증한 정보 응답·개인정보 수집·상담 신청 흐름 캡처
- `portfolio/assets/cupix-ax-operations-screen.png`, `portfolio/assets/cupix-ax-analytics-screen.png`: 로컬 Agent Admin의 실제 PROD 집계 화면에서 비식별 상단 영역만 캡처한 인바운드 운영 현황·통화 분석 v2 증거 이미지
- `portfolio/assets/agent-admin-call-classification-evidence.png`: 실제 통화 상세의 예약·정보·상담원·종료 분류 카드 중 개인·병원·통화 식별정보를 완전히 제외한 규칙 기반 다중 분류 증거 이미지
- `portfolio/assets/aiu-web-knowledge-answer.png`, `portfolio/assets/aiu-slack-knowledge-answer.jpg`: 동일한 AIU 지식 질문을 Web·Slack에서 실행한 서비스 증거 화면
- `portfolio/assets/agent-admin-warm-transfer-evidence.png`: 실제 Warm Transfer의 대기열 진입·DTMF 수락·연결 성공·AI 브리핑을 보여주는 비식별 운영 증거 화면

## 저장소 구성

- `resume/product-engineer.md`: 현재 사실 기준(source-of-truth)으로 사용하는 이력서
- `docs/guides/`: 재사용 가능한 이력서 작성 가이드와 채용공고 검색 가이드
- `docs/plans/`: 문서 구조, 케이스 스터디, 저장소 문서화 관련 설계 및 구현 계획
- `resume/`: 최종 이력서 산출물
- `case-studies/`: 개별 프로젝트 기반 케이스 스터디 문서
- `portfolio/html/`: 직접 편집하는 포트폴리오 HTML 원본
- `portfolio/pdf/`: 제출과 공유에 사용하는 포트폴리오 PDF
- `portfolio/assets/`: 포트폴리오와 케이스 스터디에 사용하는 이미지와 시각 자료
- `portfolio/dist/`: Cloudflare Pages 배포 시 생성되는 사이트 결과물(Git 제외)
- `scripts/build_portfolio_pdf.py`: 현재 v4 HTML을 30쪽 16:9 벡터 PDF로 인쇄하고 페이지 크기·텍스트·외부 링크를 검증하는 빌드 스크립트
- `scripts/build_portfolio_site.sh`: v4 HTML과 공개에 필요한 이미지 5개만 `portfolio/dist/`에 모아 Cloudflare Pages 배포본을 만드는 빌드 스크립트
- `.agents/skills/`: 에이전트별 중복 없이 공통으로 사용하는 로컬 스킬 모음

## 추천 읽기 순서

1. `README.md`로 저장소 목적과 구조를 파악합니다.
2. `resume/product-engineer.md`로 사실 기반 경력 재료와 현재 정본 이력서를 함께 확인합니다.
3. `docs/guides/resume-guide.md`로 작성 원칙을 확인합니다.
4. 채용공고 탐색 작업이 필요할 때는 `docs/guides/job-search-protocol.md`를 확인합니다.
5. 필요할 때 현재 이력서 표현을 가이드 기준으로 다듬습니다.
6. `case-studies/outbound-voice-agent.md`, `case-studies/inbound-voice-agent.md`, `case-studies/hospital-customer-support-agent.md`에서 프로젝트 케이스 스터디 문서를 읽습니다.
7. 필요할 때만 `docs/plans/`에서 설계 의도와 작업 계획을 확인합니다.

## 포트폴리오 웹 배포

Cloudflare Pages는 GitHub의 `main` 브랜치와 연결한다. 빌드 명령은 `bash scripts/build_portfolio_site.sh`, 빌드 출력 디렉터리는 `portfolio/dist`를 사용한다. `main`에 새 커밋을 푸시하면 v4 포트폴리오가 자동으로 다시 배포된다.
