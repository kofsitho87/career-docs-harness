# 송 희 웅

**연락처:** +821030982011 | [kofsitho@naver.com](mailto:kofsitho@naver.com)

소프트웨어 개발자로서 웹 개발 전문성을 바탕으로 최근에는 LLM과 AI 기술을 활용한 제품 개발에 깊은 관심과 열정을 가지고 있습니다.

Langchain, RAG, Langgraph, Livekit(Voice Agent) 등 최신 LLM 기술을 활용한 AI 서비스 개발 경험을 보유하고 있으며, 특히 Claude, GPT 등 다양한 LLM을 활용한 실제 프로덕션 경험을 통해 AI 기반 서비스의 설계와 구현 능력을 갖추고 있습니다.

풀스택 개발 경험을 토대로 AI 솔루션의 프론트엔드부터 백엔드까지 전반적인 아키텍처 설계와 구현이 가능합니다.

**경력:** 9년 7개월

---

## 경력

### 와이즈에이아이

**2025.03 - 재직중 (1년 1개월)** | 정규직 | AI 엔지니어 | 센터장

#### 병원 고객상담 Agent 개발 및 배포

**2025.03 - 2025.05**

의료기관(치과/병원) 고객 상담 자동화를 위한 AI 기반 대화형 에이전트 시스템 개발 및 AWS 클라우드 환경 배포, NextJS 기반 Agent 모니터링 웹 대시보드 구축

1. **LangGraph 기반 AI Agent 아키텍처 설계 및 개발**
  - 성과: Langgraph Agent 기반 대화 상태 관리 시스템 구축으로 95% 이상의 정확한 고객 상담 응답 달성
  - 역할: LangGraph를 활용한 에이전트 워크플로우 설계 및 구현
  - 기술: LangGraph Platform API(Redis, PostgreSQL), LLM: GPT/Claude, Python
2. **웹사이트 크롤링 및 데이터 추출 시스템 개발**
  - 성과: 웹사이트 텍스트를 6개 토픽으로 자동 분류 및 구조화된 데이터 추출 시스템 구현
  - 역할: TrustCall 기반 정보 추출 워크플로우 설계 및 대규모 텍스트 청킹 알고리즘 개발
  - 기여: 토픽별 구조화된 스키마 정의 및 결과 통합 로직 구현으로 90% 이상의 정보 추출 정확도 달성
  - 기술: Crawl4ai, LangGraph, Langchain-TrustCall, Pydantic
3. **FastAPI 기반 REST API 서버 개발**
  - 성과: 비동기 처리를 통한 동시 요청 처리 성능 개선 및 실시간 스트리밍 응답 구현
  - 역할: FastAPI 서버 아키텍처 설계 및 LangGraph SDK 통합
  - 기여:
    - Agent 대화 API, 정보 추출 API, 배치 처리 API 개발
    - 스레드 기반 대화 세션 관리 시스템 구현
    - API 응답 속도 70% 개선 (비동기 처리 도입)
  - 기술: FastAPI, LangGraph SDK, Uvicorn, Pydantic
4. **벡터 데이터베이스 및 검색 시스템 구축**
  - 성과: Qdrant 벡터 DB를 활용한 하이브리드(키워드 + 의미 기반 검색 시스템) 구축으로 관련 정보 검색 정확도 향상
  - 역할: 벡터 임베딩 파이프라인 설계 및 검색 최적화
  - 기여: 주제별 필터링 및 키워드 검색 기능 구현
  - 기술: Qdrant Vector DB, OpenAI Embeddings, gRPC
5. **AWS 클라우드 인프라 설계 및 CI/CD 구축**
  - 성과: Blue/Green 배포를 통한 무중단 서비스 구현 및 99.9% 가용성 달성
  - 역할: AWS ECS Fargate 기반 마이크로서비스 아키텍처 설계 및 구축
  - 기여:
    - ECS Cluster, ALB, VPC, Security Group 설정
    - GitHub Actions 기반 CI/CD 파이프라인 구축
    - 개발/운영 환경 분리 및 자동 배포 시스템 구현
  - 기술: AWS ECS Fargate, ALB, VPC, ECR, GitHub Actions, Docker, Terraform

**사용 기술 스택**

- Backend: Python, FastAPI, LangGraph, Crawl4ai
- Frontend: Nextjs15(App router), shadcnUI, Copilotkit, tanstack-query, langchain/langgraph-sdk
- AI: GPT-4.1, Claude, OpenAI Embeddings, TrustCall, LangSmith
- Database: Qdrant Vector DB, PostgreSQL, Redis
- Infrastructure: AWS ECS Fargate, ALB, VPC, ECR, CloudWatch
- DevOps: Docker, GitHub Actions, Terraform, Blue/Green Deployment
- Monitoring: LangSmith Tracing, CloudWatch Logs

---

### 투썬월드

**2019.03 - 2025.02 (6년)** | 정규직

#### 프로젝트명: 공맵 - 공부의 길을 이어주는 멘토링 플랫폼

**2023.04 - 2023.08**

