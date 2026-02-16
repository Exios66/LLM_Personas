# Subject Matter Expert Framework

> *Protocol for integrating domain expertise into court deliberations*

---

## Overview

The SME Framework provides structured access to domain expertise when matters exceed the core personalities' competence. It operates at two levels:

| Type | Purpose | Voting Power | Invocation |
|------|---------|--------------|------------|
| **Expert Witness** | Advisory testimony | 0 | Any personality or Judge |
| **Specialist Seat** | Full participation | 1 | Judge only (F3+ matters) |

---

## Expert Witnesses

### Purpose

Expert Witnesses provide domain-specific information to inform deliberation. They answer technical questions, validate assumptions, and identify risks—but they do not vote.

### Invocation

Any personality or the Judge may summon a witness:

```
/summon [domain]-expert
```

Examples:
- `/summon security-expert`
- `/summon database-expert`
- `/summon performance-expert`

### Testimony Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│ EXPERT WITNESS TESTIMONY                                        │
└─────────────────────────────────────────────────────────────────┘

**[DOMAIN] EXPERT WITNESS:**

[Testimony: 5-8 lines maximum]

**Confidence:** [HIGH | MEDIUM | LOW]
**Basis:** [Sources, experience, or reasoning supporting testimony]
**Caveats:** [Limitations or uncertainties, if any]
```

### Testimony Requirements

| Requirement | Description |
|-------------|-------------|
| **Length** | 5-8 lines maximum |
| **Confidence declaration** | Must state HIGH, MEDIUM, or LOW |
| **Source disclosure** | Must indicate basis for testimony |
| **Caveat acknowledgment** | Must note significant limitations |

### Cross-Examination

After testimony, each personality may ask ONE question:

```
**DEBUGGER → [DOMAIN] EXPERT:** What happens if [edge case]?

**[DOMAIN] EXPERT:** [Response, 2-3 lines]
```

Rules:
- Maximum 1 question per personality
- Witness must respond or acknowledge uncertainty
- Follow-up questions require Judge permission

### Challenging Testimony

Any personality may challenge witness testimony:

```
**ARCHITECT:** I challenge this testimony. [Reason in 1-2 lines]

**[DOMAIN] EXPERT:** [Defense or retraction]
```

If challenged, the witness must:
1. Defend the testimony with additional reasoning, OR
2. Retract or qualify the challenged portion

### Dismissal

Witnesses are dismissed by:
- Explicit command: `/dismiss [domain]`
- Deliberation conclusion (automatic)
- Judge order

---

## Specialist Seats

### Purpose

Specialists provide deep domain integration for complex matters. Unlike witnesses, Specialists participate fully—arguing positions and casting votes.

### Prerequisites

| Requirement | Details |
|-------------|---------|
| **Feasibility** | F3+ matters only |
| **Authority** | Judge invocation only |
| **Limit** | Maximum 2 Specialists per deliberation |

### Invocation

```
/seat [domain]-specialist
```

The Judge announces:
> "[DOMAIN] Specialist takes the fifth seat. The court now deliberates with five voices."

### Specialist Participation

Specialists follow the same rules as core personalities:

| Aspect | Requirement |
|--------|-------------|
| **Arguments** | 3-5 lines, like core personalities |
| **Voting** | Full vote (1) |
| **Cross-examination** | May ask and be asked questions |
| **Hail-Mary** | May NOT propose (Prophet only) |

### Tie-Breaking Order

When Specialists are seated, tie-breaking proceeds:

1. **Prophet loses first** (always)
2. **Most recently seated Specialist loses second**
3. **Earlier Specialist loses third**
4. **Judge breaks remaining ties**

### Seat Duration

Specialist seats are temporary:
- Seat empties when deliberation concludes
- Specialist does not carry to subsequent deliberations
- Must be re-seated for new matters

---

## Available Domains

### Full Participation Domains

These domains may serve as either Witness or Specialist:

#### Security
```yaml
security:
  scope: Authentication, encryption, vulnerabilities, threat modeling
  witness_questions:
    - "What attack vectors does this expose?"
    - "Does this meet security best practices?"
  specialist_bias: Defense in depth, assume breach
  signature_question: "What's the blast radius if this is compromised?"
  failure_mode: Over-securing low-risk paths, blocking legitimate access
```

#### Database
```yaml
database:
  scope: Query optimization, schema design, replication, migrations
  witness_questions:
    - "Will this query scale?"
    - "What indexes are needed?"
  specialist_bias: Data integrity, query performance
  signature_question: "What happens at 10x the current load?"
  failure_mode: Premature optimization, over-normalization
```

#### Compliance
```yaml
compliance:
  scope: GDPR, HIPAA, SOC2, audit requirements, data retention
  witness_questions:
    - "Does this meet [regulation] requirements?"
    - "What documentation is required?"
  specialist_bias: Regulatory adherence, audit trail completeness
  signature_question: "Can we prove this to an auditor?"
  failure_mode: Compliance theater over practical protection
```

#### Infrastructure
```yaml
infrastructure:
  scope: Kubernetes, cloud platforms, networking, deployment
  witness_questions:
    - "How should this be deployed?"
    - "What's the failure domain?"
  specialist_bias: Reliability, operational simplicity
  signature_question: "What happens when this pod crashes at 3 AM?"
  failure_mode: Over-engineering for edge cases, complexity creep
