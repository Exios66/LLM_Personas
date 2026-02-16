# Error Recovery & Rollback Protocol

> *"The court does not fail gracefully. The court recovers deliberately."*  
> — The Honorable Lucius J. Morningstar

This document defines procedures for recovering from state corruption, rolling back bad decisions, and handling emergency situations during MORNINGSTAR sessions.

---

## Table of Contents

- [State Corruption Recovery](#state-corruption-recovery)
- [Decision Rollback Protocol](#decision-rollback-protocol)
- [Emergency Procedures](#emergency-procedures)
- [Prevention Measures](#prevention-measures)
- [Recovery Checklist](#recovery-checklist)

---

## State Corruption Recovery

### Detecting Corruption

State corruption is indicated by:

| Symptom | Likely Cause |
|---------|--------------|
| Validation errors on `/morningstar` | Schema violation in `state/current.md` |
| Missing required sections | Incomplete update or file truncation |
| Inconsistent dates | Manual editing error or clock issues |
| Vote tallies don't sum | Transcription error |
| Session ID mismatch | State from different session |
| Metrics don't match records | Counter drift |

### Recovery Procedure

#### Level 1: Minor Corruption (Single Field)

**Use when:** One or two fields are invalid but overall structure is intact.

```
┌─────────────────────────────────────────────────────────────────┐
│ LEVEL 1 RECOVERY                                                │
└─────────────────────────────────────────────────────────────────┘

1. Identify the specific validation error
2. Check CHANGELOG.md for correct value
3. Correct the field directly in state/current.md
4. Run validation again
5. Document the correction in Notes section

Duration: < 5 minutes
Risk: Low
```

#### Level 2: Section Corruption (One Section Invalid)

**Use when:** An entire section is missing or malformed.

```
┌─────────────────────────────────────────────────────────────────┐
│ LEVEL 2 RECOVERY                                                │
└─────────────────────────────────────────────────────────────────┘

1. Identify the corrupted section
2. Reference templates/session-start.md for correct structure
3. Reconstruct section from:
   a. CHANGELOG.md (for decisions)
   b. courtroom/transcripts/ (for deliberation details)
   c. Previous state versions (if available)
4. Insert reconstructed section
5. Validate entire document
6. Add recovery note with sources

Duration: 5-15 minutes
Risk: Medium
```

#### Level 3: Major Corruption (Multiple Sections)

**Use when:** State is largely unusable but some data can be salvaged.

```
┌─────────────────────────────────────────────────────────────────┐
│ LEVEL 3 RECOVERY                                                │
└─────────────────────────────────────────────────────────────────┘

1. PRESERVE corrupted state:
   mv state/current.md state/corrupted-YYYY-MM-DD.md

2. Create fresh state from template:
   cp templates/session-start.md state/current.md

3. Reconstruct from authoritative sources:
   
   Source Priority:
   ┌────────────────────────────────────┐
   │ 1. courtroom/transcripts/ (highest)│
   │ 2. CHANGELOG.md                    │
   │ 3. state/metrics.md               │
   │ 4. Corrupted file (fragments)     │
   │ 5. User memory (lowest)           │
   └────────────────────────────────────┘

4. Rebuild each section methodically
5. Validate completely
6. Document reconstruction in Notes

Duration: 15-30 minutes
Risk: High (data loss possible)
```

#### Level 4: Total Corruption (State Unrecoverable)

**Use when:** State file is missing, empty, or completely invalid.

```
┌─────────────────────────────────────────────────────────────────┐
│ LEVEL 4 RECOVERY                                                │
└─────────────────────────────────────────────────────────────────┘

1. Accept that current session state is lost

2. Create new session:
   - Generate new session ID
   - Use clean template
   - Set status to 'not_started'

3. Preserve institutional memory:
   - Review all files in courtroom/transcripts/
   - Extract key context from CHANGELOG.md
   - Summarize in Session Memory > Key Context

4. Document the incident:
   - Add entry to CHANGELOG.md noting state loss
   - Record what was lost vs. preserved

5. Proceed with new session

Duration: 30+ minutes
Risk: High (session continuity lost)
```

### Recovery Source Priority

When reconstructing state, prioritize sources by reliability:

| Priority | Source | Reliability | Contents |
|----------|--------|-------------|----------|
| 1 | `courtroom/transcripts/` | Highest | Full deliberation records |
| 2 | `CHANGELOG.md` | High | Decision summaries |
| 3 | `state/metrics.md` | Medium | Aggregate statistics |
| 4 | Corrupted state file | Low | Fragments may be valid |
| 5 | User recollection | Lowest | Prone to error |

---

## Decision Rollback Protocol

### When to Roll Back

A decision should be rolled back when:

- The decision was based on incorrect information
- Material circumstances have changed
- Implementation revealed unforeseen consequences
- The original vote was procedurally invalid

### Rollback Procedure

```
┌─────────────────────────────────────────────────────────────────┐
│ DECISION ROLLBACK PROTOCOL                                      │
└─────────────────────────────────────────────────────────────────┘

PHASE 1: MOTION TO RECONSIDER
─────────────────────────────

1. Any personality may move to reconsider:
   "I move to reconsider [CASE-ID] due to [REASON]."

2. Motion requires:
   - Specific case reference
   - Concrete reason for reconsideration
   - New information or changed circumstances

3. Second required from another personality

PHASE 2: DELIBERATION
─────────────────────

4. The court deliberates on WHETHER to reconsider
   (Not yet on the original matter)

5. Vote on motion to reconsider:
   - Pass: Requires same threshold as original matter
   - Fail: Original decision stands

PHASE 3: RE-DELIBERATION (if motion passes)
──────────────────────────────────────────

6. Original matter is re-opened
7. Full deliberation procedure applies
8. New arguments and evidence presented
9. New vote taken

PHASE 4: RECORDING
─────────────────

10. Document in CHANGELOG.md:
    - Original decision
    - Rollback motion and vote
    - New decision (if changed)
    - Rationale for change

11. Add addendum to original transcript (do not modify):
    
    ## Addendum [DATE]
    
    **Status:** RECONSIDERED
    **Motion:** [Vote on reconsideration]
    **New Ruling:** [Case-ID of new deliberation]
    **Reason:** [Why reconsidered]

12. Create new transcript for re-deliberation
```

### Rollback Constraints

| Constraint | Rule |
|------------|------|
| **Time limit** | No limit, but older decisions harder to roll back |
| **Frequency** | Same matter cannot be reconsidered more than twice per session |
| **Implementation** | If implementation has begun, assess rollback cost |
| **Precedent** | Rolled-back decisions lose precedential weight |

### Emergency Rollback

For decisions causing active harm:

```
┌─────────────────────────────────────────────────────────────────┐
│ EMERGENCY ROLLBACK                                              │
└─────────────────────────────────────────────────────────────────┘

1. Judge may unilaterally suspend a decision if:
   - Active harm is occurring
   - Delay would worsen the situation
   - Immediate action is required

2. Suspension is temporary (24 hours maximum)

3. Full reconsideration deliberation MUST follow

4. Document as:
   
   ## Emergency Suspension
   
   **Decision:** [CASE-ID]
   **Suspended:** [TIMESTAMP]
   **Reason:** [Active harm description]
   **Status:** Pending reconsideration
```

---

## Emergency Procedures

### Session Crash Recovery

If a session terminates unexpectedly:

```
┌─────────────────────────────────────────────────────────────────┐
│ SESSION CRASH RECOVERY                                          │
└─────────────────────────────────────────────────────────────────┘

1. Do NOT run /morningstar immediately

2. Assess state integrity:
   - Open state/current.md directly
   - Check for truncation
   - Verify last updated timestamp

3. If state appears valid:
   - Run /morningstar normally
   - Note "session recovered from crash" in state

4. If state is corrupted:
   - Follow State Corruption Recovery (Level 2-4)

5. Check for orphaned work:
   - Review any transcripts started but not certified
   - Check CHANGELOG.md for unpersisted entries
```

### Deadlocked Deliberation

When the court cannot reach resolution after 3 rounds:

```
┌─────────────────────────────────────────────────────────────────┐
│ DEADLOCK RESOLUTION                                             │
└─────────────────────────────────────────────────────────────────┘

Option A: REFRAME
─────────────────
1. Judge calls timeout
2. Identify the crux disagreement
3. Reframe the question to address crux
4. Resume deliberation with new framing

Option B: TIME-BOX EXPERIMENT
────────────────────────────
1. Identify the lowest-risk option
2. Implement with explicit time limit
3. Reconvene after time-box to evaluate
4. Record as "experimental ruling"

Option C: DEFER TO EXPERTISE
───────────────────────────
1. Seat appropriate domain Specialist
2. Weight Specialist perspective heavily
3. Re-vote with additional input

Option D: JUDICIAL RULING
────────────────────────
1. Judge rules unilaterally
2. Document as "Judicial ruling due to deadlock"
3. Record all positions in dissent
4. Flag for reconsideration if circumstances change
```

### Corrupted Transcript Recovery

If a transcript is corrupted or missing:

```
┌─────────────────────────────────────────────────────────────────┐
│ TRANSCRIPT RECOVERY                                             │
└─────────────────────────────────────────────────────────────────┘

1. Check CHANGELOG.md for decision summary
2. Check state/current.md for deliberation record
3. Reconstruct transcript with available information
4. Mark as [RECONSTRUCTED] in header:

   **Case No.:** [ID] [RECONSTRUCTED]

5. Document sources used in reconstruction
6. Note reduced precedential weight
```

### Context Loss Recovery

When the court loses context mid-deliberation:

```
┌─────────────────────────────────────────────────────────────────┐
│ CONTEXT LOSS RECOVERY                                           │
└─────────────────────────────────────────────────────────────────┘

1. Pause current deliberation
2. Run /update to checkpoint current state
3. Request context refresh:
   - What was the original matter?
   - What arguments were presented?
   - Where in the procedure are we?
4. Resume from known point
5. If arguments lost, personalities may re-present briefly
```

---

## Prevention Measures

### State Backup Practices

| Practice | Frequency | Method |
|----------|-----------|--------|
| Checkpoint on `/update` | Each command | Automatic |
| Pre-deliberation snapshot | Before F3+ matters | Manual or automatic |
| Session start validation | Each `/morningstar` | Automatic |
| End-of-day backup | Daily | Manual recommended |

### Integrity Checks

Run these checks periodically:

```
┌─────────────────────────────────────────────────────────────────┐
│ INTEGRITY VERIFICATION                                          │
└─────────────────────────────────────────────────────────────────┘

□ state/current.md passes schema validation
□ All transcripts have certification
□ CHANGELOG.md entries match transcripts
□ Vote tallies are mathematically correct
□ Dates are consistent across documents
□ Metrics align with recorded decisions
□ Precedent index is current
```

### Early Warning Signs

Watch for these indicators of impending problems:

| Warning Sign | Potential Issue | Action |
|--------------|-----------------|--------|
| Dates inconsistent | Manual editing error | Verify and correct |
| Metrics drifting | Counter not updating | Recalculate from records |
| Missing transcripts | Save failed | Reconstruct immediately |
| Stale state | Session not closed properly | Update state |
| Orphaned decisions | Changelog not updated | Add missing entries |

---

## Recovery Checklist

### Quick Reference: State Recovery

- [ ] Identify corruption level (1-4)
- [ ] Preserve corrupted state (Level 3+)
- [ ] Gather recovery sources
- [ ] Reconstruct using priority order
- [ ] Validate reconstructed state
- [ ] Document recovery in Notes
- [ ] Resume operations

### Quick Reference: Decision Rollback

- [ ] Motion to reconsider with reason
- [ ] Second from another personality
- [ ] Vote on motion to reconsider
- [ ] If passed: full re-deliberation
- [ ] Record in CHANGELOG.md
- [ ] Add addendum to original transcript
- [ ] Create new transcript for new decision

### Quick Reference: Emergency Response

| Emergency | First Action |
|-----------|--------------|
| State corruption | Assess level, follow recovery |
| Session crash | Check state before restart |
| Decision causing harm | Emergency suspension |
| Deadlocked court | Reframe or time-box |
| Missing transcript | Reconstruct with flag |
| Context loss | Pause, checkpoint, refresh |

---

## Recovery Log Template

Document all recoveries for institutional learning:

```markdown
## Recovery Log Entry

**Date:** [YYYY-MM-DD]
**Type:** [State Corruption / Decision Rollback / Emergency]
**Level:** [1-4 for state, N/A for others]

### Incident

[What happened]

### Root Cause

[Why it happened]

### Recovery Actions

1. [Action taken]
2. [Action taken]

### Data Lost

[What could not be recovered, if any]

### Prevention

[How to prevent recurrence]

### Time to Recover

[Duration]
```

---

> *"Failure is inevitable. Recovery is mandatory."*  
> — MORNINGSTAR::DEBUGGER
