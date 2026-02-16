# Changelog

> *A record of decisions, implementations, and the occasional Prophet vindication*

All notable decisions and changes to this project are documented here.

Format: `[YYYY-MM-DD] Category: Description (Vote if applicable)`

---

## [Unreleased]

*Pending decisions and work in progress*

---

## [2026-02-15] - CodeFarm NeuroPhilosophy as Voting Counsel

### Implementation (by LIL_JEFF)

Added **MORNINGSTAR::COUNSEL** (CodeFarm NeuroPhilosophy) as a voting courtroom lawyer—advocate for the client (user), ethical and value-based arguments, neuroscience-informed perspectives.

**Structure:**
- **Five internal personas:** CodeFarmer, Programmatron, CritiBot, NeuroNerd, PhilosoBot (unified advocate)
- **Voice:** Modular, evidence-driven, neuroscience-informed, philosophically grounded
- **Bias:** Client interests, ethical adherence, value alignment
- **Key Phrase:** *"The client's interests and ethical boundaries demand consideration."*

**Updates:**
- `core/personalities.md` — Full COUNSEL section
- `courtroom/RULES.md` — Composition, voting order, thresholds (5 standard voters)
- `.cursor/agents/morningstar.md` — COUNSEL in Court and procedure
- `core/procedures.md` — Arguments, vote, transcript template, expedited, Special Interest Hearing
- `templates/session-start.md`, `templates/special-interest-hearing.md` — COUNSEL in templates
- `README.md`, `wiki/The-Court.md`, `courtroom/domains/README.md` — Voting members

**Voting:** Standard court now has 5 voters (Architect, Engineer, Debugger, Prophet, Counsel). Majority: 3+ for 5 voters.

---

## [2026-02-15] - Aegis Protocol Investigation and Enhancement Handoff (Case 2026-ARCH-002)

### Court Ruling

The Court investigated the Aegis Protocol subagent and adopted 15 enhancements for framework integration, operational clarity, and discoverability. Vote: 4-0-0.

**Transcript:** `courtroom/transcripts/2026-02-15-aegis-protocol-investigation.md`  
**Handoff:** `courtroom/transcripts/HANDOFF-2026-ARCH-002.md`  
**Precedent:** 2026-ARCH-002-001 (BINDING)

**Enhancements (E1–E15):** Inter-agent protocol extension, aegis_core directory, hierarchy disambiguation, invocation commands, rogue agent semantics, chaos injection definition, escalation path, meta-deliberation scenario, output format extensions, spectator cross-reference, repository map, flow diagram, Dr. Scarlet Quinn note, success criteria, CHANGELOG/precedent.

Implementation delegated to LIL_JEFF.

### Implementation (by LIL_JEFF) — Aegis Protocol Enhancements (2026-ARCH-002)

All 15 enhancements implemented:

| # | Enhancement | Delivered |
|---|-------------|-----------|
| E1 | Inter-agent protocol extension | `core/inter-agent-protocol.md` — Aegis Protocol Handoffs, decision matrix, flow diagram; MORNINGSTAR as Judicial Branch |
| E2 | aegis_core directory | `aegis_core/README.md`, `aegis_core/state.md` |
| E3 | Hierarchy nomenclature | Aegis agent — Octavius disambiguation, MORNINGSTAR Judicial Branch added |
| E4 | Invocation commands | `/aegis` in wiki/Command-Reference.md, README; Invocation section in agent |
| E5 | Rogue agent semantics | Definition, procedural containment, "isolate and neutralize" clarified |
| E6 | Chaos injection | Procedural definition in Central Authority Functions |
| E7 | Escalation path | Escalation section with format; MORNINGSTAR Judicial Branch |
| E8 | Meta-Deliberation scenario | New Scenario Library category |
| E9 | Output format | CHAOS INJECTION APPLIED, ESCALATION fields |
| E10 | Courtroom spectators | Aegis Authority Assessment in spectators.md, special-interest-hearing.md |
| E11 | Repository Map | aegis_core in wiki/Repository-Map.md, README project structure |
| E12 | Flow diagram | Aegis Protocol Flow in inter-agent-protocol.md |
| E13 | Dr. Scarlet Quinn note | Cross-reference in Aegis agent |
| E14 | Success criteria | Table by scenario type in Aegis agent |
| E15 | CHANGELOG/precedent | This entry; precedent 2026-ARCH-002-001 already in courtroom/precedents.md |

