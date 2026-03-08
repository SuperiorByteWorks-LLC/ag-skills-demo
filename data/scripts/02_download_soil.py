#!/usr/bin/env python3
"""
02_download_soil.py - Download SSURGO soil data for Iowa fields

Queries the NRCS Soil Data Access API for soil properties at each field location.

Input:  data/field-boundaries/iowa_10_fields.geojson
Output: data/soil/iowa_10_fields_soil.csv
"""

import sys
import os
import geopandas as gpd
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.opencode/skills/ssurgo-soil/src'))

from ssurgo_soil import download_soil, get_dominant_soil

def main():
    print("=" * 60)
    print("Step 2: Download SSURGO Soil Data")
    print("=" * 60)
    
    os.makedirs('data/soil', exist_ok=True)
    
    fields = gpd.read_file('data/field-boundaries/iowa_10_fields.geojson')
    print(f"Loaded {len(fields)} fields")
    
    soil_data = download_soil(
        fields,
        field_id_column='field_id',
        max_depth_cm=30,
        output_path='data/soil/iowa_10_fields_soil.csv'
    )
    
    print(f"\n✓ Downloaded {len(soil_data)} soil records for {soil_data['field_id'].nunique()} fields")
    print(f"  Output: data/soil/iowa_10_fields_soil.csv")
    
    return soil_data

if __name__ == "__main__":
    main()
