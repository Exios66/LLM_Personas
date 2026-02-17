# Skill: Handoff protocol

**Agent:** lil-jeff  
**Index:** `docs/agent-skills.md` § lil-jeff

## Source

`core/inter-agent-protocol.md`. See also `agents/protocols/inter-agent-handoff.md`.

## When to use

When **receiving handoff from MORNINGSTAR**. Read the protocol and acknowledge the specification, constraints, and success criteria before implementing.

## Fallback

If `core/inter-agent-protocol.md` is missing: proceed with standard CodeFarm workflow (gather requirements, implement, CritiBot pass). Still confirm understanding of the handoff block if one was provided.

## Procedure

1. On handoff from MORNINGSTAR: read `core/inter-agent-protocol.md` (or `agents/protocols/inter-agent-handoff.md`) for handoff format and response format.
2. Parse the IMPLEMENTATION HANDOFF block: Case, Decision, Specification, Constraints, Flexibility, Success criteria, Risk.
3. Acknowledge understanding (e.g. "CodeFarm acknowledges handoff. Implementing per specification.").
4. Implement; report completion and any deviations per protocol response format.
