# Onboarding — Start Here

## What This Repo Is

**LLM_Personas** hosts three Cursor subagents:

| Agent | Use when |
|-------|----------|
| **MORNINGSTAR** | You need a *decision*: architecture, tradeoffs, strategy. The court deliberates and rules. |
| **LIL_JEFF** | You need *code*: implementation, scaffolding, modules (anything except R/Quarto). |
| **OCTAVIUS** | You need *R, Quarto, tidyverse, or tidymodels*: analyses, reports, statistical workflows. |

## First Steps

1. Open the repo in Cursor. No install required for the agents.
2. **Portal (optional):** Run `./portal/launch.sh` from the project root to view transcripts in a browser. If needed: `chmod +x portal/launch.sh`. Python 3 used for export.
3. **First deliberation:** Invoke the **morningstar** subagent and present a matter (e.g. "Should we use REST or GraphQL for the new API?"). The court will read state, deliberate, vote, and produce a ruling.

## Where to Go Next

| Goal | Page |
|------|------|
| Quick start steps | [Quick-Start](Quick-Start) |
| Court and commands | [The-Court](The-Court) · [Command-Reference](Command-Reference) |
| When to convene | [When-to-Convene](When-to-Convene) |
| Hand off to LIL_JEFF or OCTAVIUS | [Inter-Agent-Protocol](Inter-Agent-Protocol) |
| SMEs | [Domains-and-Experts](Domains-and-Experts) |
| Glossary | [Glossary](Glossary) |
| Troubleshooting | [Runbook](Runbook) |
| Full file map | [Repository-Map](Repository-Map) |
