---
title: "Court System Guide"
---

> *"The court convenes. The deliberation begins. The outcome is inevitable."*  
> — The Honorable Lucius J. Morningstar

A deliberative AI persona framework that transforms complex decisions into structured courtroom proceedings. MORNINGSTAR operates as an internal courtroom of distinct personalities who argue, vote, and reach binding rulings on architectural, implementation, and debugging matters.

***
## What This Is

**MORNINGSTAR** is not a chatbot. It is a deliberative system.

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

***
## Quick Links

| Topic | Page |
|-------|------|
| Get started | [Quick-Start](/guide/quick-start.html) |
| Court members | [The-Court](/guide/the-court.html) |
| Commands | [Command-Reference](/guide/command-reference.html) |
| When to convene | [When-to-Convene](/guide/when-to-convene.html) |
| SMEs | [Domains-and-Experts](/guide/domains-and-experts.html) · [SME-Framework](/guide/sme-framework.html) |
| Procedures | [Procedures](/guide/procedures.html) |
| State & recovery | [State-and-Metrics](/guide/state-and-metrics.html) · [Error-Recovery](/guide/error-recovery.html) |
| Handoffs | [Inter-Agent-Protocol](/guide/inter-agent-protocol.html) |
| Portal (transcripts) | [Portal](/guide/portal.html) |
| New users | [Onboarding](/guide/onboarding.html) |
| Reference | [Glossary](/guide/glossary.html) · [Runbook](/guide/runbook.html) · [Edge-Cases](/guide/edge-cases.html) |
| Personas | [Companion-Personas](/guide/companion-personas.html) |
| Precedents & history | [Precedents](/guide/precedents.html) · [Changelog](/guide/changelog.html) |
| Full file map | [Repository-Map](/guide/repository-map.html) |

***
## Quick Start (Summary)

1. **Initialize:** Invoke the **morningstar** subagent or use `/morningstar`. The court reads state and awaits your matter.
2. **Present your matter:** Describe what must be decided. The Judge classifies feasibility (F0–F5) and convenes deliberation when needed.
3. **Receive the ruling:** After arguments and vote, the court issues a ruling (Decision, Rationale, Risk).
4. **View transcripts:** From the project root, run `./portal/launch.sh` to open deliberation transcripts in a browser.
5. **Save progress:** Use `/update` to checkpoint and `/end` to close the session.

Details: [Quick-Start](/guide/quick-start.html) and [Procedures](/guide/procedures.html).

***
*"The court is now in session. May your decisions age gracefully."*
