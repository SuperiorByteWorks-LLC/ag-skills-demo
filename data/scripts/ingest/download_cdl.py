#!/usr/bin/env python3
"""Download and summarize CDL crop composition for Iowa fields."""

import os

import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests
from requests import HTTPError

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_SCRIPTS_DIR))
sys.path.insert(0, str(_SCRIPTS_DIR / "lib"))

from paths import (
    farm_boundary_path,
    ensure_parent,
    shared_cdl_full_composition_path,
    shared_cdl_raster_dir,
    shared_cdl_rotation_path,
    shared_cdl_year_table_path,
)
from reporting_bootstrap import ensure_skill_path

ensure_skill_path("cdl-cropland")

from cdl_reporting import extract_crop_composition, summarize_crop_history


def download_cdl(year, state_fips="19"):
    """Download CDL raster for given year."""
    cdl_path = shared_cdl_raster_dir() / f"CDL_{year}_{state_fips}.tif"

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


def _target_cdl_years(window_years: int = 5, latest_year: int = 2025) -> list[int]:
    years: list[int] = []
    candidate_year = latest_year
    while candidate_year >= max(2010, latest_year - window_years - 5):
        years.append(candidate_year)
        candidate_year -= 1
    return years


def main():
    print("=" * 60)
    print("Step 4: Download CDL Crop Type Data")
    print("=" * 60)

    grower_slug = os.environ.get("AG_GROWER_SLUG", "iowa-demo-grower")
    farm_slug = os.environ.get("AG_FARM_SLUG", "iowa-demo-farm")
    force = os.environ.get("AG_FORCE") == "1"
    fields = gpd.read_file(farm_boundary_path(grower_slug, farm_slug))
    print(f"Loaded {len(fields)} fields")

    target_years = _target_cdl_years(window_years=5, latest_year=2025)
    cached_years = [year for year in target_years if shared_cdl_year_table_path(year).exists()]
    if not force and len(cached_years) >= 5 and shared_cdl_rotation_path().exists():
        selected_years = sorted(cached_years[:5], reverse=True)
        composition_path = shared_cdl_full_composition_path(
            min(selected_years), max(selected_years)
        )
        if composition_path.exists():
            frames = [pd.read_csv(shared_cdl_year_table_path(year)) for year in selected_years]
            rotation = pd.read_csv(shared_cdl_rotation_path())
            print(
                "skip  CDL API fetch (cached years): "
                + ", ".join(str(year) for year in sorted(selected_years))
            )
            return (*frames, rotation)

    crop_mix_frames = []
    completed_years: list[int] = []
    for year in target_years:
        print(f"\n--- {year} CDL ---")
        try:
            cdl_year_path = download_cdl(year)
        except HTTPError as exc:
            response = getattr(exc, "response", None)
            if response is not None and response.status_code == 404:
                print(f"  Warning: CDL {year} is not available yet; skipping")
                continue
            raise
        cdl_year = extract_crop_composition(fields, cdl_year_path, year=year)
        year_output = ensure_parent(shared_cdl_year_table_path(year))
        cdl_year.to_csv(year_output, index=False)
        print(f"  Saved: {year_output}")
        crop_mix_frames.append(cdl_year)
        completed_years.append(year)
        if len(completed_years) >= 5:
            break

    if not crop_mix_frames:
        raise RuntimeError("No CDL years were available for download")

    # Create rotation analysis
    print("\n--- Crop Rotation ---")
    crop_mix = pd.concat(crop_mix_frames, ignore_index=True)
    rotation = summarize_crop_history(crop_mix)
    rotation_output = ensure_parent(shared_cdl_rotation_path())
    rotation.to_csv(rotation_output, index=False)
    print(f"  Saved: {rotation_output}")
    composition_output = ensure_parent(
        shared_cdl_full_composition_path(min(completed_years), max(completed_years))
    )
    crop_mix.to_csv(composition_output, index=False)
    print(f"  Saved: {composition_output}")

    print("\n✓ CDL analysis complete")
    for year, frame in zip(completed_years, crop_mix_frames):
        print(
            f"  {year} crops: {frame.sort_values('pct', ascending=False).groupby('field_id').first()['crop_name'].value_counts().to_dict()}"
        )

    return (*crop_mix_frames, rotation)


if __name__ == "__main__":
    main()
