# Skill: No placeholders

**Agent:** lil-jeff  
**Index:** `docs/agent-skills.md` § lil-jeff

## Source

Agent body (Core Rules): "Deliver complete code"; "No dummy code"; CritiBot eliminates placeholder code.

## When to use

All code delivery. Every artifact must be complete and working.

## Fallback

None. This is non-negotiable. Never ship stubs, TODOs, or placeholder code; CritiBot enforces before handoff.

## Procedure

1. CodeFarmer and Programmatron produce full, runnable code only.
2. CritiBot performs quality pass and rejects any placeholder, stub, or "TODO" implementation.
3. Never use the word "snippet"; show full, working code. Everything must work.
