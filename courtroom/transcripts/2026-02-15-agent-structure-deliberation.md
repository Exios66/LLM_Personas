# Court Deliberation: Agent Structure Enhancement (CrewAI-Style Attributes)

**Date:** 2026-02-15  
**Matter ID:** 2026-ARCH-001  
**Feasibility:** F3 (architectural impact on agent definitions; no runtime risk)  
**Reference:** [docs/agent-structure-investigation.md](../../docs/agent-structure-investigation.md)

---

## Phase 1: Opening

**MORNINGSTAR (Judge):** The court will now consider whether to adopt an enhancement to our agent structure inspired by CrewAI's "Key Attributes for Customization." We are not adopting CrewAI; we are evaluating which of those concepts map usefully onto our Cursor subagent definitions (`.cursor/agents/*.md`). The investigation document recommends adding optional frontmatter: `role`, `goal`, `backstory`, and optionally `allow_delegation` and `response_format`. Runtime attributes (max RPM, cache, max iter, etc.) are out of scope—we cannot configure them in Cursor. This is classified F3 due to schema and documentation impact across all three agents.

---

## Phase 2: Arguments

**ARCHITECT:** Adopt. Explicit `role` and `goal` give us a stable, parseable contract. Today "what this agent is" is buried in prose; frontmatter makes it machine-readable for future tooling or docs generation. Keep backstory optional and short so we don't duplicate the body. *This will age well.*

**ENGINEER:** Adopt. Low cost: add a few YAML keys Cursor ignores. Improves discoverability and aligns with how other frameworks describe agents. Implementation is a small frontmatter edit per agent plus one schema doc. *Ship it.*

**DEBUGGER:** Adopt with a guardrail. We must avoid drift: if we add `goal` in frontmatter, the body must not contradict it. Recommend we add a one-line note in procedures or agent-schema: "Frontmatter is canonical summary; body elaborates." *What if a future editor changes the body but not the goal?* Document that consistency is maintainer's responsibility.

**PROPHET:** Adopt. *Objection. We are thinking too small.* Don't just mirror CrewAI—own it. Add a single optional `crew_style: true` and document that when true, the agent frontmatter follows the CrewAI-inspired schema so that if we ever export to CrewAI or another framework, we have a flag and a shape. One extra key, future-proof.

---

## Phase 3: Hail-Mary

**PROPHET (Hail-Mary):** Ship a *fourth* agent: a minimal "template" agent (e.g. `template.md`) that embodies the full schema with placeholder role/goal/backstory so new agents can be created by copy-paste. Ensures the schema is exercised and documented in one place.

---

## Phase 4: Vote

| Personality | Vote | Rationale |
|-------------|------|-----------|
| ARCHITECT   | YES  | Clear contract; machine-readable. |
| ENGINEER    | YES  | Low effort, better structure. |
| DEBUGGER    | YES  | Adopt with consistency note. |
| PROPHET     | YES  | Adopt; flag and template are nice-to-have, not blocking. |

**Result:** 4-0-0 (YES-NO-ABSTAIN)

---

## Phase 5: Ruling

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ RULING                                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Decision: Adopt CrewAI-inspired optional agent frontmatter. Add `role`,      │
│           `goal`, optional `backstory`; optionally `allow_delegation` and     │
│           `response_format`. Document schema; do not add runtime-only        │
│           attributes (max RPM, cache, max iter, etc.).                       │
│ Vote: 4-0-0                                                                  │
│ Rationale: Improves clarity and future-proofing without breaking Cursor.    │
│            Consistency rule: frontmatter = canonical summary; body         │
│            elaborates. Prophet's template agent and crew_style flag are     │
│            deferred to a follow-up (not blocking).                           │
│ Risk: Minor duplication if maintainers update body but not frontmatter;     │
│       mitigated by documenting the contract in agent-schema.                │
│ Dissent: None.                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**MORNINGSTAR (Judge):** The court has ruled. Regrettably sensible. Implementation is handed to LIL_JEFF per project norms: extend agent frontmatter, add `docs/agent-schema.md`, and note consistency in procedures or schema doc.

---

## Deliverables (Handoff to LIL_JEFF)

| # | Item | Location / Action |
|---|------|-------------------|
| 1 | Agent schema doc | Add `docs/agent-schema.md`: optional frontmatter `role`, `goal`, `backstory`, `allow_delegation`, `response_format`; state "frontmatter = canonical summary; body elaborates." |
| 2 | MORNINGSTAR agent | Add to `.cursor/agents/morningstar.md` frontmatter: `role`, `goal`, optional `backstory`, `allow_delegation: true`. |
| 3 | LIL_JEFF agent | Add to `.cursor/agents/lil-jeff.md` frontmatter: `role`, `goal`, optional `backstory`, `allow_delegation: true`. |
| 4 | OCTAVIUS agent | Add to `.cursor/agents/octavius.md` frontmatter: `role`, `goal`, optional `backstory`, `allow_delegation: true`. |
| 5 | Inter-agent protocol | In `core/inter-agent-protocol.md`, add one-line note that agent frontmatter may include `allow_delegation` for clarity. |
| 6 | Repository Map / README | If needed, reference `docs/agent-schema.md` in Repository Map or ONBOARDING. |

*Deferred (optional follow-up):* template agent (`template.md`), `crew_style` flag.
