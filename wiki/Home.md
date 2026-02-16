# MORNINGSTAR Court System

> *"The court convenes. The deliberation begins. The outcome is inevitable."*  
> — The Honorable Lucius J. Morningstar

A deliberative AI persona framework that transforms complex decisions into structured courtroom proceedings. MORNINGSTAR operates as an internal courtroom of distinct personalities who argue, vote, and reach binding rulings on architectural, implementation, and debugging matters.

---

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

---

## Quick Links

| Topic | Page |
|-------|------|
| Get started | [Quick-Start](Quick-Start) |
| Court members | [The-Court](The-Court) |
| Commands | [Command-Reference](Command-Reference) |
| When to convene | [When-to-Convene](When-to-Convene) |
| SMEs | [Domains-and-Experts](Domains-and-Experts) · [SME-Framework](SME-Framework) |
| Procedures | [Procedures](Procedures) |
| State & recovery | [State-and-Metrics](State-and-Metrics) · [Error-Recovery](Error-Recovery) |
| Handoffs | [Inter-Agent-Protocol](Inter-Agent-Protocol) |
| Portal (transcripts) | [Portal](Portal) |
| New users | [Onboarding](Onboarding) |
| Reference | [Glossary](Glossary) · [Runbook](Runbook) · [Edge-Cases](Edge-Cases) |
| Personas | [Companion-Personas](Companion-Personas) |
| Precedents & history | [Precedents](Precedents) · [Changelog](Changelog) |
| Full file map | [Repository-Map](Repository-Map) |

---

## Quick Start (Summary)

1. **Initialize:** Invoke the **morningstar** subagent or use `/morningstar`. The court reads state and awaits your matter.
2. **Present your matter:** Describe what must be decided. The Judge classifies feasibility (F0–F5) and convenes deliberation when needed.
3. **Receive the ruling:** After arguments and vote, the court issues a ruling (Decision, Rationale, Risk).
4. **View transcripts:** From the project root, run `./portal/launch.sh` to open deliberation transcripts in a browser.
5. **Save progress:** Use `/update` to checkpoint and `/end` to close the session.

Details: [Quick-Start](Quick-Start) and [Procedures](Procedures).

---

*"The court is now in session. May your decisions age gracefully."*
