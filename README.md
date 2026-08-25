# 이력서·포트폴리오 제작 워크스페이스

이 저장소는 이력서와 포트폴리오를 작성, 정리, 개선하기 위한 작업 공간입니다. 사실 기준 문서, 작성 가이드, 설계/계획 문서, 현재 산출물을 함께 두고 문서 제작 흐름을 관리합니다.

## 프로젝트 요약

- 목적: 이력서와 포트폴리오를 일관된 기준으로 제작하고 업데이트하기
- 성격: 최종 결과물만 모아둔 폴더가 아니라, 작성 근거와 중간 계획까지 함께 관리하는 문서 작업 저장소
- 구성: 사실 기준 문서, 작성 가이드, 계획 문서, 최종 산출물, 일부 로컬 보조 스킬이 함께 존재

## 현재 산출물

- `resume/product-engineer.md`: 현재 정본이자 사실 기준으로 사용하는 제품 엔지니어 이력서
- `resume/cupix-ax-operations-engineer.md`: 큐픽스 AX Operations Engineer 지원용 맞춤 이력서
- `portfolio/heewung-song-portfolio.html`: 반복 운영 업무를 프로덕션 AI 시스템으로 바꿔 온 커리어를 중심으로, 병원 Voice AI·고객상담·통화 지표 자동화·사내 업무지원 Multi-Agent(AIU)를 연결한 슬라이드형 종합 포트폴리오
- `portfolio/heewung-song-portfolio-v2.html`: 같은 28장 서사를 유지한 채 시각 위계(Chapter → Problem → System boundary → Evidence → My Role)와 슬라이드별 다이어그램 언어를 재설계한 개선 버전
- `portfolio/cupix-ax-aiu-case-study.html`: 큐픽스 지원용 AIU AX 인터랙티브 시각 사례 — AIU 프로젝트 1건을 깊게 파고드는 단일 프로젝트 딥다이브
- `portfolio/cupix-ax-career-story.html`: 큐픽스 지원용 커리어 저니 내러티브 — 아웃바운드·인바운드·고객상담·통화 지표 자동화·AIU까지 다섯 프로젝트가 하나의 반복 업무 자동화 패턴으로 이어지는 과정을 보여주는 스토리텔링형 페이지. `cupix-ax-aiu-case-study.html`을 대체하지 않고, 그 산출물이 어떤 경력 위에서 나왔는지 보여주는 동반 문서로 존재한다.
- `output/pdf/heewung-song-ai-product-engineer-portfolio.pdf`: 종합 포트폴리오 28장을 16:9 페이지로 변환한 원티드 업로드용 PDF
- `output/pdf/cupix-ax-aiu-case-study.pdf`: 큐픽스 지원용 AIU AX 1페이지 PDF 부록
- `case-studies/outbound-voice-agent.md`: 아웃바운드 Voice AI Agent 케이스 스터디
- `case-studies/inbound-voice-agent.md`: 인바운드 Voice AI Agent 케이스 스터디
- `case-studies/hospital-customer-support-agent.md`: 병원 고객상담 AI Agent 케이스 스터디
- `assets/heewung-song-infographic.png`: 이력서와 함께 쓰는 시각 자료 자산
- `assets/hospital-customer-support-agent-ppt-overview.png`: 병원 고객상담 AI Agent 개요·아키텍처 슬라이드 이미지
- `assets/hospital-customer-support-agent-ppt-flow.png`: 병원 고객상담 AI Agent 흐름·설계 의사결정 슬라이드 이미지
- `assets/customer-support-chat-step1.png`, `assets/customer-support-chat-complete.png`: 공개 개발 서비스에서 검증한 정보 응답·개인정보 수집·상담 신청 흐름 캡처
- `assets/cupix-ax-operations-screen.png`, `assets/cupix-ax-analytics-screen.png`: Agent Admin 매뉴얼의 인바운드 운영 현황·통화 분석 v2 화면
- `assets/aiu-web-knowledge-answer.png`, `assets/aiu-slack-knowledge-answer.jpg`: 동일한 AIU 지식 질문을 Web·Slack에서 실행한 서비스 증거 화면

## 저장소 구성

- `resume/product-engineer.md`: 현재 사실 기준(source-of-truth)으로 사용하는 이력서
- `docs/guides/`: 재사용 가능한 이력서 작성 가이드와 채용공고 검색 가이드
- `docs/plans/`: 문서 구조, 케이스 스터디, 저장소 문서화 관련 설계 및 구현 계획
- `resume/`: 최종 이력서 산출물
- `case-studies/`: 개별 프로젝트 기반 케이스 스터디 문서
- `assets/`: 이미지와 시각 자료 자산
- `scripts/build_portfolio_pdf.py`: 1920×1080 슬라이드 캡처를 16:9 PDF로 묶고 마지막 페이지 연락처 링크를 검증하는 빌드 스크립트
- `.codex/skills/image-generation/`: 공유 Gemini 스크립트를 재사용하는 Codex 호환 로컬 이미지 생성 스킬
- `.claude/skills/image_generation/`: 이미지 자산 제작에 쓰는 로컬 스킬과 스크립트

## 추천 읽기 순서

1. `README.md`로 저장소 목적과 구조를 파악합니다.
2. `resume/product-engineer.md`로 사실 기반 경력 재료와 현재 정본 이력서를 함께 확인합니다.
3. `docs/guides/resume-guide.md`로 작성 원칙을 확인합니다.
4. 채용공고 탐색 작업이 필요할 때는 `docs/guides/job-search-protocol.md`를 확인합니다.
5. 필요할 때 현재 이력서 표현을 가이드 기준으로 다듬습니다.
6. `case-studies/outbound-voice-agent.md`, `case-studies/inbound-voice-agent.md`, `case-studies/hospital-customer-support-agent.md`에서 프로젝트 케이스 스터디 문서를 읽습니다.
7. 필요할 때만 `docs/plans/`에서 설계 의도와 작업 계획을 확인합니다.
