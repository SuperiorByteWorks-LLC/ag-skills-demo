#!/usr/bin/env python3
"""Generate Illinois fields and run SSURGO vector visualization workflow - simplified."""

import json
import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent
sys.path.insert(0, str(project_root / ".opencode/skills/ssurgo-soil/src"))

import geopandas as gpd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

from ssurgo_soil import download_soil
from ssurgo_workflows import prepare_ssurgo_field_package, render_complete_workflow_figure, render_ssurgo_property_map

ILLINOIS_LOCATIONS = [
    {"lat": 40.6331, "lon": -89.3985, "name": "central"},
    {"lat": 40.1163, "lon": -88.2073, "name": "urbana"},
    {"lat": 40.4406, "lon": -88.9937, "name": "champaign"},
]

def generate_irregular_field(center_lon: float, center_lat: float, size_acres: float = 5.0, seed: int = 42) -> dict:
    import random
    import numpy as np
    from shapely.geometry import Polygon
    random.seed(seed)
    np.random.seed(seed)
    acres_to_sqm = 4046.86
    side_m = (size_acres * acres_to_sqm) ** 0.5
    half_deg = (side_m / 2) * 0.00001
    num_points = random.randint(6, 10)
    angles = sorted(np.random.uniform(0, 2 * 3.14159, num_points))
    radii = []
    for i, a in enumerate(angles):
        r = half_deg * random.uniform(0.7, 1.3)
        if i % 3 == 0:
            r *= random.uniform(0.85, 0.95)
        radii.append(r)
    coords = []
    for a, r in zip(angles, radii):
        x = center_lon + r * 1.0
        y = center_lat + r * 0.85
        coords.append((x, y))
    coords.append(coords[0])
    geom = Polygon(coords)
    return geom.__geo_interface__

def main():
    output_dir = Path("data/ssurgo-vector-viz")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    fields = []
    field_id = 1
    
    for center in ILLINOIS_LOCATIONS:
        for i in range(2):
            seed = field_id * 100
            geom = generate_irregular_field(
                center["lon"] + (i * 0.015),
                center["lat"] + (i * 0.01),
                size_acres=5.0 + field_id,
                seed=seed
            )
            fields.append({
                "type": "Feature",
                "properties": {
                    "field_id": f"IL_{field_id:03d}",
                    "state": "IL",
                    "region": center["name"],
                    "area_est_acres": 5.0 + field_id
                },
                "geometry": geom
            })
            field_id += 1
    
    geojson = {
        "type": "FeatureCollection",
        "features": fields
    }
    
    fields_path = output_dir / "illinois_6_fields.geojson"
    with open(fields_path, "w") as f:
        json.dump(geojson, f, indent=2)
    print(f"Generated {len(fields)} fields -> {fields_path}")
    
    gdf = gpd.read_file(fields_path)
    print(f"Loaded {len(gdf)} fields, CRS: {gdf.crs}")
    
    print("\n--- Downloading SSURGO soil data ---")
    soil = download_soil(gdf, field_id_column="field_id", max_depth_cm=30)
    soil_csv = output_dir / "soil_data_6_fields.csv"
    soil.to_csv(soil_csv, index=False)
    print(f"Downloaded {len(soil)} soil records")
    
    if soil.empty:
        print("No soil data retrieved - API may be slow or unavailable")
        return
    
    for idx, row in gdf.iterrows():
        fid = row["field_id"]
        print(f"\n--- Processing {fid} ---")
        
        field_single = gdf[gdf["field_id"] == fid].copy()
        field_soil = soil[soil["field_id"] == fid].copy()
        
        if field_soil.empty:
            print(f"  No soil data")
            continue
        
        dissolved, detail, agg = prepare_ssurgo_field_package(
            field_single,
            field_id_column="field_id",
            max_depth_cm=30
        )
        
        if dissolved.empty:
            print(f"  No SSURGO polygons")
            continue
        
        output_png = output_dir / f"ssurgo_workflow_{fid}.png"
        render_complete_workflow_figure(
            field_single,
            dissolved,
            detail,
            output_png
        )
        print(f"  Saved -> {output_png.name}")
        
        for prop in ["om_r", "ph1to1h2o_r"]:
            if prop in dissolved.columns:
                prop_png = output_dir / f"ssurgo_{prop}_{fid}.png"
                try:
                    render_ssurgo_property_map(field_single, dissolved, prop, prop_png)
                    print(f"  {prop} -> {prop_png.name}")
                except Exception as e:
                    print(f"  {prop} failed: {e}")
    
    print(f"\n=== Complete ===")

if __name__ == "__main__":
    main()
