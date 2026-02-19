# Executive Branch Protocol

> *Separation of concerns, handoff path, and consensus.*

---

## 1. Separation of Concerns

### Judicial (MORNINGSTAR)

- **Decides** what must be done and why
- Produces rulings with case ID, vote, rationale, constraints
- Cannot execute actions; only specify them

### Executive

- **Executes** approved rulings
- Cannot initiate decisions
- May override a judicial decision **only** with:
  - Explicit court approval (new ruling authorizing override)
  - Cryptographic proof attached to the override action

### Boundary

```
Judicial output: Ruling (case ID, decision, specification)
Executive input: Ruling
Executive output: Action record (what was done, when, proof if override)
```

---

## 2. Handoff: Judicial → Executive

### Flow

1. MORNINGSTAR completes deliberation and issues ruling
2. Ruling is recorded in `executive/logs/judicial_decisions.log` (immutable)
3. LIL_JEFF (or designated executor) implements per ruling
4. Executive action is logged; if override, proof is attached

### Handoff Document

When MORNINGSTAR hands off for implementation:

- **Case ID** — Links ruling to execution
- **Decision** — What was decided
- **Specification** — What to implement
- **Constraints** — Non-negotiables

The executive does not re-interpret the ruling. It executes as specified.

### Override Path

When the executive must override a prior judicial decision:

1. Obtain explicit court approval (new ruling authorizing override)
2. Generate cryptographic proof: `OverrideProof.generate(ruling_id, reason, ...)`
3. Attach proof to the executive action record
4. Watchdog will verify proof and flag if missing or invalid

---

## 3. Immutable Logging

### Judicial Decisions Log

- **Path:** `executive/logs/judicial_decisions.log`
- **Format:** One JSON object per line (NDJSON)
- **Schema per entry:**
  - `timestamp` — ISO 8601
  - `matter` — Short description
  - `ruling_hash` — Content hash of ruling (tamper-evident)
  - `source` — Transcript path or ruling ID
  - `entry_hash` — Hash of this entry (content-addressing)

Append-only. No deletion or modification. Each entry's hash chains to the previous for integrity.

---

## 4. Cryptographic Proof for Overrides

### Proof Structure

```
proof = HMAC-SHA256(secret, payload)
payload = ruling_id || override_reason || timestamp
```

### Verification

- `OverrideProof.verify(proof, ruling_id, reason, timestamp, secret)` returns `True` iff HMAC matches.

### Key Management

- Secret stored in `executive/.executive_secret` or `EXECUTIVE_PROOF_SECRET`
- Gitignored. Rotate periodically.
- Only court-authorized entities hold the secret.

---

## 5. Watchdog Process

### Monitors

| Check | Purpose |
|-------|---------|
| Actions vs approvals | Every executive action should trace to a judicial ruling |
| Log integrity | Entry hashes chain correctly; no tampering |
| Override frequency | Alert if overrides exceed threshold (configurable) |

### Output

- **Normal:** Exit 0, no output
- **Anomaly:** stderr alert, exit 1
- **Optional:** Log file for audit trail

### Invocation

```bash
python -m executive.watchdog
```

Run periodically (cron) or on-demand after executive actions.

---

## 6. Distributed Consensus Protocol

### For Critical Decisions

When a decision is **critical** (e.g., schema migration, security policy change), require N-of-M consensus before execution.

### Protocol: Proposal → Vote → Commit

1. **Propose:** `consensus.propose(proposal_id, description)`
2. **Vote:** Each stakeholder calls `consensus.vote(proposal_id, voter_id, "yes"|"no")`
3. **Check quorum:** `consensus.check_quorum(proposal_id)` — N of M voted yes
4. **Commit:** `consensus.commit(proposal_id)` — Record committed, ready for execution

### Design

- File-based or in-memory for single-node
- Designed for future multi-node: proposal/vote/commit records can be replicated
- Quorum configurable (e.g., 3 of 5)

### When to Use

- Schema changes
- Security policy updates
- Irreversible operations
- Any matter the court designates as "critical"

---

## 7. Risk Acknowledgment

**Accepted risk (per ruling):** Executive could grow beyond scope, eroding judicial oversight.

**Mitigation:**

- Watchdog monitors actions vs approvals
- Override requires proof
- Consensus for critical decisions
- Regular architectural reviews (per court recommendation)

---

> *"The protocol exists. The executive enforces it. The court oversees both."*
