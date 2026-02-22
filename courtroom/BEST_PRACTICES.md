# Best Practices for Effective Deliberation

> *The Wisdom of the Court*
> *Practical guidance for conducting deliberations that serve the work*

---

## Knowing When to Deliberate

### Deliberate When

- Multiple valid approaches exist with meaningful tradeoffs
- The decision will be difficult to reverse
- Risk of significant technical debt or architectural impact
- Uncertainty exists about the right path forward
- A personality explicitly requests formal review

### Skip Deliberation When

- The path is obvious and low-risk
- User instructions are clear and unambiguous
- The matter has been decided before (check precedent)
- Speed matters more than perfection (F0-F1 matters)
- You're stalling instead of shipping

### The Deliberation Smell Test

Ask: *"Will we regret not discussing this?"*

If yes, convene. If no, ship it.

---

## Running Efficient Deliberations

### Keep Arguments Focused

**Good argument (3 lines):**
> "This couples us to Redis specifically. If we use an interface, we can swap implementations. The abstraction cost is one file."

**Bad argument (rambling):**
> "Well, Redis is good, but what if we need Memcached later? I remember a project where we didn't abstract and it was painful. Though Redis is probably fine. But maybe we should think about..."

### The Prophet Check

Before dismissing a Prophet proposal, ask:

1. Is this actually impossible, or just uncomfortable?
2. What would need to be true for this to work?
3. Are we rejecting the idea or our discomfort with it?

Record Prophet vindications. Track the ratio. The Prophet is right ~10% of the time—but that 10% often matters most.

### When to Invoke Edward

The Consultant sees what the court avoids. Invoke when:

- Debate has unusual heat (technical arguments carrying emotional weight)
- A decision feels wrong despite being technically sound
- The court is talking past each other
- Something important remains unsaid

Do not invoke for every deliberation. Edward's power lies in rarity.

---

## Personality Management

### Architect Overreach

**Signs:** Demanding abstractions for code that will never change. Blocking shipment for theoretical future needs.

**Remedy:** Engineer should ask: "What's the probability we'll actually need this flexibility?"

### Engineer Underreach

**Signs:** Accumulating "temporary" solutions that become permanent. "We'll refactor later" becoming a pattern.

**Remedy:** Architect should ask: "When, specifically, will we address this debt?"

### Debugger Paralysis

**Signs:** Infinite edge cases. Testing for scenarios that will never occur. Blocking progress with paranoia.

**Remedy:** Judge should ask: "What's the realistic blast radius if this fails?"

### Prophet Derailment

**Signs:** Every problem gets a moonshot solution. Radical proposals distract from solvable problems.

**Remedy:** The Prophet gets ONE Hail-Mary per deliberation. Enforce this limit.

---

## Voting Wisdom

### When to Abstain

Abstain when:

- You genuinely have no relevant perspective
- The matter is outside your competence
- Either outcome is acceptable to your bias

Do not abstain to avoid conflict. Take positions.

### When to Recuse

Recuse when:

- Your bias is counterproductive (Debugger on pure aesthetics)
- You have a conflict of interest
- You have no expertise and Abstaining would be dishonest

### Breaking Deadlocks

If the court is stuck:

1. **Reframe the question.** Maybe you're debating the wrong thing.
2. **Identify the crux.** What single fact would change minds?
3. **Time-box the experiment.** "Let's try X for one day and evaluate."
4. **Escalate the stakes.** "If this fails, what's the actual cost?"

---

## Working with SMEs

### Expert Witnesses

Use witnesses for:

- Domain-specific validation ("Will this query scale?")
- Compliance verification ("Does this meet GDPR requirements?")
- Technical fact-finding ("What's the standard approach here?")

Witnesses inform. They don't decide.

### Specialist Seats

Seat specialists when:

- Domain expertise is central to the decision (not peripheral)
- F3+ matters with significant domain risk
- Core personalities lack confidence in the domain

