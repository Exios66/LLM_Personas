---
title: "Get Started"
---

Local setup for the MORNINGSTAR repository and this Posit Connect Cloud website.

## 1. Clone and environment

```bash
git clone https://github.com/Exios66/LLM_Personas.git
cd LLM_Personas
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pandas   # used by index.qmd corpus stats on render
```

## 2. Use the court (Cursor / agents)

1. Open the repo in Cursor.
2. Invoke the **morningstar** subagent or `/morningstar`.
3. Present a matter with tradeoffs; receive a ruled decision.
4. Checkpoint with `/update`; close with `/end`.

Details: [Quick Start](site/guide/quick-start.md) · [Onboarding](site/guide/onboarding.md) · [Runbook](site/guide/runbook.md).

## 3. Browser apps (local)

```bash
# Live courtroom (static)
python3 -m http.server 8080
# → http://localhost:8080/index.html

# Transcript portal launcher
./courtroom/portal/launch.sh
```

On this published site: [Applications](site/apps/index.md).

## 4. Litigation runner (local / free LLMs)

```bash
cp litigation/config.example.yaml litigation/config.yaml
# edit provider: ollama | lmstudio | openrouter
python -m litigation.run
```

See [Litigation Runner](site/litigation/runner.md).

## 5. Render this Quarto site

Requires [Quarto](https://quarto.org) ≥ 1.10.

```bash
python scripts/build_posit_site_pages.py
cd posit
quarto check
quarto render          # writes posit/_site/
quarto preview         # local preview
```

## 6. Publish to JackJBurleson Posit Connect Cloud

Creates or updates the **MORNINGSTAR** content item (separate from the PSYCH 755 manuscript). Uses device-code OAuth or `POSIT_CONNECT_CLOUD_*` env tokens.

```bash
python scripts/build_posit_site_pages.py
python scripts/publish_posit_morningstar.py
# or if already rendered:
python scripts/publish_posit_morningstar.py --skip-render
```

After the first successful publish, `posit/_publish.yml` stores the content id and share URL.

| Field | Value |
|---|---|
| Account | `jackjburleson` |
| Quarto project | `posit/` |
| Share URL | https://019f9a59-7b27-9a28-b0e8-d4576d860993.share.connect.posit.cloud/ |
| Dashboard | https://connect.posit.cloud/jackjburleson/content/019f9a59-7b27-9a28-b0e8-d4576d860993 |
| Content ID | `019f9a59-7b27-9a28-b0e8-d4576d860993` |
| Config | `posit/_publish.yml`, `posit/_quarto.yml` |
| Helper | `scripts/publish_posit_morningstar.py` |
