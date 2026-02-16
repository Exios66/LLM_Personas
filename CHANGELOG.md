# Changelog

> *A record of decisions, implementations, and the occasional Prophet vindication*

All notable decisions and changes to this project are documented here.

Format: `[YYYY-MM-DD] Category: Description (Vote if applicable)`

---

## [Unreleased]

*Pending decisions and work in progress*

- None

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
