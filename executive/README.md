# Executive Branch

> *"The court decides. The executive executes. Neither usurps the other."*  
> — MORNINGSTAR Ruling 2026-DEL-001

The Executive Branch executes approved judicial rulings. It does not initiate decisions; it carries out what MORNINGSTAR has decreed.

---

## Purpose

- **Execute** rulings handed down by MORNINGSTAR (Judicial Branch)
- **Log** all judicial decisions immutably
- **Require** cryptographic proof for any override of judicial decisions
- **Support** distributed consensus for critical decisions

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     MORNINGSTAR (Judicial)                       │
│                     Decides what and why                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Ruling (transcript, case ID, decision)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     EXECUTIVE BRANCH                             │
│                     Executes approved rulings                    │
├─────────────────────────────────────────────────────────────────┤
│  judicial_log.py  │ Append-only log of judicial decisions       │
│  proof.py         │ Cryptographic proof for overrides           │
│  watchdog.py      │ Oversight: actions vs approvals, integrity   │
│  consensus.py     │ N-of-M protocol for critical decisions      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Action record (with proof if override)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     LIL_JEFF / Aegis / User                      │
│                     Implementation / consumption                 │
└─────────────────────────────────────────────────────────────────┘
```

### Separation of Concerns

| Branch   | Responsibility                    | Cannot |
|----------|-----------------------------------|--------|
| Judicial | Deliberate, rule, specify         | Execute actions |
| Executive| Execute rulings, log, prove       | Initiate decisions or override without proof |

---

## Usage

### Recording a Judicial Decision

```python
from executive.judicial_log import JudicialLog

log = JudicialLog()
log.append(
    matter="2026-DEL-001: Executive branch addition",
    ruling_hash="sha256:abc123...",
    source="litigation/transcripts/2026-02-19-the-addition-of-an-executive-branch-into-the-larger-architec.md",
)
```

### Generating Override Proof

When the executive must override a judicial decision (emergency, explicit court approval):

```python
from executive.proof import OverrideProof

proof = OverrideProof.generate(
    ruling_id="2026-DEL-001",
    override_reason="Emergency rollback per court approval 2026-EXEC-001",
    secret_path="executive/.executive_secret",  # or env var
)
# proof is attached to the executive action record
```

### Running the Watchdog

```bash
python -m executive.watchdog
# Or: python executive/watchdog.py
```

Runs checks on: (a) executive actions vs judicial approvals, (b) log integrity, (c) override frequency. Alerts to stderr or log file on anomalies.

### Consensus for Critical Decisions

```python
from executive.consensus import Consensus

consensus = Consensus(quorum_n=3, total_m=5)
proposal_id = consensus.propose("CRITICAL-001", "Deploy schema migration")
# Stakeholders vote
consensus.vote(proposal_id, "agent-a", "yes")
consensus.vote(proposal_id, "agent-b", "yes")
consensus.vote(proposal_id, "agent-c", "yes")
if consensus.check_quorum(proposal_id):
    consensus.commit(proposal_id)
```

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `protocol.md` | Separation, handoff, consensus protocol |
| `logs/` | Judicial decisions log (append-only) |
| `judicial_log.py` | Append-only log with content-addressing |
| `proof.py` | HMAC-based proof for overrides |
| `watchdog.py` | Oversight monitoring |
| `consensus.py` | Proposal → vote → commit |

---

## Dependencies

- **Python 3.9+**
- **Standard library only** for `judicial_log`, `proof`, `consensus`, `watchdog`
- See project `requirements.txt` for litigation/portal; executive modules have no extra deps

---

## Key Management (Override Proof)

The override proof uses HMAC-SHA256. A secret key is required:

1. **File-based:** Create `executive/.executive_secret` (gitignored). Generate with:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))" > executive/.executive_secret
   ```
2. **Environment:** Set `EXECUTIVE_PROOF_SECRET` with the hex-encoded secret.

The secret must be shared only with authorized signers (court-authorized entities). Rotate periodically.

---

## Canonical References

| Reference | Path |
|-----------|------|
| Inter-agent protocol | `core/inter-agent-protocol.md` |
| Ruling transcript | `litigation/transcripts/2026-02-19-the-addition-of-an-executive-branch-into-the-larger-architec.md` |
| Handoff | `courtroom/transcripts/HANDOFF-2026-EXEC-001.md` |
