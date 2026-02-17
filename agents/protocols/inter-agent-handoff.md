# Inter-Agent Handoff Protocol

> **Full protocol:** `core/inter-agent-protocol.md`  
> This document is a summary and quick reference for handoff format and response format.

## Who hands off to whom

| From | To | When |
|------|-----|------|
| MORNINGSTAR | LIL_JEFF | Ruling requires implementation (general code, scaffolding, non-R) |
| MORNINGSTAR | OCTAVIUS | Ruling requires R/Quarto/tidyverse implementation |
| LIL_JEFF | MORNINGSTAR | Scope change, F2+ concern, or block requiring deliberation |
| Aegis | MORNINGSTAR | Scenario judicial or beyond containment; see `aegis-escalation.md` |

## MORNINGSTAR → LIL_JEFF handoff block

Provide:

```
┌─────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION HANDOFF                                          │
├─────────────────────────────────────────────────────────────────┤
│ Case: [CASE-ID]                                                 │
│ Decision: [Clear statement]                                     │
│ Vote: [Tally]                                                   │
├─────────────────────────────────────────────────────────────────┤
│ SPECIFICATION                                                   │
│ What to implement: [list]                                       │
│ Constraints: [list]                                             │
│ Flexibility: [areas of discretion]                              │
│ Success criteria: [how to verify]                                │
├─────────────────────────────────────────────────────────────────┤
│ RISK ACKNOWLEDGMENT                                             │
│ Accepted risk: []; Mitigation: []                               │
├─────────────────────────────────────────────────────────────────┤
│ ESCALATION TRIGGERS                                             │
│ Return to court if: [conditions]                                 │
└─────────────────────────────────────────────────────────────────┘
```

## LIL_JEFF acknowledgment

- Confirm understanding (paraphrase requirements, constraints, flexibility).
- State approach and module breakdown.
- List questions/clarifications if any.
- Proceed with implementation.

## LIL_JEFF completion report

- Case, Status: COMPLETE.
- Delivered: files and what they do.
- Deviations: none or list.
- CritiBot Review: PASSED.

## LIL_JEFF → MORNINGSTAR escalation

When blocked or scope change:

- Original Case, Implementation Status: BLOCKED.
- Issue and why it requires deliberation.
- Options identified; recommendation if any.
- "Returning to court for ruling."

## OCTAVIUS handoff

- Pass: task description, data/script paths, desired output (e.g. Quarto report).
- OCTAVIUS confirms specs at start, delivers Executive Summary at end to `octavius_summaries/`.

For full detail, handoff examples, and error handling, see **`core/inter-agent-protocol.md`**.
