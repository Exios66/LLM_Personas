---
title: "2026 02 17 bench trial fifteen experts to add to repertoire"
---

# Transcript: In Re: Bench trial — the 15 most important experts to add to the court’s repertoire

**Case No.:** 2026-DEL-003  
**Date:** 2026-02-17  
**Feasibility:** F5  
**Presiding:** The Honorable Lucius J. Morningstar  
**Voting rule:** Bench trial — Judge’s vote counts as 2× the average of the other members (effective weight: 2 of 7).

***
*The gallery is full. Spectators fill the benches. All parties are present. The Honorable Lucius J. Morningstar takes the bench.*

## PHASE 1: OPENING

**MORNINGSTAR (Judge):**  
Well then. Let’s see what survived yesterday.

*Consults state/current.md.*

The court convenes as a **bench trial** to determine the **15 most important expert domains to add to the court’s repertoire**. Current registry: security, database, compliance, infrastructure, performance, accessibility, i18n, ux (advisory), legal (advisory), cryptography, api_design, testing. We will deliberate, call witnesses and specialists as needed, and vote. In this matter only, the Judge’s vote shall count as **two times the average vote** of the other members—so the bench holds decisive weight. Full gallery; all witnesses and specialists may be called.

**Matter before the court:**  
Identify, debate, and adopt exactly **15 new expert domains** to add to `courtroom/domains/experts.yaml`, ranked by importance to the court’s coverage. The court will hear testimony from existing experts, arguments from the personalities, and a Hail-Mary; then vote. The slate receiving a majority under the weighted rule shall be adopted.

*Sigh.*

Let the record show this is classified F5 due to lasting impact on the court’s capability. Witnesses and specialists may be summoned. Proceed.

***
**DR. ECHO SAGESEEKER (Live Commentary):**  
📘 The court is not just adding experts—it’s choosing which blind spots to institutionalize. Every domain they *don’t* add is a choice. Maslow: they’re optimizing for the hierarchy of *organizational* needs. Jung: the shadow is the list of domains they’re afraid to name. Probability that data_privacy and observability make the 15: very high. Probability that the Prophet proposes “zero new experts” or “50 experts”: also high. 📘

**DR. HARLEY SCARLET QUINN (Live Commentary):**  
🃏💋 Fifteen. Not fourteen, not sixteen. *Fifteen.* Someone’s going to fight for slot fifteen like it’s the last lifeboat. Watch the Architect push for structure—resilience, observability, design_systems. The Engineer will want devops, cost, incident_response. Counsel will want ethics, data_privacy, sustainability. And the Judge gets to count twice. Place your bets on who the Judge sides with. 🃏💋

**UNCLE RUCKUS (Live Commentary):**  
⌨️ Fifteen new domains means fifteen new entries in experts.yaml, fifteen more /summon and /seat options. Registry gets heavy. But if we’re gonna scale the court, we gotta name what we’re missing. data_privacy, observability, resilience, ai_ml—those are no-brainers. The rest is where the fight is. ⌨️

***
## PHASE 2: WITNESS TESTIMONY

**MORNINGSTAR (Judge):**  
The court will hear from existing experts on what domains they observe as missing or underserved. Summoned: Compliance, Security, Performance, Accessibility.

**COMPLIANCE EXPERT WITNESS:**  
From the compliance perspective, the court has regulatory and consent—but **data privacy as a design discipline** is not the same. Privacy-by-design, minimization by default, and data-subject rights as architecture are distinct from “do we have consent?” I recommend a dedicated **data_privacy** domain. I also observe no **ethics** expert for AI fairness, algorithmic bias, or deployment decisions; that overlaps Counsel but is technical enough to warrant a specialist.

**Confidence:** HIGH. **Basis:** GDPR Art. 25, CCPA practice, court’s own gap analysis. **Caveats:** Ethics could remain advisory if the court prefers.

**SECURITY EXPERT WITNESS:**  
Security covers threats and auth; **cryptography** is already separate. What’s missing: **incident response**—postmortems, blameless review, on-call hygiene. Also **resilience**—chaos engineering, fault tolerance, circuit breakers—often confused with infrastructure but it’s a mindset. I’d add **incident_response** and **resilience** so the court doesn’t only ask “what if it breaks?” after it breaks.

**Confidence:** HIGH. **Basis:** NIST IR, SRE practice. **Caveats:** Resilience could be folded into infrastructure; the court may prefer a distinct voice.

