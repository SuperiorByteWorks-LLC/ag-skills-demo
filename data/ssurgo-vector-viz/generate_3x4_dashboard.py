#!/usr/bin/env python3
"""Generate SSURGO 3x4 dashboard visualizations for Illinois fields."""

import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent
sys.path.insert(0, str(project_root / ".opencode/skills/ssurgo-soil/src"))

import geopandas as gpd
import matplotlib
matplotlib.use('Agg')
import pandas as pd

from ssurgo_soil import download_soil
from ssurgo_workflows import prepare_ssurgo_field_package, render_3x4_dashboard


def main():
    output_dir = Path("data/ssurgo-vector-viz")
    
    fields_path = output_dir / "illinois_10_fields.geojson"
    print(f"Loading fields from {fields_path}")
    gdf = gpd.read_file(fields_path)
    print(f"Loaded {len(gdf)} fields, CRS: {gdf.crs}")
    
    soil_csv = output_dir / "soil_data_10_fields.csv"
    if soil_csv.exists():
        print(f"Loading existing soil data from {soil_csv}")
        soil = pd.read_csv(soil_csv)
        print(f"Loaded {len(soil)} soil records")
    else:
        print("\n--- Downloading SSURGO soil data ---")
        soil = download_soil(gdf, field_id_column="field_id", max_depth_cm=30)
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
        
        output_png = output_dir / f"ssurgo_3x4_{fid}.png"
        render_3x4_dashboard(
            field_single,
            dissolved,
            detail,
            output_png,
            combine_width_m=9.0
        )
        print(f"  Saved -> {output_png.name}")
    
    print(f"\n=== Complete ===")

if __name__ == "__main__":
    main()
