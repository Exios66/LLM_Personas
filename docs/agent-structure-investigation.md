# Agent Structure Investigation: CrewAI-Style Attributes

**Case:** 2026-ARCH-001 (proposed)  
**Matter:** Addition of CrewAI-inspired "Key Attributes for Customization" to LLM_Personas agent structure  
**Source:** [CrewAI — Customizing Agents](https://docs.crewai.com/how-to/Customizing-Agents/#key-attributes-for-customization)  
**Status:** Court deliberation complete. Ruling: Adopted (4-0-0). Handoff: HANDOFF-2026-ARCH-001.  

---

## 1. Current Agent Structure (LLM_Personas)

- **Location:** `.cursor/agents/*.md` (morningstar.md, lil-jeff.md, octavius.md)
- **Format:** YAML frontmatter + Markdown body
  - **Frontmatter:** `name`, `description` (Cursor subagent contract)
  - **Body:** Full system prompt (persona, directives, procedures)
- **Runtime:** Cursor subagents; no CrewAI or other agent framework in-repo

---

## 2. Proposed Attributes (CrewAI Reference)

| Attribute | CrewAI purpose | Fit for Cursor agents |
|-----------|----------------|------------------------|
| **Role** | Agent's job in the crew (e.g. Analyst, Customer Service Rep) | **High.** Maps to "what this agent does"; currently implied in `description` and body. Explicit `role` would clarify and could drive UI/docs. |
| **Goal** | What the agent aims to achieve, aligned with crew objectives | **High.** Aligns with "when to use" and success criteria; can be derived from body or made explicit in frontmatter. |
| **Backstory** | Depth to persona, motivations, engagements | **Medium.** Already in body (e.g. Court personalities, Triumvirate). Optional frontmatter or dedicated section could standardize. |
| **Tools** | Capabilities/methods (functions, integrations) | **Low in Cursor.** Cursor provides tools (read_file, run_terminal_cmd, etc.); we don't define tools per agent. Document as "uses Cursor toolset" or leave for future integration. |
| **Cache** | Whether agent uses cache for tool usage | **N/A.** Not exposed in Cursor subagent model. |
| **Max RPM** | Max requests per minute | **N/A.** Cursor/platform concern, not per-agent in our repo. |
| **Verbose** | Detailed logging of agent actions | **N/A.** Not configurable in our agent files. |
| **Allow Delegation** | Whether agent can delegate to other agents | **High (concept).** We have handoff rules in `core/inter-agent-protocol.md`. Could add `allow_delegation` as a documented trait (e.g. MORNINGSTAR may hand off to LIL_JEFF; LIL_JEFF may suggest OCTAVIUS). |
| **Max Iter** | Max iterations per task | **N/A.** Not exposed in Cursor. |
| **Max Execution Time** | Max time to complete a task | **N/A.** Not exposed in Cursor. |
| **System Template** | System format for the agent | **Medium.** Our body *is* the system content; we could document a standard structure (e.g. Core Directives, Procedures, References) as the "template." |
| **Prompt Template** | Prompt format for the agent | **Low.** User/composer provides prompts; we don't define prompt templates per agent. |
| **Response Template** | Response format for the agent | **Medium.** We have conventions (e.g. ruling format, CodeFarm banner, OCTAVIUS summaries). Could document as optional `response_format` in frontmatter or body. |
| **Use System Prompt** | Whether agent uses a system prompt | **N/A.** Cursor always uses the agent body as system context. |
| **Respect Context Window** | Sliding context / context size | **N/A.** Platform/LLM concern. |
| **Max Retry Limit** | Max retries on task error | **N/A.** Not configurable in our files. |

---

## 3. Recommendations (Pre-Deliberation)

### 3.1 Adopt in frontmatter (high value, no runtime dependency)

- **role** — Short label (e.g. `Deliberative Court`, `CodeFarm Developer`, `R/Quarto Data Science`). Enables consistent docs and future tooling.
- **goal** — One sentence: what the agent aims to achieve when invoked. Complements `description` (which is "when to use").
- **backstory** — Optional; one or two sentences or a reference to a section in the body. Keeps frontmatter small while allowing depth.

### 3.2 Document as conventions (no schema change)

- **allow_delegation** — Document in inter-agent protocol and/or agent body; optional boolean in frontmatter for clarity (e.g. `allow_delegation: true`).
- **response_format** — Optional short description or pointer to a section (e.g. "Ruling: Decision, Rationale, Risk"; "CodeFarm banner"; "OCTAVIUS Executive Summary"). Prefer body text for full format; frontmatter only if we want machine-readable hints.

### 3.3 Do not add (out of scope or N/A)

- Tools, Cache, Max RPM, Verbose, Max Iter, Max Execution Time, Use System Prompt, Respect Context Window, Max Retry Limit — either not applicable to Cursor subagents or not configurable in our repo. Can be noted in this doc for future integration (e.g. if we generate CrewAI configs).

### 3.4 Template standardization

- **System template:** Document in `docs/` or `core/` a recommended structure for agent body (e.g. Identity → Directives → Procedures → References). Do not require it for existing agents; use for new agents and gradual refactors.

---

## 4. Compatibility and Constraints

- **Cursor contract:** Cursor expects `name` and `description` in agent frontmatter. Additional keys are allowed and ignored by Cursor; they do not break the subagent.
- **Backward compatibility:** Adding optional frontmatter (role, goal, backstory, allow_delegation) and leaving body unchanged preserves current behavior.
- **Single source of truth:** Role/goal/backstory in frontmatter could duplicate body content if not careful. Recommendation: frontmatter = short, canonical summary; body = full narrative.

---

## 5. Proposed Next Steps (If Court Adopts)

1. **Schema/doc:** Add `docs/agent-schema.md` (or a section in Repository Map / ONBOARDING) describing optional frontmatter: `role`, `goal`, `backstory`, `allow_delegation`, and optional `response_format`.
2. **Implement:** Extend `.cursor/agents/morningstar.md`, `lil-jeff.md`, `octavius.md` with the new optional fields; keep body as-is or add one-line backstory references where useful.
3. **Protocol:** In `core/inter-agent-protocol.md`, add a one-line note that agent frontmatter may include `allow_delegation` for clarity.
4. **Changelog:** Record adoption and hand off implementation to LIL_JEFF per project norms.

---

*Document prepared for Court deliberation. No ruling until vote.*