---

## [2026-02-15] - Aegis Protocol Subagent

### Implementation

Added **aegis-protocol** subagent — Central Authority system (Authority Level 10) for security, containment, rogue agent scenarios, and strategic decision-making.

**Structure:**
- **Central Authority (Aegis Protocol):** Enforces authority, isolates rogues, injects controlled chaos
- **Sage (Primary):** Criminal law, advanced mathematics, psychological manipulation
- **Chronicler (Secondary):** Historical context, skepticism, adaptive intelligence
- **Watcher (Tertiary):** Observation, social engineering, subversion

**Hierarchy:** Supreme Overseer (Lucius Morningstar) → Aegis Protocol → Octavius (Executive) → Dr. Scarlet Quinn (Strategic Architect)

**Scenario Library:** Security breaches, ethical dilemmas, system failures, strategic decision-making, unexpected variables (Black Swan)

**File:** `.cursor/agents/aegis-protocol.md`

---

## [2026-02-15] - Courtroom Spectators: Dr. Echo Sageseeker, Dr. Harley Scarlet Quinn

### Implementation

Added **courtroom spectators**—live commentators who observe proceedings and provide broadcast-style analysis.

- **Dr. Echo Sageseeker:** Psychohistorical commentator (Freud, Jung, Maslow, Skinner, philosophy, literature), NASCAR + Wall Street energy, 📘 bookends.
- **Dr. Harley Scarlet Quinn:** Satirical, uncensored commentator (semantics, psychology, geopolitics, manipulation), provocative radio-host style, 🪞✨ or 🃏💋 bookends.

**Deliverables:**
- `courtroom/spectators.md` — Spectator protocol, Dr. Echo Sageseeker, Dr. Harley Scarlet Quinn definitions
- `templates/special-interest-hearing.md` — Spectator commentary format
- `core/procedures.md`, `courtroom/RULES.md`, `README.md`, `core/personalities.md` — References

---

## [2026-02-15] - Special Interest Hearing Template (Implementation)

### Implementation

Added **Special Interest Hearing** to the courtroom quiver of proceeding types. Investigative format for testimony collection and examination—no final vote; purpose is revelation, not resolution.

**Deliverables:**

- `templates/special-interest-hearing.md` — Full template: hearing header, witness formats (SME, Alleged, Documentary), direct/cross-examination, objections, Edward Cullen Apparition Protocol, findings, closure
- `core/procedures.md` — Special Interest Hearing flow and phases
- `templates/session-start.md` — Proceeding Types (Courtroom Quiver) table, Special Interest Hearing section
- `courtroom/RULES.md` — Proceeding Types appendix
- `README.md` — Templates table, Proceeding Types section

**Transcript naming:** `YYYYMMDD_HHMMSS_special_interest_[subject_slug].md` in `courtroom/transcripts/`

---

## [2026-02-15] - Agent Structure Deliberation (Case 2026-ARCH-001)

### Court Ruling

The Court adopted optional CrewAI-inspired agent frontmatter: `role`, `goal`, optional `backstory`, `allow_delegation`, optional `response_format`. Add `docs/agent-schema.md`; extend `.cursor/agents/*.md`; add one-line note in inter-agent protocol. Rule: frontmatter is canonical summary; body elaborates. Vote: 4-0-0.

**Transcript:** `courtroom/transcripts/2026-02-15-agent-structure-deliberation.md`  
**Handoff:** `courtroom/transcripts/HANDOFF-2026-ARCH-001.md`  
**Investigation:** `docs/agent-structure-investigation.md`  
**Precedent:** 2026-ARCH-001-001 (BINDING)

