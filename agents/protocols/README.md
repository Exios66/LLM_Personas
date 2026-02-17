# Agent Protocols

Interaction and task protocols for agents in `.cursor/agents/` and `agents/`. These documents define how agents hand off, when to invoke which agent, and how to run task flows.

## Layout

| Document | Purpose |
|----------|---------|
| **`inter-agent-handoff.md`** | MORNINGSTAR ↔ LIL_JEFF ↔ OCTAVIUS handoff format and response format. Summary; full text in `core/inter-agent-protocol.md`. |
| **`invocation-and-delegation.md`** | When to invoke morningstar, octavius, aegis-protocol, lil-jeff; when to delegate. |
| **`aegis-escalation.md`** | Aegis → MORNINGSTAR escalation format and procedure. |
| **`task-deliberation.md`** | Task protocol for standard deliberation; references `agents/tasks/` and `core/procedures.md`. |

## Canonical References

- **Full inter-agent protocol:** `core/inter-agent-protocol.md`
- **Task definitions:** `agents/tasks/`
- **Court procedures:** `core/procedures.md`
