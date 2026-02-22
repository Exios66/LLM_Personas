"""
Append-only log for judicial decisions.

Each entry is content-addressed (hash of entry) for tamper-evidence.
Schema: timestamp, matter, ruling_hash, source, entry_hash, prev_hash.
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Union


LOG_FILENAME = "judicial_decisions.log"
LOG_DIR = "logs"


def _log_path(base_dir: Optional[Path] = None) -> Path:
    """Return path to judicial decisions log."""
    if base_dir is None:
        base_dir = Path(__file__).resolve().parent
    return base_dir / LOG_DIR / LOG_FILENAME


def _hash_content(content: str) -> str:
    """SHA-256 hash of content, hex-encoded."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _entry_hash(entry: dict) -> str:
    """Content hash of entry (excluding entry_hash and prev_hash for recursion)."""
    canonical = {
        "timestamp": entry["timestamp"],
        "matter": entry["matter"],
        "ruling_hash": entry["ruling_hash"],
        "source": entry["source"],
    }
    return _hash_content(json.dumps(canonical, sort_keys=True))


class JudicialLog:
    """
    Append-only log for judicial decisions.

    Each entry includes: timestamp, matter, ruling_hash, source, entry_hash, prev_hash.
    prev_hash chains entries for integrity verification.
    """

    def __init__(self, log_path: Optional[Union[Path, str]] = None):
        if log_path is None:
            log_path = _log_path()
        self._path = Path(log_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def append(
        self,
        matter: str,
        ruling_hash: str,
        source: str,
        timestamp: Optional[str] = None,
    ) -> dict:
        """
        Append a judicial decision record.

        Args:
            matter: Short description of the matter
            ruling_hash: Content hash of the ruling (tamper-evident)
            source: Transcript path or ruling ID
            timestamp: ISO 8601 (default: now UTC)

        Returns:
            The appended entry dict including entry_hash and prev_hash.
        """
        if timestamp is None:
            timestamp = datetime.now(timezone.utc).isoformat()

        prev_hash = self._last_hash()

        entry = {
            "timestamp": timestamp,
            "matter": matter,
            "ruling_hash": ruling_hash,
            "source": source,
        }
        entry["entry_hash"] = _entry_hash(entry)
        entry["prev_hash"] = prev_hash

        line = json.dumps(entry, ensure_ascii=False) + "\n"
        with open(self._path, "a", encoding="utf-8") as f:
            f.write(line)

        return entry

    def _last_hash(self) -> str:
        """Return prev_hash of last entry, or empty string if log empty."""
        if not self._path.exists():
            return ""
        with open(self._path, "r", encoding="utf-8") as f:
            lines = [l for l in f if l.strip()]
        if not lines:
            return ""
        last = json.loads(lines[-1])
        return last.get("entry_hash", "")

    def verify(self) -> tuple[bool, list[str]]:
        """
        Verify log integrity: entry hashes and prev_hash chain.

        Returns:
            (ok, list of error messages)
        """
        errors = []
        if not self._path.exists():
            return True, []

        prev_hash = ""
        with open(self._path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError as e:
                    errors.append(f"Line {i + 1}: invalid JSON: {e}")
                    continue

                expected_prev = entry.get("prev_hash", "")
                if expected_prev != prev_hash:
                    errors.append(
                        f"Line {i + 1}: prev_hash mismatch (expected {prev_hash[:16]}..., got {expected_prev[:16] if expected_prev else 'none'}...)"
                    )

                computed = _entry_hash(entry)
                stored = entry.get("entry_hash", "")
                if computed != stored:
                    errors.append(f"Line {i + 1}: entry_hash mismatch")

                prev_hash = stored

        return len(errors) == 0, errors

    def entries(self) -> list[dict]:
        """Read all entries (for verification or audit)."""
        if not self._path.exists():
            return []
        result = []
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    result.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return result


def compute_ruling_hash(content: str) -> str:
    """
    Compute content hash of a ruling string.

    Use for ruling_hash when appending a judicial decision.
    """
    return "sha256:" + _hash_content(content)
