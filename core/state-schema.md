# State Validation Schema

> *"State that cannot be validated cannot be trusted."*  
> — MORNINGSTAR::DEBUGGER

This document defines the required fields, validation rules, and constraints for `state/current.md`. Use this schema to verify session state integrity and to construct valid state documents.

---

## Table of Contents

- [Overview](#overview)
- [Required Sections](#required-sections)
- [Field Specifications](#field-specifications)
- [Validation Rules](#validation-rules)
- [Examples](#examples)
- [Common Errors](#common-errors)

---

## Overview

The session state file (`state/current.md`) maintains continuity across MORNINGSTAR sessions. It is:

- **Read** at session initialization (`/morningstar`)
- **Updated** at checkpoints (`/update`)
- **Finalized** at session close (`/end`)

Invalid state blocks session initialization. The court cannot convene on corrupted foundations.

---

## Required Sections

Every valid `state/current.md` MUST contain these sections in order:

| Section | Required | Purpose |
|---------|----------|---------|
| **Header** | YES | Session identification |
| **Active Context** | YES | Current work state |
| **Pending Matters** | YES | Queued deliberations |
| **Session Memory** | YES | Persistent context |
| **Prophet Tracker** | YES | Hail-Mary tracking |
| **SME Activity** | YES | Expert involvement |
| **Session Metrics** | YES | Quantitative tracking |
| **Notes** | NO | Freeform observations |

---

## Field Specifications

### Header

```markdown
# MORNINGSTAR Session State

> *Last updated: YYYY-MM-DD*
> *Session: YYYY-XXXX-NNN*
```

| Field | Format | Validation | Required |
|-------|--------|------------|----------|
| **Last updated** | `YYYY-MM-DD` | Valid date, not future | YES |
| **Session** | `YYYY-XXXX-NNN` | Year-Category-Sequence | YES |

**Session ID Format:**

- `YYYY` — Four-digit year
- `XXXX` — Category code (e.g., `INFRA`, `FEAT`, `BUG`, `ARCH`)
- `NNN` — Sequence number (001-999)

**Valid categories:**

- `INFRA` — Infrastructure work
- `FEAT` — Feature development
- `BUG` — Bug investigation
- `ARCH` — Architectural decisions
- `MAINT` — Maintenance tasks
- `DOC` — Documentation work

---

### Active Context

```markdown
## Active Context

### Current Task

**Task:** [Description]
**Status:** `[status]`
**Feasibility:** F[0-5]
**Started:** YYYY-MM-DD

### Working Files

- `path/to/file.ext`

### Recent Decisions

| Decision | Ruling | Vote | Date |
|----------|--------|------|------|
```

#### Current Task Fields

| Field | Format | Validation | Required |
|-------|--------|------------|----------|
| **Task** | Free text | Non-empty, max 200 chars | YES |
| **Status** | Enum | See status values | YES |
| **Feasibility** | `F[0-5]` | Valid feasibility level | YES |
| **Started** | `YYYY-MM-DD` | Valid date, not future | YES |

**Valid Status Values:**

- `not_started` — Task defined but not begun
- `in_progress` — Active work underway
- `blocked` — Waiting on dependency
- `completed` — Task finished
- `abandoned` — Task cancelled

#### Working Files

| Constraint | Rule |
|------------|------|
| Format | Relative path from workspace root |
| Existence | Files SHOULD exist (warning if not) |
| Maximum | 10 files per session |

#### Recent Decisions

| Column | Format | Validation | Required |
|--------|--------|------------|----------|
| **Decision** | Free text | Non-empty, max 100 chars | YES |
| **Ruling** | Free text | Non-empty, max 50 chars | YES |
| **Vote** | `X-Y-Z` | Three integers, sum ≤ 6 | YES |
| **Date** | `YYYY-MM-DD` | Valid date | YES |

---

### Pending Matters

```markdown
## Pending Matters

### Queued Deliberations

1. [Matter description]

### Open Questions

- [Question]

### Blocked Items

| Item | Blocked By | Since |
|------|------------|-------|
```

| Field | Format | Validation | Required |
|-------|--------|------------|----------|
| **Queued Deliberations** | Numbered list | May be empty | YES (section) |
| **Open Questions** | Bullet list | May be empty | YES (section) |
| **Blocked Items** | Table | May be empty | YES (section) |

---

### Session Memory

```markdown
## Session Memory

### Key Context

- [Critical information]

### Assumptions in Effect

- [Working assumption]

### Technical Debt Acknowledged

| Debt | Accepted | Reason | Priority |
|------|----------|--------|----------|
```

| Field | Validation | Required |
|-------|------------|----------|
| **Key Context** | Bullet list, may be empty | YES (section) |
| **Assumptions in Effect** | Bullet list, may be empty | YES (section) |
| **Technical Debt Acknowledged** | Table, may be empty | YES (section) |

#### Technical Debt Table

| Column | Format | Validation |
|--------|--------|------------|
| **Debt** | Free text | Non-empty, max 100 chars |
| **Accepted** | `YYYY-MM-DD` | Valid date |
| **Reason** | Free text | Non-empty, max 200 chars |
| **Priority** | Enum | `HIGH`, `MEDIUM`, `LOW` |

---

### Prophet Tracker

```markdown
## Prophet Tracker

### Pending Hail-Marys

| Proposal | Session | Status |
|----------|---------|--------|

### Vindication Record

**Total Vindications:** [N]
**Vindication Rate:** [X.X%] or N/A
```

| Field | Format | Validation | Required |
|-------|--------|------------|----------|
| **Pending Hail-Marys** | Table | May be empty | YES (section) |
| **Total Vindications** | Integer | ≥ 0 | YES |
| **Vindication Rate** | Percentage or `N/A` | Valid if vindications > 0 | YES |

#### Pending Hail-Marys Table

| Column | Format | Validation |
|--------|--------|------------|
| **Proposal** | Free text | Non-empty, max 100 chars |
| **Session** | Session ID | Valid session format |
| **Status** | Enum | `Pending`, `Deferred`, `Vindicated`, `Rejected` |

---

### SME Activity

```markdown
## SME Activity

### Active Specialists

- [domain]-specialist (or "[None seated]")

### Recent Witnesses

| Domain | Matter | Confidence |
|--------|--------|------------|
```

| Field | Format | Validation | Required |
|-------|--------|------------|----------|
| **Active Specialists** | Bullet list | Max 2 specialists | YES (section) |
| **Recent Witnesses** | Table | May be empty | YES (section) |

**Valid SME Domains:**

- `security`
- `database`
- `compliance`
- `infrastructure`
- `performance`
- `accessibility`
- `ux` (witness only)
- `legal` (witness only)

**Confidence Levels:**

- `HIGH`
- `MEDIUM`
- `LOW`

---

### Session Metrics

```markdown
## Session Metrics

| Metric | Value |
|--------|-------|
| Deliberations This Session | [N] |
| Decisions Made | [N] |
| Implementations Completed | [N] |
| Prophet Proposals | [N] |
| SMEs Consulted | [N] |
```

| Metric | Type | Validation |
|--------|------|------------|
| **Deliberations This Session** | Integer | ≥ 0 |
| **Decisions Made** | Integer | ≥ 0 |
| **Implementations Completed** | Integer | ≥ 0 |
| **Prophet Proposals** | Integer | ≥ 0 |
| **SMEs Consulted** | Integer | ≥ 0 |

---

### Notes (Optional)

```markdown
## Notes

[Freeform text]
```

No validation requirements. Freeform observations by the Scribe.

---

## Validation Rules

### Document-Level Rules

| Rule | Constraint |
|------|------------|
| **V1** | All required sections must be present |
| **V2** | Sections must appear in specified order |
| **V3** | Header must be first content after title |
| **V4** | Document must end with closing quote block |

### Cross-Field Rules

| Rule | Constraint |
|------|------------|
| **V5** | `Last updated` ≤ current date |
| **V6** | `Started` ≤ `Last updated` |
| **V7** | `Decisions Made` ≤ `Deliberations This Session` |
| **V8** | Active Specialists count ≤ 2 |
| **V9** | Vote tallies must sum to ≤ total voters (4 + specialists) |
| **V10** | Prophet vindication rate = (vindications / total proposals) × 100 |

### Integrity Rules

| Rule | Constraint |
|------|------------|
| **V11** | If status is `completed`, there should be recent decisions |
| **V12** | If deliberations > 0, decisions should be > 0 |
| **V13** | Blocked items should have valid dates |
| **V14** | Technical debt priority must be valid enum |

---

## Examples

### Valid Minimal State

```markdown
# MORNINGSTAR Session State

> *Last updated: 2026-02-15*
> *Session: 2026-MAINT-001*

---

## Active Context

### Current Task

**Task:** Session initialization test
**Status:** `not_started`
**Feasibility:** F1
**Started:** 2026-02-15

### Working Files

- `state/current.md`

### Recent Decisions

| Decision | Ruling | Vote | Date |
|----------|--------|------|------|
| - | - | - | - |

---

## Pending Matters

### Queued Deliberations

*None pending.*

### Open Questions

*None open.*

### Blocked Items

| Item | Blocked By | Since |
|------|------------|-------|
| - | - | - |

---

## Session Memory

### Key Context

*New session.*

### Assumptions in Effect

*None established.*

### Technical Debt Acknowledged

| Debt | Accepted | Reason | Priority |
|------|----------|--------|----------|
| - | - | - | - |

---

## Prophet Tracker

### Pending Hail-Marys

| Proposal | Session | Status |
|----------|---------|--------|
| - | - | - |

### Vindication Record

**Total Vindications:** 0
**Vindication Rate:** N/A

---

## SME Activity

### Active Specialists

- [None seated]

### Recent Witnesses

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

> *"The state persists. The court endures. The work continues."*
> — MORNINGSTAR::SCRIBE
```

### Invalid State Examples

#### Missing Required Section

```markdown
# MORNINGSTAR Session State

> *Last updated: 2026-02-15*
> *Session: 2026-INFRA-001*

## Active Context
...

## Pending Matters
...

## Session Memory
...

## Prophet Tracker
...

## Session Metrics  ❌ Missing SME Activity section
...
```

**Error:** `VALIDATION_ERROR: Required section 'SME Activity' missing`

#### Invalid Status Value

```markdown
### Current Task

**Task:** Fix authentication bug
**Status:** `working`  ❌ Invalid status
**Feasibility:** F2
**Started:** 2026-02-15
```

**Error:** `VALIDATION_ERROR: Invalid status 'working'. Valid values: not_started, in_progress, blocked, completed, abandoned`

#### Future Date

```markdown
> *Last updated: 2027-01-01*  ❌ Future date
> *Session: 2027-FEAT-001*
```

**Error:** `VALIDATION_ERROR: Last updated date cannot be in the future`

#### Invalid Vote Tally

```markdown
| Framework Enhancements | Adopted | 5-2-1 | 2026-02-15 |  ❌ Sum exceeds max voters
```

**Error:** `VALIDATION_ERROR: Vote tally 5-2-1 sums to 8, exceeds maximum voters (6)`

#### Invalid Session ID

```markdown
> *Session: 2026-15-001*  ❌ Invalid category
```

**Error:** `VALIDATION_ERROR: Invalid session category '15'. Valid categories: INFRA, FEAT, BUG, ARCH, MAINT, DOC`

---

## Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| Missing header | File doesn't start with `# MORNINGSTAR Session State` | Add header |
| Stale date | `Last updated` is old | Run `/update` to refresh |
| Section order | Sections not in canonical order | Reorder sections |
| Empty required field | Task or status is blank | Fill in required values |
| Invalid enum | Status, priority, or confidence not in allowed set | Use valid enum value |
| Vote overflow | Vote tally exceeds possible voters | Correct vote count |

---

## Recovery

If state validation fails:

1. **Check `CHANGELOG.md`** for recent decisions
2. **Check `courtroom/transcripts/`** for deliberation records
3. **Reconstruct state** from available evidence
4. **Use recovery protocol** in `core/error-recovery.md`

Do not attempt to initialize a session with invalid state. The court requires solid ground.

---

> *"A state file is a promise. Validate it, or break it."*  
> — MORNINGSTAR::DEBUGGER
