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
