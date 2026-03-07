#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai",
#   "python-dotenv",
# ]
# ///

"""
Gemini 이미지 생성 API를 호출하여 이미지를 생성하고 저장한다.

사용법:
  uv run generate_image.py --prompt "..." --name "my-image" --output ./output
  uv run generate_image.py --prompt "..." --name "my-image" --aspect 9:16
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

# ── 상수 ──────────────────────────────────────────────────────────────────────

DEFAULT_MODEL = "gemini-3-pro-image-preview"

ASPECT_RATIO_MAP = {
    "16:9": "wide landscape 16:9 aspect ratio",
    "9:16": "tall portrait 9:16 aspect ratio",
    "1:1": "square 1:1 aspect ratio",
    "4:3": "landscape 4:3 aspect ratio",
    "3:4": "portrait 3:4 aspect ratio",
}


# ── Gemini API 호출 ───────────────────────────────────────────────────────────

def generate_image(api_key: str, prompt: str, aspect: str, model: str) -> bytes:
    """Gemini 이미지 생성 API를 호출하고 이미지 바이트를 반환한다."""
    client = genai.Client(api_key=api_key)

    aspect_hint = ASPECT_RATIO_MAP.get(aspect, ASPECT_RATIO_MAP["16:9"])
    full_prompt = f"{prompt}\n\nImage format: {aspect_hint}."

    try:
        response = client.models.generate_content(
            model=model,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )
    except Exception as e:
        print(f"Gemini API error: {e}", file=sys.stderr)
        raise SystemExit(1) from e

    for part in response.candidates[0].content.parts:
        if getattr(part, "inline_data", None):
            return part.inline_data.data

    print("No image data in response.", file=sys.stderr)
    if hasattr(response, "text"):
        print(f"Response text: {response.text}", file=sys.stderr)
    raise SystemExit(1)


# ── 메인 ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gemini API로 이미지를 생성합니다."
    )
    parser.add_argument(
        "--prompt", required=True,
        help="이미지 생성 프롬프트",
    )
    parser.add_argument(
        "--name", required=True,
        help="저장할 파일명 (확장자 제외). 예: my-diagram",
    )
    parser.add_argument(
        "--output", default=".",
        help="저장 폴더 경로 (기본: 현재 디렉토리)",
    )
    parser.add_argument(
        "--aspect", default="16:9",
        choices=list(ASPECT_RATIO_MAP.keys()),
        help="이미지 비율 (기본: 16:9)",
    )
    args = parser.parse_args()

    # .env 로드
    load_dotenv(dotenv_path=Path(__file__).parent / ".env")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(
            "GEMINI_API_KEY is not set.\n"
            "Add GEMINI_API_KEY=your-key to skills/image_generation/scripts/.env",
            file=sys.stderr,
        )
        raise SystemExit(1)

    # 파일명 생성
    safe_name = args.name.replace(" ", "-")
    filename = f"{safe_name}.png"
    save_path = Path(args.output) / filename

    print(f"Generating image...")
    print(f"  Model  : {DEFAULT_MODEL}")
    print(f"  Aspect : {args.aspect}")
    print(f"  Output : {save_path}")

    image_bytes = generate_image(api_key, args.prompt, args.aspect, DEFAULT_MODEL)

    save_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.write_bytes(image_bytes)

    print(f"Image saved: {save_path}")


if __name__ == "__main__":
    main()