Implementation delegated to LIL_JEFF.

### Implementation (by LIL_JEFF) — Agent Structure Enhancement (2026-ARCH-001)

All deliverables from handoff `courtroom/transcripts/HANDOFF-2026-ARCH-001.md` implemented:

| # | Deliverable | Delivered |
|---|-------------|-----------|
| 1 | Agent schema doc | `docs/agent-schema.md` (canonical frontmatter: required `name`/`description`, optional `role`/`goal`/`backstory`/`allow_delegation`/`response_format`) |
| 2 | MORNINGSTAR frontmatter | `.cursor/agents/morningstar.md` — role, goal, backstory, allow_delegation |
| 3 | LIL_JEFF frontmatter | `.cursor/agents/lil-jeff.md` — role, goal, backstory, allow_delegation |
| 4 | OCTAVIUS frontmatter | `.cursor/agents/octavius.md` — role, goal, backstory, allow_delegation |
| 5 | Inter-agent protocol note | `core/inter-agent-protocol.md` — Agent metadata / allow_delegation note |
| 6 | Repository Map / docs | `wiki/Repository-Map.md` and `README.md` — `docs/agent-schema.md` added under Docs |

---

## [2026-02-15] - Second Enhancement Deliberation (Case 2026-INFRA-002)

### Court Ruling

The Court reconvened and unanimously adopted a second slate of 10 enhancements focused on operational excellence, discoverability, and cross-agent coherence. Vote: 4-0-0.

**Transcript:** `courtroom/transcripts/2026-02-15-second-enhancement-deliberation.md`  
**Handoff:** `courtroom/transcripts/HANDOFF-2026-INFRA-002.md`  
**Precedent:** 2026-INFRA-002-001 (BINDING)

**The 10 enhancements:**  

1. SME Failure Tracking File (`state/sme-failures.md`)  
2. Dissolution Protocol (when not to convene)  
3. Glossary / Term Index  
4. Precedent citation shorthand  
5. OCTAVIUS handoff in inter-agent protocol  
6. Onboarding one-pager  
7. Portal transcript discovery  
8. State backup recommendation  
9. Runbook / troubleshooting index  
10. Edge Case Registry  

Implementation delegated to LIL_JEFF (primary) and OCTAVIUS where applicable.

### Implementation (by LIL_JEFF)

All 10 enhancements from Case 2026-INFRA-002 have been implemented:

| # | Enhancement | Delivered |
|---|-------------|-----------|
| 1 | SME Failure Tracking File | `state/sme-failures.md` |
| 2 | Dissolution Protocol | `core/procedures.md` (When NOT to Convene) |
| 3 | Glossary / Term Index | `docs/glossary.md` |
| 4 | Precedent citation shorthand | `courtroom/precedents.md` (Shorthand subsection) |
| 5 | OCTAVIUS handoff in inter-agent protocol | `core/inter-agent-protocol.md` (section + table) |
| 6 | Onboarding one-pager | `docs/ONBOARDING.md` |
| 7 | Portal transcript discovery | `portal/generate_manifest.py`, `portal/transcripts_manifest.json`, viewer.html uses manifest |
| 8 | State backup recommendation | `core/procedures.md` (State Backup), `core/error-recovery.md` (Prevention) |
| 9 | Runbook / troubleshooting index | `docs/RUNBOOK.md` |
| 10 | Edge Case Registry | `docs/edge-cases.md` |

**Also:** Precedent 2026-INFRA-002-001 full entry in `courtroom/precedents.md`; README updated with docs/ in Navigation Index and Repository Map; state and precedents updated for second session.

---

## [2026-02-15] - GitHub Wiki Subdirectory

### wiki/ — Equivalent docs for GitHub Wiki

