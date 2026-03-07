---
name: image-generation
description: 사용자의 요청을 이미지로 생성하는 범용 스킬. "이미지 만들어줘", "그림 생성", "시각화", "다이어그램", "목업" 등 이미지 생성 의도가 감지되면 호출한다.
allowed-tools: Bash, Read, AskUserQuestion
argument-hint: "[생성할 이미지에 대한 설명]"
---

# 이미지 생성 (Image Generation)

사용자의 의도를 파악하고 프롬프트를 정제하여 Gemini API로 이미지를 생성한다.

사용자 요청: `$ARGUMENTS`

---

## Step 1: 사용자 의도 파악

사용자의 요청에서 다음을 파악한다:

- **무엇을** 그리려는가 (주제, 대상)
- **어떤 스타일**인가 (다이어그램, 일러스트, 사진풍, 와이어프레임 등)
- **어떤 용도**인가 (문서 삽입, 발표자료, SNS 등)
- **특별한 요구사항** (색상, 분위기, 텍스트 포함 여부 등)

정보가 부족하면 `AskUserQuestion`으로 한 가지만 확인한다. 과도한 질문은 하지 않는다.

---

## Step 2: 프롬프트 정제

사용자의 의도를 바탕으로 Gemini에 전달할 영문 프롬프트를 구성한다.

**프롬프트 정제 규칙:**

1. **구체적으로 서술**: 모호한 표현을 구체적 시각 묘사로 변환
2. **스타일 명시**: flat design, wireframe, photorealistic, watercolor 등
3. **레이아웃 명시**: 구성 요소의 배치, 크기 관계, 계층 구조
4. **색상/분위기**: 컬러 팔레트 또는 분위기 지정
5. **텍스트 처리**: 이미지에 포함할 텍스트가 있으면 명확히 지정 (한국어 텍스트는 "Korean text labels" 명시)
6. **불필요 요소 제외**: "no shadows, no gradients" 등 네거티브 프롬프트

**정제 예시:**

| 사용자 요청 | 정제된 프롬프트 |
|------------|---------------|
| "로그인 화면 목업 그려줘" | "Clean wireframe mockup of a login page. Email and password input fields, 'Login' button, 'Forgot password?' link, social login buttons. Minimal grayscale design, white background, clear component boundaries." |
| "마이크로서비스 아키텍처 다이어그램" | "Professional architecture diagram showing microservices. API Gateway at top, 3 service boxes (Auth, Order, Payment) in middle, shared database and message queue at bottom. Clean flat design, blue and gray color scheme, labeled arrows showing data flow." |
| "귀여운 고양이 일러스트" | "Cute cartoon cat illustration, sitting pose, big round eyes, soft pastel colors, minimal flat style, white background." |

---

## Step 3: 비율 결정

용도에 맞는 비율을 선택한다:

| 용도 | 비율 |
|------|------|
| 문서 삽입, 발표자료, 다이어그램 | 16:9 (기본값) |
| 모바일 화면, 스토리, 세로 목업 | 9:16 |
| 프로필, 아이콘, 정사각형 | 1:1 |
| 일반 사진, 블로그 이미지 | 4:3 |
| 세로 포스터, 인쇄물 | 3:4 |

---

## Step 4: 저장 위치 및 파일명 결정

- **파일명**: 사용자 요청 내용을 요약한 짧은 영문 kebab-case (예: `login-mockup`, `microservice-architecture`)
- **저장 위치**: 프로젝트 상황에 맞게 결정
  - 기본: 현재 작업 디렉토리
  - 문서 보완용: 해당 문서와 가까운 `assets/` 폴더
  - 사용자 지정 경로가 있으면 그대로 사용

---

## Step 5: 스크립트 실행

사전 조건: `skills/image_generation/scripts/.env`에 `GEMINI_API_KEY` 설정

```bash
uv run skills/image_generation/scripts/generate_image.py \
  --prompt "[정제된 영문 프롬프트]" \
  --name "[파일명]" \
  --output "[저장 폴더]" \
  --aspect [비율]
```

---

## Step 6: 결과 확인

1. 생성된 이미지 파일 경로를 사용자에게 알려준다
2. Read 도구로 이미지를 읽어 사용자에게 보여준다
3. `AskUserQuestion`으로 다음 단계를 확인한다:
   - "이대로 사용"
   - "프롬프트 수정 후 재생성"
   - "비율/스타일 변경 후 재생성"

재생성 요청 시 Step 2로 돌아가 프롬프트를 수정하고 다시 실행한다.

---

## 완성 체크리스트

- [ ] 사용자 의도를 정확히 파악했는가?
- [ ] 프롬프트가 구체적이고 명확한가?
- [ ] 적절한 비율을 선택했는가?
- [ ] 이미지가 정상 생성되었는가?
- [ ] 사용자에게 결과를 보여주고 확인을 받았는가?
