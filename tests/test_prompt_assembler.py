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

    _, user_prompt = build_deliberation_prompts("Should we refactor the parser?", feasibility="F3")
    assert "Should we refactor the parser?" in user_prompt
    assert "**Feasibility:** F3" in user_prompt


@pytest.mark.parametrize("hearing_type", ["expedited", "special_inquiry", "contempt"])
def test_build_deliberation_prompts_hearing_types(hearing_type: str) -> None:
    from litigation.prompts.assembler import build_deliberation_prompts

    system_prompt, user_prompt = build_deliberation_prompts(
        "Hearing type matter",
        hearing_type=hearing_type,
    )
    assert "Hearing type matter" in user_prompt
    assert len(system_prompt) > 100


def test_build_deliberation_prompts_excludes_spectators_when_disabled() -> None:
    from litigation.prompts.assembler import build_deliberation_prompts

    with_spectators, _ = build_deliberation_prompts("Matter", include_spectators=True)
    without_spectators, _ = build_deliberation_prompts("Matter", include_spectators=False)

    assert "## Spectators (Optional Commentary)" in with_spectators
    assert "## Spectators (Optional Commentary)" not in without_spectators