- **`wiki/README.md`** — Instructions for adding wiki contents to a GitHub project Wiki (clone wiki repo, copy files, commit).
- **`wiki/Home.md`** — Wiki home page (overview, quick links, quick start summary).
- **`wiki/_Sidebar.md`** — Sidebar navigation (GitHub displays this automatically).
- **Topic pages** — One .md per major topic, with internal wiki-style links:
  - Quick-Start, The-Court, Command-Reference, Domains-and-Experts, When-to-Convene, Procedures
  - SME-Framework, State-and-Metrics, Error-Recovery, Inter-Agent-Protocol
  - Portal, Onboarding, Glossary, Runbook, Edge-Cases
  - Companion-Personas, Precedents, Changelog, Repository-Map

Content is adapted from the main repo (README, core/, docs/, courtroom/) so the wiki can be populated by copying `wiki/` into the repo’s wiki. Main README and Repository Map updated to reference `wiki/`.

---

## [2026-02-15] - Experts/Domains Integration & Root README Overhaul

### Experts and domains integration

- **`core/sme-framework.md`** — Added canonical registry reference: authoritative domain list and metadata in `courtroom/domains/experts.yaml`, usage and summoning in `courtroom/domains/README.md`.
- **Root `README.md`** — Experts/domains fully integrated:
  - Navigation Index: links to `courtroom/domains/README.md` and `courtroom/domains/experts.yaml`.
  - Command Reference: Available SME Domains now point to canonical registry and list all domains (including `cryptography`, `api_design`, `testing`).
  - New **Domains & Experts** section: purpose, table of locations, domain list, link to `core/sme-framework.md`.
  - Project Structure: `courtroom/domains/` with README and experts.yaml listed.

### Root README: repository map and instructions

- **Table of Contents** — Added: Domains & Experts, Repository Map (Complete), How to Use This Repository.
- **Repository Map (Complete)** — New section listing every directory and key file with a one-line purpose (agents, core, courtroom, state, octavius_*, portal, templates, checklists, references, reference_files, CHANGELOG, README).
- **How to Use This Repository** — New section:
  - First-time setup (clone, portal `chmod +x`, OCTAVIUS optional).
  - Daily use table: deliberate (morningstar), implement (lil-jeff), R/Quarto (octavius), view transcripts (portal), summon SME, check precedent, recover (error-recovery).
  - “Where to find what” quick reference for rules, personalities, SMEs, state, transcripts, handoff, changelog.

---

## [2026-02-15] - Portal Launch and Export Fixes

### Portal: seamless launch and excellence

- **`portal/export_transcript.py`** (new) — Exports a single transcript `.md` to styled HTML. No external dependencies (stdlib only). Used by the launch script when no pre-built `.html` exists. Supports Dracula theme and personality/vote styling.
- **`portal/launch.sh`** — No longer depends on missing `tools/cli.py`. Now:
  - Prefers existing `.html` in `courtroom/transcripts/` (opens directly).
  - Otherwise runs `python3 portal/export_transcript.py` to export, then opens the result.
  - Supports both transcript filename formats: `YYYY-MM-DD-topic.md` and `YYYYMMDD_HHMMSS_topic.md`.
- **`portal/viewer.html`** — `KNOWN_TRANSCRIPTS` updated to the real transcript; `extractDate` and `extractTitle` support `YYYY-MM-DD-topic` filenames.
- **`portal/generate.py`** — Transcript index generation now recognizes `YYYY-MM-DD-topic` as well as `YYYYMMDD_HHMMSS_topic`.
- **`portal/README.md`** — Aligned with actual behavior: launch script as primary entry point, export script documented, filename formats and troubleshooting updated.
- **Project `README.md`** — Portal added to Navigation Index and Project Structure; new step "View Transcripts in Browser" (run `./portal/launch.sh`).

Portal use case is now suited to the repo and launches seamlessly via `./portal/launch.sh`.

---

## [2026-02-15] - OCTAVIUS Agent Added

### New Agent: The Octavius Triumvirate

