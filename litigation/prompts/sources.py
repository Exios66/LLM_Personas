"""Source paths for MORNINGSTAR framework content."""

from pathlib import Path


def repo_root() -> Path:
    """Project root (parent of litigation/)."""
    return Path(__file__).resolve().parent.parent.parent


def agents_path(name: str) -> Path:
    """Path to agent definition. Prefers agents/, fallback .cursor/agents/."""
    root = repo_root()
    p = root / "agents" / f"{name}.md"
    if not p.exists():
        p = root / ".cursor" / "agents" / f"{name}.md"
    return p


def core_path(name: str) -> Path:
    """Path to core document."""
    return repo_root() / "core" / f"{name}.md"


def courtroom_path(name: str) -> Path:
    """Path to courtroom document."""
    return repo_root() / "courtroom" / f"{name}.md"


def checklist_path(name: str) -> Path:
    """Path to checklist."""
    return repo_root() / "checklists" / f"{name}.md"


def template_path(name: str) -> Path:
    """Path to template."""
    return repo_root() / "templates" / f"{name}.md"


def state_path() -> Path:
    """Path to session state."""
    return repo_root() / "state" / "current.md"


# Canonical source map for litigation runner
SOURCES = {
    "agent": lambda: agents_path("morningstar"),
    "procedures": lambda: core_path("procedures"),
    "personalities": lambda: core_path("personalities"),
    "rules": lambda: courtroom_path("RULES"),
    "best_practices": lambda: courtroom_path("BEST_PRACTICES"),
    "spectators": lambda: courtroom_path("spectators"),
    "mfaf": lambda: core_path("mfaf"),
    "checklist_judge": lambda: checklist_path("judge-morningstar"),
    "checklist_scribe": lambda: checklist_path("courtroom-scribe"),
    "checklist_aegis": lambda: checklist_path("aegis-protocol"),
    "special_interest_template": lambda: template_path("special-interest-hearing"),
    "contempt_template": lambda: template_path("contempt-hearing"),
    "state": state_path,
}
