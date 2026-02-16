# Agent Schema (Frontmatter)

Canonical description of optional agent frontmatter for Cursor subagents in this repository. Inspired by [CrewAI — Customizing Agents](https://docs.crewai.com/how-to/Customizing-Agents/#key-attributes-for-customization). Runtime-only attributes (max RPM, cache, max iterations, max execution time, verbose, etc.) are not configurable in Cursor and are documented as N/A here.

---

## Rule

**Frontmatter is canonical summary; body elaborates.** Maintainers must keep frontmatter and agent body content consistent. When in doubt, the frontmatter is the short contract; the markdown body below it holds detailed behavior and procedures.

---

## Required (Cursor contract)

| Attribute    | Type   | Description |
|-------------|--------|--------------|
| `name`      | string | Agent identifier (e.g. `morningstar`, `lil-jeff`, `octavius`). Used for invocation and handoffs. |
| `description` | string | When to use this agent. Shown in UI and used for routing; keep concise and actionable. |

---

## Optional (CrewAI-style)

| Attribute         | Type    | Description |
|-------------------|---------|-------------|
| `role`            | string  | Short label for the agent (e.g. "Deliberative Court", "CodeFarm Developer"). |
| `goal`            | string  | One sentence: what the agent aims to achieve when invoked. |
| `backstory`       | string  | Optional; one or two sentences, or a reference to a section in the body (e.g. "See ## The Court."). |
| `allow_delegation`| boolean | When `true`, the agent may hand off to other agents per the inter-agent protocol. When `false` or omitted, treat as no delegation unless the protocol specifies otherwise. |
| `response_format` | string  | Optional; short description of output style or a pointer to a body section (e.g. "See ## Response Format."). |

---

## Example (minimal)

```yaml
---
name: morningstar
description: Sardonic deliberative coding partner; use for architectural decisions and deliberation.
role: Deliberative Court
goal: Reach reasoned, documented decisions on architectural and process matters through internal debate and vote.
allow_delegation: true
---
```

---

## Not applicable in Cursor

The following CrewAI agent attributes are runtime/execution concerns and are **not** part of this schema for Cursor subagents:

- Max RPM / rate limits  
- Cache settings  
- Max iterations / max execution time  
- Verbose / logging flags  

These remain N/A unless Cursor gains equivalent configuration surfaces.

---

## References

- **Handoff:** `courtroom/transcripts/HANDOFF-2026-ARCH-001.md`
- **Precedent:** 2026-ARCH-001-001 (BINDING)
- **CrewAI:** [Customizing Agents — Key attributes](https://docs.crewai.com/how-to/Customizing-Agents/#key-attributes-for-customization)
- **Protocol:** `core/inter-agent-protocol.md` (handoff and `allow_delegation`)
