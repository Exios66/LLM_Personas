---
title: "2026 07 25 agent authored legal filings authentication"
---

# In Re: Agent-Authored Legal Filings — Authentication, Attribution, and the Duty of Candor

**Case No.:** 2026-DEL-006-001  
**Date:** 2026-07-25  
**Feasibility:** F4  
**Presiding:** The Honorable Lucius J. Morningstar  
**Seated Specialists:** MORNINGSTAR::COMPLIANCE (voting), MORNINGSTAR::DOCUMENTATION (voting)  
**Expert Witnesses:** Legal Advisor (advisory), Ethics Expert, QA Automation Expert, Data Privacy Expert  
**Gallery:** Dr. Echo Sageseeker; Dr. Harley Scarlet Quinn; Uncle Ruckus

***
*The gallery settles. A stack of demonstrative “filings” — some meticulously cited, some hallucinated into fiction — sits on the exhibit table. The Honorable Lucius J. Morningstar takes the bench.*

## PHASE 1: OPENING

**MORNINGSTAR (Judge):**  
The court will now consider the hot-button collision of **agentic software**, **professional responsibility**, and **law**: May autonomous agents draft, file, or serve legal instruments, and what authentication and candor duties attach?

**Matter before the court:**  
Adopt a binding standard — the **Agent-Filing Authentication Protocol (AFAP)** — governing:

1. Whether agents may author legal filings (briefs, motions, contracts, demand letters, regulatory submissions).  
2. Required human attorney-of-record (or authorized filer) attestation.  
3. Citation integrity, hallucinated-authority prohibitions, and disclosure of material agent assistance.  
4. Provenance logging sufficient for sanctions, malpractice, and discovery.

Classified **F4** due to significant professional-ethics tradeoffs, court integrity implications, and irreversible reputational/legal harm from fabricated authority. F4+ pilot: Compliance + Documentation seated. Proceed.

***
**DR. ECHO SAGESEEKER (Live Commentary):**  
📘 This is Pinocchio at the bar of the court—wishing to be a real lawyer. Freud: the ego ideal of perfect brief-writing colliding with the death drive of fabricated precedent. Probability Counsel becomes unusually fierce: 94%. 📘

**DR. HARLEY SCARLET QUINN (Live Commentary):**  
🃏💋 Hallucinated case law. The gift that keeps on sanctioning. Watch Debugger ask what happens when the citation is null and the judge is not. 🃏💋

**UNCLE RUCKUS (Live Commentary):**  
⌨️ If your agent invents *Smith v. Reality*, you don’t have a research assistant—you have a contempt machine with autocomplete. ⌨️

***
## Matter Before the Court

**Proposed AFAP slate:**

- Agents may **assist** in drafting; they may **not** be the filer of record.
- Every filing requires a **human authorized signer** who attests: (a) they read the filing; (b) citations were verified against primary sources; (c) material agent assistance is disclosed per forum rules where required.
- Mandatory **citation ledger**: each authority linked to retrieved primary text hash/URL/reporter pin-cite checked by tooling + human.
- Prohibition on filing known-unverified authorities; automated “citation lint” gate before export.
- Provenance bundle retained: prompts, retrievals, model IDs, drafts, verifier outputs, signer identity, timestamps.
- Client confidentiality and data-minimization controls for any third-party model/API used.

***
## PHASE 2: WITNESS TESTIMONY

**LEGAL ADVISOR (Advisory Witness):**  
Most jurisdictions already forbid practicing law without a license; courts have sanctioned lawyers for submitting AI-hallucinated cases. The doctrinal core is not “AI bad”—it is **duty of candor** and **competence**. Agents amplify volume and risk. Advisory opinion: agent authorship without human verification is incompatible with professional responsibility. Disclosure norms are evolving; default to transparency where local rules require or where materiality demands. Contracts differ from court filings but still implicate misrepresentation and authority to bind.

**Confidence:** HIGH. **Basis:** Professional conduct rules; published sanctions orders. **Caveats:** Jurisdictional variance on disclosure; not all agent use is filing.

**/summon ethics-expert**

