"""YAML and JSON Schema loading and validation helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_ROOT = REPOSITORY_ROOT / "schemas"


class SchemaValidationError(ValueError):
    """Raised when a document does not match its schema."""


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def write_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(data, stream, allow_unicode=True, sort_keys=False)


def load_schema(schema_name: str, schema_root: Path = SCHEMA_ROOT) -> dict[str, Any]:
    schema_path = schema_root / schema_name
    with schema_path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def validate_data(data: Any, schema: dict[str, Any], label: str = "document") -> None:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
    if not errors:
        return

    messages = []
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        messages.append(f"{label}:{location}: {error.message}")
    raise SchemaValidationError("\n".join(messages))


def validate_yaml_file(
    document_path: Path,
    schema_name: str,
    schema_root: Path = SCHEMA_ROOT,
) -> None:
    validate_data(
        load_yaml(document_path),
        load_schema(schema_name, schema_root),
        str(document_path),
    )
