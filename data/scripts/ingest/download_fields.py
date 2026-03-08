#!/usr/bin/env python3
"""
01_download_fields.py - Download Iowa corn belt field boundaries

Downloads 10 agricultural field polygons from OpenStreetMap via Overpass API.
These serve as the basis for all subsequent analysis.

Input:  None (uses Overpass API)
Output: data/field-boundaries/iowa_10_fields.geojson
"""

import sys
import os
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_SCRIPTS_DIR))

from reporting_bootstrap import ensure_skill_path

ensure_skill_path("field-boundaries")

from field_boundaries import download_fields


def main():
    print("=" * 60)
    print("Step 1: Download Iowa Field Boundaries")
    print("=" * 60)

    os.makedirs("data/field-boundaries", exist_ok=True)

    fields = download_fields(
        count=10, regions=["corn_belt"], output_path="data/field-boundaries/iowa_10_fields.geojson"
    )

    print(f"\n✓ Downloaded {len(fields)} fields")
    print(f"  Total area: {fields['area_acres'].sum():.1f} acres")
    print(f"  Output: data/field-boundaries/iowa_10_fields.geojson")

    return fields


if __name__ == "__main__":
    main()
