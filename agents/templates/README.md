# Agent Templates

Reusable templates for agent outputs: session state, transcript certification, handoffs, escalation, and executive summary. Full session lifecycle templates live in repo `templates/`; these are agent-focused snippets and blocks.

## Layout

| Template | Used by | Purpose |
|----------|---------|---------|
| **`session-state-init.md`** | morningstar | Minimal state structure for init; full template in `templates/session-start.md` |
| **`transcript-certification.md`** | morningstar | Scribe certification line and closing block |
| **`handoff-from-morningstar.md`** | morningstar | IMPLEMENTATION HANDOFF block for MORNINGSTAR → LIL_JEFF |
| **`handoff-acknowledgment.md`** | lil-jeff | LIL_JEFF acknowledgment block on receiving handoff |
| **`completion-report.md`** | lil-jeff | LIL_JEFF completion report block |
| **`escalation-lil-jeff-to-morningstar.md`** | lil-jeff | LIL_JEFF → MORNINGSTAR escalation block |
| **`aegis-escalation.md`** | aegis-protocol | Aegis → MORNINGSTAR escalation block |
| **`executive-summary-octavius.md`** | octavius | Octavius Executive Summary block for `octavius_summaries/` |

## Canonical References

- **Session start (full):** `templates/session-start.md`
- **Handoff protocol (full):** `core/inter-agent-protocol.md`, `agents/protocols/inter-agent-handoff.md`
