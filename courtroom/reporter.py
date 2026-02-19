#!/usr/bin/env python3
"""
MORNINGSTAR Court Reporter — Documentation Integration Script

Audits courtroom and litigation transcripts, regenerates portal manifest,
and outputs a report for full integration (precedents, metrics, dashboard).

Run every 3 hours via cron, or invoke before Court Reporter subagent.

Usage:
    python courtroom/reporter.py
    # or from project root:
    python courtroom/reporter.py

Output: stdout report; regenerates courtroom/portal/transcripts_manifest.json
"""

import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COURTROOM_TRANSCRIPTS = REPO_ROOT / "courtroom" / "transcripts"
LITIGATION_TRANSCRIPTS = REPO_ROOT / "litigation" / "transcripts"
CERTIFICATION_MARKER = "Transcript certified by MORNINGSTAR::SCRIBE"

# Filename patterns
STANDARD_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-.+")
SPECIAL_INTEREST_PATTERN = re.compile(r"^\d{8}_\d{6}_special_interest_.+")
HANDOFF_PATTERN = re.compile(r"^HANDOFF-", re.I)


def _skip_file(name: str) -> bool:
    """Skip non-transcript files."""
    if name.startswith(".") or name == "README.md" or name == ".gitkeep":
        return True
    if HANDOFF_PATTERN.match(name):
        return True
    return False


def audit_transcripts(dir_path: Path) -> tuple[list[dict], list[dict]]:
    """Audit transcripts in dir. Return (certified, uncertified) lists."""
    certified = []
    uncertified = []
    if not dir_path.exists():
        return certified, uncertified

    for path in sorted(dir_path.glob("*.md")):
        if _skip_file(path.name):
            continue
        content = path.read_text(encoding="utf-8")
        is_certified = CERTIFICATION_MARKER in content
        entry = {
            "name": path.name,
            "path": str(path.relative_to(REPO_ROOT)),
            "certified": is_certified,
        }
        # Check filename format
        if STANDARD_PATTERN.match(path.stem) or SPECIAL_INTEREST_PATTERN.match(path.stem):
            entry["format_ok"] = True
        else:
            entry["format_ok"] = False

        if is_certified:
            certified.append(entry)
        else:
            uncertified.append(entry)

    return certified, uncertified


def regenerate_manifest() -> bool:
    """Run generate_manifest.py. Return True on success."""
    script = REPO_ROOT / "courtroom" / "portal" / "generate_manifest.py"
    if not script.exists():
        return False
    try:
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0
    except Exception:
        return False


def main() -> None:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print("=" * 60)
    print("MORNINGSTAR Court Reporter — Integration Report")
    print(f"Run: {now}")
    print("=" * 60)

    # Audit courtroom transcripts
    court_cert, court_uncert = audit_transcripts(COURTROOM_TRANSCRIPTS)
    print(f"\n## Courtroom Transcripts ({COURTROOM_TRANSCRIPTS.relative_to(REPO_ROOT)})")
    print(f"  Certified:   {len(court_cert)}")
    print(f"  Uncertified: {len(court_uncert)}")
    if court_uncert:
        for e in court_uncert:
            fmt = " [format OK]" if e.get("format_ok", True) else " [CHECK FORMAT]"
            print(f"    - {e['name']}{fmt}")

    # Audit litigation transcripts
    lit_cert, lit_uncert = audit_transcripts(LITIGATION_TRANSCRIPTS)
    print(f"\n## Litigation Transcripts ({LITIGATION_TRANSCRIPTS.relative_to(REPO_ROOT)})")
    print(f"  Certified:   {len(lit_cert)}")
    print(f"  Uncertified: {len(lit_uncert)}")
    if lit_uncert:
        for e in lit_uncert:
            fmt = " [format OK]" if e.get("format_ok", True) else " [CHECK FORMAT]"
            print(f"    - {e['name']}{fmt}")

    total = len(court_cert) + len(court_uncert) + len(lit_cert) + len(lit_uncert)
    uncert_total = len(court_uncert) + len(lit_uncert)
    print(f"\n## Summary")
    print(f"  Total transcripts: {total}")
    print(f"  Uncertified:        {uncert_total}")

    # Regenerate manifest
    print(f"\n## Manifest")
    if regenerate_manifest():
        print("  courtroom/portal/transcripts_manifest.json — regenerated")
    else:
        print("  WARNING: Could not regenerate manifest")

    # ACTION REQUIRED — Court Reporter MUST act on this
    all_certified = court_cert + lit_cert
    print("\n## ACTION REQUIRED (Court Reporter: complete or face contempt)")
    print("  The agent MUST act on this output. Do not merely report.")
    print("")
    print("  1. PRECEDENTS: Add these certified transcripts to courtroom/precedents.md if not indexed:")
    for e in all_certified:
        print(f"     - {e['path']}")
    print("  2. METRICS: Sync state/metrics.md from transcript data")
    print("  3. DASHBOARD: Update templates/project-dashboard.md (transcript counts, metrics)")
    print("  4. STATE: Validate state/current.md per core/state-schema.md")
    print("  5. CHANGELOG: Verify CHANGELOG.md has recent decisions")
    print("")
    print("  Incomplete integration = contempt before the Court.")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
