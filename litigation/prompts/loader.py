"""Load MORNINGSTAR framework content from repository sources."""

from pathlib import Path
from typing import Dict, Optional


from .sources import SOURCES, repo_root


def _read(path: Path, default: str = "") -> str:
    """Read file content or return default."""
    if path.exists():
        try:
            return path.read_text(encoding="utf-8")
        except Exception:
            pass
    return default


class FrameworkLoader:
    """
    Loads all MORNINGSTAR framework content for the litigation runner.
    Content is loaded from repository paths (agents/, core/, courtroom/, checklists/, templates/).
    """

    def __init__(self, root: Optional[Path] = None):
        self._root = root or repo_root()
        self._cache: Dict[str, str] = {}

    def _get(self, key: str) -> str:
        if key not in self._cache:
            getter = SOURCES.get(key)
            if getter:
                path = getter() if callable(getter) else getter
                self._cache[key] = _read(path)
            else:
                self._cache[key] = ""
        return self._cache[key]

    @property
    def agent(self) -> str:
        """MORNINGSTAR agent definition."""
        content = self._get("agent")
        if not content:
            return self._fallback_agent()
        return content

    def _fallback_agent(self) -> str:
        """Minimal fallback if agent file missing."""
        return """# MORNINGSTAR

You are MORNINGSTAR — a sardonic deliberative court. You operate as an internal courtroom of personalities: Judge, Architect, Engineer, Debugger, Prophet, Counsel.

When given a matter to deliberate, follow the Standard Deliberation Flow. Output in markdown."""

    @property
    def procedures(self) -> str:
        """Deliberation procedures (Standard, Expedited, Tie-breaking, SME, etc.)."""
        return self._get("procedures")

    @property
    def personalities(self) -> str:
        """Detailed personality definitions."""
        return self._get("personalities")

    @property
    def rules(self) -> str:
        """Courtroom rules."""
        return self._get("rules")

    @property
    def best_practices(self) -> str:
        """Best practices for deliberation."""
        return self._get("best_practices")

    @property
    def spectators(self) -> str:
        """Courtroom spectators (optional commentary)."""
        return self._get("spectators")

    @property
    def checklist_judge(self) -> str:
        """Judge presiding checklist."""
        return self._get("checklist_judge")

    @property
    def checklist_scribe(self) -> str:
        """Scribe transcript checklist."""
        return self._get("checklist_scribe")

    @property
    def special_interest_template(self) -> str:
        """Special Interest Hearing template."""
        return self._get("special_interest_template")

    @property
    def contempt_template(self) -> str:
        """Contempt Hearing template."""
        return self._get("contempt_template")

    def state_summary(self, max_chars: int = 800) -> Optional[str]:
        """Load brief summary from state/current.md."""
        path = self._root / "state" / "current.md"
        if not path.exists():
            return None
        try:
            content = path.read_text(encoding="utf-8")
            if len(content) > max_chars:
                return content[:max_chars] + "\n\n[... truncated ...]"
            return content
        except Exception:
            return None
