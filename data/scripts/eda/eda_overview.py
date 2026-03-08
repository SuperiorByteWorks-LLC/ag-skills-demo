#!/usr/bin/env python3
"""
05_eda_overview.py - Combined data overview

Creates an overview of all downloaded data and saves summary statistics.

Input:  All downloaded data (fields, soil, weather, CDL)
Output: data/EDA/iowa_field_summary.csv, summary stats
"""

import sys
import os
import geopandas as gpd
import pandas as pd

def main():
    print("=" * 60)
    print("Step 5: Data Overview")
    print("=" * 60)
    
    os.makedirs('data/EDA', exist_ok=True)
    
    # Load all data
    fields = gpd.read_file('data/field-boundaries/iowa_10_fields.geojson')
    soil = pd.read_csv('data/soil/iowa_10_fields_soil.csv')
    weather = pd.read_csv('data/weather/iowa_10_fields_weather.csv', parse_dates=['date'])
    cdl_2023 = pd.read_csv('data/cdl/iowa_2023_cdl.csv')
    cdl_2024 = pd.read_csv('data/cdl/iowa_2024_cdl.csv')
    
    print(f"\n=== Data Summary ===")
    print(f"Fields: {len(fields)} Iowa corn belt fields")
    print(f"  Total area: {fields['area_acres'].sum():.1f} acres")
    print(f"  Crops (OSM): {fields['crop_name'].value_counts().to_dict()}")
    
    print(f"\nSoil: {len(soil)} records for {soil['field_id'].nunique()} fields")
    print(f"  Dominant soil types: {soil.groupby('field_id').first()['muname'].to_dict()}")
    
    print(f"\nWeather: {len(weather)} daily records")
    print(f"  Date range: {weather['date'].min().date()} to {weather['date'].max().date()}")
    print(f"  Mean temp: {weather['T2M'].mean():.1f}C")
    print(f"  Total precip: {weather['PRECTOTCORR'].sum():.1f} mm")
    
    print(f"\nCDL 2023: {len(cdl_2023)} fields")
    print(f"  Crop types: {cdl_2023['crop_name'].value_counts().to_dict()}")
    
    # Create merged summary
    dominant_soil = soil.sort_values(['field_id', 'comppct_r'], ascending=[True, False]).groupby('field_id').first().reset_index()
    
    summary = fields.merge(dominant_soil[['field_id', 'muname', 'compname', 'om_r', 'ph1to1h2o_r', 'cec7_r', 'drainagecl']], on='field_id')
    summary = summary.merge(cdl_2023[['field_id', 'crop_name', 'dominant_pct']].rename(columns={'crop_name': 'cdl_2023', 'dominant_pct': 'cdl_2023_pct'}), on='field_id')
    summary = summary.merge(cdl_2024[['field_id', 'crop_name', 'dominant_pct']].rename(columns={'crop_name': 'cdl_2024', 'dominant_pct': 'cdl_2024_pct'}), on='field_id')
    
    summary.to_csv('data/EDA/iowa_field_summary.csv', index=False)
    print(f"\n✓ Saved: data/EDA/iowa_field_summary.csv")
    
    return summary

if __name__ == "__main__":
    main()
