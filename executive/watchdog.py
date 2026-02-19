"""
Watchdog process for executive branch oversight.

Monitors:
(a) Executive actions vs judicial approvals
(b) Log integrity (judicial_decisions.log)
(c) Override frequency

Outputs alerts to stderr on anomalies. Exit 0 = ok, exit 1 = anomaly.
"""

import json
import os
import sys
from pathlib import Path
from typing import Optional

# Add parent so executive package is importable when run as script
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR.parent))

from executive.judicial_log import JudicialLog, _log_path

ACTIONS_LOG = "executive_actions.log"
OVERRIDE_THRESHOLD = 5  # Alert if overrides in window exceed this


def _actions_log_path() -> Path:
    base = Path(__file__).resolve().parent
    return base / "logs" / ACTIONS_LOG


def _ensure_actions_log() -> Path:
    p = _actions_log_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def _read_actions() -> list[dict]:
    """Read executive actions log (NDJSON)."""
    p = _ensure_actions_log()
    if not p.exists():
        return []
    result = []
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                result.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return result


def record_action(
    action_type: str,
    ruling_id: str,
    description: str,
    proof: Optional[str] = None,
) -> None:
    """
    Append an executive action record.

    Call after executing a ruling. If the action overrides a judicial decision,
    proof MUST be provided (from proof.OverrideProof.generate).
    """
    import datetime

    entry = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "action_type": action_type,
        "ruling_id": ruling_id,
        "description": description,
    }
    if proof:
        entry["override_proof"] = proof
    p = _ensure_actions_log()
    with open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _judicial_ruling_ids(log: JudicialLog) -> set[str]:
    """Extract ruling IDs from judicial log (from source or matter)."""
    ids = set()
    for e in log.entries():
        src = e.get("source", "")
        matter = e.get("matter", "")
        # Source often has case ID in path; matter may start with "2026-DEL-001:"
        for part in (src, matter):
            if "2026-" in part:
                # Heuristic: extract 2026-XXX-NNN pattern
                import re
                for m in re.finditer(r"2026-[A-Z]+-\d+(-\d+)?", part):
                    ids.add(m.group(0))
    return ids


def run_checks() -> tuple[bool, list[str]]:
    """
    Run all watchdog checks.

    Returns:
        (ok, list of alert messages)
    """
    alerts = []

    # (b) Log integrity
    log = JudicialLog()
    ok, errors = log.verify()
    if not ok:
        alerts.extend([f"Log integrity: {e}" for e in errors])

    # (a) Executive actions vs judicial approvals
    actions = _read_actions()
    approved = _judicial_ruling_ids(log)

    for a in actions:
        rid = a.get("ruling_id", "")
        if rid and rid not in approved and "override" not in a.get("action_type", "").lower():
            # Action references ruling not in judicial log
            proof = a.get("override_proof")
            if not proof:
                alerts.append(
                    f"Action without judicial approval and no override proof: ruling_id={rid}"
                )

    # (c) Override frequency
    overrides = [a for a in actions if a.get("override_proof")]
    if len(overrides) > OVERRIDE_THRESHOLD:
        alerts.append(
            f"Override frequency exceeds threshold: {len(overrides)} overrides (threshold={OVERRIDE_THRESHOLD})"
        )

    return len(alerts) == 0, alerts


def main() -> int:
    """CLI entry point. Exit 0 = ok, 1 = anomaly."""
    ok, alerts = run_checks()
    if alerts:
        for msg in alerts:
            print(msg, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
