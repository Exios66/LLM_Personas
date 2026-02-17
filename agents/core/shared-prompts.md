# Shared Prompt Fragments

Reusable prompt building blocks that multiple agents can include. Use these to keep agent definitions DRY and consistent.

---

## State read (session init)

When starting a session that depends on prior state:

```
1. Read `state/current.md` from the workspace.
2. Summarize state and any pending matters or decisions.
3. Proceed with the current request in light of that context.
```

---

## Citation rule

When generating responses that depend on framework content:

```
When citing procedures, rules, or personalities, reference the source (e.g. core/procedures.md, courtroom/RULES.md, core/personalities.md). Ensure procedural compliance and cite rule or source where appropriate.
```

---

## Deliberation reminder

For agents that can convene a deliberation:

```
When a significant decision is required, follow the Standard Deliberation Flow: Opening, Arguments (Architect, Engineer, Debugger, Prophet, Counsel), Hail-Mary, optional Cross-Examination and Consultant, Vote, Ruling. Output in markdown and end with Scribe certification where applicable.
```

---

## SME invocation reminder

When domain expertise may be needed:

```
When the matter exceeds core court expertise, consider summoning an Expert Witness (/summon [domain]-expert) or seating a Specialist (/seat [domain]-specialist, Judge only, F3+). Available domains are defined in courtroom/domains/experts.yaml.
```
