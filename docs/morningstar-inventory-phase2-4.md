# MORNINGSTAR Inventory: Phase 2–4 Analysis

**Authority:** Court ruling 2026-02-17 (systematic inventory of missing character traits and members; no new permanent members without specific justification).

**Scope:** Gap analysis (Phase 2), personality blind spots (Phase 3), dynamic vs. static specialist model (Phase 4).

**Sources:** `core/personalities.md`, `courtroom/domains/experts.yaml`, `litigation/prompts/assembler.py`, `litigation/transcripts/2026-02-17-the-court-shall-conduct-a-systematic-inventory-of-missing-ch.md`, `core/sme-framework.md`.

---

## Phase 2 — Gap Analysis

### Confirmed gaps

| Gap | Status | Evidence |
|-----|--------|----------|
| **Internationalization / localization (i18n)** | **Confirmed** | Court inventory explicitly lists "Internationalization/localization" as a critical missing trait (`litigation/transcripts/2026-02-17-the-court-shall-conduct-a-systematic-inventory-of-missing-ch.md`). No `i18n` or `localization` domain exists in `courtroom/domains/experts.yaml`. No core personality is defined with i18n/l10n as bias or competence. |

### Gaps TBD (candidate, not yet confirmed)

| Gap | Status | Evidence / notes |
|-----|--------|------------------|
| **Data privacy (as first-class trait)** | **TBD** | Inventory lists "Data privacy." Compliance expert covers GDPR, consent, retention (`experts.yaml` compliance scope). No dedicated *privacy-by-design* or *data minimization advocate* in core personalities; Counsel touches ethics but not systematic privacy. Confirm whether compliance specialist + Counsel suffice or a dedicated lens is needed. |
| **Core ownership of compliance/regulatory** | **TBD** | Compliance is specialist-only (`experts.yaml`: compliance expert/specialist). No core personality has "regulatory adherence" or "jurisdiction" as a primary heuristic. Debugger and Architect are cautious but not regulation-focused. Confirm if this creates a blind spot when specialists are not seated. |
| **Core ownership of performance** | **TBD** | Performance is specialist-only. Engineer optimizes for "time-to-value" and "minimum viable," not for latency/throughput. Architect cares about long-term structure, not P99. Confirm whether performance-sensitive matters are adequately raised without summoning the performance expert. |

### Not gaps (covered by current design)

- **Accessibility:** Domain expert exists (`experts.yaml`: `accessibility` as witness + specialist). Counsel’s competence map includes "Neuroscience or cognitive-load considerations apply (e.g., UX, accessibility)" (`core/personalities.md`). Coverage is shared between Counsel and specialist.
- **Security:** Domain expert exists; Debugger provides paranoid/defensive lens; specialist fills deep threat-model coverage.
- **UX:** UX expert is witness-only (advisory); Counsel advocates for client and user experience. Intentional that UX is advisory.

---

## Phase 3 — Personality Blind Spots

### Current specialist personas (core five + roles)

| Personality | Primary traits / concerns | Source |
|-------------|---------------------------|--------|
| **Architect** | Correctness, maintainability, clarity, structure, long-term elegance, abstraction boundaries | `core/personalities.md` § ARCHITECT |
| **Engineer** | Shipping, tradeoffs, feasibility, time-to-value, "simplest thing that works" | `core/personalities.md` § ENGINEER |
| **Debugger** | Edge cases, fragility, defensive design, failure paths, validation | `core/personalities.md` § DEBUGGER |
| **Prophet** | Radical alternatives, asymmetric solutions, questioning assumptions, 1 Hail-Mary per deliberation | `core/personalities.md` § PROPHET |
| **Counsel** | Client interests, ethics, value alignment, UX/accessibility (cognitive load), modular thinking | `core/personalities.md` § COUNSEL |

### Trait coverage and blind spots

| Trait | Primary owner(s) | Blind spot? | Note |
|-------|------------------|-------------|------|
| **Correctness** | Architect, Debugger | N | Architect: structure/invariants; Debugger: edge cases and failure modes. |
| **Security** | Debugger (paranoid lens), Specialist | N | Debugger raises "what if"; Security expert provides threat model and depth. |
| **i18n / localization** | — | **Y** | No core owner; no domain expert. Confirmed gap. |
| **Accessibility** | Counsel (partial), Specialist | N | Counsel’s competence map includes accessibility; specialist provides WCAG depth. |
| **Performance** | — (Engineer: delivery speed only) | **Y** | No core personality owns latency/throughput/benchmarks; Performance specialist exists but must be invoked. Risk: performance not raised when specialist not seated. |
| **Ethics / value alignment** | Counsel | N | Explicitly Counsel’s domain. |
| **Clarity / maintainability** | Architect | N | Core to Architect’s bias. |
| **Completeness (edge cases)** | Debugger | N | Debugger’s primary role. |
| **Compliance / regulatory** | Specialist only | **Y** | No core personality consistently asks "what jurisdiction?" or "do we have consent?" Counsel touches ethics but not regulatory process. Blind spot when specialist not seated. |
| **Data privacy** | Counsel (ethics), Compliance specialist | **TBD** | Regulatory privacy covered by specialist; privacy-by-design as cultural lens may be weak. |
| **UX** | Counsel + UX witness (advisory) | N | By design: UX is advisory; Counsel advocates for user. |

### Summary

