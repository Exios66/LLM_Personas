# Quick Start

1. **Initialize a session** — Invoke the **morningstar** subagent or use `/morningstar`. The court reads `state/current.md`, summarizes active context, and awaits your matter.

2. **Present your matter** — Describe what needs to be decided. The Judge will classify its feasibility and convene the appropriate level of deliberation.  
   *Example:* "I need to decide between a REST API and GraphQL for the new service."

3. **Watch the court deliberate** — Each personality argues (3–5 lines). The Prophet offers one radical alternative. Votes are cast.

4. **Receive the ruling** — The court issues a ruling with Decision, Vote, Rationale, Risk, and optional Dissent.

5. **View transcripts in browser** — From the project root: `./portal/launch.sh`. Pick a deliberation; it opens in your default browser. See [Portal](Portal).

6. **Save progress** — Use `/update` to checkpoint state and `/end` to close the session and finalize records.

---

**Next:** [The-Court](The-Court) · [Command-Reference](Command-Reference) · [Procedures](Procedures)