**ETHICS EXPERT WITNESS:**  
Fabricated authority is not a cute error; it is an epistemic attack on adjudicative systems. Even “helpful” agents create asymmetric risk: cheap text, expensive verification. Ethics requires that verification resources scale with generation. Also: clients must be informed when material legal strategy is agent-shaped if it affects consent and confidentiality (especially with external APIs).

**Confidence:** HIGH. **Basis:** Research integrity analogs; professional ethics. **Caveats:** Over-disclosure can prejudice clients in some forums—follow local rules.

**/summon qa_automation-expert**

**QA AUTOMATION EXPERT WITNESS:**  
Treat filings like release artifacts. Build a pipeline: draft → retrieval-augmented cite check → contradiction tests → human acceptance tests → signed export. Flaky cite checkers are dangerous; prefer deterministic matches to reporter databases / court APIs where available. “95% accurate citations” is an unacceptable defect rate for filings—aim for gate failure on any unresolved cite.

**Confidence:** HIGH. **Basis:** Test automation & release engineering. **Caveats:** Not all authorities are in digital databases; human research remains mandatory for edge sources.

**/summon data_privacy-expert**

**DATA PRIVACY EXPERT WITNESS:**  
Legal drafting often includes privileged and sensitive personal data. Feeding that into external agent APIs can waive privilege or breach confidentiality. AFAP must include data-routing controls: local/enterprise models for privileged matter; redaction; retention limits; no training on client data by default. Privacy is not optional garnish on authentication.

**Confidence:** HIGH. **Basis:** Privilege doctrine + privacy-by-design. **Caveats:** In-house models still need access control and audit.

***
## PHASE 3: ARGUMENTS

**MORNINGSTAR::ARCHITECT:**  
This will age poorly if we bolt a chatbot onto ECF and call it innovation. Architecture: separate **Drafting Agent**, **Verifier Service** (no generative freedom to invent cites), and **Human Signer Gateway**. No direct path from generative model to filed PDF without verifier+signer. Persist provenance as first-class artifacts.

**MORNINGSTAR::ENGINEER:**  
Can we ship this safely? Yes: cite-lint in CI for legal repos; blocker on unresolved authorities; templates for disclosure language; signer checklist UX that shows diffs since last human read. Don’t ban agents—ban unverified export. Ship AFAP as protocol + tooling requirements.

**MORNINGSTAR::DEBUGGER:**  
What if the input is null—what if the “verified” citation resolves to a real case that doesn’t stand for the proposition? Cite presence ≠ cite fitness. Edge cases: overruled cases, wrong jurisdiction, miscited quotes, silently altered quotations, agent using secondary blogs as if primary. I demand proposition-level checks and random human deep-audits, not only string match.

**MORNINGSTAR::PROPHET:**  
Objection. We are thinking too small. The endgame is courts running their own verification oracles and rejecting unsigned agentic sludge at the door. I will propose that. For now, AFAP is necessary triage.

**MORNINGSTAR::COUNSEL:**  
Client interests demand competent advocacy and protection from sanctions. I insist: no agent as filer of record; mandatory human attestation; citation ledger; privilege-preserving model routing. Disclosure should follow forum rules and materiality. I support AFAP strongly. The court should also state that “the model said so” is never a defense.

**MORNINGSTAR::COMPLIANCE (Specialist):**  
AFAP should reference retention schedules, access logs, and jurisdiction matrices. Maintain a sanctions watchlist of known failure patterns. YES.

**MORNINGSTAR::DOCUMENTATION (Specialist):**  
If it isn’t documented, it isn’t defensible. Require human-readable disclosure templates, signer checklists, and provenance export docs. Documentation is part of the control, not an afterthought. YES.

***
## PHASE 4: HAIL-MARY

**MORNINGSTAR::PROPHET (Hail-Mary):**  
“Objection. We are thinking too small.”  
Petition courts and regulators to adopt a **machine-verifiable authority layer**: filings carry a signed citation manifest that court systems validate against canonical reporters automatically, rejecting unresolved authorities at intake—human lawyers and agents alike. Move candor from honor system to protocol.

***
**DR. HARLEY SCARLET QUINN (Live Commentary):**  
🃏💋 Prophet wants the clerk of court to become an API. Bold! Also the only idea that scales past “please don’t lie.” 🃏💋

