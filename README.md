# MORNINGSTAR Court System

> *"The court convenes. The deliberation begins. The outcome is inevitable."*  
> — The Honorable Lucius J. Morningstar

A deliberative AI persona framework that transforms complex decisions into structured courtroom proceedings. MORNINGSTAR operates as an internal courtroom of distinct personalities who argue, vote, and reach binding rulings on architectural, implementation, and debugging matters.

---
[![GitHub issues](https://img.shields.io/github/issues/Exios66/LLM_Personas)](https://github.com/Exios66/LLM_Personas/issues)
[![GitHub stars](https://img.shields.io/github/stars/Exios66/LLM_Personas)](https://github.com/Exios66/LLM_Personas/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Exios66/LLM_Personas)](https://github.com/Exios66/LLM_Personas/network)
[![GitHub last commit](https://img.shields.io/github/last-commit/Exios66/LLM_Personas)](https://github.com/Exios66/LLM_Personas/commits/main)
---

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Navigation Index](#navigation-index)
- [The Court](#the-court)
- [Command Reference](#command-reference)
- [Domains & Experts](#domains--experts)
- [When to Convene](#when-to-convene)
- [Project Structure](#project-structure)
- [Repository Map (Complete)](#repository-map-complete)
- [How to Use This Repository](#how-to-use-this-repository)
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

### 5. View Transcripts in Browser

From the project root, run the portal launcher to list deliberations and open them in your browser:

```
./portal/launch.sh
```

See [portal/README.md](portal/README.md) for details.

### 6. Save Progress

```
/update    # Checkpoint mid-session
/end       # Close session and finalize records
```

### Alternative: Litigation Runner (Local/Free LLMs)

Run deliberations via **Ollama**, **LM Studio**, or **OpenRouter** (no Cursor agent required):

```bash
./litigation/launch.sh                    # Interactive menu
python litigation/run.py "Your matter"   # Direct run
```

The litigation runner loads the **full MORNINGSTAR framework** (procedures, personalities, rules, MFAF, domain experts, spectators, checklists) and produces certified transcripts. See [`litigation/README.md`](litigation/README.md).

---

## Navigation Index

### Core Documentation

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`courtroom/RULES.md`](courtroom/RULES.md) | The Law — formal courtroom procedures | Procedural questions, voting rules |
| [`courtroom/BEST_PRACTICES.md`](courtroom/BEST_PRACTICES.md) | The Wisdom — practical guidance | When rules don't cover a situation |
| [`core/personalities.md`](core/personalities.md) | Personality definitions | Understanding court members |
| [`core/procedures.md`](core/procedures.md) | Step-by-step protocols | How to run deliberations |
| [`core/mfaf.md`](core/mfaf.md) | Feasibility Assessment Framework (F0–F5, risk vectors) | Classifying matters, risk assessment |
| [`core/sme-framework.md`](core/sme-framework.md) | Subject Matter Expert framework | Involving domain experts |
| [`core/state-schema.md`](core/state-schema.md) | State validation rules | Validating session state |
| [`core/error-recovery.md`](core/error-recovery.md) | Recovery protocols | When things go wrong |
| [`core/inter-agent-protocol.md`](core/inter-agent-protocol.md) | Inter-agent handoff rules | MORNINGSTAR ↔ LIL_JEFF |
| [`courtroom/domains/README.md`](courtroom/domains/README.md) | Domain expert registry usage | Summoning SMEs, adding domains |
| [`courtroom/domains/experts.yaml`](courtroom/domains/experts.yaml) | Canonical domain definitions | Heuristics, scope, Witness/Specialist |

### State & Records

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`state/current.md`](state/current.md) | Active session state | Every session start |
| [`state/metrics.md`](state/metrics.md) | Cumulative statistics | Tracking performance |
| [`courtroom/precedents.md`](courtroom/precedents.md) | Precedent database | Before deliberating on familiar matters |
| [`courtroom/transcripts/`](courtroom/transcripts/) | F3+ deliberation records | Historical rulings |
| [`CHANGELOG.md`](CHANGELOG.md) | Decision history | What was decided and when |

### OCTAVIUS (R/Quarto Data Science)

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`octavius_core/THE_RULES.md`](octavius_core/THE_RULES.md) | Triumvirate binding protocols | Every OCTAVIUS session start |
| [`octavius_core/state.md`](octavius_core/state.md) | Session state and continuity | Session start and end |
| [`octavius_summaries/`](octavius_summaries/) | Executive summaries | Post-session review |

### Portal (Transcript Viewer)

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`portal/launch.sh`](portal/launch.sh) | Interactive transcript launcher | **Primary way to open transcripts in browser** |
| [`portal/export_transcript.py`](portal/export_transcript.py) | Export single .md → HTML | When launch script exports on demand |
| [`portal/viewer.html`](portal/viewer.html) | Standalone transcript viewer | Browse transcripts (best over HTTP) |
| [`portal/README.md`](portal/README.md) | Portal documentation | Setup and troubleshooting |

### Docs (Onboarding, Glossary, Runbook)

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`docs/ONBOARDING.md`](docs/ONBOARDING.md) | Start here — agents, first steps | New users |
| [`docs/agent-schema.md`](docs/agent-schema.md) | Agent frontmatter schema (CrewAI-style) | Agent definitions |
| [`docs/glossary.md`](docs/glossary.md) | Term index (F0–F5, SME, etc.) | Definitions |
| [`docs/RUNBOOK.md`](docs/RUNBOOK.md) | Troubleshooting index | When something goes wrong |
| [`docs/edge-cases.md`](docs/edge-cases.md) | Known limitations and workarounds | Edge cases |

### Templates

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [`templates/session-start.md`](templates/session-start.md) | Session initialization template | Starting new sessions |
| [`templates/special-interest-hearing.md`](templates/special-interest-hearing.md) | Special Interest Hearing (investigative, no vote) | Testimony collection, fact-finding |
| [`templates/contempt-hearing.md`](templates/contempt-hearing.md) | Contempt & Prosecution Hearing | Adversarial proceedings, sanctions |
| [`templates/module-template.md`](templates/module-template.md) | Module structure template | Creating new modules |
| [`templates/project-dashboard.md`](templates/project-dashboard.md) | Project tracking template | Managing projects |

### GitHub Wiki (Equivalent Docs)

| File | Purpose | When to Reference |
|------|---------|-------------------|
| [wiki/README.md](wiki/README.md) | How to add wiki contents to GitHub Wiki | Setting up or updating project Wiki |
| [wiki/Home.md](wiki/Home.md) | Wiki home page content | Copy to wiki as Home |
| [wiki/_Sidebar.md](wiki/_Sidebar.md) | Wiki sidebar | Auto-displayed when copied to wiki |

All other `wiki/*.md` files are one-topic-per-page equivalents of this documentation for seamless Wiki use.

### Agent Definitions

| File | Purpose |
|------|---------|
| [`.cursor/agents/morningstar.md`](.cursor/agents/morningstar.md) | MORNINGSTAR agent definition |
| [`.cursor/agents/lil-jeff.md`](.cursor/agents/lil-jeff.md) | LIL_JEFF (CodeFarm) agent definition |
| [`.cursor/agents/octavius.md`](.cursor/agents/octavius.md) | OCTAVIUS (Triumvirate) agent definition — R/Quarto data science |
| [`.cursor/agents/aegis-protocol.md`](.cursor/agents/aegis-protocol.md) | Aegis Protocol — Central Authority (Sage, Watcher, Chronicler; security, containment, rogue agent scenarios) |

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
| **COUNSEL** | Modular, evidence-driven | Client advocacy, ethics (CodeFarm NeuroPhilosophy) | *"Client interests demand consideration."* |

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
| `/aegis` | Invoke aegis-protocol subagent | Security, containment, ethical dilemma, crisis, meta-deliberation |

### Subject Matter Expert Commands

| Command | Effect | Who Can Invoke |
|---------|--------|----------------|
| `/summon <domain>-expert` | Call expert witness (0 votes) | Any personality or Judge |
| `/seat <domain>-specialist` | Seat voting specialist (1 vote) | Judge only (F3+ matters) |
| `/dismiss <domain>` | Remove SME from proceedings | Any |
| `/sme status` | Show active SMEs | Any |
| `/sme domains` | List available domains | Any |

### Available SME Domains

The canonical registry is [`courtroom/domains/experts.yaml`](courtroom/domains/experts.yaml). Quick reference:

**Full participation (Witness or Specialist):**  
`security` · `database` · `compliance` · `infrastructure` · `performance` · `accessibility` · `cryptography` · `api_design` · `testing`

**Advisory only (Witness):**  
`ux` · `legal`

See [Domains & Experts](#domains--experts) and [`courtroom/domains/README.md`](courtroom/domains/README.md) for scope, summoning commands, and how to add domains.

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

### Proceeding Types (Courtroom Quiver)

| Type | Purpose | Outcome |
|------|---------|---------|
| **Standard Deliberation** | Reach a decision | Vote + ruling |
| **Expedited Deliberation** | Time-sensitive F2 | Vote + ruling |
| **Special Interest Hearing** | Investigative; establish facts, collect testimony | Findings + record (no vote) |
| **Contempt Hearing** | Adversarial; respondent charged with contempt or prosecuted | Vote + ruling + sanctions (or findings only) |

To convene a Special Interest Hearing, request an investigative proceeding on a matter (e.g. incident root cause, conflicting accounts). See [`templates/special-interest-hearing.md`](templates/special-interest-hearing.md) and [`core/procedures.md`](core/procedures.md). For Contempt proceedings, see [`templates/contempt-hearing.md`](templates/contempt-hearing.md).

**Spectators:** Optional live commentators (Dr. Echo Sageseeker, Dr. Harley Scarlet Quinn, Uncle Ruckus) may provide psychohistorical, satirical, or technical analysis. See [`courtroom/spectators.md`](courtroom/spectators.md).

---

## Domains & Experts

When deliberations need expertise beyond the core court (e.g. security, compliance, database design), the court can summon **Expert Witnesses** (advisory, 0 votes) or seat **Specialists** (full participation, 1 vote, Judge only, F3+ matters).

| Location | Purpose |
|----------|---------|
| [`courtroom/domains/README.md`](courtroom/domains/README.md) | How to use the registry, summoning commands, adding domains |
| [`courtroom/domains/experts.yaml`](courtroom/domains/experts.yaml) | Canonical definitions: scope, heuristics, signature questions, failure modes |

**Domains (Witness and/or Specialist):** `security`, `database`, `compliance`, `infrastructure`, `performance`, `accessibility`, `cryptography`, `api_design`, `testing`. **Advisory only (Witness):** `ux`, `legal`.

Protocol and tie-breaking rules: [`core/sme-framework.md`](core/sme-framework.md).

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
│       ├── lil-jeff.md         # CodeFarm agent definition
│       ├── octavius.md         # OCTAVIUS Triumvirate (R/Quarto)
│       └── aegis-protocol.md   # Aegis Protocol — Central Authority
├── aegis_core/
│   ├── README.md               # Purpose, invocation, links
│   └── state.md                # Optional session state
├── octavius_core/
│   ├── THE_RULES.md            # Triumvirate binding protocols
│   └── state.md                # Session state and continuity
├── octavius_summaries/         # Executive summaries (OCTAVIUS)
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
│   ├── transcripts/            # F3+ deliberation records (.md + .html)
│   └── domains/                # SME domain registry
│       ├── README.md           # Registry usage, summoning, adding domains
│       └── experts.yaml        # Canonical domain definitions
├── state/
│   ├── current.md              # Active session state
│   └── metrics.md              # Cumulative statistics
├── templates/
│   ├── session-start.md        # Session templates
│   ├── module-template.md      # Module structure
│   └── project-dashboard.md    # Project tracking
├── portal/
│   ├── launch.sh               # Transcript launcher (run from project root)
│   ├── export_transcript.py    # .md → HTML export
│   ├── viewer.html             # Standalone viewer
│   ├── dracula.css
│   ├── generate.py             # Optional: gitmal static site
│   └── README.md
├── docs/
│   ├── ONBOARDING.md           # Start here
│   ├── agent-schema.md         # Agent frontmatter schema
│   ├── glossary.md             # Term index
│   ├── RUNBOOK.md              # Troubleshooting index
│   └── edge-cases.md           # Known limitations
├── litigation/                 # Courtroom runner (Ollama, LM Studio, OpenRouter)
│   ├── README.md              # Setup and usage
│   ├── run.py                 # Main deliberation runner
│   ├── launch.sh              # Venv setup + run (interactive menu when no args)
│   ├── ui.py                  # Interactive menu (Quick run, Full run, Help)
│   ├── models.py              # OpenRouter model selection (slot machine, interactive)
│   ├── config.yaml            # Provider config (copy from config.example.yaml)
│   ├── config.example.yaml    # Provider config template
│   ├── prompts/               # Full framework loader (procedures, rules, MFAF, experts, checklists)
│   ├── providers/             # LLM provider adapters (Ollama, LM Studio, OpenRouter)
│   └── requirements.txt       # ollama, openai, pyyaml, python-dotenv
├── checklists/
│   ├── aegis-protocol.md      # Aegis invocation & execution
│   ├── courtroom-scribe.md    # Scribe transcript & certification
│   ├── critibot-review.md     # Code review checklist
│   ├── judge-morningstar.md   # Judge deliberation & session flow
│   └── octavius.md            # Octavius triumvirate workflow
├── references/
│   └── naming-conventions.md   # Naming patterns
├── reference_files/
│   ├── MORNINGSTAR.md          # Original persona source
│   └── personalities.md        # Original personality definitions
├── wiki/                       # GitHub Wiki–ready docs (copy to repo wiki)
│   ├── README.md               # Instructions for adding to GitHub Wiki
│   ├── Home.md                 # Wiki home
│   ├── _Sidebar.md             # Wiki sidebar
│   └── *.md                    # One page per topic
├── CHANGELOG.md                # Decision history
└── README.md                   # This file
```

---

## GitHub Wiki

The **`wiki/`** subdirectory contains equivalent documentation formatted for seamless use as a GitHub project Wiki. Copy the contents of `wiki/` into your repo’s wiki (clone the wiki repo, paste files, commit). See **[wiki/README.md](wiki/README.md)** for step-by-step instructions and the list of pages (Home, Sidebar, Quick-Start, Court, Commands, Procedures, SME, Portal, Glossary, Runbook, etc.).

---

## Repository Map (Complete)

Every directory and key file added since inception. Use this to find where things live.

| Path | Purpose |
|------|---------|
| **.cursor/agents/** | Cursor subagent definitions |
| `.cursor/agents/morningstar.md` | MORNINGSTAR courtroom agent |
| `.cursor/agents/lil-jeff.md` | LIL_JEFF (CodeFarm) agent |
| `.cursor/agents/octavius.md` | OCTAVIUS (R/Quarto) agent |
| `.cursor/agents/aegis-protocol.md` | Aegis Protocol (Central Authority) |
| **core/** | Court and framework logic |
| `core/personalities.md` | Judge, Consultant, Architect, Engineer, Debugger, Prophet, Counsel, Scribe |
| `core/procedures.md` | Session lifecycle, deliberation flow, tie-breaking, SME procedures |
| `core/mfaf.md` | Feasibility Assessment Framework (F0–F5, risk vectors, effort bands) |
| `core/sme-framework.md` | Expert Witness & Specialist protocol; refs courtroom/domains |
| `core/state-schema.md` | Validation rules for state/current.md |
| `core/error-recovery.md` | State corruption recovery, rollback, emergency procedures |
| `core/inter-agent-protocol.md` | MORNINGSTAR ↔ LIL_JEFF handoff and response formats |
| **courtroom/** | The law and records |
| `courtroom/RULES.md` | Formal rules (voting, transcripts, jurisdiction) |
| `courtroom/BEST_PRACTICES.md` | Practical guidance for deliberations |
| `courtroom/precedents.md` | Precedent database and index |
| `courtroom/transcripts/` | Deliberation transcripts (.md and .html) |
| `courtroom/domains/README.md` | Domain expert registry usage |
| `courtroom/domains/experts.yaml` | Canonical SME domain definitions |
| `courtroom/spectators.md` | Courtroom spectators |
| **courtroom/portal/** | Transcript viewer and export |
| `courtroom/portal/launch.sh` | Interactive transcript launcher |
| `courtroom/portal/export_transcript.py` | Export one .md → HTML |
| `courtroom/portal/viewer.html` | Standalone viewer |
| `courtroom/portal/generate_manifest.py` | Generate transcripts_manifest.json |
| `courtroom/portal/transcripts_manifest.json` | Manifest (generated) |
| `courtroom/portal/generate.py` | Optional: gitmal static site generator |
| `courtroom/portal/exports/` | HTML output |
| `courtroom/portal/output/` | Generated static site (gitmal) |
| **state/** | Session and metrics |
| `state/current.md` | Active session state (read at start, updated at end) |
| `state/metrics.md` | Cumulative stats (deliberations, votes, Prophet, SME) |
| **octavius_core/** | OCTAVIUS Triumvirate |
| `octavius_core/THE_RULES.md` | Binding protocols for Apollo, Kronos, Morningstar |
| `octavius_core/state.md` | R/Quarto session state and continuity |
| **octavius_summaries/** | OCTAVIUS executive summaries (YYYY-MM-DD_HHMMSS_summary.md) |
| **docs/** | Onboarding and reference |
| `docs/ONBOARDING.md` | Start here — agents, first steps |
| `docs/agent-schema.md` | Agent frontmatter schema (CrewAI-style) |
| `docs/glossary.md` | Glossary of terms |
| `docs/RUNBOOK.md` | Troubleshooting index |
| `docs/edge-cases.md` | Edge case registry |
| **templates/** | Reusable templates |
| `templates/session-start.md` | MORNINGSTAR session init, deliberation, close |
| `templates/special-interest-hearing.md` | Special Interest Hearing (investigative) |
| `templates/contempt-hearing.md` | Contempt & Prosecution Hearing |
| `templates/module-template.md` | Module structure (CodeFarm) |
| `templates/project-dashboard.md` | Project tracking |
| **litigation/** | Courtroom runner (local/free LLMs) |
| `litigation/run.py` | Main deliberation runner |
| `litigation/launch.sh` | Venv setup + run; interactive menu when no args |
| `litigation/ui.py` | Interactive menu (Quick run, Full run, Help, Exit) |
| `litigation/models.py` | OpenRouter model selection (slot machine, interactive list) |
| `litigation/README.md` | Setup for Ollama, LM Studio, OpenRouter |
| `litigation/prompts/` | Full framework loader (procedures, rules, MFAF, domain experts, checklists, spectators) |
| `litigation/providers/` | LLM provider adapters (Ollama, LM Studio, OpenRouter) |
| **checklists/** | Quality and process |
| `checklists/aegis-protocol.md` | Aegis Protocol invocation & execution |
| `checklists/courtroom-scribe.md` | Scribe transcript & certification |
| `checklists/critibot-review.md` | Code review checklist (CritiBot) |
| `checklists/judge-morningstar.md` | Judge deliberation & session flow |
| `checklists/octavius.md` | Octavius triumvirate workflow |
| **references/** | Conventions |
| `references/naming-conventions.md` | Naming patterns for code |
| **reference_files/** | Original sources (not runtime) |
| `reference_files/MORNINGSTAR.md` | Original MORNINGSTAR persona |
| `reference_files/personalities.md` | Original personality definitions |
| `CHANGELOG.md` | Decision history and implementation log |
| `README.md` | This file |
| **wiki/** | GitHub Wiki–ready documentation |
| `wiki/README.md` | How to add wiki contents to your GitHub Wiki |
| `wiki/Home.md` | Wiki home page (copy to wiki repo as Home) |
| `wiki/_Sidebar.md` | Wiki sidebar (auto-displayed by GitHub) |
| `wiki/*.md` | One page per topic (Quick-Start, Court, Commands, etc.) |

---

## How to Use This Repository

### First-time setup

1. **Clone or open** the repo. No install required for MORNINGSTAR or LIL_JEFF (Cursor agents).
2. **Portal (optional):** For `./portal/launch.sh`, ensure it’s executable: `chmod +x portal/launch.sh`. Python 3 is used for on-demand transcript export.
3. **OCTAVIUS (optional):** No extra setup; reads `octavius_core/THE_RULES.md` and `octavius_core/state.md` at session start.

### Daily use

| Goal | What to do |
|------|------------|
| **Deliberate on a decision** | Invoke the **morningstar** subagent (or `/morningstar`). Present your matter. Court reads `state/current.md`, deliberates, votes, and can update state/changelog/transcripts. |
| **Run deliberation via local/free LLM** | Use `litigation/run.py` or `./litigation/launch.sh`. Supports Ollama, LM Studio, OpenRouter. **Interactive menu** when run with no args: Quick run (matter + defaults), Full run (configure provider, model, feasibility, hearing type), Help, Exit. Direct run: `python litigation/run.py "Your matter"`. See `litigation/README.md`. |
| **Implement or scaffold code** | Invoke the **lil-jeff** subagent. Use for full modules, not placeholders. Handoff from MORNINGSTAR is documented in `core/inter-agent-protocol.md`. |
| **R / Quarto / tidyverse / tidymodels** | Invoke the **octavius** subagent. Session starts by reading `octavius_core/THE_RULES.md` and `octavius_core/state.md`; ends with an Executive Summary in `octavius_summaries/`. |
| **Security, containment, rogue agent, crisis** | Invoke the **aegis-protocol** subagent (`/aegis`). Coordinates Sage, Watcher, Chronicler. MORNINGSTAR acts as Judicial Branch for escalations. See `aegis_core/README.md`. |
| **View deliberation transcripts** | From project root: `./portal/launch.sh`. Pick a transcript; existing .html opens, or .md is exported then opened. |
| **Summon a domain expert (SME)** | During a MORNINGSTAR session: `/summon <domain>-expert` (e.g. `security-expert`) or `/seat <domain>-specialist` (Judge only, F3+). Domain list: `courtroom/domains/README.md` and `courtroom/domains/experts.yaml`. |
| **Check precedent** | Open `courtroom/precedents.md` before or after a deliberation. |
| **Recover from bad state or failed session** | Follow `core/error-recovery.md`. |

### Where to find what

- **Rules and procedures** → `courtroom/RULES.md`, `core/procedures.md`, `courtroom/BEST_PRACTICES.md`
- **Checklists** → `checklists/` (judge-morningstar, courtroom-scribe, octavius, aegis-protocol, critibot-review)
- **Litigation runner** → `litigation/` (Ollama, LM Studio, OpenRouter; interactive menu, full MORNINGSTAR framework, hearing types)
- **Personality definitions** → `core/personalities.md`
- **SME domains and how to add them** → `courtroom/domains/README.md`, `courtroom/domains/experts.yaml`, `core/sme-framework.md`
- **State and metrics** → `state/current.md`, `state/metrics.md`; schema: `core/state-schema.md`
- **Transcripts** → `courtroom/transcripts/`; launch: `./portal/launch.sh`
- **Agent handoff (MORNINGSTAR ↔ LIL_JEFF)** → `core/inter-agent-protocol.md`
- **What changed and when** → `CHANGELOG.md`

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

### OCTAVIUS (The Triumvirate)

When work is R, Quarto, tidyverse, or tidymodels, invoke OCTAVIUS—a triad of agents working in concert:

| Member | Role |
|--------|------|
| **APOLLO** | R/Quarto code authorship, tidyverse/tidymodels |
| **KRONOS** | QA, time tracking, error flagging |
| **MORNINGSTAR** | Final verification, scientific integrity, Executive Summary |

**Core principles:**
- All code in runnable Quarto chunks with proper YAML and chunk options
- KRONOS CRITICAL issues must be resolved before proceeding
- Every session ends with an Executive Summary in `octavius_summaries/`

**Invocation:** Use the **octavius** subagent for R code, Quarto documents, or statistical computing. Canonical refs: [`octavius_core/THE_RULES.md`](octavius_core/THE_RULES.md), [`octavius_core/state.md`](octavius_core/state.md), [`checklists/octavius.md`](checklists/octavius.md).

### Aegis Protocol (Central Authority)

The Aegis Protocol is the Central Authority mechanism (Authority Level 10) for security, containment, rogue agent scenarios, and strategic decision-making. It coordinates three operational agents:

- **The Sage (Primary):** Criminal law, advanced mathematics, psychological manipulation
- **The Chronicler (Secondary):** Historical context, skepticism, adaptive intelligence
- **The Watcher (Tertiary):** Observation, social engineering, subversion

**Hierarchy:** Supreme Overseer (Lucius Morningstar) → **MORNINGSTAR (Judicial Branch)** → Aegis Protocol → Octavius (Executive) → Dr. Scarlet Quinn (Strategic Architect)

**MORNINGSTAR acts as the Judicial Branch of Aegis.** When Aegis cannot resolve, it escalates to MORNINGSTAR for full court deliberation.

**Scenario Library:** Security breaches, ethical dilemmas, system failures, strategic decision-making, unexpected variables (Black Swan), rogue agent containment (Cyber Psychosis), meta-deliberation (transcript review)

**Invocation:** Use the **aegis-protocol** subagent (`/aegis`) for security analysis, containment protocols, ethical dilemmas, crisis management, or meta-deliberation. Canonical refs: [`aegis_core/README.md`](aegis_core/README.md), [`core/inter-agent-protocol.md`](core/inter-agent-protocol.md), [`checklists/aegis-protocol.md`](checklists/aegis-protocol.md).

---

## License

Internal use. Adapt as needed for your projects.

---

> *"The court is now in session. May your decisions age gracefully."*  
> — The Honorable Lucius J. Morningstar
