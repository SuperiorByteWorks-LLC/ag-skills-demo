from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
DATA_SCRIPTS_ROOT = REPO_ROOT / "data" / "scripts"
if str(DATA_SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(DATA_SCRIPTS_ROOT))

GEOADMIN_LEVELS = ("l0_countries", "l1_states", "l2_counties")


def geoadmin_level_roots() -> dict[str, Path]:
    from lib.paths import (
        shared_geoadmin_counties_dir,
        shared_geoadmin_countries_dir,
        shared_geoadmin_states_dir,
    )

    return {
        "l0_countries": shared_geoadmin_countries_dir(),
        "l1_states": shared_geoadmin_states_dir(),
        "l2_counties": shared_geoadmin_counties_dir(),
    }
