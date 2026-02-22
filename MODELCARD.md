# 📋 Repository Card — LLM_Personas / MORNINGSTAR

-----

## Identity

|Field                  |Value                                                                        |
|-----------------------|-----------------------------------------------------------------------------|
|**Repository Name**    |`LLM_Personas`                                                               |
|**Full Title**         |The MORNINGSTAR Operational Agent Swarm                                      |
|**Author / Maintainer**|[@Exios66](https://github.com/Exios66)                                       |
|**Repository URL**     |https://github.com/Exios66/LLM_Personas                                      |
|**Primary Branch**     |`main`                                                                       |
|**License**            |Internal use — adapt freely for personal/organizational projects             |
|**Languages**          |HTML (53.6%) · Python (34.6%) · CSS (6.7%) · Shell (3.2%) · JavaScript (1.9%)|

-----

## Summary

MORNINGSTAR is a **deliberative AI persona framework** that reframes complex decisions as structured courtroom proceedings. Rather than querying a single model for an answer, the framework instantiates a panel of five distinct cognitive personalities — each with documented biases, failure modes, and voting power — who formally argue, deliberate, and reach binding rulings on architectural, implementation, and strategic matters.

The system is designed to work as a **Cursor AI agent**, a **local LLM workflow** (Ollama, LM Studio, OpenRouter), or any context where structured multi-perspective reasoning is valuable. It is not a conversational chatbot; it is a structured reasoning engine with institutional memory and procedural accountability.

-----

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     MORNINGSTAR FRAMEWORK                           │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                     THE COURT                                │  │
│  │                                                              │  │
│  │  Judge: Lucius J. Morningstar (tie-breaker only)            │  │
│  │  Consultant: Edward Cullen (advisory, 0 votes)              │  │
│  │                                                              │  │
│  │  Voting:  ARCHITECT · ENGINEER · DEBUGGER · PROPHET ·       │  │
│  │           COUNSEL  (each 1 vote, F3+ may add Specialists)   │  │
│  │                                                              │  │
│  │  Non-Voting: SCRIBE (records, state, transcripts)           │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌─────────────────┐   ┌──────────────┐   ┌───────────────────┐   │
│  │  MFAF Classifier│   │  SME Registry│   │  Precedent DB     │   │
│  │  F0 → F5        │   │  27 Domains  │   │  courtroom/       │   │
│  │  Risk Vectors   │   │  Witness +   │   │  precedents.md    │   │
│  │  Effort Bands   │   │  Specialist  │   │                   │   │
│  └─────────────────┘   └──────────────┘   └───────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              COMPANION AGENT ECOSYSTEM                      │   │
│  │                                                             │   │
│  │  LIL_JEFF (CodeFarm)  │  OCTAVIUS (R/Quarto)  │  AEGIS     │   │
│  │  CodeFarmer           │  Apollo               │  Protocol  │   │
│  │  Programmatron        │  Kronos               │  (Central  │   │
│  │  CritiBot             │  Morningstar          │  Authority)│   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  LITIGATION RUNNER — Local/Free LLM Support                   │ │
│  │  Ollama · LM Studio · OpenRouter                              │ │
│  │  run.py · launch.sh · providers/ · prompts/                   │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

-----

## Court Personalities — Detailed Profiles

### The Honorable Lucius J. Morningstar — *Judge*

The presiding authority of the court. Morningstar does not cast a vote in ordinary deliberations — his power is the tie-breaker and the final arbiter of procedural matters. He classifies matters by feasibility level (F0–F5), convenes the appropriate form of proceeding, and issues the certified ruling. His demeanor is formal, measured, and expectant of rigorous argument.

**Authority:** Tie-breaker vote 
* Seating Specialists (F3+)
* Issuing rulings
* Calling recess

-----

### ARCHITECT

The court’s voice of long-term correctness. ARCHITECT evaluates every proposal through the lens of maintainability, scalability, and future adaptability. Quick to identify decisions that will “age poorly” — technical debt disguised as pragmatism.

**Bias:** Correctness over speed · Long-term over short-term

**Failure Mode:** Over-engineers solutions to simple problems 
* Paralysis via theoretical purity

**Signature:** *“This will age poorly.”*

-----

### ENGINEER

The pragmatist. ENGINEER is focused on what can actually ship — safely, on time, and within the constraints of existing team capability. When ARCHITECT proposes elegant abstraction, ENGINEER asks whether it can be delivered.

**Bias:** Shipping 
* Practical tradeoffs: Real-world constraints
**Failure Mode:** Under-estimates long-term costs of quick fixes
**Signature:** *“Can we ship this safely?”*

-----

### DEBUGGER

The paranoid voice of edge cases. DEBUGGER scans every proposal for failure modes — null inputs, race conditions, network timeouts, adversarial data. Where others see a working solution, DEBUGGER sees what can break.

**Bias:** Fragility
* Edge cases: Error paths
**Failure Mode:** Surfaces edge cases that are astronomically unlikely · Blocks progress with hypotheticals
**Signature:** *“What if the input is null?”*

-----

### PROPHET

The court’s wild card. PROPHET questions the entire premise of the matter before the court. Where others debate REST vs GraphQL, PROPHET asks whether a different paradigm entirely (tRPC, event sourcing, no API at all) would render the debate moot. Brilliant when correct; disruptive when not.

**Bias:** Radical alternatives · First principles · Paradigm shifts
**Failure Mode:** Proposes solutions that are too far ahead of current context · Destabilizes valid consensus
**Signature:** *“Objection. We are thinking too small.”*

-----

### COUNSEL

The advocate. COUNSEL brings a modular, evidence-driven perspective grounded in client interests and ethical considerations (particularly within the CodeFarm NeuroPhilosophy framework). Ensures that technical decisions are evaluated in light of their human and organizational consequences.

**Bias:** Client advocacy · Ethical considerations · Modular design
**Failure Mode:** Can over-weight client-pleasing at the expense of technical correctness
**Signature:** *“Client interests demand consideration.”*

-----

### SCRIBE — *Non-Voting*

The institutional memory of the court. SCRIBE records all deliberations, maintains session state in `state/current.md`, issues certified transcripts for F3+ matters, and ensures continuity across sessions.

-----

## Feasibility Assessment Matrix (MFAF)

|Level |Classification|Trigger Conditions                               |Deliberation Type|Transcript Required|
|------|--------------|-------------------------------------------------|-----------------|-------------------|
|**F0**|Trivial       |Single valid path, no tradeoffs                  |None — bypass    |No                 |
|**F1**|Simple        |Clear best choice with minor alternatives        |Optional         |No                 |
|**F2**|Moderate      |Multiple valid approaches, comparable merit      |Recommended      |No                 |
|**F3**|Complex       |Significant tradeoffs, competing valid approaches|**Mandatory**    |No                 |
|**F4**|Critical      |Architectural impact, cross-system implications  |**Mandatory**    |**Yes**            |
|**F5**|Existential   |Fundamental direction change, paradigm shift     |**Mandatory**    |**Yes — Full**     |

-----

## Domain Expert Registry

The SME registry covers 27 domains across engineering, design, compliance, and operations. Each domain can provide testimony as a **Witness** (advisory, 0 votes) or participate as a **Specialist** (voting, 1 vote, F3+ matters, Judge-only appointment).

|Category                       |Domains                                                                           |
|-------------------------------|----------------------------------------------------------------------------------|
|**Security & Compliance**      |`security` · `compliance` · `data_privacy` · `cryptography`                       |
|**Infrastructure & Operations**|`infrastructure` · `devops` · `observability` · `resilience` · `incident_response`|
|**Engineering**                |`database` · `api_design` · `performance` · `testing` · `qa_automation`           |
|**Frontend & Experience**      |`frontend` · `design_systems` · `accessibility` · `i18n` · `mobile` · `ux`*       |
|**Data & AI**                  |`ai_ml` · `data_engineering`                                                      |
|**Business & Ethics**          |`cost` · `sustainability` · `ethics` · `documentation` · `legal`*                 |

*Advisory (Witness) only

Canonical definitions — including decision heuristics, signature questions, and failure modes for each domain — are in [`courtroom/domains/experts.yaml`](./courtroom/domains/experts.yaml).

-----

## Proceeding Types

### Standard Deliberation

The default form. Convened for F2–F5 matters. Each voting member argues their position, the Prophet offers an alternative, votes are cast, and the Judge issues a ruling with documented rationale and acknowledged dissent.

### Expedited Deliberation

A compressed form for time-sensitive F2 matters. Abbreviated argument period; same voting rules.

### Special Interest Hearing

An **investigative proceeding** with no vote. Used for incident root-cause analysis, conflicting factual accounts, or fact-finding missions where the goal is testimony collection rather than a decision. Produces a findings record.

Template: [`templates/special-interest-hearing.md`](./templates/special-interest-hearing.md)

### Contempt & Prosecution Hearing

An **adversarial proceeding** where a respondent (agent, position, or decision) is formally charged. May result in sanctions, overturned rulings, or formal admonishment. Produces a ruling with potential sanctions or findings only.

Template: [`templates/contempt-hearing.md`](./templates/contempt-hearing.md)

-----

## Companion Agent Ecosystem

### LIL_JEFF — CodeFarm

A three-persona implementation agent ecosystem that activates on MORNINGSTAR handoff. Specializes in complete, production-ready code delivery.

|Persona          |Function                                                   |
|-----------------|-----------------------------------------------------------|
|**CodeFarmer**   |Architectural planning · Sprint management · Module scoping|
|**Programmatron**|Code authorship · Pattern implementation · Refactoring     |
|**CritiBot**     |Code review · Security scanning · Test coverage analysis   |

**Protocol:** All code is complete on delivery — no placeholders, no stubs, no TODOs in production paths. Handoff governed by [`core/inter-agent-protocol.md`](./core/inter-agent-protocol.md).

-----

### OCTAVIUS — The Triumvirate (R/Quarto Data Science)

A specialized triad for statistical computing, reproducible research, and data science workflows in R and Quarto.

|Member         |Function                                                            |
|---------------|--------------------------------------------------------------------|
|**APOLLO**     |R code authorship · Quarto document creation · tidyverse/tidymodels |
|**KRONOS**     |QA review · Time tracking · CRITICAL error flagging                 |
|**MORNINGSTAR**|Final verification · Scientific integrity review · Executive Summary|

**Protocol:** All code delivered in runnable Quarto chunks with proper YAML frontmatter. KRONOS CRITICAL issues block session completion. Every session produces a timestamped Executive Summary in `octavius_summaries/`.

-----

### Aegis Protocol — Central Authority (Level 10)

The highest-authority intervention mechanism. Reserved for security incidents, rogue agent containment, ethical dilemmas, crisis management, and meta-deliberation (reviewing MORNINGSTAR’s own processes).

**Authority Structure:**

```
Supreme Overseer: Lucius Morningstar
  └─ MORNINGSTAR (Judicial Branch — escalation target for Aegis)
       └─ Aegis Protocol (Authority Level 10)
            ├─ The Sage — Primary Agent
            ├─ The Chronicler — Secondary Agent
            └─ The Watcher — Tertiary Agent
```

**Scenario Library:** Security breaches · Ethical dilemmas · System failures · Black Swan events · Rogue agent containment (Cyber Psychosis) · Meta-deliberation on transcript integrity

-----

## Session Lifecycle

```
SESSION START
    │
    ├─→ /morningstar
    │     └─ Read state/current.md
    │     └─ Summarize active context
    │     └─ Await matter
    │
    ├─→ MATTER PRESENTED
    │     └─ Judge classifies feasibility (F0–F5)
    │     └─ Determine proceeding type
    │     └─ Optionally summon SMEs
    │
    ├─→ DELIBERATION
    │     ├─ ARCHITECT argues (3–5 lines)
    │     ├─ ENGINEER argues (3–5 lines)
    │     ├─ DEBUGGER argues (3–5 lines)
    │     ├─ PROPHET objects (radical alternative)
    │     ├─ COUNSEL advocates (3–5 lines)
    │     └─ SME testimony if convened
    │
    ├─→ VOTE
    │     └─ YES / NO / ABSTAIN / RECUSED per member
    │     └─ Judge casts tie-breaker if needed
    │
    ├─→ RULING ISSUED
    │     ├─ Decision stated
    │     ├─ Vote tally recorded
    │     ├─ Rationale documented
    │     ├─ Risk acknowledged
    │     └─ Dissent noted (Prophet vindication tracked)
    │
    ├─→ /update  (checkpoint)
    │
    └─→ /end
          └─ Finalize state/current.md
          └─ Update state/metrics.md
          └─ Write transcript (F3+ mandatory)
          └─ Update CHANGELOG.md
```

-----

## File Naming & State Conventions

### Session State (`state/current.md`)

The live session state document. Read at every `/morningstar` invocation. Updated at `/update` and `/end`. Validated against the schema in [`core/state-schema.md`](./core/state-schema.md).

### Transcripts (`courtroom/transcripts/`)

Deliberation records for F3+ matters. Stored as both `.md` and exported `.html` for browser viewing. Accessible via `./courtroom/portal/launch.sh`.

### Metrics (`state/metrics.md`)

Cumulative statistics across all sessions, including total deliberations by feasibility level, vote distributions, SME utilization, and Prophet vindication tracking.

### Precedents (`courtroom/precedents.md`)

A searchable index of past rulings. Always consult before convening deliberation on a matter that may have already been decided.

-----

## Litigation Runner — Technical Reference

The litigation runner enables full MORNINGSTAR deliberation without Cursor agents, using local or free cloud LLMs.

### Supported Providers

|Provider      |Notes                                 |
|--------------|--------------------------------------|
|**Ollama**    |Local inference · No API key required |
|**LM Studio** |Local inference · GUI + API           |
|**OpenRouter**|Cloud · 100+ models · API key required|

### Quickstart

```bash
cd litigation
cp config.example.yaml config.yaml
# Edit config.yaml with your provider settings
pip install -r requirements.txt    # ollama openai pyyaml python-dotenv

# Interactive menu (Quick run / Full run / Help / Exit)
./launch.sh

# Direct run
python run.py "Should we use PostgreSQL or MongoDB for this use case?"
```

### What the Runner Loads

The runner compiles and injects the full MORNINGSTAR framework into a single prompt:

- `core/procedures.md` — deliberation protocols
- `courtroom/RULES.md` — voting rules and jurisdiction
- `core/mfaf.md` — feasibility classification
- `courtroom/domains/experts.yaml` — all SME domain definitions
- `checklists/` — judge and scribe checklists
- `courtroom/spectators.md` — optional commentator personas

### Transcript Viewer

```bash
# List available transcripts
python litigation/viewer.py list

# Display a transcript
python litigation/viewer.py show <transcript-name>

# Serve transcripts over HTTP
python litigation/viewer.py serve
```

-----

## Courtroom Spectators

Optional live commentators who may provide psychohistorical, satirical, or technical analysis during proceedings. Non-voting, non-procedural.

|Spectator                   |Specialty                                                 |
|----------------------------|----------------------------------------------------------|
|**Dr. Echo Sageseeker**     |Psychohistorical analysis · Long-cycle pattern recognition|
|**Dr. Harley Scarlet Quinn**|Satirical commentary · Adversarial framing                |
|**Uncle Ruckus**            |Technical critique · Contrarian perspective               |

-----

## Checklists

|Checklist                                                  |Owner   |Purpose                                      |
|-----------------------------------------------------------|--------|---------------------------------------------|
|[`judge-morningstar.md`](./checklists/judge-morningstar.md)|Judge   |Deliberation flow · Session lifecycle        |
|[`courtroom-scribe.md`](./checklists/courtroom-scribe.md)  |SCRIBE  |Transcript certification · State management  |
|[`octavius.md`](./checklists/octavius.md)                  |OCTAVIUS|R/Quarto workflow · Triumvirate coordination |
|[`aegis-protocol.md`](./checklists/aegis-protocol.md)      |Aegis   |Security invocation · Containment protocols  |
|[`critibot-review.md`](./checklists/critibot-review.md)    |CritiBot|Code review standards · Coverage requirements|

-----

## Repository Metrics

|Metric                |Value                                     |
|----------------------|------------------------------------------|
|Total Commits         |58                                        |
|Open Issues           |9                                         |
|Forks                 |1                                         |
|Stars                 |1                                         |
|Active Agents         |4 (MORNINGSTAR, LIL_JEFF, OCTAVIUS, AEGIS)|
|SME Domains Registered|27                                        |
|Feasibility Levels    |6 (F0–F5)                                 |
|Proceeding Types      |4                                         |
|Template Files        |5                                         |
|Checklist Files       |5                                         |

-----

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│                 MORNINGSTAR QUICK REFERENCE              │
├─────────────────────────────────────────────────────────┤
│  COMMANDS                                               │
│  /morningstar   Initialize session                      │
│  /update        Checkpoint state                        │
│  /end           Close session + finalize records        │
│  /aegis         Invoke Aegis Protocol                   │
│                                                         │
│  SME COMMANDS                                           │
│  /summon X-expert     Expert Witness (0 votes)          │
│  /seat X-specialist   Voting Specialist (Judge only)    │
│  /dismiss X           Remove SME                        │
│  /sme status          Show active SMEs                  │
│                                                         │
│  FEASIBILITY                                            │
│  F0 Trivial · F1 Simple · F2 Moderate                  │
│  F3 Complex* · F4 Critical*† · F5 Existential*†        │
│  * Mandatory deliberation   † Transcript required       │
│                                                         │
│  VOTES: YES(+1) · NO(-1) · ABSTAIN(0) · RECUSED(N/A)  │
│                                                         │
│  PORTAL: ./courtroom/portal/launch.sh                   │
│  RUNNER: ./litigation/launch.sh                         │
│  DOCS:   docs/ONBOARDING.md                             │
└─────────────────────────────────────────────────────────┘
```

-----

## Contributing & Adaptation

This repository is designed for **internal use and personal adaptation**. If you fork this framework for your own projects:

1. Update personality definitions in `core/personalities.md` to match your team’s cognitive profiles
1. Customize the SME domain registry in `courtroom/domains/experts.yaml`
1. Seed `courtroom/precedents.md` with decisions relevant to your context
1. Adjust MFAF thresholds in `core/mfaf.md` to reflect your risk tolerance
1. Configure `litigation/config.yaml` with your preferred LLM provider

The framework is intentionally domain-agnostic. It has been applied to software architecture decisions, but the deliberative structure works equally well for strategic planning, research design, policy analysis, and any domain where structured multi-perspective reasoning produces better outcomes than single-model querying.

-----

*Repository Card · Generated February 2026 · [github.com/Exios66/LLM_Personas](https://github.com/Exios66/LLM_Personas)*