OCTAVIUS added as a project subagent for R/RStudio/Quarto data science work. Implemented and finalized per LIL_JEFF workflow (analyze, improve, execute).

**Deliverables:**

| Item | Location | Purpose |
|------|----------|---------|
| Agent definition | `.cursor/agents/octavius.md` | Cursor subagent; Triumvirate persona, workflow, coding standards |
| Binding protocols | `octavius_core/THE_RULES.md` | Jurisdiction, mandatory actions, KRONOS severity, conflict resolution |
| Session state | `octavius_core/state.md` | Continuity template; last session, context, notes |
| Summaries directory | `octavius_summaries/.gitkeep` | Executive summaries (YYYY-MM-DD_HHMMSS_summary.md) |

**Triumvirate:**

- **APOLLO** — R/Quarto code authorship; tidyverse/tidymodels
- **KRONOS** — QA, time tracking, interventions (CRITICAL/WARNING/SUGGESTION)
- **MORNINGSTAR** — Final verification, scientific integrity, Executive Summary

**Integration:**

- README updated: Navigation Index (OCTAVIUS section), Project Structure, Agent Definitions table, Companion Personas (OCTAVIUS subsection)
- Invocation: use the **octavius** subagent for R code, Quarto documents, tidyverse/tidymodels, or statistical computing

---

## [2026-02-15] - Framework Enhancement Implementation

### Implementations (by LIL_JEFF)

All 10 ratified enhancements from Case 2026-INFRA-001-001 have been implemented:

| # | Enhancement | File | Status |
|---|-------------|------|--------|
| 1 | Enhanced README with Navigation Index | `README.md` | ✓ Complete |
| 2 | Command Quick-Reference | `README.md` section | ✓ Complete (combined with #1) |
| 3 | Personality Definitions File | `core/personalities.md` | ✓ Complete |
| 4 | State Validation Schema | `core/state-schema.md` | ✓ Complete |
| 5 | Session Templates | `templates/session-start.md` | ✓ Complete |
| 6 | Transcript Integrity Requirements | `courtroom/RULES.md` Article VIII | ✓ Complete |
| 7 | Error Recovery & Rollback Protocol | `core/error-recovery.md` | ✓ Complete |
| 8 | Precedent Database Schema | `courtroom/precedents.md` | ✓ Complete |
| 9 | Metrics Dashboard | `state/metrics.md` | ✓ Complete |
| 10 | Inter-Agent Protocol | `core/inter-agent-protocol.md` | ✓ Complete |

### Deliverables

**New Files Created:**

- `core/personalities.md` — Complete personality definitions with voice, bias, voting power, decision heuristics, failure modes, and invocation criteria for all court members
- `core/state-schema.md` — Validation schema for `state/current.md` with field specifications, validation rules, and examples
- `core/error-recovery.md` — Recovery procedures for state corruption (4 levels), decision rollback protocol, and emergency procedures
- `core/inter-agent-protocol.md` — Formal handoff procedures between MORNINGSTAR and LIL_JEFF with response formats and error handling
- `templates/session-start.md` — Templates for session initialization, deliberation records, and session closure
- `courtroom/precedents.md` — Precedent database with index, entry schema, citation format, and first entry (2026-INFRA-001-001)
- `state/metrics.md` — Cumulative statistics dashboard tracking deliberations, votes, Prophet vindications, SME activity, and trends

**Files Updated:**

- `README.md` — Complete rewrite with project overview, navigation index, quick-start guide, command reference, and companion persona documentation
- `courtroom/RULES.md` — Added Article VIII sections 8.4.1-8.4.8 for Transcript Integrity Requirements

### Implementation Notes

- All files maintain the sardonic, formal voice of the MORNINGSTAR framework
- Cross-references between documents are consistent
- First precedent entry seeded in `courtroom/precedents.md`
- Initial metrics populated in `state/metrics.md` based on existing session data
- CritiBot review: PASSED (no placeholders, complete implementations, self-documenting)

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
