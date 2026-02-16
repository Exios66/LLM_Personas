# GitHub Wiki Content — LLM_Personas

This directory contains markdown files that can be **seamlessly added to your GitHub project Wiki**.

## How to add to GitHub Wiki

1. **Enable the Wiki** for your GitHub repo (Settings → Features → Wiki).
2. **Clone the wiki repo** (each GitHub repo has an optional wiki; clone it via `git clone https://github.com/YOUR_USER/YOUR_REPO.wiki.git`).
3. **Copy the contents of this `wiki/` folder** into the cloned wiki repo:
   - Copy every `.md` file from `wiki/` into the wiki repo root.
   - **Important:** Rename `Home.md` to the default wiki home page name your GitHub uses (often `Home.md` is already the default; if not, use the name GitHub shows as "Home").
   - The file **`_Sidebar.md`** will appear in the wiki sidebar automatically on GitHub.
4. **Commit and push** to the wiki repo. The wiki will update.

## File list

| File | Wiki page purpose |
|------|-------------------|
| `Home.md` | Main landing page |
| `_Sidebar.md` | Sidebar navigation (GitHub displays this automatically) |
| `Quick-Start.md` | Getting started steps |
| `The-Court.md` | Court members and roles |
| `Command-Reference.md` | Session and SME commands |
| `Domains-and-Experts.md` | SME registry and summoning |
| `When-to-Convene.md` | Feasibility levels and dissolution |
| `Procedures.md` | Deliberation and session lifecycle |
| `SME-Framework.md` | Expert Witness vs Specialist |
| `State-and-Metrics.md` | State and metrics overview |
| `Error-Recovery.md` | Recovery and rollback |
| `Inter-Agent-Protocol.md` | Handoff between agents |
| `Portal.md` | Transcript viewer and export |
| `Onboarding.md` | Start here for new users |
| `Glossary.md` | Term index |
| `Runbook.md` | Troubleshooting index |
| `Edge-Cases.md` | Known limitations |
| `Companion-Personas.md` | LIL_JEFF and OCTAVIUS |
| `Precedents.md` | Precedent database overview |
| `Repository-Map.md` | Full directory and file map |
| `Changelog.md` | Link/overview to decision history |

## Notes

- **Internal links** in the wiki pages use GitHub Wiki style: `[Page Name](Page-Name)`. After upload, adjust if your wiki uses different naming (e.g. spaces).
- **Repo links** to the main codebase use full URLs or relative paths as appropriate; you may replace with your actual repo URL.
- The source of truth for the project remains the main repo (README, `core/`, `courtroom/`, etc.). The wiki is a reader-friendly mirror for documentation.
