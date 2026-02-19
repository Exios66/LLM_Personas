# Cursor Skills (Project)

Project-scoped Cursor agent skills for LLM_Personas. These teach the agent how to perform MORNINGSTAR-specific workflows.

| Skill | Purpose |
|-------|---------|
| **morningstar-court-reporter** | Integrates all courtroom documentation (transcripts, precedents, metrics, dashboard); run every 3 hours or on demand |
| **morningstar-deliberation-runner** | Outlines and initiates full-length court deliberation sessions; 7-phase flow, feasibility gate, initiation workflow |
| **morningstar-scribe** | Transcript certification, state/CHANGELOG updates, Scribe checklist application |

See each skill's `SKILL.md` for description and trigger scenarios. Distinct from `agents/skills/` (agent skill docs indexed in `docs/agent-skills.md`).