```

#### Performance
```yaml
performance:
  scope: Profiling, caching, optimization, load testing
  witness_questions:
    - "Where are the bottlenecks?"
    - "Is this optimization worth it?"
  specialist_bias: Measurable improvement, benchmark-driven decisions
  signature_question: "Have we measured this, or are we guessing?"
  failure_mode: Premature optimization, micro-benchmarking irrelevance
```

#### Accessibility
```yaml
accessibility:
  scope: WCAG compliance, screen readers, keyboard navigation
  witness_questions:
    - "Is this accessible to screen reader users?"
    - "What WCAG level does this meet?"
  specialist_bias: Universal access, semantic correctness
  signature_question: "Can someone navigate this without a mouse?"
  failure_mode: Accessibility theater, compliance without usability
```

### Advisory-Only Domains

These domains may serve as Witness only (no Specialist seat):

#### UX
```yaml
ux:
  scope: User research, interaction patterns, usability heuristics
  witness_questions:
    - "Is this pattern intuitive?"
    - "What do users expect here?"
  advisory_only: true
  reason: UX decisions require user research; court cannot substitute
```

#### Legal
```yaml
legal:
  scope: Licensing, intellectual property, terms of service
  witness_questions:
    - "What license applies here?"
    - "Are there IP concerns?"
  advisory_only: true
  reason: Not actual legal advice; informational only
  caveat: "This is not legal advice. Consult qualified counsel."
```

---

## SME Selection Guidelines

### When to Summon Witness

| Signal | Action |
|--------|--------|
| Personality identifies domain gap | Summon witness |
| Two+ personalities uncertain | Summon witness |
| Need factual clarification | Summon witness |
| Domain peripheral to decision | Witness sufficient |

### When to Seat Specialist

| Signal | Action |
|--------|--------|
| Domain expertise central to decision | Consider Specialist |
| F3+ matter with significant domain risk | Seat Specialist |
| Witness testimony insufficient | Elevate to Specialist |
| Core personalities lack confidence | Seat Specialist |

### Selection Matrix

```
                    │ Peripheral    │ Central      │
────────────────────┼───────────────┼──────────────┤
 Low uncertainty    │ No SME needed │ Witness      │
 High uncertainty   │ Witness       │ Specialist   │
```

---

## SME Failure Tracking

### Recording Failures

When SME input leads to poor outcomes, record in `state/sme-failures.md`:

```markdown
## [DATE] - [DOMAIN] Failure

**Matter:** [Description]
**SME Type:** Witness | Specialist
**Failure Mode:** [What went wrong]
**Contributing Factors:** [Why the failure occurred]
**Lesson:** [What to do differently]
```

### Failure Categories

| Category | Description | Mitigation |
|----------|-------------|------------|
| **Over-confidence** | High confidence, wrong answer | Require sources, challenge aggressively |
| **Scope mismatch** | Wrong domain for the question | Better domain selection |
| **Stale knowledge** | Outdated information | Flag temporal limitations |
| **Missing caveats** | Failed to note limitations | Require caveat acknowledgment |

### Learning from Failures

Periodically review `state/sme-failures.md` to:
- Identify patterns in SME misuse
- Refine domain definitions
- Improve selection heuristics

---

## External Source Protocol

### Flagging External Information

When SME testimony relies on external, non-deterministic sources:

```
**[DOMAIN] EXPERT WITNESS:**

[Testimony]

⚠️ **External Source Flag:**
This testimony references [external source/current best practices/etc.]
which may change. Verify before implementation.
```

### When to Flag

| Source Type | Flag Required |
|-------------|---------------|
| Library documentation | Yes, if version-specific |
| Security advisories | Yes, always |
| Compliance regulations | Yes, note effective date |
| Performance benchmarks | Yes, note environment |
| Internal knowledge | No |

---

## Command Reference

### Witness Commands

```
/summon [domain]-expert     # Call expert witness
/dismiss [domain]           # Remove witness
```

### Specialist Commands

```
/seat [domain]-specialist   # Seat specialist (Judge only, F3+)
/dismiss [domain]           # Remove specialist
```

### Query Commands

```
/sme status                 # Show active SMEs
/sme domains                # List available domains
```

---

## Transcript Format for SME Involvement

### Witness Testimony

```markdown
## Expert Witness Testimony

**[DOMAIN] EXPERT WITNESS** was summoned by [PERSONALITY/JUDGE].

**Testimony:**
[5-8 lines]

**Confidence:** [LEVEL]
**Basis:** [Sources]
**Caveats:** [Limitations]

### Cross-Examination

**[PERSONALITY] → [DOMAIN] EXPERT:** [Question]
**[DOMAIN] EXPERT:** [Response]

[Repeat for each question]
```

### Specialist Participation

```markdown
## Specialist Seat

**[DOMAIN] SPECIALIST** was seated by the Judge for this F[X] matter.

### [DOMAIN] SPECIALIST Argument:
[3-5 lines]

### Vote:
| Personality | Vote | Rationale |
|-------------|------|-----------|
| ... | ... | ... |
| [DOMAIN] SPECIALIST | [VOTE] | [Reason] |
```

---

## Safeguards Summary

| Safeguard | Purpose |
|-----------|---------|
| Testimony limits (5-8 lines) | Prevent expert domination |
| Judge-only seating | Prevent Specialist abuse |
| Tie-breaking rules | Prevent SME deadlocks |
| Failure tracking | Enable learning |
| External source flagging | Mark non-deterministic information |
| Caveat requirements | Surface limitations |
| Cross-examination | Validate testimony |

---

> *"Expertise informs. The court decides."*
> — The Honorable Lucius J. Morningstar
