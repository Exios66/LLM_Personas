#!/usr/bin/env python3
"""
MORNINGSTAR Court Reporter — Documentation Integration Script

Audits courtroom and litigation transcripts, regenerates portal manifest,
and outputs a report for full integration (precedents, metrics, dashboard).

Authenticates transcript filenames per core/case-format.md. Flags non-conforming
files for rename. Validates headers (Case No., certification).

Run every 3 hours via cron, or invoke before Court Reporter subagent.

Usage:
    python courtroom/reporter.py
    python courtroom/reporter.py --rename   # Rename non-conforming uncertified transcripts (interactive)
    python courtroom/reporter.py --rename --yes  # Non-interactive rename

Output: stdout report; regenerates courtroom/portal/transcripts_manifest.json
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
COURTROOM_TRANSCRIPTS = REPO_ROOT / "courtroom" / "transcripts"
LITIGATION_TRANSCRIPTS = REPO_ROOT / "litigation" / "transcripts"
CERTIFICATION_MARKER = "Transcript certified by MORNINGSTAR::SCRIBE"

# Filename patterns — per core/case-format.md
STANDARD_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-.+")
SPECIAL_INTEREST_PATTERN = re.compile(r"^\d{8}_\d{6}_special_interest_.+")
LEGACY_SPECIAL_PATTERN = re.compile(r"^\d{8}_\d{6}_.+")  # YYYYMMDD_HHMMSS_topic (grandfathered)
HANDOFF_PATTERN = re.compile(r"^HANDOFF-", re.I)

# Header validation
CASE_NO_PATTERN = re.compile(r"\*\*Case No\.\*\*:\s*(\d{4}-[A-Z]+-\d{3}(?:-\d+)?)", re.I)
MATTER_ID_PATTERN = re.compile(r"\*\*Matter ID\*\*:\s*(\d{4}-[A-Z]+-\d{3}(?:-\d+)?)", re.I)
DATE_HEADER_PATTERN = re.compile(r"\*\*Date\*\*:\s*(\d{4}-\d{2}-\d{2})", re.I)


def _skip_file(name: str) -> bool:
    """Skip non-transcript files."""
    if name.startswith(".") or name == "README.md" or name == ".gitkeep":
        return True
    if HANDOFF_PATTERN.match(name):
        return True
    return False


def _extract_header_info(content: str) -> dict:
    """Extract Case No., Date from transcript header. Per core/case-format.md."""
    info = {"case_no": None, "date": None, "uses_matter_id": False}
    m = CASE_NO_PATTERN.search(content)
    if m:
        info["case_no"] = m.group(1)
    else:
        m = MATTER_ID_PATTERN.search(content)
        if m:
            info["case_no"] = m.group(1)
            info["uses_matter_id"] = True
    m = DATE_HEADER_PATTERN.search(content)
    if m:
        info["date"] = m.group(1)
    return info


def _suggest_canonical_name(path: Path, content: str) -> Optional[str]:
    """Suggest canonical filename for non-conforming transcript. Returns None if already canonical."""
    stem = path.stem
    if STANDARD_PATTERN.match(stem) or SPECIAL_INTEREST_PATTERN.match(stem):
        return None
    if LEGACY_SPECIAL_PATTERN.match(stem) and "_special_interest_" not in stem:
        # Legacy YYYYMMDD_HHMMSS_topic -> YYYYMMDD_HHMMSS_special_interest_[subject]
        parts = stem.split("_", 2)  # [YYYYMMDD, HHMMSS, topic_with_underscores]
        if len(parts) >= 3:
            subject = parts[2].replace("_", "-").lower()
            return f"{parts[0]}_{parts[1]}_special_interest_{subject}.md"
    # Unknown format — try to derive from header date
    info = _extract_header_info(content)
    if info["date"]:
        slug = stem.replace("_", "-").replace(" ", "-").lower()[:80]
        return f"{info['date']}-{slug}.md"
    return None


def audit_transcripts(dir_path: Path) -> tuple[list[dict], list[dict]]:
    """Audit transcripts in dir. Return (certified, uncertified) lists.
    Each entry includes format_ok, canonical (bool), rename_suggested, header_ok, uses_matter_id."""
    certified = []
    uncertified = []
    if not dir_path.exists():
        return certified, uncertified

    for path in sorted(dir_path.glob("*.md")):
        if _skip_file(path.name):
            continue
        content = path.read_text(encoding="utf-8")
        is_certified = CERTIFICATION_MARKER in content
        info = _extract_header_info(content)
        is_canonical = bool(
            STANDARD_PATTERN.match(path.stem) or SPECIAL_INTEREST_PATTERN.match(path.stem)
        )
        is_legacy = bool(LEGACY_SPECIAL_PATTERN.match(path.stem) and not is_canonical)
        rename_suggested = None if is_canonical else _suggest_canonical_name(path, content)
        header_ok = bool(info["case_no"] and info["date"])

        entry = {
            "name": path.name,
            "path": str(path.relative_to(REPO_ROOT)),
            "path_obj": path,
            "certified": is_certified,
            "format_ok": is_canonical or is_legacy,
            "canonical": is_canonical,
            "rename_suggested": rename_suggested,
            "header_ok": header_ok,
            "case_no": info["case_no"],
            "uses_matter_id": info["uses_matter_id"],
        }

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


def _print_transcript_list(entries: list[dict], show_auth: bool = True) -> None:
    """Print transcript list with format/auth annotations."""
    for e in entries:
        parts = []
        if not e.get("format_ok", True):
            parts.append("[CHECK FORMAT]")
        elif not e.get("canonical", True):
            parts.append("[legacy format]")
        if not e.get("header_ok", True):
            parts.append("[HEADER INCOMPLETE]")
        elif e.get("uses_matter_id"):
            parts.append("[Matter ID—prefer Case No.]")
        if e.get("rename_suggested"):
            parts.append(f"→ rename to: {e['rename_suggested']}")
        suffix = " " + " ".join(parts) if parts else ""
        print(f"    - {e['name']}{suffix}")


def _do_renames(entries: list[dict], non_interactive: bool) -> int:
    """Rename uncertified transcripts with non-canonical filenames. Returns count renamed.
    Certified legacy transcripts are NEVER renamed (grandfather rule)."""
    renamed = 0
    for e in entries:
        if e.get("certified"):
            continue
        suggestion = e.get("rename_suggested")
        if not suggestion:
            continue
        path = e.get("path_obj")
        if not path or not path.exists():
            continue
        target = path.parent / suggestion
        if target.exists():
            print(f"  SKIP (target exists): {path.name} -> {suggestion}")
            continue
        if not non_interactive:
            try:
                reply = input(f"  Rename {path.name} -> {suggestion}? [y/N] ").strip().lower()
            except EOFError:
                reply = "n"
            if reply != "y":
                continue
        try:
            path.rename(target)
            print(f"  RENAMED: {path.name} -> {suggestion}")
            renamed += 1
        except OSError as err:
            print(f"  FAILED: {path.name} -> {suggestion}: {err}")
    return renamed


def main() -> None:
    parser = argparse.ArgumentParser(description="MORNINGSTAR Court Reporter — Integration")
    parser.add_argument("--rename", action="store_true", help="Rename non-conforming uncertified transcripts")
    parser.add_argument("--yes", "-y", action="store_true", help="Non-interactive rename (no prompts)")
    args = parser.parse_args()

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
    if court_cert:
        print("  Certified:")
        _print_transcript_list(court_cert)
    if court_uncert:
        print("  Uncertified:")
        _print_transcript_list(court_uncert)

    # Audit litigation transcripts
    lit_cert, lit_uncert = audit_transcripts(LITIGATION_TRANSCRIPTS)
    print(f"\n## Litigation Transcripts ({LITIGATION_TRANSCRIPTS.relative_to(REPO_ROOT)})")
    print(f"  Certified:   {len(lit_cert)}")
    print(f"  Uncertified: {len(lit_uncert)}")
    if lit_cert:
        print("  Certified:")
        _print_transcript_list(lit_cert)
    if lit_uncert:
        print("  Uncertified:")
        _print_transcript_list(lit_uncert)

    # Rename non-conforming uncertified transcripts if requested
    if args.rename:
        to_rename = [e for e in court_uncert + lit_uncert if e.get("rename_suggested")]
        if to_rename:
            print("\n## Rename (per core/case-format.md)")
            renamed = _do_renames(to_rename, args.yes)
            print(f"  Renamed: {renamed}")
            if renamed:
                court_cert, court_uncert = audit_transcripts(COURTROOM_TRANSCRIPTS)
                lit_cert, lit_uncert = audit_transcripts(LITIGATION_TRANSCRIPTS)

    total = len(court_cert) + len(court_uncert) + len(lit_cert) + len(lit_uncert)
    uncert_total = len(court_uncert) + len(lit_uncert)
    needs_rename = sum(1 for e in court_cert + court_uncert + lit_cert + lit_uncert if e.get("rename_suggested"))
    print(f"\n## Summary")
    print(f"  Total transcripts: {total}")
    print(f"  Uncertified:        {uncert_total}")
    if needs_rename:
        print(f"  Non-canonical (rename suggested): {needs_rename}")

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
    print("  1. AUTHENTICATE/RENAME: Ensure all transcripts follow core/case-format.md.")
    print("     - Uncertified with non-canonical names: rename (e.g. courtroom/reporter.py --rename)")
    print("     - Certified legacy: leave as-is (grandfathered); ensure in precedents")
    print("     - Header: use Case No. (not Matter ID); Date must match filename")
    print("")
    print("  2. PRECEDENTS: Add these certified transcripts to courtroom/precedents.md if not indexed:")
    for e in all_certified:
        case = f" [{e.get('case_no', '?')}]" if e.get("case_no") else ""
        print(f"     - {e['path']}{case}")
    print("  3. METRICS: Sync state/metrics.md from transcript data")
    print("  4. DASHBOARD: Update templates/project-dashboard.md (transcript counts, metrics)")
    print("  5. STATE: Validate state/current.md per core/state-schema.md")
    print("  6. CHANGELOG: Verify CHANGELOG.md has recent decisions")
    print("")
    print("  7. WINDDOWN CHECKLIST VERIFICATION (per checklists/courtroom-scribe.md):")
    print("     - [ ] CHANGELOG updated with decisions")
    print("     - [ ] All transcripts archived in correct location")
    print("     - [ ] state/current.md checkpointed")
    print("     - [ ] Precedents index complete")
    print("     - [ ] Project dashboard refreshed")
    print("     - [ ] Transcript directory hygiene (correct filenames, no uncertified drafts)")
    print("     - [ ] All certified transcripts have precedent entries")
    print("")
    print("  Incomplete integration = contempt before the Court.")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
