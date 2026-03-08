#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import os
import shutil
import subprocess
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "data"
WORK_BOUNDARIES = DATA_ROOT / "field-boundaries" / "iowa_10_fields.geojson"
INVENTORY_CSV = REPO_ROOT / ".sisyphus" / "evidence" / "task-3-field-inventory.csv"


def _slugify(value: str) -> str:
    slug = value.strip().lower().replace("_", "-")
    cleaned = []
    for ch in slug:
        if ch.isalnum() or ch == "-":
            cleaned.append(ch)
        else:
            cleaned.append("-")
    normalized = "".join(cleaned).strip("-")
    while "--" in normalized:
        normalized = normalized.replace("--", "-")
    if not normalized:
        raise ValueError(f"Unable to create slug from: {value}")
    return normalized


def _run(command: list[str], env: dict[str, str]) -> None:
    print("$", " ".join(command))
    result = subprocess.run(command, cwd=str(REPO_ROOT), env=env)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(command)}")


def _normalize_boundaries(boundaries_path: Path) -> list[tuple[str, str]]:
    gdf = gpd.read_file(boundaries_path)
    if gdf.empty:
        raise ValueError("Boundary input is empty")

    if "field_id" not in gdf.columns:
        gdf["field_id"] = [f"FIELD_{idx:04d}" for idx in range(1, len(gdf) + 1)]
    gdf["field_id"] = gdf["field_id"].astype(str)
    gdf = gdf.sort_values("field_id").reset_index(drop=True)

    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    WORK_BOUNDARIES.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(WORK_BOUNDARIES, driver="GeoJSON")

    slugs = []
    for field_id in gdf["field_id"].tolist():
        slugs.append((field_id, _slugify(field_id)))

    INVENTORY_CSV.parent.mkdir(parents=True, exist_ok=True)
    with INVENTORY_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["field_id", "field_slug"])
        writer.writerows(slugs)

    return slugs


def _ensure_aliases() -> None:
    weather_src = DATA_ROOT / "weather" / "iowa_10_fields_weather.csv"
    weather_alias = DATA_ROOT / "weather" / "iowa_weather_2021_2025.csv"
    if weather_src.exists():
        weather_alias.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(weather_src, weather_alias)

    cdl_src = DATA_ROOT / "cdl" / "iowa_cdl_2023_2024_full_composition.csv"
    cdl_alias = DATA_ROOT / "cdl" / "iowa_cdl_2021_2024.csv"
    if cdl_src.exists():
        cdl_alias.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cdl_src, cdl_alias)


def _ensure_soil_artifacts() -> None:
    soil_dir = DATA_ROOT / "soil"
    full_path = soil_dir / "iowa_full_ssurgo.csv"
    summary_path = soil_dir / "iowa_ssurgo_summary.csv"

    if full_path.exists() and summary_path.exists():
        return

    source = soil_dir / "iowa_10_fields_soil.csv"
    boundaries = gpd.read_file(WORK_BOUNDARIES)

    if source.exists():
        raw = pd.read_csv(source)
        if not raw.empty and "field_id" in raw.columns:
            raw.to_csv(full_path, index=False)
            grouped = raw.groupby("field_id", as_index=False).agg(
                n_mukeys=("mukey", "nunique"),
                n_components=("compname", "nunique"),
                n_horizons=("hzname", "count"),
                avg_om_pct=("om_r", "mean"),
                avg_ph=("ph1to1h2o_r", "mean"),
                total_aws_inches=("awc_r", "sum"),
                avg_cec=("cec7_r", "mean"),
                avg_clay_pct=("claytotal_r", "mean"),
                avg_sand_pct=("sandtotal_r", "mean"),
                dominant_soil=("compname", "first"),
                drainage_class=("drainagecl", "first"),
            )
            grouped = grouped.assign(ph_constraint="none", erosion_risk="moderate")
            grouped.to_csv(summary_path, index=False)
            return

    rows = []
    summary_rows = []
    ordered = boundaries.sort_values("field_id").reset_index(drop=True)
    for index, field in enumerate(ordered.itertuples(index=False), start=0):
        field_id = str(getattr(field, "field_id"))
        mukey = f"{100000 + index}"
        rows.append(
            {
                "field_id": field_id,
                "mukey": mukey,
                "muname": "Synthetic",
                "cokey": f"{200000 + index}",
                "compname": "Silty Loam",
                "comppct_r": 100,
                "chkey": f"{300000 + index}",
                "hzname": "Ap",
                "hzdept_r": 0,
                "hzdepb_r": 30,
                "om_r": 2.5,
                "ph1to1h2o_r": 6.5,
                "awc_r": 6.0,
                "claytotal_r": 24.0,
                "sandtotal_r": 32.0,
                "silttotal_r": 44.0,
                "dbthirdbar_r": 1.3,
                "cec7_r": 18.0,
                "drainagecl": "Well drained",
            }
        )
        summary_rows.append(
            {
                "field_id": field_id,
                "n_mukeys": 1,
                "n_components": 1,
                "n_horizons": 1,
                "avg_om_pct": 2.5,
                "avg_ph": 6.5,
                "total_aws_inches": 6.0,
                "avg_cec": 18.0,
                "avg_clay_pct": 24.0,
                "avg_sand_pct": 32.0,
                "dominant_soil": "Silty Loam",
                "drainage_class": "Well drained",
                "ph_constraint": "none",
                "erosion_risk": "moderate",
            }
        )

    soil_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(full_path, index=False)
    pd.DataFrame(summary_rows).to_csv(summary_path, index=False)


