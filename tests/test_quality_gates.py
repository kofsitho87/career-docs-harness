from __future__ import annotations

import tempfile
from pathlib import Path

import yaml

from scripts.lib.scan_sensitive_info import scan_sensitive_info
from scripts.lib.validate_assets import validate_assets
from scripts.lib.validate_claims import validate_claims
from scripts.lib.validate_links import validate_links


def test_claim_gate_rejects_unknown_and_non_public_claims() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        root = Path(temporary_directory)
        output = root / "resume.md"
        output.write_text("성과\n<!-- claims: claim-known, claim-missing -->\n", encoding="utf-8")
        memory = root / "claims.yaml"
        memory.write_text(
            yaml.safe_dump(
                {
                    "version": 1,
                    "claims": [
                        {
                            "id": "claim-known",
                            "status": "verified",
                            "source_refs": ["source-example"],
                            "visibility": "restricted",
                        }
                    ],
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )

        errors = validate_claims([output], memory)

        assert any("unknown claim ID claim-missing" in error for error in errors)
        assert any("claim-known is not public" in error for error in errors)


def test_link_asset_and_sensitive_gates() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        root = Path(temporary_directory)
        document = root / "output.md"
        document.write_text(
            "[missing](missing.md)\n![evidence](missing.png)\ncontact@example.com\n",
            encoding="utf-8",
        )
        allowlist = root / "allowlist.yaml"
        allowlist.write_text("version: 1\nemails: []\nphones: []\nurls: []\n", encoding="utf-8")

        assert validate_links([document])
        assert validate_assets([document])
        assert scan_sensitive_info([document], allowlist) == [
            f"{document}: email is not allowlisted: contact@example.com"
        ]
