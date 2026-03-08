#!/usr/bin/env python3
"""Download and summarize CDL crop composition for Iowa fields."""

import os
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_SCRIPTS_DIR))

from reporting_bootstrap import ensure_skill_path

ensure_skill_path("cdl-cropland")

from cdl_reporting import extract_crop_composition, summarize_crop_history


def download_cdl(year, state_fips="19"):
    """Download CDL raster for given year."""
    cdl_path = Path(f"data/cdl/CDL_{year}_{state_fips}.tif")

    if not cdl_path.exists():
        print(f"  Downloading CDL {year}...")
        cdl_path.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://nassgeodata.gmu.edu/nass_data_cache/byfips/CDL_{year}_{state_fips}.tif"

        resp = requests.get(url, timeout=120)
        resp.raise_for_status()

        with open(cdl_path, "wb") as f:
            f.write(resp.content)
        print(f"  Downloaded CDL {year}")

    return cdl_path


def main():
    print("=" * 60)
    print("Step 4: Download CDL Crop Type Data")
    print("=" * 60)

    os.makedirs("data/cdl", exist_ok=True)

    fields = gpd.read_file("data/field-boundaries/iowa_10_fields.geojson")
    print(f"Loaded {len(fields)} fields")

    # Download and process 2023
    print("\n--- 2023 CDL ---")
    cdl_2023_path = download_cdl(2023)
    cdl_2023 = extract_crop_composition(fields, cdl_2023_path, year=2023)
    cdl_2023.to_csv("data/cdl/iowa_2023_cdl.csv", index=False)
    print(f"  Saved: data/cdl/iowa_2023_cdl.csv")

    # Download and process 2024
    print("\n--- 2024 CDL ---")
    cdl_2024_path = download_cdl(2024)
    cdl_2024 = extract_crop_composition(fields, cdl_2024_path, year=2024)
    cdl_2024.to_csv("data/cdl/iowa_2024_cdl.csv", index=False)
    print(f"  Saved: data/cdl/iowa_2024_cdl.csv")

    # Create rotation analysis
    print("\n--- Crop Rotation ---")
    crop_mix = pd.concat([cdl_2023, cdl_2024], ignore_index=True)
    rotation = summarize_crop_history(crop_mix)
    rotation.to_csv("data/cdl/iowa_crop_rotation.csv", index=False)
    print(f"  Saved: data/cdl/iowa_crop_rotation.csv")
    crop_mix.to_csv("data/cdl/iowa_cdl_2023_2024_full_composition.csv", index=False)
    print("  Saved: data/cdl/iowa_cdl_2023_2024_full_composition.csv")

    print(f"\n✓ CDL analysis complete")
    print(
        f"  2023 crops: {cdl_2023.sort_values('pct', ascending=False).groupby('field_id').first()['crop_name'].value_counts().to_dict()}"
    )
    print(
        f"  2024 crops: {cdl_2024.sort_values('pct', ascending=False).groupby('field_id').first()['crop_name'].value_counts().to_dict()}"
    )

    return cdl_2023, cdl_2024, rotation


if __name__ == "__main__":
    main()
