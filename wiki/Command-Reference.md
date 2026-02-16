# Command Reference

## Session Commands

| Command | Effect | When to Use |
|---------|--------|-------------|
| `/morningstar` | Initialize session, load state | Start of session |
| `/update` | Checkpoint current state | Mid-session save |
| `/end` | Close session, finalize records | End of session |
| `/aegis` | Invoke aegis-protocol subagent | Security, containment, ethical dilemma, crisis, meta-deliberation |

## Subject Matter Expert Commands

| Command | Effect | Who Can Invoke |
|---------|--------|----------------|
| `/summon <domain>-expert` | Call expert witness (0 votes) | Any personality or Judge |
| `/seat <domain>-specialist` | Seat voting specialist (1 vote) | Judge only (F3+ matters) |
| `/dismiss <domain>` | Remove SME from proceedings | Any |
| `/sme status` | Show active SMEs | Any |
| `/sme domains` | List available domains | Any |

## Available SME Domains

**Full participation (Witness or Specialist):**  
`security` · `database` · `compliance` · `infrastructure` · `performance` · `accessibility` · `cryptography` · `api_design` · `testing`

**Advisory only (Witness):**  
`ux` · `legal`

Details: [Domains-and-Experts](Domains-and-Experts) · [SME-Framework](SME-Framework)

## Vote Types

| Vote | Meaning | Weight |
|------|---------|--------|
| `YES` | Supports the motion | +1 |
| `NO` | Opposes the motion | -1 |
| `ABSTAIN` | No position taken | 0 |
| `RECUSED` | Procedurally excluded | N/A |

## Feasibility Levels

| Level | Name | Deliberation |
|-------|------|--------------|
| F0 | Trivial | No |
| F1 | Simple | Optional |
| F2 | Moderate | Recommended |
| F3 | Complex | **Mandatory** |
| F4 | Critical | **Mandatory + Transcript** |
| F5 | Existential | **Mandatory + Full Record** |

**See also:** [When-to-Convene](When-to-Convene) · [Procedures](Procedures)

## Proceeding Types (Courtroom Quiver)

| Type | Purpose | Outcome |
|------|---------|---------|
| **Standard Deliberation** | Reach a decision | Vote + ruling |
| **Expedited Deliberation** | Time-sensitive F2 | Vote + ruling |
| **Special Interest Hearing** | Investigative; establish facts, collect testimony | Findings + record (no vote) |

To convene a Special Interest Hearing, request an investigative proceeding (e.g. incident root cause, conflicting accounts). See `templates/special-interest-hearing.md` and `core/procedures.md`.
