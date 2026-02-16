# Start Here — LLM_Personas Onboarding

> *One page to get you from zero to productive.*

---

## What This Repo Is

**LLM_Personas** is a deliberative AI persona framework. It hosts three Cursor subagents:

| Agent | Use when |
|-------|----------|
| **MORNINGSTAR** | You need a *decision*: architecture, tradeoffs, strategy. The court deliberates and rules. |
| **LIL_JEFF** | You need *code*: implementation, scaffolding, modules (anything except R/Quarto). |
| **OCTAVIUS** | You need *R, Quarto, tidyverse, or tidymodels*: analyses, reports, statistical workflows. |

---

## First Steps

1. **Open the repo** in Cursor. No install required for the agents.
2. **Portal (optional):** To view deliberation transcripts in a browser, run from the project root:
   ```bash
   ./portal/launch.sh
   ```
   If you get "permission denied," run `chmod +x portal/launch.sh` once. Python 3 is used to export transcripts on demand.
3. **Run your first deliberation:** Invoke the **morningstar** subagent and present a matter (e.g. "Should we use REST or GraphQL for the new API?"). The court will read `state/current.md`, deliberate, vote, and produce a ruling.

---

## Where to Go Next

| Goal | Where |
|------|--------|
| Full project map and navigation | [README.md](../README.md) |
| Court rules and commands | [README — Command Reference](../README.md#command-reference) |
| View transcripts | [portal/README.md](../portal/README.md) or run `./portal/launch.sh` |
| When to convene (and when not) | [core/procedures.md](../core/procedures.md) |
| Hand off to LIL_JEFF or OCTAVIUS | [core/inter-agent-protocol.md](../core/inter-agent-protocol.md) |
| SME domains and summoning | [courtroom/domains/README.md](../courtroom/domains/README.md) |
| Glossary of terms | [docs/glossary.md](glossary.md) |
| Troubleshooting | [docs/RUNBOOK.md](RUNBOOK.md) |

---

*"The court convenes. The deliberation begins."*