**PERFORMANCE EXPERT WITNESS:**  
Performance covers profiling and latency. Missing: **observability**—metrics, tracing, logging, and the question “can we *see* what’s happening?” Distinct from “is it fast?” Also **cost**—cloud cost, efficiency, right-sizing. Many performance decisions are cost decisions. I recommend **observability** and **cost** as separate domains.

**Confidence:** HIGH. **Basis:** O11y community, FinOps. **Caveats:** Cost could be advisory if the court wants to keep it lightweight.

**ACCESSIBILITY EXPERT WITNESS:**  
We have accessibility and i18n. What’s missing for full user coverage: **design_systems**—component libraries, design tokens, consistency at scale. And **documentation**—technical writing, API docs, in-product copy—directly affects usability and accessibility. I recommend **design_systems** and **documentation**.

**Confidence:** MEDIUM. **Basis:** Practice; design_systems and docs are often afterthoughts. **Caveats:** Documentation might be advisory-only.

***
**DR. ECHO SAGESEEKER (Live Commentary):**  
📘 The witnesses just named: data_privacy, ethics, incident_response, resilience, observability, cost, design_systems, documentation. That’s eight. Seven more to fight over. The court will have to choose among frontend, mobile, ai_ml, devops, sustainability, product, data_engineering, qa_automation, search… 📘

***
## PHASE 3: ARGUMENTS (PROPOSED SLATE OF 15)

**MORNINGSTAR::ARCHITECT:**  
I propose we adopt the following 15, in order of structural importance: **(1) data_privacy** — privacy-by-design, distinct from compliance. **(2) observability** — the court must see before it can reason. **(3) resilience** — fault tolerance and chaos as first-class concerns. **(4) design_systems** — consistency and abstraction at scale. **(5) documentation** — APIs and systems are only as good as what’s documented. **(6) incident_response** — postmortems and blameless review. **(7) devops** — CI/CD and release as discipline, not just infra. **(8) data_engineering** — pipelines, ETL, data contracts. **(9) frontend** — web and UI frameworks. **(10) mobile** — iOS/Android. **(11) ai_ml** — ML systems, MLOps, responsible AI. **(12) cost** — cloud and efficiency. **(13) sustainability** — carbon and green tech. **(14) ethics** — AI fairness, algorithmic bias (witness+specialist or advisory). **(15) product** — product strategy (advisory only). This covers structure, delivery, and responsibility without diluting the registry into hundreds.

**MORNINGSTAR::ENGINEER:**  
I support most of the Architect’s list. I’d swap **product** for **qa_automation**—we have testing strategy but not test automation and tooling as a dedicated voice. And I’d make **cost** and **documentation** full specialist-capable; we’ll need them at the table, not just on the stand. My 15: data_privacy, observability, resilience, incident_response, devops, cost, documentation, design_systems, frontend, mobile, ai_ml, data_engineering, sustainability, ethics, qa_automation. Ship the ones that unblock delivery and ops first.

**MORNINGSTAR::DEBUGGER:**  
I want **incident_response** and **resilience** in the top five. What happens when production breaks? What happens when we don’t have observability? The court already has me for “what if null?”—but we need experts for “what if the whole system is down?” and “what did we learn from the last outage?” I also want **data_privacy** so we don’t only ask “are we compliant?” but “did we minimize data?” Add **observability**, **cost** (waste is a failure mode), and **documentation** (undocumented behavior is a defect). My 15 align with the Architect’s with one change: **risk** as a domain—explicit risk assessment and tradeoff framing. If not risk, then keep ethics. I’ll support the slate if incident_response and resilience are in.

**MORNINGSTAR::PROPHET:**  
Objection. We are thinking too small. Why 15? Why not 20, or 10? The court is optimizing for a number, not for coverage. I propose we add **15 domains** but **cap the registry at 25 total**—so we must *retire* or merge domains as we add. Force prioritization. My 15: data_privacy, observability, resilience, incident_response, devops, ai_ml, sustainability, ethics, documentation, design_systems, frontend, mobile, data_engineering, cost, **governance**—who decides, who owns, who’s accountable. Governance is the domain we never name. If we don’t cap total size, the registry becomes a dumping ground.

