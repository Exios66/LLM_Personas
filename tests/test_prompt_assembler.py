"""Tests for litigation prompt assembly helpers."""

from __future__ import annotations

import pytest

from litigation.prompts.assembler import _parse_feasibility


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("F3", 3),
        ("f5", 5),
        (" F2 ", 2),
        ("invalid", 3),
        ("F", 3),
        ("F9", 9),
    ],
)
def test_parse_feasibility(raw: str, expected: int) -> None:
    assert _parse_feasibility(raw) == expected


def test_build_deliberation_prompts_includes_matter() -> None:
    from litigation.prompts.assembler import build_deliberation_prompts

    _, user_prompt = build_deliberation_prompts("Should we refactor the auth module?")
    assert "Should we refactor the auth module?" in user_prompt
    assert "**MATTER:**" in user_prompt


def test_build_deliberation_prompts_hearing_type_instructions() -> None:
    from litigation.prompts.assembler import build_deliberation_prompts

    _, standard = build_deliberation_prompts("matter", hearing_type="standard")
    _, expedited = build_deliberation_prompts("matter", hearing_type="expedited")
    _, contempt = build_deliberation_prompts("matter", hearing_type="contempt")

    assert "Standard Deliberation Flow" in standard
    assert "EXPEDITED format" in expedited
    assert "CONTEMPT HEARING" in contempt


def test_build_deliberation_prompts_excludes_spectators() -> None:
    from litigation.prompts.assembler import build_deliberation_prompts

    system_with, _ = build_deliberation_prompts("matter", include_spectators=True)
    system_without, _ = build_deliberation_prompts("matter", include_spectators=False)

    if "## Spectators (Optional Commentary)" in system_with:
        assert "## Spectators (Optional Commentary)" not in system_without
