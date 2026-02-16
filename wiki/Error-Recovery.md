# Error Recovery

Procedures for state corruption, rollback of bad decisions, and emergencies. Full detail: `core/error-recovery.md` in the repo.

## State Corruption

- **Level 1:** Single field invalid → correct from CHANGELOG or transcript.
- **Level 2:** One section invalid → reconstruct from templates and records.
- **Level 3:** Multiple sections → restore from backup if available; otherwise reconstruct from CHANGELOG, transcripts, precedent.
- **Level 4:** State lost → full reconstruction from transcripts and CHANGELOG; document as recovered.

## Decision Rollback

Motion to reconsider → second → vote. If passed, full re-deliberation. Record in CHANGELOG and add addendum to original transcript.

## Prevention

- Checkpoint on `/update`.
- **Pre-session backup:** Copy `state/current.md` to `state/backups/YYYY-MM-DD-current.md` before major or F3+ sessions.
- End-of-day backup recommended.

**See:** [State-and-Metrics](State-and-Metrics) · [Procedures](Procedures) · [Runbook](Runbook)
