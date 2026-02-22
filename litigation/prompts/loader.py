"""Load MORNINGSTAR framework content from repository sources."""

from pathlib import Path
from typing import Dict, Optional

from .sources import SOURCES, litigation_prompt_path, repo_root


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

    @property
    def mfaf(self) -> str:
        """Feasibility Assessment Framework."""
        return self._get("mfaf")

    @property
    def checklist_aegis(self) -> str:
        """Aegis Protocol checklist (F4+ Authority Assessment)."""
        return self._get("checklist_aegis")

    @property
    def domain_experts(self) -> str:
        """Domain Expert Registry (formatted from experts.yaml)."""
        if "domain_experts" not in self._cache:
            self._cache["domain_experts"] = self._load_domain_experts()
        return self._cache["domain_experts"]

    def _load_domain_experts(self) -> str:
        """Load and format domain experts from experts.yaml."""
        path = self._root / "courtroom" / "domains" / "experts.yaml"
        if not path.exists():
            return ""
        try:
            import yaml
            # experts.yaml may have multiple documents (---); merge them
            data = {}
            for doc in yaml.safe_load_all(path.read_text(encoding="utf-8")):
                if isinstance(doc, dict):
                    data.update(doc)
        except Exception:
            return ""
        if not data:
            return ""
        lines = [
            "# Domain Expert Registry",
            "",
            "The court may summon Expert Witnesses (/summon [domain]-expert) or seat Specialists (/seat [domain]-specialist, Judge only, F3+).",
            "",
            "## Available Domains",
            "",
        ]
        for key, val in data.items():
            if key.startswith("_") or not isinstance(val, dict):
                continue
            name = val.get("name", key)
            available = val.get("available_as", [])
            scope = val.get("scope", "")
            if isinstance(scope, str):
                scope = scope.strip()
            heuristics = val.get("heuristics", [])
            sig_questions = val.get("signature_questions", [])
            voice = val.get("voice", "")
            failure = val.get("failure_mode", "")
            witness = "witness" in available
            specialist = "specialist" in available
            roles = []
            if witness:
                roles.append("Witness")
            if specialist:
                roles.append("Specialist")
            lines.append(f"### {name} ({key})")
            lines.append(f"- **Roles:** {', '.join(roles)}")
            lines.append(f"- **Scope:** {scope}")
            lines.append(f"- **Voice:** {voice}")
            lines.append("- **Heuristics:**")
            for h in heuristics[:5]:
                lines.append(f"  - {h}")
            lines.append("- **Signature Questions:**")
            for q in sig_questions[:3]:
                lines.append(f"  - {q}")
            lines.append(f"- **Failure Mode:** {failure}")
            lines.append("")
        return "\n".join(lines).rstrip()

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

    @property
    def runner_instruction(self) -> str:
        """Litigation runner tail instruction (litigation/prompts/runner-instruction.md)."""
        return _read(litigation_prompt_path("runner-instruction")).strip()

    @property
    def user_prefix(self) -> str:
        """Common user prompt opening line (litigation/prompts/user-prefix.md)."""
        return _read(litigation_prompt_path("user-prefix")).strip()

    def user_instructions(self, hearing_type: str) -> str:
        """Hearing-type instructions from litigation/prompts/user/<hearing_type>.md."""
        path = litigation_prompt_path(hearing_type, "user")
        return _read(path).strip()
