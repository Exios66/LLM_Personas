# Courtroom Litigation Runner

Run the MORNINGSTAR courtroom litigation protocol using local or free-tier LLMs. Supports **Ollama**, **LM Studio** (or LLM Studio), and **OpenRouter** (free models).

---

## Overview

This directory orchestrates the deliberation flow defined in `core/procedures.md` and agent documentation. The `litigation/prompts/` subdirectory loads the full MORNINGSTAR framework (procedures, rules, personalities, checklists, best practices). It:

1. Loads session state from `state/current.md`
2. Presents a matter for deliberation
3. Invokes the court personalities (Judge, Architect, Engineer, Debugger, Prophet, Counsel) via LLM calls
4. Records arguments, vote, and ruling
5. Saves transcripts to `courtroom/transcripts/` and updates state

---

## Supported Providers

| Provider | Type | Cost | Setup |
|----------|------|------|-------|
| **OpenRouter** (default) | API | Free tier available | API key; model from list (slot machine) |
| **Ollama** | Local | Free | Install Ollama, pull a model |
| **LM Studio** | Local | Free | Install LM Studio, load model, start server |

### Ollama

- **URL:** `http://localhost:11434`
- **Models:** `llama3.2`, `mistral`, `qwen2`, etc.
- **Setup:** [ollama.com](https://ollama.com) → install → `ollama pull llama3.2`

### LM Studio / LLM Studio

- **URL:** `http://localhost:1234` (OpenAI-compatible API)
- **Models:** Any model you load in LM Studio
- **Setup:** [lmstudio.ai](https://lmstudio.ai) → download → load model → Start Server (Developer tab)

### OpenRouter

- **URL:** `https://openrouter.ai/api/v1`
- **Models:** When no `--model` is set, a model is chosen from the list (slot machine by default; `--model-select` for interactive). Only free-tier models (`:free` suffix) are used to avoid "insufficient funds" errors.
- **Setup:** Create API key at [openrouter.ai/keys](https://openrouter.ai/keys) → set `OPENROUTER_API_KEY`
- **Free models:** If you see "No endpoints found matching your data policy", configure [Privacy Settings](https://openrouter.ai/settings/privacy) — enable "Model Training" or relax restrictions for free model access.
- **Best practices:** See [litigation/OPENROUTER_BEST_PRACTICES.md](OPENROUTER_BEST_PRACTICES.md) — app attribution, provider routing, credits, latency, and courtroom-specific recommendations.

---

## Quick Start

### 1. Install Dependencies

**Option A — Venv in `litigation/` (recommended for local litigation work):**

```bash
cd /path/to/LLM_Personas
python3 -m venv litigation/.venv
source litigation/.venv/bin/activate   # Windows: litigation\.venv\Scripts\activate
pip install -r litigation/requirements.txt
```

**Option B — Repo-root venv:**

```bash
cd /path/to/LLM_Personas
python3 -m venv .venv
source .venv/bin/activate
pip install -r litigation/requirements.txt
```

### 2. Configure Provider

Copy the example config and edit:

```bash
cp litigation/config.example.yaml litigation/config.yaml
```

Edit `litigation/config.yaml`:

```yaml
provider: openrouter   # default; or ollama | lm_studio
# OpenRouter: set OPENROUTER_API_KEY; model chosen from list (slot machine)
```

For OpenRouter, set your API key either:

- **Option A:** Add to `litigation/providers/.env`:

  ```
  OPENROUTER_API_KEY=sk-or-v1-your-key
  ```

  (The runner loads this automatically.)

- **Option B:** Export in your shell:

  ```bash
  export OPENROUTER_API_KEY=sk-or-v1-...
  ```

### 3. Run a Deliberation

From project root:

**Interactive menu** (when no matter provided):

- Run `python litigation/run.py` for the main menu
- **Quick run** — Enter matter, use defaults (fastest)
- **Full run** — Configure provider, model, feasibility, hearing type, then run
- **Help** — Show command-line options
- **Exit** — Quit
- Press Enter alone at any prompt to return to the previous menu

**Direct run** (matter on command line):

```bash
python litigation/run.py "Should we adopt a new naming convention for API endpoints?"
```

**OpenRouter model selection** (when `provider: openrouter` and no `--model`):

- Default: slot machine animation picks a random model from the list
- `--model-select`: prompt to choose from the list (or 0 for random)

Or use the launch script:

```bash
./litigation/launch.sh "Should we adopt a new naming convention for API endpoints?"
./litigation/launch.sh          # Interactive menu
```

---

## Configuration Reference

| Key | Description | Example |
|-----|--------------|---------|
| `provider` | `ollama`, `lm_studio`, or `openrouter` | `ollama` |
| `model` | Model identifier for the provider | `llama3.2` |
| `ollama.base_url` | Ollama API URL | `http://localhost:11434` |
| `lm_studio.base_url` | LM Studio OpenAI-compat URL | `http://localhost:1234/v1` |
| `openrouter.base_url` | OpenRouter API URL | `https://openrouter.ai/api/v1` |
| `openrouter.app_attribution` | HTTP-Referer, X-Title for rankings | See `OPENROUTER_BEST_PRACTICES.md` |
| `openrouter.provider` | Routing: sort, allow_fallbacks, data_collection, zdr | See `OPENROUTER_BEST_PRACTICES.md` |
| `openrouter.models` | List for selection (slot machine or `--model-select`) | See `config.example.yaml` |
| `max_tokens` | Max tokens per response | `2048` |
| `temperature` | Sampling temperature (0–1) | `0.7` |

---

## Environment Variables

| Variable | Provider | Purpose |
|----------|----------|---------|
| `OPENROUTER_API_KEY` | OpenRouter | API authentication |
| `LITIGATION_CONFIG` | All | Path to config file (default: `litigation/config.yaml`) |

---

## Output

- **Transcripts (default):** `litigation/transcripts/YYYY-MM-DD-[matter-slug].md`
- **Transcripts (optional):** `courtroom/transcripts/` — use `--save-to courtroom` or choose in menu
- **State:** `state/current.md` updated with session outcome
- **CHANGELOG:** Updated if decisions were made (F3+)

---

## Transcript Viewer (local portal)

View transcripts from the terminal or in a browser. All operations are local to `litigation/`.

**List transcripts:**

```bash
python litigation/viewer.py list
python litigation/viewer.py list --plain   # One filename per line
```

**Show a transcript (terminal):**

```bash
python litigation/viewer.py show                    # Latest
python litigation/viewer.py show 2026-02-17         # By name/prefix
python litigation/viewer.py show 2026-02-17 --pager # Through less
```

**Serve in browser (index + rendered markdown):**

```bash
python litigation/viewer.py serve        # http://127.0.0.1:8765/
python litigation/viewer.py serve 9000   # Custom port
```

Then open http://127.0.0.1:8765/ in a browser. Styling matches the courtroom portal (Dracula-like, personality/vote highlighting).

---

## Prompts Subdirectory

`litigation/prompts/` loads and assembles the **full** MORNINGSTAR framework:

- **Agent** (`agents/morningstar.md`)
- **Procedures** (`core/procedures.md`) — Standard, Expedited, Special Interest, Contempt, SME, Consultant
- **Personalities** (`core/personalities.md`) — Judge, Edward Cullen, Architect, Engineer, Debugger, Prophet, Counsel, Scribe
- **Rules** (`courtroom/RULES.md`)
- **MFAF** (`core/mfaf.md`) — Feasibility Assessment Framework
- **Domain Experts** (`courtroom/domains/experts.yaml`) — Security, Database, Compliance, Infrastructure, Performance, Accessibility, i18n, Cryptography, API Design, Testing, Data Privacy, Observability, Resilience, Incident Response, DevOps, Documentation, Design Systems, Frontend, Mobile, AI/ML, Data Engineering, Cost, Sustainability, Ethics, QA Automation; advisory: UX, Legal
- **Spectators** (`courtroom/spectators.md`) — Dr. Echo Sageseeker, Dr. Harley Scarlet Quinn, Uncle Ruckus
- **Checklists** — Judge, Scribe, Aegis (F4+)
- **Best practices** (`courtroom/BEST_PRACTICES.md`)
- **Templates** — Special Interest Hearing, Contempt Hearing

See `litigation/prompts/README.md` for the full source map.

### Hearing Types

| Type | Flag | Use |
|------|------|-----|
| **Standard** | (default) | Full deliberation: Opening, Arguments, Hail-Mary, Cross-examination, Consultant, Vote, Ruling |
| **Expedited** | `--hearing-type expedited` | Brief format for F2 matters |
| **Special Inquiry** | `--hearing-type special_inquiry` | Investigative hearing, no vote; testimony and findings |
| **Contempt** | `--hearing-type contempt` | Adversarial proceeding; respondent charged |

### Options

- `--menu` — Show interactive menu (even when matter is provided)
- `--no-spectators` — Exclude spectator commentary (Dr. Echo, Dr. Harley, Uncle Ruckus) from system prompt
- `--no-save` — Do not save transcript
- `--save-to litigation|courtroom` — Save to `litigation/transcripts/` (default) or `courtroom/transcripts/`

---

## Canonical References

- `core/procedures.md` — Deliberation flow, session lifecycle
- `courtroom/RULES.md` — Transcript rules, titling
- `checklists/judge-morningstar.md` — Presiding checklist
- `.cursor/agents/morningstar.md` — MORNINGSTAR agent definition

---

> *"The court runs on silicon now. The rulings remain regrettably sensible."*
> — The Honorable Lucius J. Morningstar
