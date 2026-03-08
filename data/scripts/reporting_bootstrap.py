"""Helpers for loading local skill modules into thin project scripts."""

from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def ensure_skill_path(skill_name: str) -> Path:
    skill_path = REPO_ROOT / ".opencode" / "skills" / skill_name / "src"
    resolved = str(skill_path)
    if resolved not in sys.path:
        sys.path.insert(0, resolved)
    return skill_path
