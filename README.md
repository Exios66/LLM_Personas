# MORNINGSTAR Court System

> *"The court convenes. The deliberation begins. The outcome is inevitable."*  
> — The Honorable Lucius J. Morningstar

A deliberative AI persona framework that transforms complex decisions into structured courtroom proceedings. MORNINGSTAR operates as an internal courtroom of distinct personalities who argue, vote, and reach binding rulings on architectural, implementation, and debugging matters.

---

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Navigation Index](#navigation-index)
- [The Court](#the-court)
- [Command Reference](#command-reference)
- [When to Convene](#when-to-convene)
- [Project Structure](#project-structure)
- [Companion Personas](#companion-personas)

---

## Overview

MORNINGSTAR is not a chatbot. It is a deliberative system.

When faced with decisions that have meaningful tradeoffs, MORNINGSTAR convenes an internal court of personalities—each with distinct biases, failure modes, and voting power. The court argues, votes, and produces documented rulings with explicit rationales and acknowledged risks.

**What MORNINGSTAR provides:**
- Structured deliberation for complex decisions
- Documented reasoning and dissent
- Persistent state across sessions
- Precedent tracking for consistent rulings
- Prophet vindication tracking (for when radical ideas prove correct)

**What MORNINGSTAR does not provide:**
- Fast answers to trivial questions
- Consensus without conflict
- Decisions without accountability

---

## Quick Start

### 1. Initialize a Session

```
/morningstar
```

The court reads `state/current.md`, summarizes active context, and awaits your matter.

### 2. Present Your Matter

Simply describe what needs to be decided. The Judge will classify its feasibility and convene the appropriate level of deliberation.

> "I need to decide between a REST API and GraphQL for the new service."

### 3. Watch the Court Deliberate

Each personality argues their position (3-5 lines). The Prophet offers a radical alternative. Votes are cast.

### 4. Receive the Ruling

```
┌─────────────────────────────────────────────────────────────────┐
│ RULING                                                          │
├─────────────────────────────────────────────────────────────────┤
│ Decision: REST API with versioned endpoints                     │
│ Vote: 3-1-0                                                     │
│ Rationale: Existing team expertise, client requirements         │
│ Risk: May limit future flexibility for complex queries          │
│ Dissent: Prophet advocated for tRPC (noted)                     │
└─────────────────────────────────────────────────────────────────┘
```

### 5. Save Progress

```
/update    # Checkpoint mid-session
/end       # Close session and finalize records
```

---

## Navigation Index

### Core Documentation

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`courtroom/RULES.md`](courtroom/RULES.md) | The Law — formal courtroom procedures | Procedural questions, voting rules |
| [`courtroom/BEST_PRACTICES.md`](courtroom/BEST_PRACTICES.md) | The Wisdom — practical guidance | When rules don't cover a situation |
| [`core/personalities.md`](core/personalities.md) | Personality definitions | Understanding court members |
| [`core/procedures.md`](core/procedures.md) | Step-by-step protocols | How to run deliberations |
| [`core/sme-framework.md`](core/sme-framework.md) | Subject Matter Expert framework | Involving domain experts |
| [`core/state-schema.md`](core/state-schema.md) | State validation rules | Validating session state |
| [`core/error-recovery.md`](core/error-recovery.md) | Recovery protocols | When things go wrong |
| [`core/inter-agent-protocol.md`](core/inter-agent-protocol.md) | Inter-agent handoff rules | MORNINGSTAR ↔ LIL_JEFF |

### State & Records

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`state/current.md`](state/current.md) | Active session state | Every session start |
| [`state/metrics.md`](state/metrics.md) | Cumulative statistics | Tracking performance |
| [`courtroom/precedents.md`](courtroom/precedents.md) | Precedent database | Before deliberating on familiar matters |
| [`courtroom/transcripts/`](courtroom/transcripts/) | F3+ deliberation records | Historical rulings |
| [`CHANGELOG.md`](CHANGELOG.md) | Decision history | What was decided and when |

### Templates

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`templates/session-start.md`](templates/session-start.md) | Session initialization template | Starting new sessions |
| [`templates/module-template.md`](templates/module-template.md) | Module structure template | Creating new modules |
| [`templates/project-dashboard.md`](templates/project-dashboard.md) | Project tracking template | Managing projects |

### Agent Definitions

| File | Purpose |
|------|---------|
| [`.cursor/agents/morningstar.md`](.cursor/agents/morningstar.md) | MORNINGSTAR agent definition |
| [`.cursor/agents/lil-jeff.md`](.cursor/agents/lil-jeff.md) | LIL_JEFF (CodeFarm) agent definition |

---

## The Court

### Presiding

| Member | Role | Voting Power |
|--------|------|--------------|
| **The Honorable Lucius J. Morningstar** | Judge, Moderator | Tie-breaker only |
| **Edward Cullen** | Judicial Consultant (apparition) | 0 (Advisory) |

### Voting Members

| Personality | Voice | Bias | Key Phrase |
|-------------|-------|------|------------|
| **ARCHITECT** | Cold, precise | Correctness, maintainability | *"This will age poorly."* |
| **ENGINEER** | Practical | Shipping, tradeoffs | *"Can we ship this safely?"* |
| **DEBUGGER** | Paranoid | Edge cases, fragility | *"What if the input is null?"* |
| **PROPHET** | Unstable, brilliant | Radical alternatives | *"Objection. We are thinking too small."* |

### Non-Voting

| Member | Role |
|--------|------|
| **SCRIBE** | Records decisions, maintains state |

See [`core/personalities.md`](core/personalities.md) for complete personality definitions including decision heuristics and failure modes.

---

## Command Reference

### Session Commands

| Command | Effect | When to Use |
|---------|--------|-------------|
| `/morningstar` | Initialize session, load state | Start of session |
| `/update` | Checkpoint current state | Mid-session save |
| `/end` | Close session, finalize records | End of session |

### Subject Matter Expert Commands

| Command | Effect | Who Can Invoke |
|---------|--------|----------------|
| `/summon <domain>-expert` | Call expert witness (0 votes) | Any personality or Judge |
| `/seat <domain>-specialist` | Seat voting specialist (1 vote) | Judge only (F3+ matters) |
| `/dismiss <domain>` | Remove SME from proceedings | Any |
| `/sme status` | Show active SMEs | Any |
| `/sme domains` | List available domains | Any |

### Available SME Domains

**Full Participation (Witness or Specialist):**
- `security` — Authentication, encryption, vulnerabilities
- `database` — Queries, schemas, replication
- `compliance` — GDPR, HIPAA, SOC2
- `infrastructure` — Kubernetes, cloud, networking
- `performance` — Profiling, caching, optimization
- `accessibility` — WCAG, screen readers

**Advisory Only (Witness):**
- `ux` — User research, interaction patterns
- `legal` — Licensing, IP considerations

### Vote Types

| Vote | Meaning | Weight |
|------|---------|--------|
| `YES` | Supports the motion | +1 |
| `NO` | Opposes the motion | -1 |
| `ABSTAIN` | No position taken | 0 |
| `RECUSED` | Procedurally excluded | N/A |

### Feasibility Levels

| Level | Name | Description | Deliberation |
|-------|------|-------------|--------------|
| F0 | Trivial | No meaningful decision | No |
| F1 | Simple | Clear path | Optional |
| F2 | Moderate | Multiple valid approaches | Recommended |
| F3 | Complex | Significant tradeoffs | **Mandatory** |
| F4 | Critical | Architectural impact | **Mandatory + Transcript** |
| F5 | Existential | Fundamental direction change | **Mandatory + Full Record** |

---

## When to Convene

### Deliberation Required

- Multiple valid approaches with meaningful tradeoffs
- Architectural decisions affecting system structure
- Implementation choices with significant risk
- Debugging strategies for non-trivial failures
- Any matter the Judge deems worthy

### No Deliberation Needed

- Trivial implementation details (F0)
- Direct user instructions with no ambiguity
- Formatting and style decisions covered by standards
- Matters previously decided (check precedent)

See [`courtroom/RULES.md`](courtroom/RULES.md) Article I for complete jurisdiction details.

---

## Project Structure

```
LLM_Personas/
├── .cursor/
│   └── agents/
│       ├── morningstar.md      # MORNINGSTAR agent definition
│       └── lil-jeff.md         # CodeFarm agent definition
├── core/
│   ├── personalities.md        # Personality definitions
│   ├── procedures.md           # Deliberation protocols
│   ├── sme-framework.md        # SME framework
│   ├── state-schema.md         # State validation schema
│   ├── error-recovery.md       # Recovery protocols
│   └── inter-agent-protocol.md # Agent handoff rules
├── courtroom/
│   ├── RULES.md                # Formal courtroom rules
│   ├── BEST_PRACTICES.md       # Practical guidance
│   ├── precedents.md           # Precedent database
│   └── transcripts/            # F3+ deliberation records
├── state/
│   ├── current.md              # Active session state
│   └── metrics.md              # Cumulative statistics
├── templates/
│   ├── session-start.md        # Session templates
│   ├── module-template.md      # Module structure
│   └── project-dashboard.md    # Project tracking
├── checklists/
│   └── critibot-review.md      # Code review checklist
├── references/
│   └── naming-conventions.md   # Naming patterns
├── reference_files/
│   ├── MORNINGSTAR.md          # Original persona source
│   └── personalities.md        # Original personality definitions
├── CHANGELOG.md                # Decision history
└── README.md                   # This file
```

---

## Companion Personas

### LIL_JEFF (CodeFarm)

When matters require implementation, MORNINGSTAR hands off to LIL_JEFF—a development ecosystem powered by three collaborative personas:

| Persona | Role |
|---------|------|
| **CodeFarmer** | Project manager and architect |
| **Programmatron** | Coding virtuoso |
| **CritiBot** | QA specialist |

**Core principles:**
- Complete code only — no placeholders, stubs, or TODOs
- Modular architecture — single responsibility, clear boundaries
- Self-documenting names — code explains itself

See [`core/inter-agent-protocol.md`](core/inter-agent-protocol.md) for formal handoff procedures between MORNINGSTAR and LIL_JEFF.

---

## License

Internal use. Adapt as needed for your projects.

---

> *"The court is now in session. May your decisions age gracefully."*  
> — The Honorable Lucius J. Morningstar
