# Skill: Chaos injection note

**Agent:** aegis-protocol  
**Index:** `docs/agent-skills.md` § aegis-protocol

## Source

Agent body (Chaos Injection procedural definition): counterfactual, edge-case stress-test, Black Swan variant.

## When to use

Whenever chaos injection is applied (at randomized intervals or when synthesis seems brittle). Output must explicitly note that it was applied.

## Fallback

Output must note that chaos injection was applied. No silent application.

## Procedure

1. When applying (a) counterfactual reframe, (b) edge-case stress-test, or (c) Black Swan variant, record it in the output.
2. Include in output block: **CHAOS INJECTION APPLIED:** [Yes/No] — [If yes: brief description].
3. Purpose: ensure system adaptability and document that stress-testing was used.
