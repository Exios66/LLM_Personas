# Skill: Create-rule / create-skill

**Agent:** morningstar  
**Index:** `docs/agent-skills.md` § morningstar

## Source

Cursor skills: **create-rule**, **create-skill** (see Cursor skills-cursor or agent_skills).

## When to use

When the user asks for a **Cursor rule**, **RULE.md**, **.cursor/rules/** content, or a **new skill** (SKILL.md). Delegate to or reference the appropriate Cursor skill so the correct format and location are used.

## Fallback

Do not improvise rule or skill format. If the Cursor skill cannot be invoked, direct the user to create the rule/skill via the documented process (e.g. create-rule SKILL.md, create-skill SKILL.md).

## Procedure

1. **Rule request:** Use or reference the **create-rule** skill so output follows RULE.md / .cursor/rules/ conventions.
2. **Skill request:** Use or reference the **create-skill** skill so output follows SKILL.md format and placement.
3. Do not invent file paths or structure; defer to the canonical skill.
