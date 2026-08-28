from __future__ import annotations

import re
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PROJECT_ROOT / ".agents" / "skills"
CAREER_SKILLS = (
    "career-intake",
    "career-memory",
    "master-resume",
    "targeted-resume",
    "career-review",
)


def split_frontmatter(content: str) -> tuple[dict, str]:
    _, frontmatter, body = content.split("---", 2)
    return yaml.safe_load(frontmatter), body


def test_career_skills_have_valid_discovery_and_references() -> None:
    for skill_name in CAREER_SKILLS:
        skill_root = SKILLS_ROOT / skill_name
        skill_content = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        frontmatter, body = split_frontmatter(skill_content)
        interface = yaml.safe_load(
            (skill_root / "agents" / "openai.yaml").read_text(encoding="utf-8")
        )["interface"]

        assert frontmatter["name"] == skill_name
        assert len(frontmatter["description"]) >= 80
        assert f"${skill_name}" in interface["default_prompt"]
        assert 25 <= len(interface["short_description"]) <= 64
        assert "TODO" not in skill_content

        reference_paths = re.findall(r"\]\((references/[^)]+)\)", body)
        assert reference_paths
        for reference_path in reference_paths:
            assert (skill_root / reference_path).is_file()


def test_resume_templates_are_traceable_and_separate() -> None:
    master_template = (PROJECT_ROOT / "templates" / "resume" / "master.md").read_text(
        encoding="utf-8"
    )
    targeted_template = (
        PROJECT_ROOT / "templates" / "resume" / "tailored.md"
    ).read_text(encoding="utf-8")

    assert "claim_ids" in master_template
    assert "claim_ids" in targeted_template
    assert "resume/master.md" in targeted_template
    assert master_template != targeted_template
