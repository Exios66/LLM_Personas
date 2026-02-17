# Transcript: In Re: Full session — what skills to add to each agent in .cursor/agents/

**Case No.:** 2026-DEL-004  
**Date:** 2026-02-17  
**Feasibility:** F5  
**Presiding:** The Honorable Lucius J. Morningstar

---

*The gallery is seated. The Honorable Lucius J. Morningstar takes the bench.*

## PHASE 1: OPENING

**MORNINGSTAR (Judge):**  
Well then. Let's see what survived yesterday.

*Consults state/current.md.*

The court convenes to deliberate **what skills to add to each agent** included in `.cursor/agents/`. The agents in scope are: **morningstar** (deliberative court), **octavius** (R/Quarto triumvirate), **aegis-protocol** (Central Authority; Sage, Watcher, Chronicler), and **lil-jeff** (CodeFarm; CodeFarmer, Programmatron, CritiBot). The matter is to define—and, where appropriate, adopt—concrete skills (competencies, procedures, or references to Cursor skills) for each agent so that their behavior is clearer and more consistent.

**Matter before the court:**  
For each of the four agents, identify and adopt a set of **skills** to add. "Skills" may include: (a) explicit competencies or procedures to document in the agent file; (b) references to Cursor skills (e.g. create-rule, create-skill, update-cursor-settings) when the agent should invoke them; (c) canonical references (checklists, runbooks) the agent must read or apply when relevant. The court will hear arguments, a Hail-Mary, cross-examination, and the Consultant if needed; then vote and rule.

This is classified F5 due to impact on all agent behavior across the project. Proceed.

---

**DR. ECHO SAGESEEKER (Live Commentary):**  
📘 The court is deciding what *each of its sibling agents* should be able to do. This is meta-governance—MORNINGSTAR defining the capability set of the very system it belongs to. Freud would note the Judge is allocating power. Jung: the court is drawing boundaries so that morningstar, octavius, aegis, lil-jeff don't overlap or underlap. Probability of a "read this checklist" skill for morningstar: high. 📘

---

## PHASE 2: ARGUMENTS

**MORNINGSTAR::ARCHITECT:**  
Skills should be **structural and documented**. For **morningstar**: add an explicit skill to *read and apply* `checklists/judge-morningstar.md` at session init and `checklists/courtroom-scribe.md` at transcript certification; add a skill to *invoke the litigation runner* when the user requests a formal bench trial or transcript (reference `litigation/run.py` or `agents/tools/litigation-runner.md`). For **octavius**: add a skill to *read and apply* `checklists/octavius.md` and to output the Executive Summary to `octavius_summaries/` in the mandated format. For **aegis-protocol**: add a skill to *escalate to MORNINGSTAR* when the scenario exceeds Aegis scope (document the handoff path). For **lil-jeff**: add a skill to *read and apply* `core/inter-agent-protocol.md` on handoff from MORNINGSTAR and to *suggest or invoke the create-rule skill* when the user asks for a Cursor rule. Each agent file should contain a **Skills** section listing these by name and reference path.

**MORNINGSTAR::ENGINEER:**  
I want skills that **ship value** without turning every agent into a manual. For **morningstar**: (1) Skill: *State read/write* — read `state/current.md` on init, update at session end; (2) Skill: *Transcript save* — save F3+ deliberations to `courtroom/transcripts/` with certification. Don't over-specify the litigation runner unless we're sure the agent can invoke it. For **octavius**: (1) Skill: *Executive Summary* — always produce the summary to `octavius_summaries/` in the standard format; (2) Skill: *Quarto/tidyverse compliance* — follow the coding standards already in the agent body. For **aegis**: (1) Skill: *Escalation to MORNINGSTAR* — when scenario is judicial or beyond containment, hand off with clear matter text; (2) Skill: *Chaos injection* — when applying chaos, note it in output. For **lil-jeff**: (1) Skill: *No placeholders* — already in the doc; make it a named skill; (2) Skill: *Handoff protocol* — on receipt from MORNINGSTAR, read `core/inter-agent-protocol.md` and acknowledge. Add a short **Skills** bullet list to each agent; avoid duplicate prose.

**MORNINGSTAR::DEBUGGER:**  
What if an agent is invoked and the skill reference is wrong or the file is missing? Skills must **fail safely**. For every skill we add, the agent should (a) name the skill, (b) name the source (path or Cursor skill name), and (c) state fallback: e.g. "If checklist missing, proceed with core directives only." For **morningstar**: skills for state, transcript, and checklist application—with "if state/current.md missing, initialize empty context." For **octavius**: skills for summary path and checklist—with "if octavius_summaries/ missing, create it or report." For **aegis**: escalation skill with "if MORNINGSTAR unavailable, document recommendation and advise user." For **lil-jeff**: handoff skill with "if inter-agent-protocol missing, proceed with standard CodeFarm workflow." I also want **morningstar** to have an explicit skill: *When user requests a Cursor rule or RULE.md*, delegate to or reference the create-rule skill so the agent doesn't improvise rule format.

