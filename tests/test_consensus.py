"""Regression tests for executive consensus quorum and commit guards."""

from __future__ import annotations

import pytest

from executive.consensus import Consensus


def test_quorum_commit_happy_path(tmp_path) -> None:
    c = Consensus(quorum_n=2, total_m=3, base_dir=tmp_path / "consensus")
    c.propose("p1", "deploy change")
    c.vote("p1", "voter-a", "yes")
    c.vote("p1", "voter-b", "yes")

    assert c.check_quorum("p1") is True
    record = c.commit("p1")
    assert record["proposal_id"] == "p1"
    assert c.get_proposal("p1")["status"] == "committed"


def test_commit_without_quorum_raises(tmp_path) -> None:
    c = Consensus(quorum_n=3, total_m=5, base_dir=tmp_path / "consensus")
    c.propose("p2", "risky action")
    c.vote("p2", "voter-a", "yes")

    with pytest.raises(ValueError, match="Quorum not met"):
        c.commit("p2")


def test_vote_rejects_invalid_ballot(tmp_path) -> None:
    c = Consensus(base_dir=tmp_path / "consensus")
    c.propose("p3", "test")
    with pytest.raises(ValueError, match="yes.*no"):
        c.vote("p3", "voter-a", "maybe")
