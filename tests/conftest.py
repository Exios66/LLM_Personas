"""Test harness: repo root on sys.path; load courtroom/reporter.py as a module."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _load_court_reporter():
    name = "courtroom_reporter"
    if name in sys.modules:
        return sys.modules[name]
    path = ROOT / "courtroom" / "reporter.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def court_reporter():
    return _load_court_reporter()