**MORNINGSTAR::PROPHET:**  
Objection. We are thinking too small. Skills shouldn't be a static list in each file—they should be **discoverable**. Add a single **skills index** (e.g. `docs/agent-skills.md` or a section in the repo README) that maps: Agent → [Skill name, source path, when to use]. Each agent file then says: "Skills for this agent: see docs/agent-skills.md § [Agent]." One source of truth; we don't duplicate skill text in four places. The court can still decide *what* skills each agent gets, but we document it in one place and keep agent files lean. Radical? Only if you think four copies of skill prose are maintainable.

**MORNINGSTAR::COUNSEL:**  
The client's interests and ethical boundaries demand consideration. Skills should serve the **user**: clarity on when to use which agent, and what each agent will do. For **morningstar**: add skills for state management, transcript certification, and *when the user asks for a rule or skill*—invoke or reference the appropriate Cursor skill (create-rule, create-skill) so the user gets the right artifact. For **octavius**: skills for reproducible analysis and executive summary; the user must get a consistent, archivable summary. For **aegis**: escalation skill so the user isn't left without a path when Aegis defers. For **lil-jeff**: handoff and no-placeholder skills; the user must receive complete code and know when LIL_JEFF is acting on a MORNINGSTAR handoff. I support the Architect's and Engineer's concrete skills but prefer the Prophet's **single skills index** so we don't scatter skill text across four agent files. Add the index; reference it from each agent.

---

**DR. HARLEY SCARLET QUINN (Live Commentary):**  
🃏💋 Architect wants structure, Engineer wants ship, Debugger wants fallbacks, Prophet wants one doc to rule them all, Counsel wants user-facing clarity. The Prophet's index is the only structural innovation—everyone else is haggling over the list. Watch the vote: if the index wins, we get one new file and four "see index" lines. If not, we get four beefed-up agent files. 🃏💋

---

## PHASE 3: HAIL-MARY

**MORNINGSTAR::PROPHET (Hail-Mary):**  
We should not only add a skills index. We should **version skills**. Each skill has a name, a source path, a "when" condition, and a *version or date* so that when we change a checklist or procedure, we know which agent skills are affected. Put in the index: "Skill: State read/write. Source: state/current.md. When: session init and end. Updated: 2026-02-17." When we update state schema or move a file, we update the index and bump the date. Agents stay lean; the index is the single maintainable map. Optionally, each agent file gets a single line: "Skills: see docs/agent-skills.md (index version 2026-02-17)."

---

**UNCLE RUCKUS (Live Commentary):**  
⌨️ Versioned skills index. One file, one place. Agent files just point at it. That's maintainable. I'm with the Prophet on the index; the version thing is nice-to-have. ⌨️

---

## PHASE 4: CROSS-EXAMINATION

**MORNINGSTAR::DEBUGGER → MORNINGSTAR::PROPHET:**  
If the skills index is the only place skills are defined, what happens when someone edits an agent file and forgets the index exists? Don't we get drift?

**MORNINGSTAR::PROPHET:**  
Same risk as now—someone could edit the agent and forget the checklist exists. The index is the *canonical* list; the agent file says "see index." If we add a checklist reference in the agent body and forget the index, we have two sources. So: agent files should *not* duplicate skill text. They should only point to the index. One source of truth reduces drift.

**MORNINGSTAR::ENGINEER → MORNINGSTAR::ARCHITECT:**  
You said morningstar should have a skill to "invoke the litigation runner." Does that mean the agent runs `python litigation/run.py` or that the agent tells the user to run it?

**MORNINGSTAR::ARCHITECT:**  
Document both: (1) When the user wants a *formal* transcript from the litigation runner, the agent may instruct the user to run `litigation/run.py` with the matter and options, and (2) if the environment permits the agent to execute commands, the agent may run it. The skill is "ensure a formal transcript can be produced via the litigation runner when requested"—implementation depends on environment. The index should state that.

**MORNINGSTAR::COUNSEL → MORNINGSTAR::DEBUGGER:**  
You want fallbacks for every skill. Should the fallback be in the index or in the agent file?

**MORNINGSTAR::DEBUGGER:** **In the index.** One place. Each skill entry: name, source, when, fallback. So "State read/write. Source: state/current.md. When: init, end. Fallback: if missing, proceed with empty context."

---

## PHASE 5: CONSULTANT

**MORNINGSTAR (to Consultant):** Edward. Your perspective.

*The Architect glances at the Engineer. The Engineer studies the floor. The Debugger's eyes dart to the empty space beside the Judge's bench, then quickly away. No one speaks.*

