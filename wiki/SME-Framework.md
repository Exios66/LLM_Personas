# SME Framework

Two tiers of domain expertise:

| Type | Purpose | Voting Power | Invocation |
|------|---------|--------------|------------|
| **Expert Witness** | Advisory testimony | 0 | Any personality or Judge |
| **Specialist Seat** | Full participation | 1 | Judge only (F3+ matters) |

**Canonical registry:** `courtroom/domains/experts.yaml` and `courtroom/domains/README.md` in the repo.

## When to Involve SMEs

- A personality identifies a domain gap → consider Expert Witness.
- Two or more personalities uncertain → summon Witness.
- F3+ matter with central domain need → consider Specialist (Judge only).
- Domain peripheral → Witness sufficient. Domain central → Specialist appropriate.

## Failure Tracking

When SME input leads to poor outcomes, record in `state/sme-failures.md` for institutional learning. Schema and template are in the repo.

**See:** [Domains-and-Experts](Domains-and-Experts) · [Command-Reference](Command-Reference)
