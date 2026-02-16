# Glossary

**ABSTAIN** — Vote meaning no position. Counts as 0. Distinct from RECUSED.

**Architect (MORNINGSTAR::ARCHITECT)** — Voting personality. Bias: correctness, maintainability. Key phrase: *"This will age poorly."*

**Case ID** — Unique identifier for a precedent (e.g. `2026-INFRA-001-001`). Used in citations.

**Dissolution Protocol** — When *not* to convene (F0, pure implementation, already decided, etc.). See [When-to-Convene](When-to-Convene).

**Expert Witness** — SME tier with 0 votes; advisory only. Any personality or Judge may summon.

**F0–F5** — Feasibility levels. F0 = trivial (no deliberation); F3+ = mandatory deliberation; F4+ = transcript required.

**Handoff** — Formal transfer between agents (e.g. MORNINGSTAR → LIL_JEFF or OCTAVIUS). See [Inter-Agent-Protocol](Inter-Agent-Protocol).

**LIL_JEFF** — CodeFarm subagent (CodeFarmer, Programmatron, CritiBot). Use for implementation and scaffolding (non-R).

**MORNINGSTAR** — Deliberative court subagent. Convenes personalities, runs votes, produces rulings. Reads and updates `state/current.md`.

**OCTAVIUS** — R/Quarto data-science subagent (Apollo, Kronos, Morningstar). Use for R, Quarto, tidyverse, tidymodels.

**Precedent** — Prior ruling stored in `courtroom/precedents.md`. Status: BINDING, PERSUASIVE, DISTINGUISHED, OVERRULED.

**Prophet (MORNINGSTAR::PROPHET)** — Voting personality. Offers one Hail-Mary per matter. Loses ties by default.

**RECUSED** — Vote type for procedural exclusion. Not the same as ABSTAIN.

**SME (Subject Matter Expert)** — Domain expert. Witness (0 votes) or Specialist (1 vote, Judge only, F3+). Registry: `courtroom/domains/experts.yaml`.

**Specialist** — SME tier with 1 vote; Judge only, F3+ matters.

**state/current.md** — Active session state. Read at start; updated at checkpoint and end.

**Transcript** — Record of an F3+ deliberation. Stored in `courtroom/transcripts/`. View via [Portal](Portal).

**Vote tally** — Format YES-NO-ABSTAIN (e.g. 3-1-0).
