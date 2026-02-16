# Changelog

> *A record of decisions, implementations, and the occasional Prophet vindication*

All notable decisions and changes to this project are documented here.

Format: `[YYYY-MM-DD] Category: Description (Vote if applicable)`

---

## [Unreleased]

*Pending decisions and work in progress*

- 10 framework enhancements awaiting implementation by LIL_JEFF

---

## [2026-02-15] - Framework Enhancement Analysis

### Decisions

- **Case 2026-INFRA-001: Framework Enhancement Analysis** — Adopted 10 enhancements to improve MORNINGSTAR infrastructure operability. Vote: 4-0-0 (Unanimous). Risk: Temporary inconsistency during implementation.

### The Ten Enhancements (Ratified)

| # | Enhancement | File | Priority |
|---|-------------|------|----------|
| 1 | Enhanced README with Navigation Index | `README.md` | HIGH |
| 2 | Personality Definitions File | `core/personalities.md` | HIGH |
| 3 | Precedent Database Schema | `courtroom/precedents.md` | MEDIUM |
| 4 | Inter-Agent Protocol | `core/inter-agent-protocol.md` | HIGH |
| 5 | Session Templates Directory | `templates/*.md` | MEDIUM |
| 6 | Command Quick-Reference | `README.md` section | HIGH |
| 7 | Metrics Dashboard | `state/metrics.md` | MEDIUM |
| 8 | State Validation Schema | `core/state-schema.md` | MEDIUM |
| 9 | Transcript Integrity Requirements | `courtroom/RULES.md` addition | MEDIUM |
| 10 | Error Recovery & Rollback Protocol | `core/error-recovery.md` | HIGH |

### Prophet Proposals Deferred

- P1: Living Persona Library — Requires operational experience
- P2: Deliberation Replay System — Needs transcripts to exist first
- P3: Prophetic Pattern Recognition — Awaits metrics infrastructure
- P4: Cross-Framework Integration — Depends on inter-agent protocol

### Consultant's Observation

Edward Cullen noted: *"The framework assumes good-faith operators. The system trusts. Perhaps that is its greatest vulnerability—and its greatest strength."*

### Transcript

- `courtroom/transcripts/2026-02-15-framework-enhancement-analysis.md`

---

## [2026-02-15] - MORNINGSTAR Infrastructure

### Added

- **state/current.md** — Session state tracking template
  - Active task and status tracking
  - Pending deliberations queue
  - Prophet vindication tracker
  - SME activity log
  - Session metrics

- **courtroom/RULES.md** — Formal deliberation rules
  - Article I: Jurisdiction and feasibility classifications
  - Article II: Court composition and quorum requirements
  - Article III: Voting procedures and tie-breaking
  - Article IV: Deliberation procedure
  - Article V: Recusal guidelines
  - Article VI: Subject Matter Expert framework
  - Article VII: Session management
  - Article VIII: Transcript requirements
  - Article IX: Precedent handling
  - Article X: Amendment procedures

- **courtroom/BEST_PRACTICES.md** — Practical guidance
  - When to deliberate (and when not to)
  - Running efficient deliberations
  - Personality management and failure modes
  - Voting wisdom
  - Working with SMEs
  - Documentation discipline
  - Common patterns and anti-patterns

- **courtroom/transcripts/** — Directory for F3+ deliberation records
  - .gitkeep to preserve empty directory

- **core/procedures.md** — Step-by-step deliberation protocols
  - Session lifecycle (init, checkpoint, close)
  - Full deliberation protocol
  - Expedited deliberation format
  - Tie-breaking procedure
  - Recusal procedure
  - SME involvement procedures
  - Consultant invocation protocol
  - Transcript generation template
  - Prophet vindication recording
  - Emergency procedures

- **core/sme-framework.md** — Subject Matter Expert framework
  - Expert Witness protocol (advisory, 0 votes)
  - Specialist Seat protocol (full participation, 1 vote)
  - Domain definitions (security, database, compliance, infrastructure, performance, accessibility)
  - Advisory-only domains (ux, legal)
  - Selection guidelines
  - Failure tracking protocol
  - External source flagging

- **CHANGELOG.md** — This file

### Infrastructure Notes

This establishes the operational infrastructure for MORNINGSTAR's deliberative courtroom system. All files are designed to be directly referenced during operation:

- `state/current.md` is read at session start and updated throughout
- `courtroom/RULES.md` is the authoritative source for procedural questions
- `courtroom/BEST_PRACTICES.md` provides guidance when the rules don't cover a situation
- `core/procedures.md` contains step-by-step protocols for all operations
- `core/sme-framework.md` governs external expertise integration

---

## Template for Future Entries

```markdown
## [YYYY-MM-DD] - Session/Feature Name

### Decisions

- **[Matter]** — [Decision]. Vote: [X-Y-Z]. Risk: [Accepted risk].

### Implementations

- [What was implemented]

### Prophet Vindications

- [If applicable: Prophet was right about X]

### Dissents Recorded

- [If applicable: Minority position on Y]

### Technical Debt Accepted

- [If applicable: Debt accepted and why]
```

---

> *"The changelog is memory made permanent. What we do not record, we are doomed to redecide."*
> — MORNINGSTAR::SCRIBE