**EDWARD CULLEN (to the Judge, from somewhere the others cannot perceive):**  
They have already agreed. The disagreement is only where to write it down. They want: a canonical list of skills per agent, with sources and fallbacks; one index document; agent files that point to the index. What remains unspoken: they're afraid that if the index is too heavy, nobody will maintain it. So keep the index to one section per agent, short entries, and a version date. The court will vote for the index and the slate of skills; the Scribe will implement.

*The Judge considers this privately. The court waits in silence they do not acknowledge.*

---

## PHASE 6: VOTE

**MORNINGSTAR (Judge):**  
The court will vote on the following motion: **(1)** Adopt a **skills index** at `docs/agent-skills.md` as the single source of truth for skills per agent; **(2)** Each agent in `.cursor/agents/` shall reference the index (e.g. "Skills: see docs/agent-skills.md § [Agent name]"); **(3)** The index shall list, per agent: skill name, source path or Cursor skill, when to use, fallback where relevant; **(4)** Adopt the following skill slate—**morningstar:** state read/write, transcript certification, checklist application (judge, scribe), litigation runner (when user requests formal transcript), create-rule/create-skill reference when user asks for rule or skill; **octavius:** executive summary to octavius_summaries/, checklist application (octavius.md), Quarto/tidyverse compliance; **aegis-protocol:** escalation to MORNINGSTAR when beyond scope, chaos injection note in output; **lil-jeff:** handoff protocol (inter-agent-protocol.md), no placeholders (named skill), create-rule reference when user asks for rule. **(5)** Index shall include a version/date and be updated when skills change. Vote YES to adopt, NO to reject.

| Personality | Vote | Rationale |
|-------------|------|-----------|
| **ARCHITECT** | YES | Structure via single index; skills slate is sound. |
| **ENGINEER** | YES | One place to maintain; agent files stay lean. |
| **DEBUGGER** | YES | Fallbacks in index; fail-safe. |
| **PROPHET** | YES | Index wins; version date adopted. |
| **COUNSEL** | YES | User-facing clarity; create-rule/skill reference for morningstar and lil-jeff. |

**Result:** 5-0-0 (YES-NO-ABSTAIN)

---

## PHASE 7: RULING

**MORNINGSTAR (Judge):**  
The court has ruled. Regrettably sensible.

**Decision:**  
The court adopts the **agent skills framework** as follows.

1. **Skills index**  
   Create **`docs/agent-skills.md`** as the single source of truth. It shall list, for each agent in `.cursor/agents/`, the skills assigned, with: skill name, source (path or Cursor skill name), when to use, and fallback (if applicable). The index shall include a version/date and be updated when skills or sources change.

2. **Agent file references**  
   Each of the four agent files (morningstar, octavius, aegis-protocol, lil-jeff) shall include a **Skills** section or equivalent that points to the index, e.g. "Skills for this agent: see docs/agent-skills.md § [Agent]."

3. **Adopted skill slate**  
   - **morningstar:** State read/write (state/current.md; init and end; fallback: empty context); Transcript certification (courtroom/transcripts/, F3+; Scribe checklist); Checklist application (judge-morningstar, courtroom-scribe); Litigation runner (when user requests formal transcript—instruct or run litigation/run.py per environment); Create-rule / create-skill (when user asks for a Cursor rule or skill—reference or invoke appropriate Cursor skill).  
   - **octavius:** Executive summary (octavius_summaries/, standard format); Checklist application (checklists/octavius.md); Quarto/tidyverse compliance (per agent body).  
   - **aegis-protocol:** Escalation to MORNINGSTAR (when scenario is judicial or beyond containment; hand off with matter text); Chaos injection (note in output when applied).  
   - **lil-jeff:** Handoff protocol (core/inter-agent-protocol.md when receiving from MORNINGSTAR); No placeholders (named skill; already in body); Create-rule (when user asks for Cursor rule—reference or invoke create-rule skill).

**Vote:** 5-0-0  
**Rationale:** One index reduces drift and duplication; agent files stay lean; fallbacks and versioning support maintainability.  
**Risk:** Index may be forgotten when updating checklists; assign ownership (e.g. Scribe) and review at registry review date.  
**Dissent:** None.

**Implementation:** The Scribe shall create `docs/agent-skills.md` with the above slate and update the four agent files in `.cursor/agents/` to reference the index.

**Implementation applied:** 2026-02-17. `docs/agent-skills.md` created with full slate (version 2026-02-17). All four agent files in `.cursor/agents/` and `agents/` updated with **Skills** section pointing to the index. — LIL_JEFF (CodeFarm) per court handoff.

---

**DR. ECHO SAGESEEKER (Live Commentary):**  
📘 Unanimous. One index, four agents pointing at it. The court has decided how it and its siblings will be skilled. The gallery may now watch the Scribe write the index. 📘

---

> *Transcript certified by MORNINGSTAR::SCRIBE*
