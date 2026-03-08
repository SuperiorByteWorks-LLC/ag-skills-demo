from __future__ import annotations

from pathlib import Path


DATA_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_ROOT = DATA_ROOT / "scripts"
GROWERS_ROOT = DATA_ROOT / "growers"
SHARED_ROOT = DATA_ROOT / "shared"


def grower_dir(grower_slug: str) -> Path:
    return GROWERS_ROOT / grower_slug


def farm_dir(grower_slug: str, farm_slug: str) -> Path:
    return grower_dir(grower_slug) / "farms" / farm_slug


def farm_manifest_dir(grower_slug: str, farm_slug: str) -> Path:
    return farm_dir(grower_slug, farm_slug) / "manifests"


def farm_derived_dir(grower_slug: str, farm_slug: str) -> Path:
    return farm_dir(grower_slug, farm_slug) / "derived"


def farm_reports_dir(grower_slug: str, farm_slug: str) -> Path:
    return farm_derived_dir(grower_slug, farm_slug) / "reports"


def farm_summaries_dir(grower_slug: str, farm_slug: str) -> Path:
    return farm_derived_dir(grower_slug, farm_slug) / "summaries"


def farm_dashboards_dir(grower_slug: str, farm_slug: str) -> Path:
    return farm_derived_dir(grower_slug, farm_slug) / "dashboards"


def field_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return farm_dir(grower_slug, farm_slug) / "fields" / field_slug


def field_boundary_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_dir(grower_slug, farm_slug, field_slug) / "boundary"


def field_boundary_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_boundary_dir(grower_slug, farm_slug, field_slug) / "field_boundary.geojson"


def field_soil_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_dir(grower_slug, farm_slug, field_slug) / "soil"


def field_soil_polygon_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_soil_dir(grower_slug, farm_slug, field_slug) / "ssurgo_soil_types.geojson"


def field_soil_full_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_soil_dir(grower_slug, farm_slug, field_slug) / "ssurgo_full.csv"


def field_soil_summary_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_soil_dir(grower_slug, farm_slug, field_slug) / "ssurgo_summary.csv"


def field_weather_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_dir(grower_slug, farm_slug, field_slug) / "weather"


def field_weather_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_weather_dir(grower_slug, farm_slug, field_slug) / "daily_weather.csv"


def field_satellite_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_dir(grower_slug, farm_slug, field_slug) / "satellite"


def field_derived_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_dir(grower_slug, farm_slug, field_slug) / "derived"


def field_reports_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_derived_dir(grower_slug, farm_slug, field_slug) / "reports"


def field_summaries_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_derived_dir(grower_slug, farm_slug, field_slug) / "summaries"


def field_features_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_derived_dir(grower_slug, farm_slug, field_slug) / "features"


def field_tables_dir(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_derived_dir(grower_slug, farm_slug, field_slug) / "tables"


def field_logs_path(grower_slug: str, farm_slug: str, field_slug: str) -> Path:
    return field_dir(grower_slug, farm_slug, field_slug) / "logs" / "pipeline_runs.jsonl"


def shared_cdl_dir() -> Path:
    return SHARED_ROOT / "cdl"


def shared_cdl_raster_dir() -> Path:
    return shared_cdl_dir() / "rasters"


def shared_cdl_derived_dir() -> Path:
    return shared_cdl_dir() / "derived"


def shared_cdl_metadata_dir() -> Path:
    return shared_cdl_dir() / "metadata"


def shared_cdl_manifest_dir() -> Path:
    return shared_cdl_dir() / "manifests"


def shared_manifest_dir() -> Path:
    return SHARED_ROOT / "manifests"


def ensure_parent(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