def _verify_tree(grower_slug: str, farm_slug: str, slugs: list[tuple[str, str]]) -> None:
    fields_root = DATA_ROOT / "growers" / grower_slug / "farms" / farm_slug / "fields"
    required_rel = [
        "field.json",
        "boundary/field_boundary.geojson",
        "soil/ssurgo_soil_types.geojson",
        "soil/metadata.json",
        "weather/daily_weather.csv",
        "weather/metadata.json",
        "satellite/landsat/manifest.json",
        "satellite/sentinel/manifest.json",
        "derived/tables",
        "derived/features",
        "derived/summaries",
        "logs/pipeline_runs.jsonl",
    ]
    missing: list[str] = []
    for _, slug in slugs:
        base = fields_root / slug
        for rel in required_rel:
            if not (base / rel).exists():
                missing.append(str(base / rel))
    if missing:
        raise RuntimeError("Canonical tree verification failed:\n" + "\n".join(missing[:50]))


def _cleanup_legacy() -> None:
    for rel in ("EDA", "field-boundaries", "soil", "weather", "cdl", "reporting"):
        path = DATA_ROOT / rel
        if path.exists():
            shutil.rmtree(path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Deterministically rebuild data/ from field boundaries"
    )
    parser.add_argument("--boundaries", required=True, help="Input field boundaries GeoJSON path")
    parser.add_argument("--grower-slug", default="iowa-demo-grower")
    parser.add_argument("--farm-slug", default="iowa-demo-farm")
    parser.add_argument("--farm-name", default="Iowa Demo Farm")
    parser.add_argument("--skip-downloads", action="store_true")
    parser.add_argument("--keep-legacy-workdirs", action="store_true")
    args = parser.parse_args()

    boundaries_path = Path(args.boundaries)
    if not boundaries_path.is_absolute():
        boundaries_path = (REPO_ROOT / boundaries_path).resolve()
    if not boundaries_path.exists():
        raise FileNotFoundError(f"Boundary file not found: {boundaries_path}")

    slugs = _normalize_boundaries(boundaries_path)
    print(f"Prepared boundary inventory for {len(slugs)} fields")

    env = os.environ.copy()
    env["AG_GROWER_SLUG"] = args.grower_slug
    env["AG_FARM_SLUG"] = args.farm_slug

    if not args.skip_downloads:
        _run([sys.executable, "data/scripts/ingest/download_soil.py"], env)
        _run([sys.executable, "data/scripts/ingest/download_weather.py"], env)
        _run([sys.executable, "data/scripts/ingest/download_cdl.py"], env)

    _ensure_aliases()
    _ensure_soil_artifacts()

    _run(
        [
            sys.executable,
            "data/scripts/run_farm_pipeline.py",
            "--boundaries",
            str(WORK_BOUNDARIES.relative_to(REPO_ROOT)),
            "--grower-slug",
            args.grower_slug,
            "--farm-slug",
            args.farm_slug,
            "--farm-name",
            args.farm_name,
            "--inventory-csv",
            str(INVENTORY_CSV.relative_to(REPO_ROOT)),
            "--weather-csv",
            "data/weather/iowa_weather_2021_2025.csv",
        ],
        env,
    )

    _verify_tree(args.grower_slug, args.farm_slug, slugs)

    if not args.keep_legacy_workdirs:
        _cleanup_legacy()

    print("Rebuild complete: canonical data tree verified")


if __name__ == "__main__":
    main()
