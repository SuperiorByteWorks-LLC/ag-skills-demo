#!/usr/bin/env python3
"""
03_download_weather.py - Download NASA POWER weather data for Iowa fields

Fetches daily weather data (temperature, precipitation, radiation, humidity, wind)
from NASA POWER API for 2023-2024.

Input:  data/field-boundaries/iowa_10_fields.geojson
Output: data/weather/iowa_10_fields_weather.csv
"""

import sys
import os
import geopandas as gpd
import pandas as pd
import requests

def main():
    print("=" * 60)
    print("Step 3: Download NASA POWER Weather Data")
    print("=" * 60)
    
    os.makedirs('data/weather', exist_ok=True)
    
    fields = gpd.read_file('data/field-boundaries/iowa_10_fields.geojson')
    fields['centroid'] = fields.geometry.centroid
    fields['lat'] = fields.centroid.y
    fields['lon'] = fields.centroid.x
    
    print(f"Loaded {len(fields)} fields")
    
    params = ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR", "ALLSKY_SFC_SW_DWN", "RH2M", "WS10M"]
    
    all_weather = []
    
    for idx, field in fields.iterrows():
        field_id = field['field_id']
        lat, lon = field['lat'], field['lon']
        
        print(f"Fetching {field_id[-6:]} @ ({lat:.4f}, {lon:.4f})...", end=" ")
        
        try:
            for year in [2023, 2024]:
                resp = requests.get(
                    "https://power.larc.nasa.gov/api/temporal/daily/point",
                    params={
                        "parameters": ",".join(params),
                        "community": "AG",
                        "longitude": lon,
                        "latitude": lat,
                        "start": f"{year}0101",
                        "end": f"{year}1231",
                        "format": "JSON",
                    },
                    timeout=60
                )
                resp.raise_for_status()
                data = resp.json()
                
                param_data = data["properties"]["parameter"]
                
                for date_str in param_data["T2M"].keys():
                    record = {
                        "field_id": field_id,
                        "lat": lat,
                        "lon": lon,
                        "date": pd.to_datetime(date_str, format="%Y%m%d"),
                        "T2M": param_data["T2M"][date_str],
                        "T2M_MAX": param_data["T2M_MAX"][date_str],
                        "T2M_MIN": param_data["T2M_MIN"][date_str],
                        "PRECTOTCORR": param_data["PRECTOTCORR"][date_str],
                        "ALLSKY_SFC_SW_DWN": param_data["ALLSKY_SFC_SW_DWN"][date_str],
                        "RH2M": param_data["RH2M"][date_str],
                        "WS10M": param_data["WS10M"][date_str],
                    }
                    all_weather.append(record)
            
            print("OK")
            
        except Exception as e:
            print(f"FAILED: {e}")
    
    weather_df = pd.DataFrame(all_weather)
    weather_df.to_csv('data/weather/iowa_10_fields_weather.csv', index=False)
    
    print(f"\n✓ Downloaded {len(weather_df)} daily weather records")
    print(f"  Date range: {weather_df['date'].min().date()} to {weather_df['date'].max().date()}")
    print(f"  Output: data/weather/iowa_10_fields_weather.csv")
    
    return weather_df

if __name__ == "__main__":
    main()