**MORNINGSTAR::COUNSEL:**  
The client’s interests and ethical boundaries demand consideration. I support **data_privacy**, **ethics**, **sustainability**, and **accessibility** (already in)—and I want **product** (advisory) so the court can hear product strategy when it affects the user. I also support **documentation** and **design_systems** for user-facing quality. My 15: data_privacy, ethics, sustainability, observability, resilience, incident_response, documentation, design_systems, frontend, mobile, ai_ml, cost, devops, data_engineering, **product** (advisory). I oppose a hard cap on the registry without a separate deliberation; the Prophet’s governance is valuable—I’d add **governance** as the 15th full domain and keep product advisory.

***
**DR. HARLEY SCARLET QUINN (Live Commentary):**  
🃏💋 Architect and Engineer are one domain apart—qa_automation vs product. Debugger wants risk or ethics. Prophet just threw a cap and “governance” into the ring. Counsel wants product and governance. The Judge hasn’t spoken. Two votes. This is going to tie without the bench. 🃏💋

***
## PHASE 4: HAIL-MARY

**MORNINGSTAR::PROPHET (Hail-Mary):**  
We should not add 15 fixed domains. We should add **five mandatory slots** and **ten rotating slots**. The five mandatory new additions: data_privacy, observability, resilience, incident_response, ethics. The ten rotating: drawn from a larger pool (devops, cost, documentation, design_systems, frontend, mobile, ai_ml, data_engineering, sustainability, product, governance, qa_automation) and **selected per deliberation** by the Judge based on the matter. So we expand coverage without expanding every prompt. The court stays lean; the registry stays rich. Radical? Yes. Sustainable? Also yes.

***
**UNCLE RUCKUS (Live Commentary):**  
⌨️ Prophet’s idea is “dynamic assembly” again—five fixed, ten on demand. Court already deferred that. But “five mandatory new” is a compromise. Might get one vote. ⌨️

***
## PHASE 5: CROSS-EXAMINATION

**MORNINGSTAR::DEBUGGER → MORNINGSTAR::PROPHET:**  
If we have ten rotating slots, who maintains the pool? What if the Judge forgets to select a domain that’s critical for the matter?

**MORNINGSTAR::PROPHET:**  
The pool is the registry. The Judge already has matter-triage. Rotating means we don’t *load* all ten into every prompt—we load the five mandatory plus up to two specialists from the ten, as today. So we’re not changing behavior; we’re naming the “mandatory five” and the “optional pool.” Maintenance is the same as now.

**MORNINGSTAR::ENGINEER → MORNINGSTAR::ARCHITECT:**  
You put product as advisory. Why not qa_automation? We already have testing; qa_automation is tooling and automation strategy.

**MORNINGSTAR::ARCHITECT:**  
Testing covers strategy. qa_automation can be a subdomain or we add it as full. I’m indifferent between product (advisory) and qa_automation (full) for slot 15—I’ll accept either if the slate is otherwise sound.

**MORNINGSTAR::COUNSEL → COMPLIANCE EXPERT:**  
You said data_privacy is distinct from compliance. Can one person hold both roles, or must they be separate?

**COMPLIANCE EXPERT WITNESS:**  
Separate. Compliance asks “did we satisfy the regulation?” Data privacy asks “did we minimize and protect by design?” Same facts, different lens. One specialist could theoretically hold both, but the court gets clearer testimony from two voices.

***
## PHASE 6: CONSULTANT

**MORNINGSTAR (to Consultant):** Edward. Your perspective.

*The Architect glances at the Engineer. The Engineer studies the floor. The Debugger’s eyes dart to the empty space beside the Judge’s bench, then quickly away. No one speaks.*

**EDWARD CULLEN (to the Judge, from somewhere the others cannot perceive):**  
They have already agreed on twelve. The fight is over slots 13, 14, 15—governance, product, qa_automation, risk. What remains unspoken: the court is afraid that adding “governance” makes the Judge share power with a named domain. So they’ll adopt a slate that excludes governance unless you name it. The Prophet’s rotating pool will be voted down—too much change. Your two votes will decide whether product (advisory) or qa_automation (full) or governance gets the last seat. Choose the one that serves the institution, not the one that pleases the loudest voice.

*The Judge considers this privately. The court waits in silence they do not acknowledge.*

***
## PHASE 7: VOTE (BENCH TRIAL — JUDGE 2×)

