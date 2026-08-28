from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import setup_agents


class SetupAgentsTest(unittest.TestCase):
    def create_repository(self, root: Path) -> None:
        (root / "AGENTS.md").write_text("# Canonical\n", encoding="utf-8")
        (root / "harness.yaml").write_text("version: 0.1\n", encoding="utf-8")
        (root / ".agents" / "skills").mkdir(parents=True)

    def test_write_and_check_adapters(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository_root = Path(temporary_directory)
            self.create_repository(repository_root)

            setup_agents.write_adapters(repository_root)

            self.assertEqual(setup_agents.check_adapters(repository_root), [])
            self.assertEqual(
                (repository_root / "CLAUDE.md").read_text(encoding="utf-8"),
                setup_agents.CLAUDE_ADAPTER,
            )
            self.assertEqual(
                (
                    repository_root / ".cursor" / "rules" / "career-harness.mdc"
                ).read_text(encoding="utf-8"),
                setup_agents.CURSOR_ADAPTER,
            )

    def test_check_detects_adapter_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository_root = Path(temporary_directory)
            self.create_repository(repository_root)
            setup_agents.write_adapters(repository_root)
            (repository_root / "CLAUDE.md").write_text(
                "duplicated instructions\n", encoding="utf-8"
            )

            self.assertIn(
                "adapter drift: CLAUDE.md",
                setup_agents.check_adapters(repository_root),
            )

    def test_check_requires_canonical_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository_root = Path(temporary_directory)

            errors = setup_agents.check_adapters(repository_root)

            self.assertIn("missing canonical path: AGENTS.md", errors)
            self.assertIn("missing canonical path: harness.yaml", errors)
            self.assertIn("missing canonical path: .agents/skills", errors)


if __name__ == "__main__":
    unittest.main()