- 웹사이트: [https://gongmap.com](https://gongmap.com)
- 프로젝트 개요:
  - 해외 교육 과정(SAT, IB, AP, A-Level) 준비생을 위한 온라인 멘토링 서비스
  - 교과 과목 멘토링, 에세이 첨삭, 입시 컨설팅 제공
  - 진학 희망 대학 선배와의 직접 멘토링 연결 서비스
- 담당 업무 및 기여:
  - 플랫폼 기획 및 설계: UI/UX 중심의 서비스 구조 설계
  - 멘토링 매칭 알고리즘 개발: 학습 요구사항과 멘토 전문성 기반 매칭 시스템 구현
  - 입시 정보 및 리소스 제공: 최신 입시 정보, 대학 리소스, 에세이 작성 가이드 등 통합 제공
- 개발 환경:
  - 프론트엔드: TypeScript
  - 디자인 시스템: Vuetify, Material Design System
  - 데이터 관리: @tanstack/vue-query, Pinia, Vuex
  - 데이터베이스: MongoDB
  - 클라우드 서비스: AWS

#### RAG 비자 챗봇 시스템 개발

**2024.02 - 2024.04**

- 비자문서 마크다운 포맷으로 전처리
- 벡터데이터베이스 구축
- hybrid search(keyword + semantic)
- BM25 알고리즘 기반 키워드 검색과 임베딩 기반 시맨틱 검색을 결합한 하이브리드 검색 아키텍처 구축
- 검색 정확도 향상을 위한 다단계 검색 파이프라인 구현
  1. 키워드 검색으로 1차 후보군 추출 (Recall 최적화)
  2. 시맨틱 검색으로 연관성 높은 문서 식별 (Precision 최적화)
  3. Cross-encoder 기반 Reranker로 최종 순위 결정
- 검색 성능 최적화
  - 문서 전처리 및 인덱싱 전략 수립
  - 문서 청킹 크기와 오버랩 최적화 (chunk size: 512, overlap: 50)
  - 메타데이터 추출 및 인덱싱으로 검색 필터링 강화
- 검색 속도 개선
  - 벡터 인덱스 ANN(Approximate Nearest Neighbor) 알고리즘 튜닝
  - 캐싱 레이어 도입으로 자주 사용되는 쿼리 응답 시간 80% 단축
- 검색 품질 관리 시스템 구현
  - 사용자 피드백 기반 검색 결과 평가 시스템 구축
  - Langsmith을 활용한 검색 결과 트레이싱 및 모니터링
  - A/B 테스트를 통한 검색 파라미터 최적화
  - BM25와 시맨틱 검색 가중치 조정
  - 임계값(threshold) 설정으로 검색 정확도 향상

#### 크롤링 & 데이터 수집 및 처리

**2024.06 - 2024.07**

- 주요 업무 및 담당 역할:
  - 크롤링 및 수집된 데이터에 대한 전처리, 분류, 검증, 번역 시스템 개발
  - 로깅/모니터링 시스템 개발
- 비동기 처리 도입으로 크롤링 속도 300% 향상
- 데이터 검증 파이프라인 구축으로 데이터 정확도 95% 이상 달성
- 확장 가능한 마이크로서비스 아키텍처 설계 및 구현
  - 컴포넌트 기반 모듈러 아키텍처 구축
  - 책임 분리를 통한 유지보수성 향상
  - 의존성 주입을 통한 느슨한 결합도 구현
- 대규모 데이터 수집 파이프라인 개발
  - 비동기 처리 기반의 고성능 크롤링 시스템 구축
  - 멀티스레딩을 활용한 병렬 처리 구현
  - 실시간 데이터 스트리밍 처리
- 데이터 품질 관리 시스템 구축
  - 다국어 번역 및 데이터 검증 파이프라인 구현
  - 데이터 정합성 검증 자동화
- 블랙리스트 필터링 시스템 개발
- 실시간 모니터링 및 로깅 시스템 구현
  - JSONL 기반 구조화된 로깅 시스템 구축
  - Slack/Email 기반 실시간 알림 시스템 개발
  - 성능 메트릭 수집 및 분석 대시보드 구현
- 데이터 처리 자동화 시스템 개발
  - 문서 전처리 및 정규화
  - 메타데이터 추출 및 인덱싱
  - 데이터 중복 제거 및 병합
  - 자동 카테고리 분류 시스템

#### AI 면접 데모개발 및 AI 이력서 기반 자기소개서 첨삭 기능개발

**2024.11 - 2024.11**

- 주요 업무 및 담당 역할:
  - 음성을 통해서 선택한 직군에 맞춘 AI 면접진행 PoC 개발
  - 자신의 이력서를 업로드하여 AI로 자기소개서 첨삭해주는 서비스
  - AI 서비스 개발을 통해 서비스의 경쟁력 향상
- Openai realtime api / Livekit Agent
- 면접 진행한 대화내용을 기반으로 점수평가 crewai

#### 백오피스 애플리케이션 개발

**2024.09 - 2024.11**

- 주요 업무 및 담당 역할:
  - Next.js 15 기반의 백오피스 웹 애플리케이션 구축
  - 다국어 채용 공고 관리 시스템 개발
  - AI 기반 자동 번역 시스템 구현 (Claude 3 Sonnet 모델 활용)

#### 한국어 교육 플랫폼 개발

**2023.09 - 2024.01**

- 주요 업무 및 담당 역할:
  - 웹 페이지 UI 개발: Tailwindcss와 shadcnUI를 활용한 모던하고 반응형 디자인 구현
  - API 연동 개발: RESTful API를 활용한 강의 콘텐츠 제공 및 사용자 진행 상황 추적 기능 구현
  - 한국어 콘텐츠를 위한 프롬프트 R&D: OpenAI, Gemini 등 AI 기술을 활용한 맞춤형 학습 콘텐츠 생성
- 개발 환경:
  - 프론트엔드: NextJS 14(App Router), ReactJS, TypeScript
  - 디자인 시스템: Tailwindcss, shadcnUI
  - 데이터 관리: @tanstack/react-query, @tanstack/react-table
- 프로젝트 진행 인원: 15명
- 주요 성과:
  - 페이지 로딩 속도 40% 개선 (Lighthouse 성능 점수 65점 → 91점)
  - 회사 내부 사정으로 프로젝트 중단

---

### 투미유

**2017.10 - 2018.12 (1년 3개월)** | 정규직

#### IOS 앱 개발 / 백엔드 개발

**2017.10 - 2018.12**

- 앱스토어 링크: [투덥 - 영어회화 더빙 스피킹 쉐도잉]
- 웹사이트: [https://www.2meu.me](https://www.2meu.me)
- 개발 환경 및 사용 기술:
  - 버전 관리 및 배포: Bitbucket, AWS (EC2, ELB, CloudFront, S3, RDS), Docker
  - 서버 및 프레임워크: Ubuntu, Nginx, PHP 7.2, Laravel 5.6
  - 기술 스택: Firebase, Docker, Git, Redis, NodeJS, Swift 4.0, FFmpeg

---

### 예스콜닷컴

**2014.12 - 2016.02 (1년 3개월)** | 정규직

#### 반응형 웹 기술 기반의 홈페이지 및 쇼핑몰 제작 플랫폼

**2014.12 - 2016.02**

- 주요 업무:
  - 프론트엔드 및 백엔드 개발 전담
  - 반응형 웹 빌더 "DUBUPLUS" 개발
  - 쇼핑몰 결제 시스템 및 관리자 모듈 개발
  - 검색엔진 최적화(SEO) 및 소셜미디어 통합 기능 구현
- 개발 환경:
  - 백엔드: PHP 5.3, 자체 프레임워크, MySQL
  - 프론트엔드: JavaScript, jQuery, AngularJS 1, HTML

---

## 학력

**대진대학교**

- 2006.03 - 2013.08 | 졸업 | 철학과

---

## 스킬

Git | JavaScript | Python | MySQL | GitHub | Docker | TypeScript | Next.js | React.js | React | Node.js | HTML

---

## 수상/자격증/기타

### 지피터스 Llama index로 나만의 AI 프로덕트 만들기

**2024.10** | 기타

- Livekit agent를 통해서 나만의 영어선생님 만들기
- [사례발표1](https://www.gpters.org/chatbot/post/ai-roleplaying-conversation-application-qnoe9TQDzZv9lQM)
- [사례발표2](https://www.gpters.org/chatbot/post/ai-roleplaying-conversation-application-iF1DFPjzxXdvSlm)

### 메타코드 데이터분석가 과정

**2024.09** | 기타

- 탐색적 데이터분석 EDA
- 로우데이터에서 통계데이터 추출, SQL or Python -pandas
- 데이터시각화: 구글 루커스튜디오

### 해외연수프로그램 - 중소기업청이노비즈

**2014.02** | 기타

- 독일, 오스트리아, 체코의 우수기업 및 기관 방문

### 웹접근성(KWAG2.0)가이드라인을 준수한 사이트 웹접근성 강화프로젝트

**2013.08** | 기타

- 접근성(KWAG2.0)가이드라인을 준수한 사이트 웹접근성 강화프로젝트
- 접근성 위해한 부분 찾고 접근성에 맞춘 코딩하기
- 자바스크립트, 제이쿼리로 인터랙티브 웹 만들기

### TeddyNote LangChain-OpenTutorial 오픈소스 프로젝트 참여

**2025.02** | 기타

- [https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial)
- Langchain 튜토리얼 오픈소스 프로젝트에 참여해, Core Contributor로 등록됨.

---

## 언어

- **영어:** 일상 회화

---

## 링크

- **Github:** [https://github.com/kofsitho87](https://github.com/kofsitho87)
- **Medium Tech Blog:** [https://medium.com/@kofsitho](https://medium.com/@kofsitho)
- **LinkedIn:** [https://www.linkedin.com/in/kofsitho](https://www.linkedin.com/in/kofsitho)

