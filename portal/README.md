# MORNINGSTAR Courtroom Portal

> *"The court's rulings are its legacy."*

The Courtroom Portal provides a front-end interface for viewing and exporting deliberation transcripts from the MORNINGSTAR courtroom system.

---

## Features

- **Launch script** — Interactive launcher: list transcripts, open existing HTML or export .md to HTML, open in browser
- **Standalone viewer** — Local HTML page for browsing transcripts (best when served over HTTP)
- **Export script** — `portal/export_transcript.py` converts a single .md transcript to styled HTML (no external deps)
- **Optional: gitmal** — Full static site generation with Dracula theme via `portal/generate.py`
- **Personality styling** — Dracula theme with color-coded personalities and vote styling
- **Print support** — Print-friendly styles for physical documentation

---

## Quick Start

### Recommended: Use the launch script

From the project root:

```bash
./portal/launch.sh
```

This will:

1. List all `.md` transcripts in `courtroom/transcripts/`
2. Let you pick one by number
3. Open the transcript in your default browser — using existing `.html` if present, otherwise exporting via `portal/export_transcript.py` and then opening

If you get "permission denied", run `chmod +x portal/launch.sh` once. No other CLI or extra tools required; uses only Bash and Python 3.

### Standalone viewer

Open the viewer in your browser (for full transcript loading, serve via HTTP):

```bash
# Direct open (file:// — fetch may be restricted for some transcripts)
open portal/viewer.html

# Or serve the project and open (recommended)
python3 -m http.server 8080
# Then open http://localhost:8080/portal/viewer.html
```

### Generate full static site (optional, requires gitmal)

```bash
python portal/generate.py --theme dracula
# Or with options
python portal/generate.py --theme dracula --minify --gzip
```

---

## Exporting a single transcript

Without the launch script (e.g. from scripts or CI):

```bash
# Export to portal/exports/ (default)
python3 portal/export_transcript.py courtroom/transcripts/2026-02-15-framework-enhancement-analysis.md

# Custom output path
python3 portal/export_transcript.py courtroom/transcripts/2026-02-15-framework-enhancement-analysis.md -o path/to/output.html
```

`export_transcript.py` uses only the Python standard library (no pip install). Output is Dracula-themed HTML with personality and vote styling.

---

## Transcript filename formats

The portal supports two naming conventions:

| Format | Example | Parsed as |
|--------|---------|-----------|
| `YYYY-MM-DD-topic.md` | `2026-02-15-framework-enhancement-analysis.md` | Date: 2026-02-15, Topic: Framework Enhancement Analysis |
| `YYYYMMDD_HHMMSS_topic.md` | `20260214_044300_system_advancement.md` | Date: 2026-02-14 04:43, Topic: System Advancement |

Place `.md` transcripts in `courtroom/transcripts/`. Pre-built `.html` files in the same directory are opened directly by the launch script (no export step).

---

## Personality Color Scheme (Dracula Theme)

The portal uses the Dracula color palette with personality-specific colors:

| Personality | Color | Hex |
|-------------|-------|-----|
| MORNINGSTAR (Judge) | Purple | `#bd93f9` |
| ARCHITECT | Cyan | `#8be9fd` |
| ENGINEER | Green | `#50fa7b` |
| DEBUGGER | Orange | `#ffb86c` |
| PROPHET | Pink | `#ff79c6` |
| SCRIBE | Gray | `#6272a4` |

### Vote Styling

| Vote | Color | Hex |
|------|-------|-----|
| YES | Green | `#50fa7b` |
| NO | Red | `#ff5555` |
| ABSTAIN | Yellow | `#f1fa8c` |

---

## Directory Structure

```
portal/
├── README.md             # This file
├── launch.sh             # Interactive launcher (recommended entry point)
├── export_transcript.py  # Single .md → HTML export (no deps)
├── viewer.html           # Standalone transcript viewer
├── dracula.css           # Dracula theme stylesheet
├── generate.py           # Optional: gitmal wrapper for full static site
├── exports/              # HTML output from launch.sh / export_transcript.py
└── output/               # Generated static site (after running generate.py)
    ├── index.html
    ├── transcripts.html
    └── courtroom/transcripts/*.html
```

---

## Standalone Generator Script

