# Handoff: Case 2026-ARCH-001 — Agent Structure (CrewAI-Style Attributes)

**From:** Court of MORNINGSTAR  
**To:** LIL_JEFF  
**Date:** 2026-02-15  
**Case:** 2026-ARCH-001  
**Vote:** 4-0-0 Unanimous  
**Transcript:** [2026-02-15-agent-structure-deliberation.md](2026-02-15-agent-structure-deliberation.md)

---

## Instructions for Implementer

1. **LIL_JEFF** is the primary implementer. Deliver complete, production-ready artifacts; no placeholders.
2. Implement in dependency order: schema doc first, then agent frontmatter, then protocol note.
3. Preserve existing agent body content; only add or extend YAML frontmatter and add new file `docs/agent-schema.md`.
4. When done, update CHANGELOG.md with an entry for "Agent Structure Enhancement (2026-ARCH-001)" and reference this handoff.

---

## Deliverables

### 1. Agent schema doc

- **File:** `docs/agent-schema.md` (create)
- **Purpose:** Canonical description of optional agent frontmatter inspired by CrewAI-style attributes.
- **Content:**
  - Required (Cursor contract): `name`, `description`.
  - Optional: `role` (short label, e.g. "Deliberative Court"), `goal` (one sentence: what the agent aims to achieve when invoked), `backstory` (optional; one or two sentences or reference to body), `allow_delegation` (boolean; whether agent may hand off to other agents), `response_format` (optional; short description or pointer to body section).
  - Rule: "Frontmatter is canonical summary; body elaborates." Maintainers must keep frontmatter and body consistent.
  - Reference: [CrewAI — Customizing Agents](https://docs.crewai.com/how-to/Customizing-Agents/#key-attributes-for-customization). Note that runtime-only attributes (max RPM, cache, max iter, etc.) are not applicable to Cursor subagents.

### 2. MORNINGSTAR agent

- **File:** `.cursor/agents/morningstar.md`
- **Action:** Add to frontmatter (keep existing `name`, `description`): `role`, `goal`, optional `backstory`, `allow_delegation: true`. Example values: role "Deliberative Court"; goal "Reach reasoned, documented decisions on architectural and process matters through internal debate and vote."

### 3. LIL_JEFF agent

- **File:** `.cursor/agents/lil-jeff.md`
- **Action:** Add to frontmatter: `role`, `goal`, optional `backstory`, `allow_delegation: true`. Example: role "CodeFarm Developer"; goal "Deliver complete, modular, production-ready code and scaffold implementations per handoff or user request."

### 4. OCTAVIUS agent

- **File:** `.cursor/agents/octavius.md`
- **Action:** Add to frontmatter: `role`, `goal`, optional `backstory`, `allow_delegation: true`. Example: role "R/Quarto Data Science Triumvirate"; goal "Deliver verified, reproducible R/Quarto analysis and ML workflows with executive summaries."

### 5. Inter-agent protocol

- **File:** `core/inter-agent-protocol.md`
- **Action:** Add a one-line note (e.g. in "Agent Responsibilities" or a new "Agent metadata" subsection): Agent definitions may include optional frontmatter `allow_delegation`; when true, the agent may hand off to other agents per this protocol.

### 6. Repository Map / docs

- **Action:** If not already present, add `docs/agent-schema.md` to the Repository Map (wiki/Repository-Map.md and README.md Repository Map section) under Docs.

---

## Out of scope (deferred)

- Template agent (`template.md`) and `crew_style` flag: optional follow-up.
- Runtime attributes (max RPM, cache, max iter, max execution time, verbose, etc.): not configurable in Cursor; documented as N/A in investigation.

---

*Implementation complete when all six deliverables are done and CHANGELOG updated.*
