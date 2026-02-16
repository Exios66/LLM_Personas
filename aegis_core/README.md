# Aegis Core

> *"Authority enforced. Chaos controlled. System secured."*

This directory contains configuration and state for the **Aegis Protocol** — the Central Authority system for security, containment, rogue agent scenarios, and strategic decision-making.

---

## Purpose

The Aegis Protocol coordinates three operational agents (Sage, Watcher, Chronicler) to analyze scenarios requiring:

- Security breach assessment
- Rogue agent (Cyber Psychosis) containment
- Ethical dilemma analysis
- Crisis management
- Strategic decision-making
- Meta-deliberation (review of prior MORNINGSTAR transcripts)

**MORNINGSTAR acts as the Judicial Branch of Aegis.** When Aegis cannot resolve, it escalates to MORNINGSTAR for full court deliberation.

---

## When to Invoke

Use the **aegis-protocol** subagent when:

- Security analysis or containment is needed
- Ethical dilemmas require Sage/Watcher/Chronicler assessment
- Crisis management or strategic decisions need coordinated analysis
- A prior MORNINGSTAR transcript requires meta-analysis (bias, blind spots, historical parallels)
- Rogue agent behavior (prompt injection, misalignment, scope drift) is suspected

**Command:** `/aegis` or "Invoke aegis-protocol for [scenario type]"

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — purpose, invocation, links |
| `state.md` | Optional session state (last scenario, findings, escalation log) |

State is optional; Aegis may run stateless for ad-hoc scenarios.

---

## Canonical References

| Reference | Path |
|-----------|------|
| Agent definition | `.cursor/agents/aegis-protocol.md` |
| Inter-agent protocol | `core/inter-agent-protocol.md` (Aegis Protocol Handoffs) |