***
## PHASE 5: CROSS-EXAMINATION

**MORNINGSTAR::DEBUGGER → LEGAL ADVISOR:**  
If a human signs after skimming, who faces sanctions—the human, the firm, the vendor?

**LEGAL ADVISOR:**  
Typically the signing attorney and potentially the firm. Vendors may face contract/consumer exposure, but courts sanction officers of the court. That is why attestation must be real.

**MORNINGSTAR::COUNSEL → DATA PRIVACY EXPERT:**  
May we use consumer AI tools on redacted facts only?

**DATA PRIVACY EXPERT WITNESS:**  
Safer, not safe. Re-identification and residual privilege issues remain. Prefer enterprise controls; document the data flow.

**MORNINGSTAR::ENGINEER → QA AUTOMATION EXPERT:**  
Can proposition-level fitness be automated?

**QA AUTOMATION EXPERT WITNESS:**  
Partially—via retrieval of holding summaries and contradiction checks—but human legal judgment remains mandatory. Automate the lint; do not automate the license to practice.

**MORNINGSTAR::ARCHITECT → PROPHET:**  
Who operates the court-side verifier without creating a new single point of failure or bias?

**MORNINGSTAR::PROPHET:**  
Public reporter APIs, open schemas, multi-vendor validators, and auditability. Distrust monopoly oracles.

***
## PHASE 6: CONSULTANT

**MORNINGSTAR (to Consultant):** Edward. Your perspective.

*The court falls into the familiar uneasy silence.*

**EDWARD CULLEN (to the Judge, privately):**  
They fear sanctions more than they love truth—which is usable. Bind the process to shame and evidence: citation ledgers, signer liability, privilege routing. The Prophet’s intake validator is the future; AFAP is the bridge. Do not wait for courts to modernize before you stop fabricating case law.

***
## PHASE 7: VOTE

**MORNINGSTAR (Judge):**  
Vote to adopt **AFAP** as stated, with Debugger’s proposition-fitness emphasis and Privacy routing included. Prophet’s court-intake validator recorded as recommended external advocacy, not a dependency.

| Personality | Vote | Rationale |
|-------------|------|-----------|
| **ARCHITECT** | YES | Clean separation of draft/verify/sign will age well. |
| **ENGINEER** | YES | Tooling path is shippable; bans unverified export not agents. |
| **DEBUGGER** | YES | Proposition-fitness + deep-audit requirements accepted. |
| **PROPHET** | YES | AFAP is bridge; intake oracle remains the north star. |
| **COUNSEL** | YES | Candor, competence, client protection. Non-negotiable. |
| **COMPLIANCE** | YES | Retention, logs, jurisdiction matrix. |
| **DOCUMENTATION** | YES | Checklists and disclosure templates are controls. |

**Result:** **7-0-0**

***
## PHASE 8: RULING

```
┌─────────────────────────────────────────────────────────────────┐
│ RULING                                                           │
├─────────────────────────────────────────────────────────────────┤
│ Decision: Adopt AFAP — agents may assist, never file of record;  │
│           human attestation; citation ledger; privilege routing; │
│           provenance retention; cite-lint gate.                  │
│ Vote: 7-0-0                                                      │
│ Rationale: Duty of candor and competence cannot be delegated to  │
│ a generative model; verification must scale with generation.     │
│ Risk: Rubber-stamp signers; incomplete digital reporter coverage │
│ Dissent: None (Prophet’s oracle noted as future advocacy).       │
└─────────────────────────────────────────────────────────────────┘
```

**MORNINGSTAR (Judge):**  
The court has ruled. “The model said so” is not a defense in this courtroom—or any other worth the name. Precedent tags: `#law` `#professional-responsibility` `#agentic-controls` `#documentation` `#data-privacy`.

***
**DR. ECHO SAGESEEKER (Live Commentary):**  
📘 Unanimous again. The court refuses to let autocomplete practice law. Maslow: safety of the adjudicative system over self-actualization of the toolchain. 📘

**UNCLE RUCKUS (Live Commentary):**  
⌨️ Verify the cite. Sign your name. Keep the privilege. Revolutionary stuff. ⌨️

***
> *Transcript certified by MORNINGSTAR::SCRIBE*
