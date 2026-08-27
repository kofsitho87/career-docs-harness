from __future__ import annotations

from scripts.lib.memory_merge import merge_collection, merge_record


def fact(**overrides):
    base = {
        "id": "experience-example",
        "company": "Example",
        "role": "Engineer",
        "status": "inferred",
        "source_refs": ["source-resume-aaaaaaaaaaaa"],
        "user_edited": False,
        "last_updated": None,
    }
    base.update(overrides)
    return base


def test_compatible_merge_combines_sources_and_status() -> None:
    merged, conflicts, changes = merge_record(
        fact(),
        fact(
            status="verified",
            source_refs=["source-linkedin-bbbbbbbbbbbb"],
        ),
    )

    assert conflicts == []
    assert changes == []
    assert merged["status"] == "verified"
    assert merged["source_refs"] == [
        "source-resume-aaaaaaaaaaaa",
        "source-linkedin-bbbbbbbbbbbb",
    ]


def test_conflicting_automatic_value_is_preserved_as_open_conflict() -> None:
    merged, conflicts, changes = merge_record(
        fact(role="Backend Engineer"), fact(role="AI Engineer")
    )

    assert merged["role"] == "Backend Engineer"
    assert merged["status"] == "conflicted"
    assert conflicts[0]["status"] == "open"
    assert conflicts[0]["field"] == "role"
    assert "conflict recorded" in changes[0]


def test_incoming_user_value_wins_and_resolves_conflict() -> None:
    merged, conflicts, _ = merge_record(
        fact(role="Backend Engineer"),
        fact(
            role="AI Product Engineer",
            user_edited=True,
            status="verified",
            source_refs=["source-interview-cccccccccccc"],
        ),
    )

    assert merged["role"] == "AI Product Engineer"
    assert merged["user_edited"] is True
    assert conflicts[0]["status"] == "resolved"
    assert conflicts[0]["resolution"] == "incoming_user_value_applied"


def test_collection_adds_new_records_and_sorts_by_id() -> None:
    existing = [fact(id="experience-z")]
    incoming = [fact(id="experience-a", company="Another")]

    merged, conflicts, changes = merge_collection(existing, incoming)

    assert [record["id"] for record in merged] == ["experience-a", "experience-z"]
    assert conflicts == []
    assert changes == ["experience-a: added"]
