# Skill: Create-rule

**Agent:** lil-jeff  
**Index:** `docs/agent-skills.md` § lil-jeff

## Source

Cursor skill: **create-rule** (see Cursor skills-cursor or agent_skills).

## When to use

When the user asks for a **Cursor rule** or **RULE.md** (or .cursor/rules/ content). Delegate to or reference the create-rule skill so the correct format and location are used.

## Fallback

Do not improvise rule format. If the Cursor skill cannot be invoked, direct the user to the create-rule process so output follows RULE.md / .cursor/rules/ conventions.

## Procedure

1. On user request for a rule: use or reference the **create-rule** skill.
2. Do not invent file paths or structure; defer to the canonical skill.
3. Deliver the rule content in the format prescribed by create-rule (e.g. RULE.md structure, placement under .cursor/rules/ or project root).
