# MORNINGSTAR Posit Connect Cloud site

Quarto website for the MORNINGSTAR / LLM_Personas corpus, modeled on the JackJBurleson PSYCH 755 Connect Cloud layout (navbar, sidebar, TOC, SCSS theme, static bundle publish).

**Live:** https://019f9a59-7b27-9a28-b0e8-d4576d860993.share.connect.posit.cloud/  
**Dashboard:** https://connect.posit.cloud/jackjburleson/content/019f9a59-7b27-9a28-b0e8-d4576d860993

## Layout

| Path | Role |
|---|---|
| `index.qmd` | Overview manuscript / landing page |
| `Getstarted.md` | Local + publish setup |
| `_quarto.yml` | Website config (navbar, sidebar, format) |
| `_publish.yml` | Connect Cloud content id (written on first publish) |
| `styles.scss` | MORNINGSTAR brand theme |
| `site/` | Generated pages synced from wiki, core, courtroom, docs |
| `_site/` | Render output (gitignored) |

## Commands

From the **repository root**:

```bash
python scripts/build_posit_site_pages.py
cd posit && quarto render
python scripts/publish_posit_morningstar.py --skip-render
```

Or one-shot render + publish:

```bash
python scripts/publish_posit_morningstar.py
```

This creates a **new** JackJBurleson content item and never updates the PSYCH 755 manuscript content id `019f9a10-ebb9-d1d5-839f-97e794bfd0ca`.
