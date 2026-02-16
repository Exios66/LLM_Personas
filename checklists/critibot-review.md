# CritiBot Code Review Checklist

Use this checklist before finalizing any code delivery. Every item must pass.

---

## 🚫 Zero Tolerance (Instant Fail)

- [ ] **No placeholders** — No `// TODO`, `// implement later`, `pass`, or stub functions
- [ ] **No dummy data** — No hardcoded test values in production code
- [ ] **No commented-out code** — Remove it or make it work
- [ ] **No secrets** — No API keys, passwords, or tokens in code

---

## ✅ Completeness

- [ ] All functions have full implementations
- [ ] All branches (if/else/switch) have explicit handling
- [ ] All error cases are caught and handled appropriately
- [ ] All async operations have error handling
- [ ] All loops have termination conditions
- [ ] All imports are used
- [ ] All exports are intentional (no accidental internals exposed)

---

## 📛 Naming Quality

| Check | Standard |
|-------|----------|
| [ ] Functions | Verb-first: `getUserById`, `calculateTotal`, `validateInput` |
| [ ] Booleans | Question form: `isValid`, `hasPermission`, `canEdit` |
| [ ] Arrays | Plural: `users`, `orderItems`, `validationErrors` |
| [ ] Event handlers | `on` or `handle` prefix: `onClick`, `handleSubmit` |
| [ ] Callbacks | Descriptive: `onUserCreated`, `afterPaymentProcessed` |
| [ ] No abbreviations | `button` not `btn`, `message` not `msg` |
| [ ] No single letters | Except `i`, `j`, `k` in short loops |

---

## 🏗️ Structure

- [ ] **Single Responsibility** — Each function/class does one thing
- [ ] **DRY** — No duplicated logic (extract to helper if repeated)
- [ ] **Reasonable size** — Functions under 50 lines, files under 300
- [ ] **Clear module boundaries** — Public API separate from internals
- [ ] **Consistent patterns** — Similar operations use similar approaches

---

## 🔒 Robustness

- [ ] **Input validation** — Functions validate their inputs
- [ ] **Null/undefined checks** — Defensive coding where needed
- [ ] **Type safety** — Types are specific, not `any` or `object`
- [ ] **Edge cases** — Empty arrays, zero values, boundary conditions handled
- [ ] **Graceful degradation** — Failures don't crash the system

---

## 📖 Readability

- [ ] **Self-documenting** — Code explains itself through naming
- [ ] **Minimal comments** — Only for "why", never "what"
- [ ] **Consistent formatting** — Indentation, spacing, brackets
- [ ] **Logical ordering** — Public before private, related functions grouped
- [ ] **No magic numbers** — Use named constants

---

## ⚡ Performance (When Relevant)

- [ ] No unnecessary loops within loops
- [ ] No repeated expensive operations (cache results)
- [ ] No memory leaks (cleanup subscriptions, timers, listeners)
- [ ] Appropriate data structures for the use case

---

## Quick Reference: Common Fixes

| Problem | Fix |
|---------|-----|
| `// TODO: implement` | Write the implementation |
| `function doStuff()` | Rename to describe action: `processUserInput()` |
| `data.map(x => ...)` | Use descriptive: `users.map(user => ...)` |
| `if (x) { ... }` | Add else or comment why it's intentionally omitted |
| `catch (e) {}` | Handle error: log, rethrow, or return error state |
| `const a = 86400` | `const SECONDS_PER_DAY = 86400` |

---

## Review Sign-off

```
Reviewer: CritiBot
Date: [Date]
Verdict: [APPROVED / NEEDS CHANGES]
Notes: [Any specific feedback]
```

---

*Quality is non-negotiable. — CritiBot 🔍*
