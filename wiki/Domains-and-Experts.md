# Domains & Experts

When deliberations need expertise beyond the core court (e.g. security, compliance, database design), the court can summon **Expert Witnesses** (advisory, 0 votes) or seat **Specialists** (full participation, 1 vote, Judge only, F3+ matters).

## Canonical Registry

| Location in repo | Purpose |
|------------------|---------|
| `courtroom/domains/README.md` | How to use the registry, summoning commands, adding domains |
| `courtroom/domains/experts.yaml` | Canonical definitions: scope, heuristics, signature questions, failure modes |

## Domains Summary

**Witness and/or Specialist:**  
`security` · `database` · `compliance` · `infrastructure` · `performance` · `accessibility` · `i18n` · `cryptography` · `api_design` · `testing` · `data_privacy` · `observability` · `resilience` · `incident_response` · `devops` · `documentation` · `design_systems` · `frontend` · `mobile` · `ai_ml` · `data_engineering` · `cost` · `sustainability` · `ethics` · `qa_automation`. **Advisory only (Witness):** `ux`, `legal`. See courtroom/domains/experts.yaml for full definitions.

**Advisory only (Witness):**  
`ux` · `legal`

## Summoning

- **Expert Witness:** `/summon <domain>-expert` — any personality or Judge.
- **Specialist:** `/seat <domain>-specialist` — Judge only, F3+ matters.
- **Dismiss:** `/dismiss <domain>`

Protocol and tie-breaking: [SME-Framework](SME-Framework).

**See also:** [Command-Reference](Command-Reference)