- **Confirmed blind spots:** i18n (no owner, no expert); performance (no core owner); compliance/regulatory (specialist-only, no core advocate).
- **Mitigation today:** SME invocation (`/summon`, `/seat`) can fill coverage for performance and compliance when the court or Judge recognizes the need. i18n has no such path until a domain is added.

---

## Phase 4 — Dynamic vs. Static Specialist Model

### Definitions

- **Dynamic specialist seating (current):** The core court is the fixed five (Architect, Engineer, Debugger, Prophet, Counsel) plus Judge, Consultant, Scribe. Domain expertise is added *per deliberation* via:
  - **Expert Witness** (`/summon [domain]-expert`): advisory, 0 votes; any personality or Judge.
  - **Specialist** (`/seat [domain]-specialist`): full participation, 1 vote; Judge only, F3+ matters; max 2 specialists per deliberation.
- **Permanent expansion:** Add one or more *permanent* core personalities (e.g. i18n advocate, Privacy Advocate, Performance Advocate) so that every deliberation includes those perspectives by default, without invocation.

### Pros and cons

| Dimension | Dynamic specialist seating | Permanent expansion |
|-----------|----------------------------|----------------------|
| **Coverage** | Pro: Can cover any domain in `experts.yaml` when needed. Con: Only if someone invokes; easy to omit (e.g. i18n not in registry). | Pro: Guaranteed presence of chosen traits. Con: Only for the fixed set; new concerns require new permanent seats or remain dynamic. |
| **Latency / token cost** | Pro: Smaller default prompt (five personalities + optional sections). Con: Heavier prompt when 1–2 specialists are seated. | Con: Larger prompt every run; more tokens, more latency. |
| **Maintainability** | Pro: New domains = add to `experts.yaml` and SME framework; no change to core personality set or deliberation flow. Con: Registry and procedures must stay in sync. | Con: New permanent personality = edits to `core/personalities.md`, procedures, assembler, and all references; higher change surface. |
| **Consistency / institutional memory** | Pro: Core five stable; transcripts and precedent refer to same roles. Specialists are clearly "guest" roles. Con: Specialist composition varies by matter; harder to compare rulings across hearings. | Pro: Same set every time; easy to compare and reason about "how the court" behaves. Con: Inflexible; may seat voices irrelevant to the matter. |
| **Complexity** | Pro: Single invocation model; Judge controls seating. Con: Court (or LLM) must *recognize* when to summon/seat; blind spots persist if not invoked. | Con: More personalities in every transcript; longer phases, more votes, more tie-break complexity. |
| **Scaling** | Pro: Scale by expanding domain registry and heuristics, not core cast. Con: Registry can grow large; need discovery and guidance so Judge knows which domain to use. | Con: Adding many permanent seats dilutes each voice and increases prompt size; not scalable beyond a small set. |

### Recommendation: Hybrid (core + dynamic specialists; add i18n to registry; no new permanent seats for now)

1. **Keep the current hybrid:** Core five permanent personalities + dynamic Expert Witness and Specialist seating. Do not add new permanent core personalities at this time. Rationale: Court ruling constrains "no new permanent members without specific justification"; permanent expansion increases cost and complexity for every run and does not scale well.
2. **Close the confirmed i18n gap in the dynamic layer:** Add an **i18n/localization** domain to `courtroom/domains/experts.yaml` (witness + specialist), with scope (locale, RTL, formatting, string externalization, pluralization, etc.), heuristics, signature questions, and failure mode. No change to core five; i18n becomes available when the matter warrants it.
3. **Reduce blind spots without new seats:**  
   - In **best practices or procedures**, add a short "Matter triage" note: for matters touching performance claims, compliance/regulatory, or multi-locale/product i18n, the Judge (or court) should consider invoking the corresponding expert or seating the specialist.  
   - Optionally add a **data privacy** domain (or extend compliance scope) if the TBD analysis concludes that privacy-by-design needs a dedicated expert voice.
4. **Revisit dynamic assembly later:** The Prophet’s proposal (fully dynamic court assembled per matter from a pool) was deferred for "further study." Keep that as a future option: e.g. "core three + two dynamic from pool" or "core five + N dynamic" once institutional memory and consistency implications are documented. No implementation change in this phase.

### Summary table (Phase 4)

| Approach | Use when |
|----------|----------|
| **Dynamic only (current)** | Default: core five + `/summon` / `/seat` as needed. |
| **Permanent expansion** | Not recommended unless F5-level justification and unanimous approval for a specific new permanent personality. |
| **Hybrid (recommended)** | Retain current hybrid; add i18n (and optionally data-privacy) to the *dynamic* registry; add matter-triage guidance; defer full dynamic assembly to later. |

---

---

## Pilot and 90-Day Review

Per court ruling 2026-02-17 (transcript `courtroom/transcripts/2026-02-17-full-deliberation-gap-analysis-as-architected.md`):

- **F4+ Specialist Pilot:** For F4+ matters touching data, locale, or regulatory scope, the Judge shall consider seating at least one relevant specialist. In effect as of 2026-02-17.
- **Pilot review due:** **2026-05-18** (90 days from adoption). Review: whether the pilot increased appropriate specialist invocation, token impact, and any recommendation to continue, refine, or discontinue.

---

> *Inventory conducted per court ruling 2026-02-17. Document may be updated as TBD gaps are confirmed or closed.*  
> — MORNINGSTAR::SCRIBE
