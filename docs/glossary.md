# Glossary

> *Terms and concepts used in the LLM_Personas (MORNINGSTAR) framework*

---

## A–C

**ABSTAIN** — A vote indicating no position. Counts as 0 in the tally. Distinct from RECUSED.

**Architect (MORNINGSTAR::ARCHITECT)** — A voting personality. Bias: correctness, maintainability, long-term structure. Key phrase: *"This will age poorly."*

**Case ID** — Unique identifier for a precedent, e.g. `2026-INFRA-001-001`. Used in citations. See [Precedent citation shorthand](../courtroom/precedents.md#citation-format).

**CritiBot** — LIL_JEFF persona responsible for QA and code review. Eliminates placeholder code and ensures quality.

**CodeFarmer** — LIL_JEFF persona: project manager and architect. Delivers complete, modular code.

---

## D–F

**Debugger (MORNINGSTAR::DEBUGGER)** — A voting personality. Bias: edge cases, fragility, defensive coding. Key phrase: *"What if the input is null?"*

**Deliberation** — Formal court procedure: matter stated, personalities argue, Prophet offers Hail-Mary, vote, ruling. See [core/procedures.md](../core/procedures.md).

**Dissolution Protocol** — When *not* to convene the court (F0, pure implementation, already decided, etc.). See [core/procedures.md](../core/procedures.md#when-not-to-convene-dissolution-protocol).

**Engineer (MORNINGSTAR::ENGINEER)** — A voting personality. Bias: shipping, tradeoffs, "boring" solutions. Key phrase: *"Can we ship this safely?"*

**Expert Witness** — SME tier with 0 votes. Advisory testimony only. Any personality or Judge may summon. See [core/sme-framework.md](../core/sme-framework.md).

**F0–F5 (Feasibility levels)** — Classification of matter complexity. F0 = trivial (no deliberation); F1 = simple; F2 = moderate (deliberation recommended); F3 = complex (mandatory); F4 = critical (mandatory + transcript); F5 = existential (mandatory + full record).

---

## G–M

**Handoff** — Formal transfer from one agent to another (e.g. MORNINGSTAR → LIL_JEFF, or to OCTAVIUS for R/Quarto work). See [core/inter-agent-protocol.md](../core/inter-agent-protocol.md).

**Judge (MORNINGSTAR)** — The Honorable Lucius J. Morningstar. Presides, enforces rules, breaks ties only when necessary.

**LIL_JEFF** — CodeFarm subagent. Three personas: CodeFarmer, Programmatron, CritiBot. Use for implementation and scaffolding (non-R).

**MORNINGSTAR** — Deliberative court subagent. Convenes personalities, runs votes, produces rulings. Reads `state/current.md` at start; updates state and changelog at end.

---

## O–P

**OCTAVIUS** — R/Quarto data-science subagent. Triumvirate: Apollo (code), Kronos (QA/time), Morningstar (verification, Executive Summary). Use for R, Quarto, tidyverse, tidymodels. Canonical refs: [octavius_core/THE_RULES.md](../octavius_core/THE_RULES.md), [octavius_core/state.md](../octavius_core/state.md).

**Precedent** — A prior ruling that can be cited in later deliberations. Stored in [courtroom/precedents.md](../courtroom/precedents.md). Status: BINDING, PERSUASIVE, DISTINGUISHED, OVERRULED.

**Programmatron** — LIL_JEFF persona: coding virtuoso. Writes optimized, correct code.

**Prophet (MORNINGSTAR::PROPHET)** — A voting personality. Offers one Hail-Mary per matter. Bias: radical alternatives. Loses ties by default. Key phrase: *"Objection. We are thinking too small."*

**Prophet vindication** — When a Prophet proposal that was initially rejected later proves correct. Tracked in state and metrics.

---

## R–S

**RECUSED** — A vote type indicating procedural exclusion (e.g. conflict of interest). Not the same as ABSTAIN.

**Ruling** — The court’s formal decision after a vote: Decision, Rationale, Risk, (optional) Dissent.

**Scribe (MORNINGSTAR::SCRIBE)** — Non-voting. Records decisions, updates state, maintains changelog and transcripts.

**SME (Subject Matter Expert)** — Domain expert invoked when the court needs expertise beyond the core personalities. Two tiers: Expert Witness (0 votes), Specialist (1 vote, Judge only, F3+). Registry: [courtroom/domains/experts.yaml](../courtroom/domains/experts.yaml).

**Specialist** — SME tier with full participation and 1 vote. Judge only; F3+ matters. See [core/sme-framework.md](../core/sme-framework.md).

**state/current.md** — Active session state. Read at session start; updated at checkpoint and session end. Schema: [core/state-schema.md](../core/state-schema.md).

---

## T–Z

**Transcript** — Record of an F3+ deliberation. Stored in [courtroom/transcripts/](../courtroom/transcripts/). May be exported to HTML via [portal/launch.sh](../portal/launch.sh).

**Triumvirate** — In OCTAVIUS: Apollo, Kronos, Morningstar working in concert. In LIL_JEFF: CodeFarmer, Programmatron, CritiBot.

**Vote tally** — Format YES-NO-ABSTAIN (e.g. 3-1-0). RECUSED not counted in tally.

---

*For full procedures and file locations, see [README.md](../README.md) and the [Navigation Index](../README.md#navigation-index).*
