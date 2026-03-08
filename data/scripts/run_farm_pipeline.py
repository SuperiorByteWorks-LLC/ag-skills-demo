#!/usr/bin/env python3
"""
run_farm_pipeline.py — Master pipeline entrypoint.

Usage:
    python data/scripts/run_farm_pipeline.py \\
        --boundaries data/field-boundaries/iowa_10_fields.geojson \\
        [--farm-name "Iowa Demo Farm"] \\
        [--force]

Runs the full farm intelligence reporting pipeline from a single field
boundaries GeoJSON file.  Each step is idempotent and will be skipped if
inputs, code, and config are unchanged since the last run.

Outputs:
    data/EDA/field_cards/iowa_field_report_NN.png   — one per field
    data/EDA/iowa_farm_report.png                   — farm portfolio poster
    data/EDA/iowa_farm_report.html                  — self-contained HTML report
    data/reporting/manifests/                       — per-step manifests
"""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import sys
import time
from pathlib import Path

from reporting_bootstrap import ensure_canonical_data_tree

_REPO = Path(__file__).resolve().parents[2]
_SCRIPTS = Path(__file__).parent


def _field_slug_map(inventory_path: Path) -> list[tuple[str, str]]:
    inventory = inventory_path
    pairs: list[tuple[str, str]] = []
    if not inventory.exists():
        return pairs
    with inventory.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            fid = str(row.get("field_id", "")).strip()
            slug = str(row.get("field_slug", "")).strip()
            if fid and slug:
                pairs.append((fid, slug))
    return pairs


def _sync_outputs_to_canonical(
    grower_slug: str = "iowa-demo-grower",
    farm_slug: str = "iowa-demo-farm",
    boundaries_path: Path = Path("data/field-boundaries/iowa_10_fields.geojson"),
    weather_path: Path = Path("data/weather/iowa_weather_2021_2025.csv"),
    inventory_path: Path = Path(".sisyphus/evidence/task-3-field-inventory.csv"),
) -> None:
    import geopandas as gpd
    import pandas as pd

    pairs = _field_slug_map(_REPO / inventory_path)
    if not pairs:
        return

    farm_root = _REPO / "data" / "growers" / grower_slug / "farms" / farm_slug
    fields_root = farm_root / "fields"
    farm_summaries = farm_root / "derived" / "summaries"
    farm_soil_cards = farm_summaries / "soil_cards"
    farm_soil_maps = farm_summaries / "soil_maps"
    farm_summaries.mkdir(parents=True, exist_ok=True)
    farm_soil_cards.mkdir(parents=True, exist_ok=True)
    farm_soil_maps.mkdir(parents=True, exist_ok=True)

    legacy_eda = _REPO / "data" / "EDA"
    for name in ("iowa_farm_report.png", "iowa_farm_report.html", "iowa_farm_report.md"):
        src = legacy_eda / name
        if src.exists():
            shutil.copy2(src, farm_summaries / name)

    farm_compare = legacy_eda / "soil_cards" / "farm_comparison.png"
    if farm_compare.exists():
        shutil.copy2(farm_compare, farm_soil_cards / "farm_comparison.png")

    legacy_soil_map_dir = legacy_eda / "soil_maps"
    if legacy_soil_map_dir.exists():
        for soil_map_file in sorted(legacy_soil_map_dir.glob("field_*_map.png")):
            shutil.copy2(soil_map_file, farm_soil_maps / soil_map_file.name)

    resolved_boundaries = _REPO / boundaries_path
    resolved_weather = _REPO / weather_path
    boundaries = gpd.read_file(resolved_boundaries) if resolved_boundaries.exists() else None
    weather = (
        pd.read_csv(resolved_weather, parse_dates=["date"]) if resolved_weather.exists() else None
    )

    for idx, (field_id, slug) in enumerate(pairs, start=1):
        field_root = fields_root / slug
        (field_root / "derived" / "summaries").mkdir(parents=True, exist_ok=True)

        poster_src = legacy_eda / "field_cards" / f"iowa_field_report_{idx:02d}.png"
        if poster_src.exists():
            shutil.copy2(poster_src, field_root / "derived" / "summaries" / "field_report.png")

        soil_props = legacy_eda / "soil_cards" / f"field_{idx:02d}_properties.png"
        if soil_props.exists():
            shutil.copy2(soil_props, field_root / "derived" / "summaries" / "soil_properties.png")
        soil_texture = legacy_eda / "soil_cards" / f"field_{idx:02d}_texture.png"
        if soil_texture.exists():
            shutil.copy2(soil_texture, field_root / "derived" / "summaries" / "soil_texture.png")
        feature_map_names = {
            "component_map": "soil_component_map.png",
            "organic_matter_map": "soil_organic_matter_map.png",
            "ph_map": "soil_ph_map.png",
            "awc_map": "soil_awc_map.png",
            "clay_map": "soil_clay_map.png",
            "sand_map": "soil_sand_map.png",
            "cec_map": "soil_cec_map.png",
        }
        for source_slug, target_name in feature_map_names.items():
            source_path = legacy_eda / "soil_maps" / f"field_{idx:02d}_{source_slug}.png"
            if source_path.exists():
                shutil.copy2(source_path, field_root / "derived" / "features" / target_name)

        om_summary_map = legacy_eda / "soil_maps" / f"field_{idx:02d}_organic_matter_map.png"
        if om_summary_map.exists():
            shutil.copy2(om_summary_map, field_root / "derived" / "summaries" / "soil_map.png")

        if boundaries is not None:
            match = boundaries[boundaries["field_id"] == field_id]
            if not match.empty:
                match.to_file(field_root / "boundary" / "field_boundary.geojson", driver="GeoJSON")

        cache_src = _REPO / "data" / "soil" / "cache" / f"{field_id}_polygons.geojson"
        if cache_src.exists():
            shutil.copy2(cache_src, field_root / "soil" / "ssurgo_soil_types.geojson")

        if weather is not None and "field_id" in weather.columns:
            field_weather = weather[weather["field_id"] == field_id].copy()
            if not field_weather.empty:
                field_weather.to_csv(field_root / "weather" / "daily_weather.csv", index=False)