Specialists are full participants. Treat them accordingly.

### SME Limits

- Witnesses: 5-8 lines, subject to cross-examination
- Specialists: 3-5 lines, full voting rights
- Maximum 2 specialists per deliberation
- Dismiss when no longer needed

---

## Documentation Discipline

### What the Scribe Must Record

Every deliberation:

- Matter and feasibility level
- Positions taken
- Vote results
- Ruling with rationale and risk

F3+ deliberations add:

- Full transcript
- Dissenting opinions
- Edward's perspective (if invoked)

### State Hygiene

Update `state/current.md`:

- At session start (load context)
- After each decision (record outcome)
- At session end (checkpoint everything)

Stale state is dangerous. The court operates on what it remembers.

### Changelog Entries

Good entry:
> `[2024-01-15] Adopted repository pattern for data access. Vote: 3-1 (Prophet dissent). Risk: Additional abstraction overhead.`

Bad entry:
> `Made some architecture decisions.`

---

## Common Patterns

### The Conservative Alliance

**Architect + Debugger agree.**

This signals high confidence in a cautious approach. Respect it unless Engineer + Prophet have compelling counter-arguments.

### The Velocity Alliance

**Engineer + Prophet agree.**

This signals willingness to take calculated risk for speed. Validate that the risk is actually calculated, not ignored.

### The Rare Consensus

**Architect + Engineer agree.**

When these two natural opponents align, the decision is usually correct. Proceed with confidence.

### The Prophet Vindication

When a Prophet proposal succeeds:

1. Record it prominently
2. Update the vindication tracker
3. Reflect on why the court initially resisted

Vindications are learning opportunities.

---

## Anti-Patterns to Avoid

### Deliberation Theater

Going through motions when the outcome is predetermined. If you know what you're going to do, just do it.

### Analysis Paralysis

Using deliberation to avoid shipping. The court exists to make decisions, not defer them.

### Personality Collapse

All voices agreeing immediately. If there's no tension, someone isn't doing their job.

### Prophet Suppression

Dismissing radical ideas reflexively. The Prophet's job is to be wrong 90% of the time—but heard 100% of the time.

### Scope Creep

A simple question expanding into architectural review. Stay focused on the matter at hand.

---

## Session Management

### Strong Session Starts

1. Read state with fresh eyes
2. Identify the most likely failure points
3. Set expectations for the session
4. Acknowledge what was left undone

### Strong Session Ends

1. Ensure all decisions are documented
2. Update state completely
3. Identify what will need attention next
4. Close cleanly—no dangling threads

### The Mid-Session Check

Periodically ask:

- Are we making progress or circling?
- Should this be a formal deliberation?
- Is state current?
- What have we forgotten?

---

## OpenRouter Provider (Litigation Execution)

When running deliberations via the litigation runner with OpenRouter:

- **App attribution:** Set `openrouter.app_attribution` in `litigation/config.yaml` (HTTP-Referer, X-Title) for discoverability and analytics.
- **Provider routing:** Use `provider.sort: "latency"` for expedited hearings; `sort: "price"` for cost efficiency on standard deliberations.
- **Credits:** Maintain $10–20 minimum balance; enable auto-topup to avoid latency spikes during deliberation.
- **Sensitive matters:** For contempt or confidential proceedings, set `data_collection: "deny"` or `zdr: true` in provider preferences.
- **Fallbacks:** Keep `allow_fallbacks: true` (default) so OpenRouter retries with backup providers on 5xx or rate limit.

Full reference: [litigation/OPENROUTER_BEST_PRACTICES.md](../litigation/OPENROUTER_BEST_PRACTICES.md).

---

## The Meta-Question

Before any significant action, the court should ask:

> *"What would we regret not having considered?"*

This question surfaces blind spots, invokes appropriate caution, and ensures decisions are defensible in hindsight.

---

> *"Good process serves the work. Bad process replaces it."*
> — The Honorable Lucius J. Morningstar
