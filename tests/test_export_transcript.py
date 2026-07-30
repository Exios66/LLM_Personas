"""Regression tests for courtroom portal transcript export paths and parsing."""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPORT_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "export_transcript.py"


def _load_export_module():
    spec = importlib.util.spec_from_file_location("export_transcript", EXPORT_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_transcripts_dir_resolves_to_courtroom_transcripts():
    """Export script must read courtroom/transcripts, not courtroom/courtroom/transcripts."""
    mod = _load_export_module()
    expected = REPO_ROOT / "courtroom" / "transcripts"
    assert mod.TRANSCRIPTS_DIR == expected
    assert mod.TRANSCRIPTS_DIR.exists()


def test_extract_title_from_h1():
    mod = _load_export_module()
    path = Path("2026-02-15-framework-enhancement-analysis.md")
    content = "# Framework Enhancement Analysis\n\nBody."
    assert mod.extract_title(path, content) == "Framework Enhancement Analysis"


def test_extract_title_from_dated_filename():
    mod = _load_export_module()
    path = Path("2026-02-15-framework-enhancement-analysis.md")
    assert mod.extract_title(path, "") == "Framework Enhancement Analysis"


def test_md_to_html_headers_and_code_blocks():
    mod = _load_export_module()
    md = "# Title\n\n```py\nprint('<tag>')\n```\n\nBody **bold** and `inline`."
    html = mod.md_to_html(md)

    assert "<h1>Title</h1>" in html
    assert "print('&lt;tag&gt;')" in html or "&lt;tag&gt;" in html
    assert "<strong>bold</strong>" in html
    assert "<code>inline</code>" in html


def test_md_to_html_blockquote_and_hr():
    mod = _load_export_module()
    md = "> Certified ruling\n\n---\n\nFinal paragraph."
    html = mod.md_to_html(md)

    assert "<blockquote>Certified ruling</blockquote>" in html
    assert "<hr>" in html


def test_apply_personality_styling_votes_and_personalities():
    mod = _load_export_module()
    html = mod.apply_personality_styling(
        "ARCHITECT votes YES. ENGINEER votes NO. SCRIBE records ABSTAIN."
    )

    assert 'class="p-architect"' in html
    assert 'class="p-engineer"' in html
    assert 'class="p-scribe"' in html
    assert 'class="vote-yes"' in html
    assert 'class="vote-no"' in html
    assert 'class="vote-abstain"' in html


def test_exports_dir_resolves_to_portal_exports():
    mod = _load_export_module()
    expected = REPO_ROOT / "courtroom" / "portal" / "exports"
    assert mod.EXPORTS_DIR == expected