def _run(script: str, extra_env: dict | None = None) -> bool:
    cmd = [sys.executable, str(_SCRIPTS / script)]
    t0 = time.monotonic()
    result = subprocess.run(cmd, cwd=str(_REPO), capture_output=False)
    elapsed = time.monotonic() - t0
    status = "ok" if result.returncode == 0 else "FAILED"
    print(f"  {status}  ({elapsed:.1f}s)  {script}")
    return result.returncode == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Farm intelligence reporting pipeline")
    parser.add_argument(
        "--boundaries",
        default="data/field-boundaries/iowa_10_fields.geojson",
        help="Path to field boundaries GeoJSON",
    )
    parser.add_argument("--farm-name", default="Iowa Demo Farm")
    parser.add_argument("--grower-slug", default="iowa-demo-grower")
    parser.add_argument("--farm-slug", default="iowa-demo-farm")
    parser.add_argument(
        "--inventory-csv",
        default=".sisyphus/evidence/task-3-field-inventory.csv",
        help="Path to field inventory CSV with field_id,field_slug",
    )
    parser.add_argument(
        "--weather-csv",
        default="data/weather/iowa_weather_2021_2025.csv",
        help="Weather CSV path used for canonical field sync",
    )
    parser.add_argument("--force", action="store_true", help="Force rerun all steps")
    parser.add_argument(
        "--structure-test",
        action="store_true",
        help="Create and verify canonical data tree, then exit",
    )
    args = parser.parse_args()

    field_slugs = ensure_canonical_data_tree(
        grower_slug=args.grower_slug,
        farm_slug=args.farm_slug,
        farm_name=args.farm_name,
        inventory_path=_REPO / args.inventory_csv,
    )
    if field_slugs:
        print(f"Canonical tree ensured for {len(field_slugs)} fields")
    else:
        print("Canonical tree ensured (no field inventory found)")

    if args.structure_test:
        print("Structure test complete.")
        return

    boundaries = Path(args.boundaries)
    if not boundaries.exists():
        print(f"ERROR: field boundaries not found: {boundaries}")
        sys.exit(1)

    print()
    print("=" * 60)
    print(f"  Farm Intelligence Reporting Pipeline")
    print(f"  Farm: {args.farm_name}")
    print(f"  Boundaries: {boundaries}")
    print("=" * 60)

    steps = [
        ("reporting/generate_field_posters.py", "Field posters"),
        ("reporting/generate_aggregate_poster.py", "Farm portfolio poster"),
        ("reporting/generate_ssurgo_cards.py", "SSURGO soil profile cards"),
        ("reporting/generate_ssurgo_maps.py", "SSURGO soil maps with basemap"),
        ("reporting/generate_farm_html.py", "Self-contained HTML report"),
        ("reporting/generate_farm_markdown.py", "Markdown report"),
    ]

    all_ok = True
    for script, label in steps:
        print(f"\n[{label}]")
        ok = _run(script)
        if not ok:
            all_ok = False
            print(f"  Pipeline halted at: {script}")
            print("  Fix the error above and rerun.")
            sys.exit(1)

    print()
    print("=" * 60)
    if all_ok:
        _sync_outputs_to_canonical(
            grower_slug=args.grower_slug,
            farm_slug=args.farm_slug,
            boundaries_path=Path(args.boundaries),
            weather_path=Path(args.weather_csv),
            inventory_path=Path(args.inventory_csv),
        )
        print("  Pipeline complete.")
        print()
        print("  Outputs:")
        output_dir = _REPO / "data" / "EDA"
        for f in sorted(output_dir.glob("iowa_farm_report.*")):
            print(f"    {f.relative_to(_REPO)}")
        card_dir = output_dir / "field_cards"
        if card_dir.exists():
            cards = sorted(card_dir.glob("*.png"))
            print(f"    {card_dir.relative_to(_REPO)}/  ({len(cards)} field posters)")
        soil_dir = output_dir / "soil_cards"
        if soil_dir.exists():
            soil_cards = sorted(soil_dir.glob("*.png"))
            print(f"    {soil_dir.relative_to(_REPO)}/  ({len(soil_cards)} soil profile cards)")
        soil_map_dir = output_dir / "soil_maps"
        if soil_map_dir.exists():
            soil_maps = sorted(soil_map_dir.glob("*.png"))
            print(
                f"    {soil_map_dir.relative_to(_REPO)}/  ({len(soil_maps)} soil maps with basemap)"
            )
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
