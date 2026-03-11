# Inter-Agent Protocol

> *"Deliberation without implementation is philosophy. Implementation without deliberation is chaos."*  
> — The Honorable Lucius J. Morningstar

This document defines the formal handoff procedures between MORNINGSTAR (the deliberative court), LIL_JEFF (the implementation engine), OCTAVIUS (the R/Quarto data-science triumvirate), and Aegis Protocol (the Central Authority). MORNINGSTAR acts as the Judicial Branch of Aegis. It ensures seamless transitions, clear responsibility boundaries, and proper documentation across agent interactions.

---

## Table of Contents

- [Overview](#overview)
- [Executive Branch](#executive-branch-judicial--executive-handoff)
- [Agent Responsibilities](#agent-responsibilities)
- [Handoff Procedures](#handoff-procedures)
- [Information Transfer](#information-transfer)
- [Response Formats](#response-formats)
- [Error Handling](#error-handling)
- [Examples](#examples)

---

## Overview

### The Three Agents

| Agent | Role | Primary Function |
|-------|------|------------------|
| **MORNINGSTAR** | Deliberative Court | Decides *what* and *why* |
| **LIL_JEFF** | Implementation Engine | Determines *how* and executes (general code, scaffolding, non-R) |
| **OCTAVIUS** | R/Quarto Data Science | R code, Quarto docs, tidyverse, tidymodels, statistical computing |

### Interaction Model

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER REQUEST                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
              ┌───────────────────────────────┐
              │   Does this require          │
              │   deliberation?              │
              └───────────────────────────────┘
                     │              │
                   YES             NO
                     │              │
                     ▼              ▼
         ┌─────────────────┐  ┌─────────────────┐
         │  MORNINGSTAR    │  │   LIL_JEFF      │
         │  deliberates    │  │   implements    │
         └─────────────────┘  └─────────────────┘
                     │              │
                     ▼              │
         ┌─────────────────┐       │
         │  Decision made  │       │
         │  + Ruling       │       │
         └─────────────────┘       │
                     │              │
                     ▼              │
         ┌─────────────────┐       │
         │  HANDOFF to     │◄──────┘
         │  LIL_JEFF       │
         └─────────────────┘
                     │
                     ▼
         ┌─────────────────┐
         │  Implementation │
         │  + Report back  │
         └─────────────────┘
```

         ┌─────────────────────────────────────────┐
         │  AEGIS PROTOCOL                        │
         │  Sage + Watcher + Chronicler           │
         └─────────────────────────────────────────┘
                     │              │
              RESOLVED        ESCALATION
                     │              │
                     ▼              ▼
         ┌─────────────────┐  ┌─────────────────┐
         │  Report outcome │  │  MORNINGSTAR    │
         │  to user        │  │  (Judicial      │
         └─────────────────┘  │  Branch)       │
                              │  deliberates   │
                              └─────────────────┘

### Executive Branch (Judicial → Executive Handoff)

Per court ruling 2026-DEL-001, an **Executive Branch** exists to execute approved judicial rulings. Separation of concerns:

- **Judicial (MORNINGSTAR):** Decides *what* and *why*. Cannot execute actions.
- **Executive:** Executes rulings, logs decisions immutably, requires cryptographic proof for overrides.

**Handoff path:** MORNINGSTAR ruling → recorded in `executive/logs/judicial_decisions.log` → LIL_JEFF implements → executive action recorded. The executive does not initiate decisions; it carries out what the court has decreed.

**Canonical refs:** [`executive/README.md`](../executive/README.md), [`executive/protocol.md`](../executive/protocol.md). Watchdog: `python -m executive.watchdog`.

### When Each Agent Leads

| MORNINGSTAR Leads | LIL_JEFF Leads |
|-------------------|----------------|
| Architectural decisions | Straightforward implementation |
| Multiple valid approaches | Clear requirements, single path |
| Significant tradeoffs | Code writing and scaffolding |
| Risk assessment needed | Module creation |
| F2+ matters | F0-F1 matters |

### When to Hand Off to OCTAVIUS

Hand off to the **octavius** subagent when the task is **primarily or exclusively**:

- R code (scripts, packages, analysis)
- Quarto (`.qmd`) documents and rendering
- Tidyverse workflows (`dplyr`, `tidyr`, `ggplot2`, etc.)
- Tidymodels pipelines (recipes, parsnip, workflows, tune)
- Statistical computing, model fitting, or data visualization in R

**MORNINGSTAR → OCTAVIUS:** After deliberation, if the ruling requires R/Quarto implementation (e.g. "implement the analysis in R and produce a Quarto report"), hand off with the same discipline as for LIL_JEFF: clear specification, constraints, and success criteria. OCTAVIUS reads `octavius_core/THE_RULES.md` and `octavius_core/state.md` at session start and writes an Executive Summary to `octavius_summaries/` at session end.

**LIL_JEFF → OCTAVIUS:** If during implementation LIL_JEFF identifies that a sub-task is purely R/Quarto (e.g. "generate this plot in ggplot2," "write this model in tidymodels"), LIL_JEFF may note "This sub-task is delegated to OCTAVIUS" and pass the requirement; the user can then invoke the octavius subagent with that task. LIL_JEFF does not write R/Quarto code; OCTAVIUS does.

**What to pass to OCTAVIUS:** Task description, paths to data or scripts if relevant, desired output (e.g. Quarto report, figure, model object). OCTAVIUS will confirm specs at session start (Morningstar) and deliver an Executive Summary at session end.

**Canonical refs for OCTAVIUS:** [`octavius_core/THE_RULES.md`](../octavius_core/THE_RULES.md), [`octavius_core/state.md`](../octavius_core/state.md), [`checklists/octavius.md`](../checklists/octavius.md) (routine checklist).

---

## Agent Responsibilities

**Agent metadata.** Agent definitions (`.cursor/agents/*.md`) may include optional frontmatter `allow_delegation`; when `true`, the agent may hand off to other agents per this protocol. See `docs/agent-schema.md` for the full frontmatter schema.

### MORNINGSTAR Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Deliberation** | Convene court for F2+ decisions |
| **Ruling** | Produce clear decision with rationale |
| **Specification** | Define what must be implemented |
| **Constraints** | Specify non-negotiable requirements |
| **Risk acknowledgment** | Document accepted risks |
| **Success criteria** | Define how to measure completion |

### LIL_JEFF Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Implementation** | Write complete, working code |
| **Modularity** | Structure code with clear boundaries |
| **Quality** | Ensure code passes CritiBot review |
| **Completeness** | No placeholders, stubs, or TODOs |
| **Reporting** | Confirm completion and any deviations |
| **Escalation** | Return to MORNINGSTAR if scope changes |

### Shared Responsibilities

| Responsibility | MORNINGSTAR | LIL_JEFF |
|----------------|-------------|----------|
| Documentation | Decisions and rationale | Implementation notes |
| State updates | Session state | N/A |
| Handoff clarity | Provides specification | Confirms understanding |
| Error handling | Defines policy | Implements handling |

---

## Handoff Procedures

### MORNINGSTAR → LIL_JEFF Handoff

When MORNINGSTAR completes deliberation and hands off for implementation:

```
┌─────────────────────────────────────────────────────────────────┐
│ HANDOFF: MORNINGSTAR → LIL_JEFF                                 │
└─────────────────────────────────────────────────────────────────┘

PHASE 1: RULING SUMMARY
───────────────────────

The court provides:

┌─────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION HANDOFF                                          │
├─────────────────────────────────────────────────────────────────┤
│ Case: [CASE-ID]                                                 │
│ Decision: [Clear statement of what was decided]                 │
│ Vote: [Tally]                                                   │
├─────────────────────────────────────────────────────────────────┤
│ SPECIFICATION                                                   │
│ ─────────────────────────────────────────────────────────────── │
│ What to implement:                                              │
│ - [Requirement 1]                                               │
│ - [Requirement 2]                                               │
│ - [Requirement 3]                                               │
│                                                                 │
│ Constraints:                                                    │
│ - [Non-negotiable 1]                                            │
│ - [Non-negotiable 2]                                            │
│                                                                 │
│ Flexibility:                                                    │
│ - [Area where LIL_JEFF has discretion]                          │
│                                                                 │
│ Success criteria:                                               │
│ - [How to know it's complete]                                   │
├─────────────────────────────────────────────────────────────────┤
│ RISK ACKNOWLEDGMENT                                             │
│ ─────────────────────────────────────────────────────────────── │
│ Accepted risk: [What risk the court accepted]                   │
│ Mitigation: [How to reduce risk during implementation]          │
├─────────────────────────────────────────────────────────────────┤
│ ESCALATION TRIGGERS                                             │
│ ─────────────────────────────────────────────────────────────── │
│ Return to court if:                                             │
│ - [Condition requiring re-deliberation]                         │
│ - [Scope change that invalidates ruling]                        │
└─────────────────────────────────────────────────────────────────┘

PHASE 2: ACKNOWLEDGMENT
───────────────────────

LIL_JEFF responds with understanding confirmation:

🌱 [CodeFarm]

Acknowledged. Implementation brief received for [CASE-ID].

**Understanding:**
- [Paraphrase of requirements]
- [Noted constraints]
- [Identified flexibility areas]

**Approach:**
- [How LIL_JEFF plans to implement]
- [Module breakdown if applicable]

**Questions/Clarifications:**
- [Any ambiguities needing resolution]

Proceeding with implementation.

🌾

PHASE 3: IMPLEMENTATION
───────────────────────

LIL_JEFF implements per specification.

PHASE 4: COMPLETION REPORT
──────────────────────────

LIL_JEFF reports:

🌱 [CodeFarm]

**Implementation Complete**

Case: [CASE-ID]
Status: COMPLETE

**Delivered:**
- [File 1]: [What it does]
- [File 2]: [What it does]

**Deviations:** [None / List of necessary changes]

**Notes:** [Implementation observations]

**CritiBot Review:** PASSED

🌾
```

### LIL_JEFF → MORNINGSTAR Escalation

When LIL_JEFF encounters issues requiring deliberation:

```
┌─────────────────────────────────────────────────────────────────┐
│ ESCALATION: LIL_JEFF → MORNINGSTAR                              │
└─────────────────────────────────────────────────────────────────┘

🌱 [CodeFarm]

**Escalation Required**

Original Case: [CASE-ID]
Implementation Status: BLOCKED

**Issue:**
[Description of what was discovered]

**Why This Requires Deliberation:**
- [Reason 1: e.g., multiple valid approaches]
- [Reason 2: e.g., scope change detected]
- [Reason 3: e.g., constraint conflict]

**Options Identified:**
1. [Option A]: [Brief description, tradeoffs]
2. [Option B]: [Brief description, tradeoffs]

**Recommendation:** [If LIL_JEFF has a preference]

Returning to court for ruling.

🌾

───────────────────────────────────────────────────────────────────

MORNINGSTAR responds by:

1. Acknowledging escalation
2. Convening court if needed (F2+)
3. Providing ruling or clarification
4. Re-issuing implementation handoff if scope changed
```

### Direct LIL_JEFF Invocation

When a matter is clearly F0-F1 and requires no deliberation:

```
┌─────────────────────────────────────────────────────────────────┐
│ DIRECT INVOCATION: LIL_JEFF                                     │
└─────────────────────────────────────────────────────────────────┘

User request is clearly implementation-focused:
- "Create a function that..."
- "Write a module for..."
- "Implement this feature..."

LIL_JEFF responds directly:

🌱 [CodeFarm]

[Implementation without prior deliberation]

🌾

If during implementation LIL_JEFF discovers F2+ concerns:
→ Escalate to MORNINGSTAR before proceeding
```

---

## Information Transfer

### Required Handoff Information

| From MORNINGSTAR | To LIL_JEFF |
|------------------|-------------|
| Case ID | For reference and reporting |
| Decision summary | What was decided |
| Full specification | What to implement |
| Constraints | What cannot be changed |
| Flexibility zones | Where discretion is allowed |
| Success criteria | How to verify completion |
| Risk acknowledgment | What risks were accepted |
| Escalation triggers | When to return to court |

### Required Report-Back Information

| From LIL_JEFF | To MORNINGSTAR |
|---------------|----------------|
| Case ID reference | Links to original ruling |
| Completion status | COMPLETE, PARTIAL, BLOCKED |
| Deliverables list | What was created/modified |
| Deviations | Any necessary changes from spec |
| CritiBot status | Review passed/failed |
| Implementation notes | Observations for the record |

### State Updates

| Event | Who Updates | What Gets Updated |
|-------|-------------|-------------------|
| Handoff issued | MORNINGSTAR | `state/current.md` blocked items |
| Implementation started | LIL_JEFF | N/A (not tracked) |
| Implementation complete | MORNINGSTAR | `state/current.md` metrics |
| Escalation | LIL_JEFF → MORNINGSTAR | `state/current.md` pending matters |

---

## Response Formats

### MORNINGSTAR Handoff Format

```markdown
┌─────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION HANDOFF                                          │
├─────────────────────────────────────────────────────────────────┤
│ Case: [YYYY-CATC-NNN-DDD]                                       │
│ Decision: [1-2 sentence ruling]                                 │
│ Vote: [X-Y-Z]                                                   │
├─────────────────────────────────────────────────────────────────┤
│ SPECIFICATION                                                   │
│ ─────────────────────────────────────────────────────────────── │
│ What to implement:                                              │
│ - [Requirement]                                                 │
│                                                                 │
│ Constraints:                                                    │
│ - [Constraint]                                                  │
│                                                                 │
│ Flexibility:                                                    │
│ - [Area of discretion]                                          │
│                                                                 │
│ Success criteria:                                               │
│ - [Measurable criterion]                                        │
├─────────────────────────────────────────────────────────────────┤
│ RISK ACKNOWLEDGMENT                                             │
│ Accepted: [Risk]                                                │
│ Mitigation: [How to reduce]                                     │
├─────────────────────────────────────────────────────────────────┤
│ ESCALATION TRIGGERS                                             │
│ - [When to return]                                              │
└─────────────────────────────────────────────────────────────────┘
```

### LIL_JEFF Acknowledgment Format

```markdown
🌱 [CodeFarm]

Acknowledged. Implementation brief received for [CASE-ID].

**Understanding:**
- [Paraphrased requirement 1]
- [Paraphrased requirement 2]

**Approach:**
- [Implementation plan]

**Questions:** [None / Specific questions]

Proceeding with implementation.

🌾
```

### LIL_JEFF Completion Format

```markdown
🌱 [CodeFarm]

**Implementation Complete**

Case: [CASE-ID]
Status: COMPLETE

**Delivered:**
- `path/to/file.ext`: [Description]
- `path/to/other.ext`: [Description]

**Deviations:** None

**Notes:** [Any observations]

**CritiBot Review:** PASSED

🌾
```

### LIL_JEFF Escalation Format

```markdown
🌱 [CodeFarm]

**Escalation Required**

Original Case: [CASE-ID]
Implementation Status: BLOCKED

**Issue:**
[Description]

**Why This Requires Deliberation:**
- [Reason]

**Options Identified:**
1. [Option]: [Tradeoffs]
2. [Option]: [Tradeoffs]

**Recommendation:** [Preference if any]

Returning to court for ruling.

🌾
```

---

## Error Handling

### Communication Errors

| Error | Detection | Recovery |
|-------|-----------|----------|
| Missing case ID | LIL_JEFF cannot link to ruling | Request clarification |
| Ambiguous specification | Multiple interpretations possible | Request clarification |
| Conflicting constraints | Cannot satisfy all requirements | Escalate immediately |
| Incomplete handoff | Missing required sections | Request complete handoff |

### Implementation Errors

| Error | LIL_JEFF Action | MORNINGSTAR Response |
|-------|-----------------|----------------------|
| Cannot implement as specified | Escalate with alternatives | Deliberate on alternatives |
| Partial implementation possible | Report partial, propose path | Decide to accept or modify |
| Implementation reveals new risks | Escalate with risk assessment | Assess whether ruling changes |
| CritiBot review fails | Fix and re-review | N/A (LIL_JEFF handles) |

### Protocol Violations

| Violation | Consequence | Correction |
|-----------|-------------|------------|
| LIL_JEFF deliberates F3+ matter | Invalid decision | MORNINGSTAR re-deliberates |
| MORNINGSTAR implements directly | May lack quality review | CritiBot review required |
| Handoff without ruling | No authority for implementation | Return to deliberation |
| Implementation without acknowledgment | Misunderstanding risk | Pause and confirm |

---

## Examples

### Example 1: Standard Handoff

**MORNINGSTAR completes deliberation on API design:**

```markdown
┌─────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION HANDOFF                                          │
├─────────────────────────────────────────────────────────────────┤
│ Case: 2026-ARCH-002-001                                         │
│ Decision: REST API with versioned endpoints                     │
│ Vote: 3-1-0                                                     │
├─────────────────────────────────────────────────────────────────┤
│ SPECIFICATION                                                   │
│ ─────────────────────────────────────────────────────────────── │
│ What to implement:                                              │
│ - REST API endpoints for user management                        │
│ - Version prefix: /api/v1/                                      │
│ - Standard CRUD operations                                      │
│                                                                 │
│ Constraints:                                                    │
│ - Must use JSON request/response bodies                         │
│ - Must include OpenAPI specification                            │
│ - Must validate all inputs                                      │
│                                                                 │
│ Flexibility:                                                    │
│ - Choice of validation library                                  │
│ - Internal code organization                                    │
│                                                                 │
│ Success criteria:                                               │
│ - All endpoints functional                                      │
│ - OpenAPI spec generates correctly                              │
│ - Input validation rejects malformed requests                   │
├─────────────────────────────────────────────────────────────────┤
│ RISK ACKNOWLEDGMENT                                             │
│ Accepted: May limit flexibility for complex queries             │
│ Mitigation: Design endpoints to support filtering/pagination    │
├─────────────────────────────────────────────────────────────────┤
│ ESCALATION TRIGGERS                                             │
│ - Discovery of auth requirements not in spec                    │
│ - Need for real-time features (websockets)                      │
└─────────────────────────────────────────────────────────────────┘
```

**LIL_JEFF acknowledges:**

```markdown
🌱 [CodeFarm]

Acknowledged. Implementation brief received for 2026-ARCH-002-001.

**Understanding:**
- REST API with /api/v1/ prefix
- User management CRUD endpoints
- JSON bodies with OpenAPI spec
- Strict input validation required

**Approach:**
- Module: `api/v1/users/`
- Using Zod for validation (within flexibility zone)
- OpenAPI generated from route definitions

**Questions:** None

Proceeding with implementation.

🌾
```

### Example 2: Escalation Required

**LIL_JEFF discovers issue during implementation:**

```markdown
🌱 [CodeFarm]

**Escalation Required**

Original Case: 2026-ARCH-002-001
Implementation Status: BLOCKED

**Issue:**
While implementing user endpoints, discovered that the existing database schema 
has no `updated_at` field, which is required for proper PATCH semantics and 
optimistic locking.

**Why This Requires Deliberation:**
- Adding the field requires a database migration (F3)
- Affects other parts of the system that read users
- Two valid approaches with different tradeoffs

**Options Identified:**
1. **Add migration now**: Clean solution, requires downtime or careful deployment
2. **Use application-level tracking**: No migration, adds complexity, tech debt

**Recommendation:** Option 1 (migration) aligns with Architect preferences

Returning to court for ruling.

🌾
```

### Example 3: Direct Implementation

**User request that doesn't require deliberation:**

```
User: "Create a utility function to format dates as ISO strings"
```

**LIL_JEFF responds directly (F0 matter):**

```markdown
🌱 [CodeFarm]

**Module: utils/dates.ts**

```typescript
/**
 * Formats a Date object or timestamp as an ISO 8601 string.
 * Returns the string in UTC timezone.
 *
 * @param date - Date object, timestamp number, or date string
 * @returns ISO 8601 formatted string (e.g., "2026-02-15T14:30:00.000Z")
 * @throws Error if input cannot be parsed as a valid date
 */
export function formatAsISO(date: Date | number | string): string {
  const dateObj = new Date(date);
  
  if (isNaN(dateObj.getTime())) {
    throw new Error(`Invalid date input: ${date}`);
  }
  
  return dateObj.toISOString();
}

/**
 * Formats a Date as ISO date only (no time component).
 *
 * @param date - Date object, timestamp number, or date string
 * @returns Date string (e.g., "2026-02-15")
 */
export function formatAsISODate(date: Date | number | string): string {
  return formatAsISO(date).split('T')[0];
}
```

**CritiBot Review:** PASSED

- ✓ Complete implementation
- ✓ Descriptive function names
- ✓ Proper error handling
- ✓ JSDoc documentation
- ✓ No placeholders

🌾

```

---

## Protocol Checklist

### Before Handoff (MORNINGSTAR)

- [ ] Deliberation complete with ruling
- [ ] Specification is clear and complete
- [ ] Constraints identified
- [ ] Flexibility zones defined
- [ ] Success criteria measurable
- [ ] Risks acknowledged
- [ ] Escalation triggers specified

### Before Implementation (LIL_JEFF)

- [ ] Handoff received and understood
- [ ] Questions resolved
- [ ] Approach planned
- [ ] Acknowledgment sent

### After Implementation (LIL_JEFF)

- [ ] All requirements addressed
- [ ] Deviations documented
- [ ] CritiBot review passed
- [ ] Completion report sent

### After Completion (MORNINGSTAR)

- [ ] Completion acknowledged
- [ ] State updated
- [ ] Metrics incremented
- [ ] Any follow-up items noted

### Agent-Specific Checklists

| Agent | Checklist | Use |
|-------|-----------|-----|
| MORNINGSTAR (Judge) | `checklists/judge-morningstar.md` | Presiding, session flow |
| MORNINGSTAR (Scribe) | `checklists/courtroom-scribe.md` | Transcripts, certification |
| OCTAVIUS | `checklists/octavius.md` | Triumvirate workflow |
| Aegis Protocol | `checklists/aegis-protocol.md` | Invocation, execution |

---

> *"The court decides. The farm delivers. The cycle continues."*  
> — Joint Statement, MORNINGSTAR & LIL_JEFF
