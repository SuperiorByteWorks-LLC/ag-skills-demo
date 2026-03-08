#!/usr/bin/env python3
"""
04_download_cdl.py - Download CDL crop type data for Iowa fields

Downloads USDA NASS Cropland Data Layer rasters for 2023 and 2024,
extracts dominant crop type for each field, and calculates crop rotation.

Input:  data/field-boundaries/iowa_10_fields.geojson
Output: data/cdl/iowa_2023_cdl.csv, data/cdl/iowa_2024_cdl.csv
        data/cdl/iowa_crop_rotation.csv
"""

import sys
import os
import geopandas as gpd
import pandas as pd
import requests
import rasterio
from rasterstats import zonal_stats
from pathlib import Path

CDL_CODES = {
    1: "Corn", 5: "Soybeans", 24: "Winter Wheat", 28: "Alfalfa", 
    36: "Forest", 38: "Grassland", 43: "Open Water", 63: "Other", 0: "No Data"
}

def download_cdl(year, state_fips="19"):
    """Download CDL raster for given year."""
    cdl_path = Path(f"data/cdl/CDL_{year}_{state_fips}.tif")
    
    if not cdl_path.exists():
        print(f"  Downloading CDL {year}...")
        cdl_path.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://nassgeodata.gmu.edu/nass_data_cache/byfips/CDL_{year}_{state_fips}.tif"
        
        resp = requests.get(url, timeout=120)
        resp.raise_for_status()
        
        with open(cdl_path, 'wb') as f:
            f.write(resp.content)
        print(f"  Downloaded CDL {year}")
    
    return cdl_path

def extract_crops(fields, cdl_path):
    """Extract dominant crop for each field."""
    results = []
    
    for idx, field in fields.iterrows():
        field_id = field['field_id']
        geom = field.geometry
        
        try:
            with rasterio.open(cdl_path) as src:
                field_proj = gpd.GeoSeries([geom], crs=fields.crs).to_crs(src.crs)[0]
                stats = zonal_stats(field_proj, cdl_path, categorical=True)
                
                if stats:
                    cat_counts = stats[0]
                    total = sum(cat_counts.values())
                    dom_code = max(cat_counts, key=cat_counts.get)
                    dom_pct = cat_counts[dom_code] / total * 100
                    
                    results.append({
                        "field_id": field_id,
                        "crop_code": dom_code,
                        "crop_name": CDL_CODES.get(dom_code, f"Code_{dom_code}"),
                        "dominant_pct": round(dom_pct, 1),
                        "total_pixels": total
                    })
        except Exception as e:
            results.append({
                "field_id": field_id, "crop_code": None, 
                "crop_name": "Error", "dominant_pct": 0, "total_pixels": 0
            })
    
    return pd.DataFrame(results)

def main():
    print("=" * 60)
    print("Step 4: Download CDL Crop Type Data")
    print("=" * 60)
    
    os.makedirs('data/cdl', exist_ok=True)
    
    fields = gpd.read_file('data/field-boundaries/iowa_10_fields.geojson')
    print(f"Loaded {len(fields)} fields")
    
    # Download and process 2023
    print("\n--- 2023 CDL ---")
    cdl_2023_path = download_cdl(2023)
    cdl_2023 = extract_crops(fields, cdl_2023_path)
    cdl_2023['year'] = 2023
    cdl_2023.to_csv('data/cdl/iowa_2023_cdl.csv', index=False)
    print(f"  Saved: data/cdl/iowa_2023_cdl.csv")
    
    # Download and process 2024
    print("\n--- 2024 CDL ---")
    cdl_2024_path = download_cdl(2024)
    cdl_2024 = extract_crops(fields, cdl_2024_path)
    cdl_2024['year'] = 2024
    cdl_2024.to_csv('data/cdl/iowa_2024_cdl.csv', index=False)
    print(f"  Saved: data/cdl/iowa_2024_cdl.csv")
    
    # Create rotation analysis
    print("\n--- Crop Rotation ---")
    rotation = cdl_2023.merge(cdl_2024, on='field_id', suffixes=('_2023', '_2024'))
    rotation['rotation'] = rotation['crop_name_2023'] + ' → ' + rotation['crop_name_2024']
    rotation.to_csv('data/cdl/iowa_crop_rotation.csv', index=False)
    print(f"  Saved: data/cdl/iowa_crop_rotation.csv")
    
    print(f"\n✓ CDL analysis complete")
    print(f"  2023 crops: {cdl_2023['crop_name'].value_counts().to_dict()}")
    print(f"  2024 crops: {cdl_2024['crop_name'].value_counts().to_dict()}")
    
    return cdl_2023, cdl_2024, rotation

if __name__ == "__main__":
    main()
