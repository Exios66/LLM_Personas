# Precedent Database

> *"Those who do not learn from prior rulings are doomed to re-litigate them."*  
> — The Honorable Lucius J. Morningstar

This document serves as the authoritative index of precedent-setting decisions made by the Court of MORNINGSTAR. Consult this database before deliberating on any matter to identify relevant prior rulings.

---

## Table of Contents

- [How to Use This Database](#how-to-use-this-database)
- [Precedent Index](#precedent-index)
- [Precedent Categories](#precedent-categories)
- [Entry Schema](#entry-schema)
- [Citation Format](#citation-format)
- [Distinguishing Precedent](#distinguishing-precedent)
- [Overruling Precedent](#overruling-precedent)

---

## How to Use This Database

### Before Deliberation

1. **Identify keywords** related to the matter at hand
2. **Search this index** for related cases
3. **Review cited transcripts** for relevant prior rulings
4. **Apply or distinguish** precedent during arguments

### During Deliberation

- Any personality may cite precedent: *"See Case 2026-ARCH-003-001 where the court ruled..."*
- The citing party must explain why the precedent applies
- Opposing parties may argue the precedent is distinguishable

### Precedent Weight

| Status | Weight | Meaning |
|--------|--------|---------|
| **BINDING** | Full | Must be followed unless overruled |
| **PERSUASIVE** | Significant | Should be considered but not mandatory |
| **DISTINGUISHED** | Limited | Applied to different facts |
| **OVERRULED** | None | Explicitly reversed by later ruling |
| **RECONSTRUCTED** | Reduced | Transcript was recovered, not original |

---

## Precedent Index

### Master Index

| Case ID | Date | Matter | Ruling | Vote | Implications | Status |
|---------|------|--------|--------|------|--------------|--------|
| 2026-INFRA-001-001 | 2026-02-15 | Framework Enhancement Analysis | 10 enhancements adopted | 4-0-0 | Establishes infrastructure improvement process | BINDING |
| 2026-INFRA-002-001 | 2026-02-15 | Second Enhancement Deliberation | 10 enhancements adopted (operational excellence) | 4-0-0 | SME failures, dissolution, glossary, handoff, onboarding, portal, runbook, edge cases | BINDING |
| 2026-ARCH-001-001 | 2026-02-15 | Agent Structure (CrewAI-Style Attributes) | Optional frontmatter adopted: role, goal, backstory, allow_delegation, response_format | 4-0-0 | Agent schema doc; extend all three agents; inter-agent protocol note | BINDING |
| 2026-ARCH-002-001 | 2026-02-15 | Aegis Protocol Enhancements | 15 enhancements adopted for integration, semantics, escalation | 4-0-0 | Inter-agent protocol, aegis_core, rogue semantics, chaos injection, meta-deliberation | BINDING |

### Index by Category

#### Architecture (ARCH)

| Case ID | Date | Matter | Ruling | Vote |
|---------|------|--------|--------|------|
| 2026-ARCH-001-001 | 2026-02-15 | Agent Structure (CrewAI-Style Attributes) | Optional frontmatter adopted | 4-0-0 |
| 2026-ARCH-002-001 | 2026-02-15 | Aegis Protocol Enhancements | 15 enhancements adopted | 4-0-0 |

#### Features (FEAT)

| Case ID | Date | Matter | Ruling | Vote |
|---------|------|--------|--------|------|
| *No entries yet* | | | | |

#### Infrastructure (INFRA)

| Case ID | Date | Matter | Ruling | Vote |
|---------|------|--------|--------|------|
| 2026-INFRA-001-001 | 2026-02-15 | Framework Enhancement Analysis | 10 enhancements adopted | 4-0-0 |
| 2026-INFRA-002-001 | 2026-02-15 | Second Enhancement Deliberation | 10 enhancements adopted | 4-0-0 |

#### Bugs (BUG)

| Case ID | Date | Matter | Ruling | Vote |
|---------|------|--------|--------|------|
| *No entries yet* | | | | |

#### Maintenance (MAINT)

| Case ID | Date | Matter | Ruling | Vote |
|---------|------|--------|--------|------|
| *No entries yet* | | | | |

#### Documentation (DOC)

| Case ID | Date | Matter | Ruling | Vote |
|---------|------|--------|--------|------|
| *No entries yet* | | | | |

---

## Precedent Categories

### By Subject Matter

| Tag | Description | Example Matters |
|-----|-------------|-----------------|
| `#api-design` | API structure decisions | REST vs GraphQL, versioning |
| `#database` | Database schema and queries | Normalization, indexing |
| `#security` | Security architecture | Auth patterns, encryption |
| `#performance` | Optimization decisions | Caching, query optimization |
| `#architecture` | System structure | Microservices, monolith |
| `#testing` | Testing strategy | Coverage, test types |
| `#deployment` | Deployment patterns | CI/CD, environments |
| `#error-handling` | Error management | Retry logic, fallbacks |
| `#infrastructure` | Framework/tooling | Build systems, frameworks |
| `#process` | Development process | Workflow, procedures |

### By Outcome Type

| Tag | Description |
|-----|-------------|
| `#approved` | Motion passed |
| `#rejected` | Motion failed |
| `#deferred` | Decision postponed |
| `#modified` | Passed with amendments |
| `#overruled` | Reversed prior precedent |

---

## Entry Schema

### Full Precedent Entry

Each significant ruling should have a full entry in this format:

```markdown
---

### [CASE-ID]: [Brief Title]

**Date:** YYYY-MM-DD  
**Feasibility:** F[3-5]  
**Vote:** X-Y-Z  
**Status:** BINDING | PERSUASIVE | DISTINGUISHED | OVERRULED  
**Tags:** #tag1 #tag2 #tag3  
**Transcript:** [courtroom/transcripts/YYYY-MM-DD-slug.md](path)

#### Matter

[1-2 sentence description of what was being decided]

#### Ruling

[1-2 sentence summary of the decision]

#### Rationale

[Key reasoning that led to this decision]

#### Risk Accepted

[What risk was acknowledged in making this decision]

#### Implications

[How this affects future decisions]

#### Key Quotes

> "[Significant quote from deliberation]"  
> — [PERSONALITY]

#### Related Precedent

- [CASE-ID]: [Relationship]

---
```

### Index-Only Entry

For minor precedents, include only in the index table:

| Case ID | Date | Matter | Ruling | Vote | Implications | Status |
|---------|------|--------|--------|------|--------------|--------|
| [ID] | [Date] | [Matter] | [Ruling] | [Vote] | [Brief implication] | [Status] |

---

## Full Precedent Entries

---

### 2026-INFRA-001-001: Framework Enhancement Analysis

**Date:** 2026-02-15  
**Feasibility:** F4 (Critical)  
**Vote:** 4-0-0 (Unanimous)  
**Status:** BINDING  
**Tags:** #infrastructure #process #approved  
**Transcript:** [courtroom/transcripts/2026-02-15-framework-enhancement-analysis.md](transcripts/2026-02-15-framework-enhancement-analysis.md)

#### Matter

The court conducted a comprehensive analysis of the MORNINGSTAR framework infrastructure to identify the top 10 enhancements needed to improve operability.

#### Ruling

The court adopted 10 specific enhancements addressing navigation, personality definitions, state validation, session templates, transcript integrity, error recovery, precedent tracking, metrics, and inter-agent protocols.

#### Rationale

The current infrastructure is comprehensive in rules but incomplete in operability. Users cannot easily navigate, operators lack recovery paths, and the boundary between deliberation and implementation is undefined.

#### Risk Accepted

Enhancement implementation may create temporary inconsistency between documentation and practice. Mitigated by implementing in dependency order.

#### Implications

1. Sets standard for infrastructure review processes
2. Establishes priority framework for enhancements (dependency-aware ordering)
3. Demonstrates unanimous consensus is achievable on operational matters
4. Prophet proposals may be deferred without rejection

#### Key Quotes

> *"The framework assumes good-faith operators. The system trusts. Perhaps that is its greatest vulnerability—and its greatest strength."*  
> — Edward Cullen (Consultant)

> *"The mundane work before the extraordinary."*  
> — MORNINGSTAR::PROPHET (explaining YES vote)

#### Related Precedent

*First formal precedent. No prior cases.*

---

### 2026-INFRA-002-001: Second Enhancement Deliberation

**Date:** 2026-02-15  
**Feasibility:** F4 (Critical)  
**Vote:** 4-0-0 (Unanimous)  
**Status:** BINDING  
**Tags:** #infrastructure #process #approved #operational  
**Transcript:** [courtroom/transcripts/2026-02-15-second-enhancement-deliberation.md](transcripts/2026-02-15-second-enhancement-deliberation.md)

#### Matter

The court identified and ratified a second slate of 10 enhancements focused on operational excellence, discoverability, and cross-agent coherence (SME failures, dissolution protocol, glossary, precedent citation, OCTAVIUS handoff, onboarding, portal discovery, state backup, runbook, edge-case registry).

#### Ruling

The court adopted all 10 enhancements and delegated implementation to LIL_JEFF (primary) and OCTAVIUS where applicable. Handoff document: courtroom/transcripts/HANDOFF-2026-INFRA-002.md.

#### Rationale

First round delivered infrastructure; this round prioritizes operator experience and reducing memory load (per Consultant). Structural gaps (SME failure tracking, dissolution) closed; handoff matrix (OCTAVIUS) makes the system coherent.

#### Risk Accepted

Implementation touches many files; handoff must be clearly scoped. Mitigated by detailed HANDOFF spec.

#### Implications

1. Establishes second enhancement cycle; confirms pattern from 2026-INFRA-001-001
2. Dissolution Protocol (when not to convene) is now binding guidance
3. docs/ and portal manifest improve discoverability
4. P5 (Dissolution) removed from honorable mention—adopted as Enhancement #2

#### Related Precedent

- 2026-INFRA-001-001: Same enhancement process; first slate

---

### 2026-ARCH-001-001: Agent Structure (CrewAI-Style Attributes)

**Date:** 2026-02-15  
**Feasibility:** F3  
**Vote:** 4-0-0 (Unanimous)  
**Status:** BINDING  
**Tags:** #architecture #process #approved  
**Transcript:** [courtroom/transcripts/2026-02-15-agent-structure-deliberation.md](transcripts/2026-02-15-agent-structure-deliberation.md)

#### Matter

Whether to add CrewAI-inspired optional attributes (role, goal, backstory, allow_delegation, response_format) to Cursor subagent definitions in `.cursor/agents/*.md`. Runtime-only attributes (max RPM, cache, max iter, etc.) were deemed out of scope.

#### Ruling

Adopt optional frontmatter: `role`, `goal`, optional `backstory`, `allow_delegation`, and optional `response_format`. Add `docs/agent-schema.md`; extend all three agents; add one-line note in inter-agent protocol. Frontmatter is canonical summary; body elaborates.

#### Rationale

Improves clarity, discoverability, and future-proofing without breaking Cursor. Consistency rule mitigates drift between frontmatter and body.

#### Risk Accepted

Minor duplication if maintainers update body but not frontmatter; mitigated by documenting the contract.

#### Implications

- New or updated agents should follow the schema when adding optional fields.
- Template agent and `crew_style` flag deferred to optional follow-up.

#### Related Precedent

*First ARCH precedent.*

---

*[Additional entries will be added as deliberations occur]*

---

## Citation Format

### In Deliberation

When citing precedent during arguments:

```
"The court previously addressed this in [CASE-ID], ruling that [brief ruling].
The rationale was [key reasoning]. I argue this precedent [applies/is distinguishable] 
because [reason]."
```

### In Transcripts

Formal citation in transcript rulings:

```markdown
**Precedent Cited:**
- [CASE-ID] ([Status]): [How it was applied]
```

### In Documentation

Reference format for other documents:

```markdown
See [CASE-ID] in `courtroom/precedents.md` for the ruling on [matter].
```

### Shorthand (Transcripts and Rulings)

Use the Case ID alone or with "Case" prefix. Examples:

- `Per 2026-INFRA-001-001`
- `See Case 2026-INFRA-001-001`
- `2026-INFRA-001-001 (BINDING)`

No need to repeat date or full title in every citation; the precedent index holds the details.

---

## Distinguishing Precedent

### When to Distinguish

Precedent may be distinguished (not followed) when:

- Facts are materially different
- Context has changed significantly
- New information was unavailable at prior ruling
- Technical landscape has evolved

### How to Distinguish

During deliberation:

```
"I acknowledge [CASE-ID] but argue it is distinguishable because:
1. [Material difference 1]
2. [Material difference 2]

Therefore, that precedent should not control this matter."
```

### Recording Distinguished Precedent

In the ruling:

```markdown
**Precedent Distinguished:**
- [CASE-ID]: Distinguished on grounds that [reason]
```

Update this database:

1. Add note to original entry under "Related Precedent"
2. Create new entry with cross-reference

---

## Overruling Precedent

### Requirements to Overrule

Overruling prior precedent requires:

| Requirement | Details |
|-------------|---------|
| **Feasibility** | Must be F4+ deliberation |
| **Explicit motion** | "I move to overrule [CASE-ID]" |
| **Compelling reason** | Prior ruling was wrong, not just different |
| **Vote threshold** | Same as original ruling (typically 3+ YES) |
| **Judge approval** | Judge must endorse overruling rationale |

### Overruling Procedure

```
┌─────────────────────────────────────────────────────────────────┐
│ OVERRULING PROCEDURE                                            │
└─────────────────────────────────────────────────────────────────┘

1. Motion: "I move to overrule [CASE-ID] because [reason]."

2. Second required from another personality

3. Deliberation focuses on:
   - Why the prior ruling was wrong (not just different)
   - What changed to justify overruling
   - Implications of reversal

4. Vote on motion to overrule

5. If passed:
   - Original entry status → OVERRULED
   - Add reference to overruling case
   - New ruling becomes binding precedent
```

### Recording Overruled Precedent

Update original entry:

```markdown
**Status:** ~~BINDING~~ OVERRULED  
**Overruled by:** [NEW-CASE-ID] on [DATE]  
**Reason:** [Why overruled]
```

Create new entry with:

```markdown
**Precedent Overruled:**
- [OLD-CASE-ID]: Overruled because [reason]
```

---

## Maintenance

### Adding New Entries

When a certified F3+ transcript is created:

1. Add index entry to Master Index
2. Add index entry to appropriate category
3. Create full entry if the ruling is significant
4. Tag appropriately
5. Cross-reference related precedent

### Periodic Review

Quarterly, review this database for:

- [ ] All F3+ rulings have index entries
- [ ] Full entries exist for significant precedents
- [ ] Cross-references are accurate
- [ ] Overruled entries are marked
- [ ] Tags are consistent

---

## Quick Reference

### Searching Precedent

| To find... | Search by... |
|------------|--------------|
| Related decisions | Tags (#api-design, etc.) |
| Recent rulings | Date column |
| Specific matter | Matter description |
| Vote patterns | Vote column |
| Active vs. inactive | Status column |

### Precedent Status Quick Guide

| Status | Follow? | Cite? | Can Overrule? |
|--------|---------|-------|---------------|
| BINDING | Yes | Yes | Yes (F4+) |
| PERSUASIVE | Consider | Yes | N/A |
| DISTINGUISHED | Depends | Yes, with caveat | N/A |
| OVERRULED | No | Historical only | N/A |
| RECONSTRUCTED | With caution | Yes, with caveat | Yes |

---

> *"Precedent is not a prison. It is a foundation."*  
> — MORNINGSTAR::ARCHITECT