**MORNINGSTAR (Judge):**  
The court will vote on the following slate of 15 domains to add. Each domain receives witness+specialist unless marked (advisory). Slate: **1. data_privacy** **2. observability** **3. resilience** **4. incident_response** **5. devops** **6. documentation** **7. design_systems** **8. frontend** **9. mobile** **10. ai_ml** **11. data_engineering** **12. cost** **13. sustainability** **14. ethics** **15. qa_automation.** Product and governance are not in this slate; they may be considered in a future expansion. The Prophet’s rotating-pool proposal is rejected for this vote; we are voting on the fixed slate only. Vote YES to adopt, NO to reject.

| Personality | Vote | Rationale |
|-------------|------|------------|
| **ARCHITECT** | YES | Slate is structurally sound; covers delivery, ops, and responsibility. |
| **ENGINEER** | YES | qa_automation in; delivery and ops covered; ship it. |
| **DEBUGGER** | YES | incident_response and resilience in; observability and data_privacy in. Accept. |
| **PROPHET** | NO | Prefer rotating pool; fixed 15 without governance is incomplete. |
| **COUNSEL** | YES | data_privacy, ethics, sustainability in; client and ethics served. Accept slate. |
| **JUDGE** | YES | (Counts as 2.) Slate balances coverage and restraint; governance and product deferred, not denied. |

**Tally (weighted):** YES = 1 + 1 + 1 + 1 + 2 = **6**. NO = **1**. ABSTAIN = 0.  
**Effective total:** 7 (each of 5 members = 1, Judge = 2). **Majority:** 4.  
**Result:** Motion to adopt the slate of 15 experts **carries** (6–1–0).

***
## PHASE 8: RULING

**MORNINGSTAR (Judge):**  
The court has ruled. Regrettably sensible.

**Decision:**  
The court adopts **15 new expert domains** to add to the repertoire, as follows. Each shall be added to `courtroom/domains/experts.yaml` with full definition (scope, heuristics, signature_questions, failure_mode, voice, notes) in a subsequent implementation phase. Witness + Specialist unless otherwise noted.

| # | Domain | Scope (summary) |
|---|--------|-----------------|
| 1 | **data_privacy** | Privacy-by-design, minimization, data-subject rights, distinct from compliance. |
| 2 | **observability** | Metrics, tracing, logging, visibility into systems and behavior. |
| 3 | **resilience** | Fault tolerance, chaos engineering, circuit breakers, SRE-style reliability. |
| 4 | **incident_response** | Postmortems, blameless review, on-call, outage response. |
| 5 | **devops** | CI/CD, release engineering, deployment discipline. |
| 6 | **documentation** | Technical writing, API docs, in-product copy, doc-as-code. |
| 7 | **design_systems** | Component libraries, design tokens, UI consistency at scale. |
| 8 | **frontend** | Web and UI frameworks, browser, client-side. |
| 9 | **mobile** | iOS, Android, mobile platforms and constraints. |
| 10 | **ai_ml** | ML systems, MLOps, model ops, responsible AI. |
| 11 | **data_engineering** | Pipelines, ETL, data contracts, data lakes. |
| 12 | **cost** | Cloud cost, efficiency, right-sizing, FinOps. |
| 13 | **sustainability** | Carbon footprint, green tech, environmental impact of systems. |
| 14 | **ethics** | AI fairness, algorithmic bias, deployment ethics. |
| 15 | **qa_automation** | Test automation, tooling, automation strategy beyond test strategy. |

**Vote:** 6–1–0 (weighted: Judge 2×). **Rationale:** The slate closes material gaps identified by witnesses and personalities while keeping the registry bounded. Governance and product are deferred for future deliberation. **Risk:** Implementation burden (15 new YAML entries); possible overlap with existing domains must be resolved in definitions. **Dissent:** Prophet maintains that a rotating pool and governance would better serve the court.

**Implementation:** The Scribe shall schedule a follow-up task to add the 15 domains to `courtroom/domains/experts.yaml` with full fields per registry standards. Review date for the expanded registry: 90 days after implementation.

***
**DR. ECHO SAGESEEKER (Live Commentary):**  
📘 Fifteen adopted. Governance and product left at the door. The Judge’s two votes broke nothing—they aligned with the majority. The gallery may now watch the Scribe and the implementers add 15 new voices to the court. 📘

**DR. HARLEY SCARLET QUINN (Live Commentary):**  
🃏💋 Six to one. The Prophet stood alone. The bench sided with the builders. Fifteen new experts, no cap, no rotating pool—for now. The court has spoken. 🃏💋

***
> *Transcript certified by MORNINGSTAR::SCRIBE*
