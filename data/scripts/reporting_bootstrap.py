"""Helpers for loading local skill modules and canonical data-tree scaffolding."""

from __future__ import annotations

import os
import sys
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data"
DEFAULT_GROWER = os.environ.get("AG_GROWER_SLUG", "iowa-demo-grower")
DEFAULT_FARM = os.environ.get("AG_FARM_SLUG", "iowa-demo-farm")


def ensure_skill_path(skill_name: str) -> Path:
    skill_path = REPO_ROOT / ".opencode" / "skills" / skill_name / "src"
    resolved = str(skill_path)
    if resolved not in sys.path:
        sys.path.insert(0, resolved)
    return skill_path


def farm_root(grower_slug: str = DEFAULT_GROWER, farm_slug: str = DEFAULT_FARM) -> Path:
    return DATA_ROOT / "growers" / grower_slug / "farms" / farm_slug


def fields_root(grower_slug: str = DEFAULT_GROWER, farm_slug: str = DEFAULT_FARM) -> Path:
    return farm_root(grower_slug, farm_slug) / "fields"


def field_slugs_from_inventory(inventory_path: Path | None = None) -> list[str]:
    inventory = inventory_path or (
        REPO_ROOT / ".sisyphus" / "evidence" / "task-3-field-inventory.csv"
    )
    if not inventory.exists():
        return []
    rows = inventory.read_text(encoding="utf-8").splitlines()
    slugs: list[str] = []
    for line in rows[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != 2:
            continue
        slugs.append(parts[1].strip())
    return slugs


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def ensure_canonical_field_artifacts(
    field_slug: str, grower_slug: str = DEFAULT_GROWER, farm_slug: str = DEFAULT_FARM
) -> None:
    base = fields_root(grower_slug, farm_slug) / field_slug
    for rel in (
        "boundary",
        "soil",
        "weather",
        "satellite/landsat",
        "satellite/sentinel",
        "derived/tables",
        "derived/features",
        "derived/summaries",
        "logs",
    ):
        (base / rel).mkdir(parents=True, exist_ok=True)

    field_geojson = {
        "type": "FeatureCollection",
        "features": [],
    }
    _write_json(
        base / "field.json",
        {
            "grower_slug": grower_slug,
            "farm_slug": farm_slug,
            "field_slug": field_slug,
            "display_name": field_slug,
            "field_id": field_slug.replace("-", "_").upper(),
            "boundary_file": "boundary/field_boundary.geojson",
            "soil_file": "soil/ssurgo_soil_types.geojson",
            "weather_file": "weather/daily_weather.csv",
            "satellite_dir": "satellite/",
            "notes": "Canonical field metadata",
        },
    )
    _write_json(base / "boundary" / "field_boundary.geojson", field_geojson)
    _write_json(base / "soil" / "ssurgo_soil_types.geojson", field_geojson)
    _write_text(
        base / "weather" / "daily_weather.csv",
        "field_id,date,T2M,T2M_MAX,T2M_MIN,PRECTOTCORR,ALLSKY_SFC_SW_DWN,RH2M,WS10M\n",
    )

    _write_json(
        base / "soil" / "metadata.json",
        {
            "dataset_name": "ssurgo_soil_types",
            "source": "usda-sda",
            "spatial_scope": "field",
            "grower_slug": grower_slug,
            "farm_slug": farm_slug,
            "field_slug": field_slug,
            "format": "geojson",
            "crs": "EPSG:4326",
        },
    )
    _write_json(
        base / "weather" / "metadata.json",
        {
            "dataset_name": "daily_weather",
            "source": "nasa-power",
            "spatial_scope": "field",
            "grower_slug": grower_slug,
            "farm_slug": farm_slug,
            "field_slug": field_slug,
            "format": "csv",
            "crs": "EPSG:4326",
        },
    )

    _write_json(
        base / "satellite" / "landsat" / "manifest.json",
        {
            "dataset_name": "landsat",
            "field_slug": field_slug,
            "years": [],
        },
    )
    _write_json(
        base / "satellite" / "sentinel" / "manifest.json",
        {
            "dataset_name": "sentinel",
            "field_slug": field_slug,
            "years": [],
        },
    )
    _write_text(base / "logs" / "pipeline_runs.jsonl", "")


def ensure_canonical_data_tree(
    grower_slug: str = DEFAULT_GROWER,
    farm_slug: str = DEFAULT_FARM,
    farm_name: str = "Iowa Demo Farm",
    inventory_path: Path | None = None,
) -> list[str]:
    (DATA_ROOT / "shared" / "cdl" / "metadata").mkdir(parents=True, exist_ok=True)
    (DATA_ROOT / "shared" / "cdl" / "rasters").mkdir(parents=True, exist_ok=True)
    (DATA_ROOT / "shared" / "reference" / "crop_codes").mkdir(parents=True, exist_ok=True)
    (DATA_ROOT / "shared" / "reference" / "units").mkdir(parents=True, exist_ok=True)
    (DATA_ROOT / "shared" / "reference" / "schemas").mkdir(parents=True, exist_ok=True)
    (DATA_ROOT / "shared" / "manifests").mkdir(parents=True, exist_ok=True)

    farm = farm_root(grower_slug, farm_slug)
    farm.mkdir(parents=True, exist_ok=True)
    _write_json(
        farm / "farm.json",
        {
            "grower_slug": grower_slug,
            "farm_slug": farm_slug,
            "display_name": farm_name,
            "state": "IA",
            "country": "US",
            "default_crs": "EPSG:4326",
            "notes": "Canonical farm metadata",
        },
    )

    slugs = field_slugs_from_inventory(inventory_path=inventory_path)
    if not slugs:
        root = fields_root(grower_slug, farm_slug)
        if root.exists():
            slugs = sorted([p.name for p in root.iterdir() if p.is_dir()])

    for slug in slugs:
        ensure_canonical_field_artifacts(slug, grower_slug, farm_slug)

    return slugs
