from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
DATA_SCRIPTS_ROOT = REPO_ROOT / "data" / "scripts"
if str(DATA_SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(DATA_SCRIPTS_ROOT))


def _paths_module() -> object:
    from lib import paths

    return paths


@dataclass(slots=True)
class AnnualMaturityConfig:
    year: int
    weather_source: str = "nasa-power"

    @property
    def geoadmin_root(self) -> Path:
        return _paths_module().shared_geoadmin_dir()

    @property
    def corn_gdd_path(self) -> Path:
        return _paths_module().shared_corn_gdd_table_path(self.year)

    @property
    def corn_rm_path(self) -> Path:
        return _paths_module().shared_corn_rm_table_path(self.year)

    @property
    def soybean_mg_path(self) -> Path:
        return _paths_module().shared_soybean_mg_table_path(self.year)


def build_year_output_index(config: AnnualMaturityConfig) -> dict[str, str]:
    return {
        "geoadmin_root": str(config.geoadmin_root),
        "corn_gdd": str(config.corn_gdd_path),
        "corn_rm": str(config.corn_rm_path),
        "soybean_mg": str(config.soybean_mg_path),
    }
