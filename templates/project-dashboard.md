# Project Dashboard: LLM_Personas (MORNINGSTAR)

> Last Updated: 2026-07-25
> Status: In Progress

## Overview

**Goal:** A deliberative AI persona framework that transforms complex decisions into structured courtroom proceedings. MORNINGSTAR operates as an internal court of distinct personalities who argue, vote, and reach binding rulings on architectural, implementation, and debugging matters.

**Tech Stack:** Python 3.9+, YAML, Markdown; OpenAI-compatible APIs (OpenRouter, Ollama, LM Studio); gpt-4.1-mini; Tavily/DuckDuckGo (web search); Gmail SMTP.

**Repository:** [Exios66/LLM_Personas](https://github.com/Exios66/LLM_Personas)

---

## Module Map

| Module | Status | Owner | Dependencies | Notes |
|--------|--------|-------|--------------|-------|
| `core/` | ✅ Complete | — | None | Personalities, procedures, MFAF, SME framework, state-schema, error-recovery |
| `courtroom/` | ✅ Complete | — | core | RULES, precedents, domains, transcripts, portal |
| `litigation/` | ✅ Complete | — | core, courtroom | Runner (Ollama, LM Studio, OpenRouter) |
| `agents/` | ✅ Complete | — | core, litigation | Definitions, skills, protocols, workflows, tools |
| `state/` | ✅ Complete | — | core | current.md, metrics.md, backups |
| `octavius_core/` | ✅ Complete | — | core | R/Quarto Triumvirate (Apollo, Kronos, Morningstar) |
| `aegis_core/` | ✅ Complete | — | core | Central Authority (Sage, Watcher, Chronicler) |
| `checklists/` | ✅ Complete | — | core | judge-morningstar, courtroom-scribe, octavius, aegis-protocol, critibot-review |
| `templates/` | ✅ Complete | — | core | session-start, hearings, module-template, project-dashboard |
| `docs/` | ✅ Complete | — | — | ONBOARDING, glossary, RUNBOOK, agent-schema, edge-cases |
| `wiki/` | ✅ Complete | — | docs | GitHub Wiki–ready equivalents |

### Status Legend
- ✅ Complete
- 🔄 In Progress  
- ⏳ Pending
- 🚫 Blocked
- 🔍 Needs Review

---

## Dependency Graph

```
[core]
   │
   ├──▶ [courtroom] ◀── transcripts, domains, portal
   │         │
   ├──▶ [litigation] ◀── providers, prompts
   │         │
   ├──▶ [agents] ◀── skills, protocols, workflows, tools
   │
   ├──▶ [octavius_core]
   ├──▶ [aegis_core]
   └──▶ [state]
```

---

## Agent & Asset Metrics

| Category | Count | Details |
|----------|-------|---------|
| **Agent Definitions** | 4 | morningstar, lil-jeff, octavius, aegis-protocol |
| **Skills** | 13 | morningstar (5), lil-jeff (3), octavius (3), aegis (2) |
| **Protocols** | 4 | task-deliberation, aegis-escalation, invocation-and-delegation, inter-agent-handoff |
| **Agent Templates** | 8 | session-state-init, handoff-*, escalation-*, transcript-certification, completion-report |
| **Tools** | 2 | litigation-runner, research-report-workflow |
| **Workflows** | 1 | Research Report (Researcher → Fact-Checker → Report Writer → Formatter → Gmail) |
| **SME Domains** | 27 | security, database, compliance, infrastructure, performance, ai_ml, etc. |
| **Checklists** | 5 | judge-morningstar, courtroom-scribe, octavius, aegis-protocol, critibot-review |

---

## Deliberation Metrics (from state/metrics.md)

| Metric | Value |
|--------|-------|
| Total Sessions | 5+ |
| Total Deliberations | 13 |
| Decisions Made | 12 |
| Unanimous Decisions | 8 |
| Total Precedents | 13 |
| Handoffs to LIL_JEFF | 3+ |
| Prophet Proposals | 9 hail-marys tracked (4 deferred, aspirations recorded) |
| Prophet Vindications | 0 |
| SME Participations (Jul 25) | 12+ witnesses; 6 specialist seatings |

---

## Transcript & Output Metrics

| Location | Count |
|----------|-------|
| Courtroom transcripts | 23 certified/filed `.md` (excl. handoffs/html) |
| Litigation transcripts | 3 |
| Handoff documents | 5 |
| Jul 25 hot-button filings | 4 (FEAT-001, DEL-005, DEL-006, SEC-003) |
| Agent reports output | `agents/reports/` (RPT_*_YYYYMMDD_HHMMSS.html) |

---

## Current Sprint

### Active Tasks

| Task | Module | Priority | Status |
|------|--------|----------|--------|
| Operationalize APMS / SCG / AFAP runbooks | courtroom, docs | High | ⏳ |
| F4+ Specialist Pilot formal review | core, procedures | Medium | 🔍 |
| Prophet vindication tracking | core, templates | Medium | 🔄 |
| LIL_JEFF handoff completion | agents | High | 🔍 |

### Completed This Sprint

- [x] Research Report workflow (4-agent pipeline, gpt-4.1-mini)
- [x] Report ID + timestamp output format
- [x] Gmail delivery for reports
- [x] agents/tools and agents/workflows layout
- [x] Tavily + DuckDuckGo search integration
- [x] 2026-07-25 hot-button docket (4 expansive proceedings certified)
- [x] Court Reporter sync (precedents, metrics, dashboard, manifest)

---

## Technical Decisions

| Decision | Rationale | Date |
|----------|-----------|------|
| OpenAI-compat APIs | Unified interface for Ollama, LM Studio, OpenRouter | — |
| OpenRouter for workflows | gpt-4.1-mini, flexible model routing | 2026-02 |
| YAML for domain registry | Human-editable, versionable SME definitions | — |
| Markdown transcripts | Portable, readable, version-control friendly | — |
| Alphanumeric report ID + timestamp | Traceable, sortable output filenames | 2026-02-19 |
| APMS default-deny unsupervised prod mutations | Agentic blast-radius control (2026-FEAT-001) | 2026-07-25 |
| SCG staged open-weight redistribution | Dual-use / geopolitics posture (2026-DEL-005) | 2026-07-25 |
| AFAP agent legal-filing authentication | Duty of candor + citation ledger (2026-DEL-006) | 2026-07-25 |

---

## Blockers & Risks

| Issue | Impact | Mitigation | Owner |
|-------|--------|------------|-------|
| Prophet proposals deferred | Pending judgment on radical ideas | Operational experience; revisit periodically | — |
| APMS/SCG/AFAP not yet runbook-tooled | Principles binding but ops incomplete | Handoff to LIL_JEFF for checklists | — |
| F4+ Specialist Pilot review overdue | Pilot used without formal closeout | Schedule review deliberation | — |

---

## Quick Commands

```bash
# MORNINGSTAR deliberation (via Cursor agent)
/morningstar

# Litigation runner (Ollama, LM Studio, OpenRouter)
./litigation/launch.sh
python litigation/run.py "Your matter"

# Research Report workflow
python agents/workflows/research_report.py "Topic" [--to email@example.com]

# Transcript viewer
./courtroom/portal/launch.sh

# Court Reporter (sync docs every 3h)
python courtroom/reporter.py
# Cron: 0 */3 * * * cd /path/to/LLM_Personas && python courtroom/reporter.py

# State checkpoint
/update   # Mid-session
/end      # Close session
```

---

## Notes

- Metrics source: `state/metrics.md`
- Agent skills index: `docs/agent-skills.md`
- Workflow docs: `agents/workflows/README.md`, `agents/tools/research-report-workflow.md`

---

*Dashboard maintained by CodeFarm 🌱 · MORNINGSTAR Operational Agent Swarm*
