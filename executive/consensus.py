"""
Distributed consensus protocol for critical decisions.

Protocol: proposal → vote → check quorum → commit.

Design: file-based for single-node; structure allows future multi-node replication.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Union


CONSENSUS_DIR = "consensus"
PROPOSALS_FILE = "proposals.json"
VOTES_FILE = "votes.json"
COMMITS_FILE = "commits.json"


def _base_dir() -> Path:
    return Path(__file__).resolve().parent / CONSENSUS_DIR


def _ensure_dir() -> Path:
    d = _base_dir()
    d.mkdir(parents=True, exist_ok=True)
    return d


def _load_json(path: Path, default: Union[dict, list]) -> Union[dict, list]:
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_json(path: Path, data: Union[dict, list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


class Consensus:
    """
    N-of-M consensus for critical decisions.

    propose(proposal_id, description) → create proposal
    vote(proposal_id, voter_id, "yes"|"no") → record vote
    check_quorum(proposal_id) → True if N of M voted yes
    commit(proposal_id) → record commit, mark ready for execution
    """

    def __init__(self, quorum_n: int = 3, total_m: int = 5, base_dir: Optional[Path] = None):
        self.quorum_n = quorum_n
        self.total_m = total_m
        self._base = Path(base_dir) if base_dir else _base_dir()
        self._proposals_path = self._base / PROPOSALS_FILE
        self._votes_path = self._base / VOTES_FILE
        self._commits_path = self._base / COMMITS_FILE

    def propose(self, proposal_id: str, description: str) -> str:
        """
        Create a proposal.

        Args:
            proposal_id: Unique identifier
            description: What is being proposed

        Returns:
            proposal_id
        """
        _ensure_dir()
        proposals = _load_json(self._proposals_path, {})
        if proposal_id in proposals:
            return proposal_id

        proposals[proposal_id] = {
            "description": description,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status": "open",
        }
        _save_json(self._proposals_path, proposals)
        return proposal_id

    def vote(self, proposal_id: str, voter_id: str, vote: str) -> None:
        """
        Record a vote. vote must be "yes" or "no".
        """
        vote = vote.lower()
        if vote not in ("yes", "no"):
            raise ValueError("vote must be 'yes' or 'no'")

        votes = _load_json(self._votes_path, {})
        if proposal_id not in votes:
            votes[proposal_id] = {}
        votes[proposal_id][voter_id] = vote
        _save_json(self._votes_path, votes)

    def check_quorum(self, proposal_id: str) -> bool:
        """
        Return True if at least quorum_n voters voted "yes".
        """
        votes = _load_json(self._votes_path, {})
        proposal_votes = votes.get(proposal_id, {})
        yes_count = sum(1 for v in proposal_votes.values() if v == "yes")
        return yes_count >= self.quorum_n

    def commit(self, proposal_id: str) -> dict:
        """
        Commit the proposal. Fails if quorum not met.

        Returns:
            Commit record.
        """
        if not self.check_quorum(proposal_id):
            raise ValueError(f"Quorum not met for proposal {proposal_id}")

        proposals = _load_json(self._proposals_path, {})
        if proposal_id not in proposals:
            raise ValueError(f"Unknown proposal {proposal_id}")

        proposals[proposal_id]["status"] = "committed"
        _save_json(self._proposals_path, proposals)

        commits = _load_json(self._commits_path, [])
        record = {
            "proposal_id": proposal_id,
            "committed_at": datetime.now(timezone.utc).isoformat(),
            "description": proposals[proposal_id].get("description", ""),
        }
        commits.append(record)
        _save_json(self._commits_path, commits)

        return record

    def get_proposal(self, proposal_id: str) -> Optional[dict]:
        """Return proposal dict or None."""
        proposals = _load_json(self._proposals_path, {})
        return proposals.get(proposal_id)

    def get_votes(self, proposal_id: str) -> dict:
        """Return {voter_id: vote} for proposal."""
        votes = _load_json(self._votes_path, {})
        return votes.get(proposal_id, {})
