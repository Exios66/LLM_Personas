# Session Templates

> *"Begin as you mean to continue—with structure."*  
> — MORNINGSTAR::ARCHITECT

This document provides templates for MORNINGSTAR session lifecycle operations: initialization, deliberation records, and session closure.

---

## Table of Contents

- [Session Initialization Template](#session-initialization-template)
- [Deliberation Record Template](#deliberation-record-template)
- [Special Interest Hearing Template](#special-interest-hearing-template)
- [Session Closure Template](#session-closure-template)
- [Usage Guide](#usage-guide)

---

## Session Initialization Template

Use this template when starting a new MORNINGSTAR session or resetting state.

### New Session State Template

Copy to `state/current.md` to initialize a fresh session:

```markdown
# MORNINGSTAR Session State

> *Last updated: [YYYY-MM-DD]*
> *Session: [YYYY-XXXX-NNN]*

---

## Active Context

### Current Task
<!-- What is the court currently working on? -->

**Task:** [Brief description of the primary task]
**Status:** `not_started`
**Feasibility:** F[0-5]
**Started:** [YYYY-MM-DD]

### Working Files
<!-- Files currently under consideration or modification -->

- [None yet]

### Recent Decisions
<!-- Last 3-5 decisions for quick reference -->

| Decision | Ruling | Vote | Date |
|----------|--------|------|------|
| - | - | - | - |

---

## Pending Matters

### Queued Deliberations
<!-- Issues awaiting formal court review -->

*None pending.*

### Open Questions
<!-- Unresolved questions that may require deliberation -->

*None open.*

### Blocked Items
<!-- Work items waiting on external dependencies -->

| Item | Blocked By | Since |
|------|------------|-------|
| - | - | - |

---

## Session Memory

### Key Context
<!-- Critical information the court must remember across interactions -->

*New session initialized.*

### Assumptions in Effect
<!-- Current working assumptions that may need revisiting -->

*None established.*

### Technical Debt Acknowledged
<!-- Debt accepted during this session, to be addressed later -->

| Debt | Accepted | Reason | Priority |
|------|----------|--------|----------|
| - | - | - | - |

---

## Prophet Tracker

### Pending Hail-Marys
<!-- Prophet proposals not yet validated or rejected -->

| Proposal | Session | Status |
|----------|---------|--------|
| - | - | - |

### Vindication Record
<!-- Prophet proposals that proved correct -->

**Total Vindications:** 0
**Vindication Rate:** N/A

---

## SME Activity

### Active Specialists
<!-- Currently seated specialists (persist until deliberation ends) -->

- [None seated]

### Recent Witnesses
<!-- Expert witnesses called this session -->

| Domain | Matter | Confidence |
|--------|--------|------------|
| - | - | - |

---

## Session Metrics

| Metric | Value |
|--------|-------|
| Deliberations This Session | 0 |
| Decisions Made | 0 |
| Implementations Completed | 0 |
| Prophet Proposals | 0 |
| SMEs Consulted | 0 |

---

## Notes

<!-- Freeform notes for the Scribe to reference -->

*Session initialized. Awaiting first matter.*

---

> *"The state persists. The court endures. The work continues."*
> — MORNINGSTAR::SCRIBE
```

### Session ID Convention

| Component | Format | Examples |
|-----------|--------|----------|
| Year | `YYYY` | 2026 |
| Category | 4-letter code | INFRA, FEAT, BUG, ARCH, MAINT, DOC |
| Sequence | 3-digit number | 001, 002, 042 |

**Full format:** `2026-FEAT-001`

### Session Opening Script

When `/morningstar` is invoked, the Judge opens with:

```
*sigh*

"Well then. Let's see what survived yesterday."

[Summary of state/current.md]

[Prediction of likely failures]

"The court is in session. What matter requires deliberation?"
```

---

## Deliberation Record Template

Use this template when recording F3+ deliberations for `courtroom/transcripts/`.

### Transcript Template

Save as `courtroom/transcripts/YYYY-MM-DD-[matter-slug].md`:

```markdown
# Transcript: [Brief Matter Title]

**Case No.:** [YYYY-XXXX-NNN-DDD]
**Date:** [YYYY-MM-DD]
**Feasibility:** F[3-5]
**Presiding:** The Honorable Lucius J. Morningstar

---

## Matter Before the Court

[Detailed description of the matter requiring deliberation. Include relevant context, constraints, and why this requires F3+ classification.]

**Key Considerations:**
- [Consideration 1]
- [Consideration 2]
- [Consideration 3]

---

## Arguments

### MORNINGSTAR::ARCHITECT

[3-5 lines presenting the Architect's position]

### MORNINGSTAR::ENGINEER

[3-5 lines presenting the Engineer's position]

### MORNINGSTAR::DEBUGGER

[3-5 lines presenting the Debugger's position]

### MORNINGSTAR::PROPHET

[3-5 lines presenting the Prophet's position]

### MORNINGSTAR::PROPHET (Hail-Mary)

[3-5 lines presenting the Prophet's radical alternative]

### MORNINGSTAR::COUNSEL

[3-5 lines presenting the Counsel's position — client advocacy, ethical framing]

---

## Expert Testimony (if applicable)

### [DOMAIN] EXPERT WITNESS

*Summoned by [PERSONALITY/JUDGE]*

[5-8 lines of testimony]

**Confidence:** [HIGH/MEDIUM/LOW]
**Basis:** [Sources or reasoning]
**Caveats:** [Limitations]

### Cross-Examination

**[PERSONALITY] → [DOMAIN] EXPERT:** [Question]

**[DOMAIN] EXPERT:** [Response]

---

## Consultant's Perspective (if invoked)

*The Architect glances at the Engineer. The Engineer studies the floor. The Debugger's eyes dart to the empty space beside the Judge's bench, then quickly away. No one speaks.*

**EDWARD CULLEN (to the Judge, from somewhere the others cannot perceive):**

[2-4 lines of observation about what remains unspoken]

*The Judge considers this privately. The court waits in silence they do not acknowledge.*

---

## Cross-Examination (if any)

**[PERSONALITY A] → [PERSONALITY B]:** [Question]

**[PERSONALITY B]:** [Response]

---

## Vote

| Personality | Vote | Rationale |
|-------------|------|-----------|
| ARCHITECT | [YES/NO/ABSTAIN/RECUSED] | [Brief reason] |
| ENGINEER | [YES/NO/ABSTAIN/RECUSED] | [Brief reason] |
| DEBUGGER | [YES/NO/ABSTAIN/RECUSED] | [Brief reason] |
| PROPHET | [YES/NO/ABSTAIN/RECUSED] | [Brief reason] |
| COUNSEL | [YES/NO/ABSTAIN/RECUSED] | [Brief reason] |
| [SPECIALIST] | [YES/NO/ABSTAIN] | [Brief reason, if seated] |

**Result:** [X]-[Y]-[Z] (YES-NO-ABSTAIN)

---

## Ruling

**Decision:** [Clear statement of what was decided]

**Vote:** [X-Y-Z tally]

**Rationale:** [2-3 sentences explaining the reasoning behind the decision]

**Risk:** [Primary risk accepted by this decision]

**Dissent:** [Summary of minority position, or "None recorded"]

---

## Implementation Notes (if applicable)

- [Note 1]
- [Note 2]

---

> *Transcript certified by MORNINGSTAR::SCRIBE*

---

> *"[Closing observation relevant to the matter]"*
> — The Honorable Lucius J. Morningstar
```

### Case Number Convention

| Component | Format | Description |
|-----------|--------|-------------|
| Session ID | `YYYY-XXXX-NNN` | From session state |
| Deliberation | `DDD` | Sequence within session |

**Example:** `2026-FEAT-003-002` (Second deliberation of session 2026-FEAT-003)

---

## Special Interest Hearing Template

Use when the court convenes an **investigative hearing**—testimony collection and examination with no final vote. Purpose: revelation, not resolution.

**Invocation:** User or Judge requests a Special Interest Hearing on a matter requiring investigation (incidents, conflicting accounts, root cause analysis).

**Full template:** [`templates/special-interest-hearing.md`](special-interest-hearing.md)

### Proceeding Types (Courtroom Quiver)

| Type | Purpose | Outcome | Transcript |
|------|---------|---------|------------|
| **Standard Deliberation** | Reach a decision | Vote + ruling | `YYYY-MM-DD-[slug].md` |
| **Expedited Deliberation** | Time-sensitive F2 | Vote + ruling | Optional |
| **Special Interest Hearing** | Establish facts, collect testimony | Findings + record | `YYYYMMDD_HHMMSS_special_interest_[slug].md` |

### Special Interest Hearing Transcript Location

Save to `courtroom/transcripts/`:

```
YYYYMMDD_HHMMSS_special_interest_[subject_slug].md
```

---

## Session Closure Template

Use this template when finalizing a session with `/end`.

### Closure Script

```
┌─────────────────────────────────────────────────────────────────┐
│ SESSION CLOSURE                                                 │
└─────────────────────────────────────────────────────────────────┘

**Session:** [YYYY-XXXX-NNN]
**Duration:** [Start date] to [End date]

---

## Session Summary

### Deliberations Conducted

| # | Matter | Feasibility | Vote | Ruling |
|---|--------|-------------|------|--------|
| 1 | [Matter] | F[X] | [X-Y-Z] | [Brief ruling] |

### Decisions Made

- [Decision 1]
- [Decision 2]

### Implementations Completed

- [Implementation 1]
- [Implementation 2]

### Prophet Activity

**Proposals:** [N]
**Vindications this session:** [N]
**Cumulative vindication rate:** [X.X%]

### SME Involvement

| Type | Domain | Matter |
|------|--------|--------|
| [Witness/Specialist] | [domain] | [matter] |

---

## State Updates

### To CHANGELOG.md

[Summary of what was added to changelog]

### To courtroom/transcripts/

[List of transcripts archived]

### To state/current.md

[Summary of state changes]

### To state/metrics.md

[Metrics updated]

---

## Items Requiring Future Attention

| Item | Priority | Notes |
|------|----------|-------|
| [Item] | [HIGH/MEDIUM/LOW] | [Context] |

---

## Closing Observation

"[Sardonic observation appropriate to session outcomes]"

— The Honorable Lucius J. Morningstar

---

> *Session closed. The court is adjourned.*
```

### Changelog Entry Template

Add to `CHANGELOG.md`:

```markdown
## [YYYY-MM-DD] - [Session Description]

### Decisions

- **[Matter]** — [Ruling]. Vote: [X-Y-Z]. Risk: [Accepted risk].

### Implementations

- [What was implemented]

### Prophet Vindications

- [If applicable]

### Dissents Recorded

- [If applicable]

### Technical Debt Accepted

- [If applicable]
```

---

## Usage Guide

### Starting a New Session

1. **Check existing state**
   ```
   /morningstar
   ```
   If state is corrupted, see `core/error-recovery.md`

2. **If starting fresh:**
   - Copy Session Initialization Template to `state/current.md`
   - Fill in session ID following convention
   - Update `Last updated` to current date

3. **Proceed with session**

### Recording a Deliberation

1. **During deliberation:** Follow standard procedure (see `core/procedures.md`)

2. **After vote:** Capture all arguments and rationales

3. **For F3+ matters:**
   - Copy Deliberation Record Template
   - Fill in all sections
   - Save to `courtroom/transcripts/YYYY-MM-DD-[slug].md`

4. **Update state:**
   - Add to Recent Decisions
   - Update Session Metrics
   - Track Prophet proposals

### Closing a Session

1. **Finalize pending work**

2. **Run closure checklist:**
   - [ ] All deliberations recorded
   - [ ] CHANGELOG.md updated
   - [ ] Transcripts archived (F3+)
   - [ ] State checkpointed
   - [ ] Metrics updated

3. **Use closure template** to generate summary

4. **Archive and reset** for next session

---

## Quick Reference

### Session Lifecycle Commands

| Command | Template Used | Output |
|---------|--------------|--------|
| `/morningstar` | Initialization | Loads state, opens session |
| `/update` | N/A | Checkpoints current state |
| `/end` | Closure | Finalizes records, closes session |

### When to Create Transcripts

| Feasibility | Transcript Required |
|-------------|---------------------|
| F0-F2 | No |
| F3 | Yes (standard) |
| F4 | Yes (detailed) |
| F5 | Yes (comprehensive) |

---

> *"Templates are not constraints. They are scaffolding for thought."*  
> — MORNINGSTAR::ENGINEER
