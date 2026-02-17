# Repository Map

Full directory and key file reference. Source of truth: main repo `README.md` (Repository Map section).

## Agents

| Path | Purpose |
| ------ | --------- |
| `.cursor/agents/morningstar.md` | MORNINGSTAR courtroom agent |
| `.cursor/agents/lil-jeff.md` | LIL_JEFF (CodeFarm) agent |
| `.cursor/agents/octavius.md` | OCTAVIUS (R/Quarto) agent |
| `.cursor/agents/aegis-protocol.md` | Aegis Protocol — Central Authority (Sage, Watcher, Chronicler; security, containment, rogue agent scenarios) |

## Core

| Path | Purpose |
| ------ | --------- |
| `core/personalities.md` | Judge, Consultant, Architect, Engineer, Debugger, Prophet, Counsel, Scribe |
| `core/procedures.md` | Session lifecycle, deliberation flow, dissolution, SME procedures |
| `core/sme-framework.md` | Expert Witness & Specialist protocol |
| `core/state-schema.md` | Validation rules for state/current.md |
| `core/error-recovery.md` | State corruption recovery, rollback, emergency procedures |
| `core/inter-agent-protocol.md` | MORNINGSTAR ↔ LIL_JEFF ↔ OCTAVIUS handoff |

## Courtroom

| Path | Purpose |
| ------ | --------- |
| `courtroom/RULES.md` | Formal courtroom rules |
| `courtroom/BEST_PRACTICES.md` | Practical guidance |
| `courtroom/precedents.md` | Precedent database |
| `courtroom/transcripts/` | Deliberation transcripts (.md and .html) |
| `courtroom/domains/README.md` | Domain expert registry usage |
| `courtroom/domains/experts.yaml` | Canonical SME domain definitions |
| `courtroom/spectators.md` | Courtroom spectators (Dr. Echo Sageseeker, Dr. Harley Scarlet Quinn) |
| **courtroom/portal/** | Transcript viewer and export |
| `courtroom/portal/launch.sh` | Interactive transcript launcher |
| `courtroom/portal/export_transcript.py` | Export one .md → HTML |
| `courtroom/portal/viewer.html` | Standalone viewer |
| `courtroom/portal/generate_manifest.py` | Generate transcripts_manifest.json |
| `courtroom/portal/transcripts_manifest.json` | Manifest (generated) |
| `courtroom/portal/generate.py` | Optional: gitmal static site generator |
| `courtroom/portal/exports/` | HTML output |
| `courtroom/portal/output/` | Generated static site (gitmal) |

## State

| Path | Purpose |
| ------ | --------- |
| `state/current.md` | Active session state |
| `state/metrics.md` | Cumulative statistics |
| `state/sme-failures.md` | SME failure log |
| `state/backups/` | Session state backups (auto-generated) |

## OCTAVIUS

| Path | Purpose |
| ------ | --------- |
| `octavius_core/THE_RULES.md` | Triumvirate binding protocols |
| `octavius_core/state.md` | R/Quarto session state |
| `octavius_summaries/` | Executive summaries |

## Aegis Protocol

| Path | Purpose |
| ------ | --------- |
| `aegis_core/README.md` | Purpose, invocation, links to agent and inter-agent protocol |
| `aegis_core/state.md` | Optional session state (last scenario, findings, escalation log) |
| `wiki/Aegis-Protocol.md` | Full Aegis Protocol documentation (Sage, Watcher, Chronicler) |

## Docs

| Path | Purpose |
| ------ | --------- |
| `docs/ONBOARDING.md` | Start here |
| `docs/agent-schema.md` | Agent frontmatter schema (CrewAI-style) |
| `docs/glossary.md` | Glossary |
| `docs/RUNBOOK.md` | Troubleshooting index |
| `docs/edge-cases.md` | Edge case registry |

## Other

| Path | Purpose |
| ------ | --------- |
| `templates/` | Session, module, project-dashboard, special-interest-hearing, contempt-hearing templates |
| `litigation/` | Courtroom runner (Ollama, LM Studio, OpenRouter) |
| `litigation/run.py` | Main deliberation runner |
| `litigation/README.md` | Setup and usage |
| `checklists/aegis-protocol.md` | Aegis Protocol invocation & execution |
| `checklists/courtroom-scribe.md` | Scribe transcript & certification |
| `checklists/critibot-review.md` | Code review checklist |
| `checklists/judge-morningstar.md` | Judge deliberation & session flow |
| `checklists/octavius.md` | Octavius triumvirate workflow |
| `references/naming-conventions.md` | Naming patterns |
| `reference_files/` | Original persona sources |
| `CHANGELOG.md` | Decision history |
| `README.md` | Main project readme |

---

**See also:** [Onboarding](Onboarding) · [Quick-Start](Quick-Start) · [Home](Home)
