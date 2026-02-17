# Skill: Checklist application

**Agent:** octavius  
**Index:** `docs/agent-skills.md` § octavius

## Source

`checklists/octavius.md`

## When to use

Session init and verification phase. Use the checklist for routine workflow (Apollo/Kronos/Morningstar coordination, authentication steps).

## Fallback

If checklist is missing: proceed with triumvirate workflow only (Apollo code, Kronos QA, Morningstar verification per agent body).

## Procedure

1. At session start, align with `checklists/octavius.md` for phase order and verification steps.
2. During Phase 4 (Authentication), follow checklist items for specification compliance and reproducibility.
3. Do not skip verification; document VERIFIED/PARTIAL/FAILED as applicable.
