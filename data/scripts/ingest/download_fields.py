#!/usr/bin/env python3
"""Download Iowa corn belt field boundaries into canonical grower paths."""

import os
import sys
from pathlib import Path

import geopandas as gpd

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_SCRIPTS_DIR))

from lib.paths import farm_boundary_path, field_boundary_path
from reporting_bootstrap import (
    ensure_canonical_data_tree,
    ensure_skill_path,
    field_slug_map_from_inventory,
)

ensure_skill_path("field-boundaries")

from field_boundaries import download_fields


def main():
    print("=" * 60)
    print("Step 1: Download Iowa Field Boundaries")
    print("=" * 60)

    grower_slug = os.environ.get("AG_GROWER_SLUG", "iowa-demo-grower")
    farm_slug = os.environ.get("AG_FARM_SLUG", "iowa-demo-farm")
    inventory_path = Path(".sisyphus/evidence/task-3-field-inventory.csv")
    ensure_canonical_data_tree(
        grower_slug=grower_slug, farm_slug=farm_slug, inventory_path=inventory_path
    )
    canonical_output = farm_boundary_path(grower_slug, farm_slug)
    canonical_output.parent.mkdir(parents=True, exist_ok=True)
    force = os.environ.get("AG_FORCE") == "1"

    if canonical_output.exists() and not force:
        fields = gpd.read_file(canonical_output)
        print(f"skip  boundary download (cached): {canonical_output}")
    else:
        try:
            fields = download_fields(
                count=10, regions=["corn_belt"], output_path=str(canonical_output)
            )
        except Exception as exc:
            if not canonical_output.exists():
                raise
            print(f"  Warning: live boundary download failed ({exc}); reusing {canonical_output}")
            fields = gpd.read_file(canonical_output)

    field_slug_map = field_slug_map_from_inventory(
        inventory_path if inventory_path.exists() else None
    )
    if field_slug_map:
        fields_gdf = gpd.read_file(canonical_output)
        for _, row in fields_gdf.iterrows():
            field_id = str(row.get("field_id", "")).strip()
            field_slug = field_slug_map.get(field_id)
            if not field_slug:
                continue
            single = gpd.GeoDataFrame([row], geometry="geometry", crs=fields_gdf.crs)
            target = field_boundary_path(grower_slug, farm_slug, field_slug)
            target.parent.mkdir(parents=True, exist_ok=True)
            single.to_file(target, driver="GeoJSON")

    print(f"\n✓ Downloaded {len(fields)} fields")
    print(f"  Total area: {fields['area_acres'].sum():.1f} acres")
    print(f"  Output: {canonical_output}")

    return fields


if __name__ == "__main__":
    main()
