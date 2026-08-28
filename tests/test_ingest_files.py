from __future__ import annotations

import hashlib
import tempfile
from pathlib import Path

import pytest
import yaml
from docx import Document
from pypdf import PdfWriter

from scripts.lib.ingest_files import IngestionError, ingest_file


def create_repository(root: Path) -> tuple[Path, Path, Path]:
    sources_root = root / "sources"
    files_root = sources_root / "files"
    extracted_root = sources_root / "extracted"
    files_root.mkdir(parents=True)
    extracted_root.mkdir(parents=True)
    manifest_path = sources_root / "manifest.yaml"
    manifest_path.write_text("version: 1\nsources: []\n", encoding="utf-8")
    return files_root, extracted_root, manifest_path


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_ingest_markdown_preserves_source_and_deduplicates() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        files_root, extracted_root, manifest_path = create_repository(repository_root)
        source_path = files_root / "profile.md"
        source_path.write_text("# 홍길동\n\nAI Engineer\n", encoding="utf-8")
        original_hash = file_hash(source_path)

        first_entry, first_created = ingest_file(
            source_path,
            repository_root=repository_root,
            sources_root=repository_root / "sources",
            manifest_path=manifest_path,
            extracted_root=extracted_root,
        )
        second_entry, second_created = ingest_file(
            source_path,
            repository_root=repository_root,
            sources_root=repository_root / "sources",
            manifest_path=manifest_path,
            extracted_root=extracted_root,
        )

        assert first_created is True
        assert second_created is False
        assert first_entry == second_entry
        assert file_hash(source_path) == original_hash
        extracted_path = repository_root / first_entry["extracted_text_path"]
        assert "AI Engineer" in extracted_path.read_text(encoding="utf-8")
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        assert len(manifest["sources"]) == 1


def test_ingest_html_docx_and_pdf() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        files_root, extracted_root, manifest_path = create_repository(repository_root)

        html_path = files_root / "profile.html"
        html_path.write_text(
            "<html><head><title>Profile</title></head><body><h1>Engineer</h1></body></html>",
            encoding="utf-8",
        )

        docx_path = files_root / "career.docx"
        document = Document()
        document.add_paragraph("Voice AI 프로젝트")
        document.save(docx_path)

        pdf_path = files_root / "resume.pdf"
        writer = PdfWriter()
        writer.add_blank_page(width=612, height=792)
        with pdf_path.open("wb") as stream:
            writer.write(stream)

        entries = []
        for source_path in (html_path, docx_path, pdf_path):
            entry, created = ingest_file(
                source_path,
                repository_root=repository_root,
                sources_root=repository_root / "sources",
                manifest_path=manifest_path,
                extracted_root=extracted_root,
            )
            assert created is True
            entries.append(entry)

        assert [entry["type"] for entry in entries] == ["html", "docx", "pdf"]
        assert entries[0]["metadata"]["title"] == "Profile"
        assert entries[1]["metadata"]["paragraphs"] == 1
        assert entries[2]["metadata"]["pages"] == 1


def test_ingest_rejects_files_outside_sources() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        repository_root = Path(temporary_directory)
        _, extracted_root, manifest_path = create_repository(repository_root)
        outside_path = repository_root / "outside.md"
        outside_path.write_text("outside", encoding="utf-8")

        with pytest.raises(IngestionError, match="inside"):
            ingest_file(
                outside_path,
                repository_root=repository_root,
                sources_root=repository_root / "sources",
                manifest_path=manifest_path,
                extracted_root=extracted_root,
            )