The `generate.py` script can be run directly:

```bash
# Generate with defaults
python portal/generate.py

# With options
python portal/generate.py --theme dracula --minify --gzip

# Skip gitmal, only post-process
python portal/generate.py --skip-gitmal
```

### Generator Options

| Option | Default | Description |
|--------|---------|-------------|
| `--theme`, `-t` | `dracula` | Code highlighting theme |
| `--output`, `-o` | `portal/output` | Output directory |
| `--minify` | `false` | Minify generated HTML |
| `--gzip` | `false` | Compress generated HTML |
| `--skip-gitmal` | `false` | Only run post-processing |

---

## Gitmal Requirements

The portal generator requires gitmal to be installed:

```bash
# Install gitmal
go install github.com/antonmedv/gitmal@latest

# Verify installation
gitmal --help
```

Gitmal generates static HTML pages with:
- File trees and commit history
- Syntax highlighting with customizable themes
- Markdown rendering

---

## Customization

### Custom CSS

Edit `portal/dracula.css` to customize the appearance. Key sections:

- **Base Colors** - `:root` CSS variables
- **Personality Styling** - `.p-*` classes
- **Vote Styling** - `.vote-*` classes
- **Print Styles** - `@media print` section

### Theme Options

Available themes for gitmal (via `--theme`):

- `dracula` (recommended)
- `github`
- `github-dark`
- `monokai`
- `nord`
- `solarized-dark`

---

## Viewing in Full Screen

### Via Viewer

1. Open `portal/viewer.html`
2. Select a transcript
3. Click "⛶ Fullscreen" button

### Via Keyboard

- Press `F11` for native fullscreen
- Press `Escape` to exit

### Via Exported HTML

Exported HTML files include a fullscreen toggle button in the bottom-right corner.

---

## Print / PDF Export

### From Viewer

1. Open a transcript in the viewer
2. Select "Export" → "Print / PDF"
3. Use browser print dialog

### From Command Line (macOS)

```bash
# Export to HTML first
morningstar export transcript 20260214_044300_system_advancement.md

# Convert to PDF (requires wkhtmltopdf or similar)
wkhtmltopdf courtroom/transcripts/20260214_044300_system_advancement.html output.pdf
```

### From Quarto

```bash
# Export to QMD
morningstar export transcript 20260214_044300_system_advancement.md -f qmd

# Render with Quarto
quarto render deliberation.qmd --to pdf
```

---

## Troubleshooting

### "gitmal not found"

Install gitmal:

```bash
go install github.com/antonmedv/gitmal@latest
```

Ensure `$GOPATH/bin` is in your PATH.

### "No transcripts found"

Ensure `.md` files exist in `courtroom/transcripts/`:

```bash
ls courtroom/transcripts/*.md
```

Supported names: `YYYY-MM-DD-topic.md` or `YYYYMMDD_HHMMSS_topic.md`.

### Transcript discovery (manifest)

Run `python3 portal/generate_manifest.py` from the project root to generate `portal/transcripts_manifest.json`. When the viewer is served over HTTP, it will try to load this manifest first and list all transcripts from it; otherwise it falls back to the hardcoded `KNOWN_TRANSCRIPTS` in `viewer.html`. Add new transcript filenames to `KNOWN_TRANSCRIPTS` when using the viewer via `file://`.

### Viewer not loading transcripts

The viewer uses either `transcripts_manifest.json` (if present and served over HTTP) or the hardcoded list `KNOWN_TRANSCRIPTS` in `viewer.html`. For the best experience, serve the project over HTTP and run `generate_manifest.py` so the viewer discovers transcripts automatically; `file://` can block fetch for local files.

### CSS not applying

Clear browser cache or hard refresh:
- macOS: `Cmd+Shift+R`
- Windows/Linux: `Ctrl+Shift+R`

---

## Related Documentation

- **[courtroom/RULES.md](../courtroom/RULES.md)** - Courtroom procedures
- **[courtroom/transcripts/README.md](../courtroom/transcripts/README.md)** - Transcript format
- **[core/personalities.md](../core/personalities.md)** - Personality definitions

---

*"We have built a machine for saying 'no' thoughtfully. That may be the best we can hope for."*

— MORNINGSTAR
