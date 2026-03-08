#!/usr/bin/env python3
"""
Aggregate Summary Poster

Creates a consolidated poster showing:
- Field locations
- Soil distribution
- Crop rotation patterns
- Weather/GDD comparisons
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    print("=" * 60)
    print("Creating Aggregate Summary Poster")
    print("=" * 60)
    
    # Load data
    fields = gpd.read_file('data/field-boundaries/iowa_10_fields.geojson')
    soil_summary = pd.read_csv('data/soil/iowa_ssurgo_summary.csv')
    weather = pd.read_csv('data/weather/iowa_weather_2021_2025.csv', parse_dates=['date'])
    cdl = pd.read_csv('data/cdl/iowa_cdl_2021_2024.csv')
    
    fields['centroid'] = fields.geometry.centroid
    
    fig = plt.figure(figsize=(24, 18))
    fig.suptitle('IOWA CORN BELT - AGGREGATE ANALYSIS SUMMARY', fontsize=20, fontweight='bold', y=0.98)
    
    gs = fig.add_gridspec(4, 4, hspace=0.35, wspace=0.3)
    
    # ========== Row 1: Locations + Soil Distribution ==========
    # Field locations map
    ax_map = fig.add_subplot(gs[0, :2])
    ax_map.scatter(fields.centroid.x, fields.centroid.y, s=fields['area_acres']*5, 
                   c='steelblue', alpha=0.7, edgecolor='black')
    for idx, row in fields.iterrows():
        ax_map.annotate(row['field_id'][-4:], (row.centroid.x, row.centroid.y), 
                       fontsize=8, ha='center')
    ax_map.set_title('Field Locations (size = acres)', fontsize=14, fontweight='bold')
    ax_map.set_xlabel('Longitude')
    ax_map.set_ylabel('Latitude')
    ax_map.grid(True, alpha=0.3)
    
    # Soil distribution
    ax_soil = fig.add_subplot(gs[0, 2:])
    soil_counts = soil_summary['dominant_soil'].value_counts()
    ax_soil.barh(soil_counts.index, soil_counts.values, color='brown', edgecolor='black')
    ax_soil.set_title('Soil Type Distribution', fontsize=14, fontweight='bold')
    ax_soil.set_xlabel('Count')
    
    # ========== Row 2: Field Sizes + Rotation Patterns ==========
    # Field sizes
    ax_sizes = fig.add_subplot(gs[1, :2])
    sorted_fields = fields.sort_values('area_acres', ascending=False)
    ax_sizes.barh(range(len(sorted_fields)), sorted_fields['area_acres'], color='steelblue', edgecolor='black')
    ax_sizes.set_yticks(range(len(sorted_fields)))
    ax_sizes.set_yticklabels([f[-6:] for f in sorted_fields['field_id']], fontsize=8)
    ax_sizes.set_title('Field Sizes (sorted)', fontsize=14, fontweight='bold')
    ax_sizes.set_xlabel('Acres')
    
    # Crop rotation matrix
    ax_rot = fig.add_subplot(gs[1, 2:])
    
    # Create rotation pairs
    cdl_sorted = cdl.sort_values(['field_id', 'year'])
    rotations = []
    for fid in cdl_sorted['field_id'].unique():
        field_crops = cdl_sorted[cdl_sorted['field_id'] == fid].sort_values('year')['crop_name'].tolist()
        for i in range(len(field_crops) - 1):
            rotations.append(f"{field_crops[i]} → {field_crops[i+1]}")
    
    rot_counts = pd.Series(rotations).value_counts()
    ax_rot.barh(rot_counts.index, rot_counts.values, color='purple', edgecolor='black')
    ax_rot.set_title('Crop Rotation Patterns (2021-2024)', fontsize=14, fontweight='bold')
    ax_rot.set_xlabel('Count')
    
    # ========== Row 3: GDD + Weather by Field ==========
    # GDD by field
    ax_gdd = fig.add_subplot(gs[2, :2])
    
    def calc_gdd(row):
        return max(0, (row['T2M_MAX'] + row['T2M_MIN']) / 2 - 10)
    
    weather['GDD'] = weather.apply(calc_gdd, axis=1)
    weather['month'] = weather['date'].dt.month
    gs_weather = weather[(weather['month'] >= 4) & (weather['month'] <= 10)]
    gdd_by_field = gs_weather.groupby('field_id')['GDD'].sum()
    
    ax_gdd.bar(range(len(gdd_by_field)), gdd_by_field.values, color='green', edgecolor='black')
    ax_gdd.set_xticks(range(len(gdd_by_field)))
    ax_gdd.set_xticklabels([f[-6:] for f in gdd_by_field.index], rotation=45, fontsize=8)
    ax_gdd.set_title('GDD by Field (Growing Season Average)', fontsize=14, fontweight='bold')
    ax_gdd.set_ylabel('GDD')
    
    # Weather by field
    ax_weather = fig.add_subplot(gs[2, 2:])
    weather_by_field = weather.groupby('field_id').agg({
        'T2M': 'mean',
        'PRECTOTCORR': 'sum'
    })
    weather_by_field = weather_by_field.loc[gdd_by_field.index]
    
    x = np.arange(len(weather_by_field))
    width = 0.35
    ax_weather.bar(x - width/2, weather_by_field['T2M'], width, label='Temp (°C x10)', color='red', alpha=0.7)
    ax_weather.bar(x + width/2, weather_by_field['PRECTOTCORR']/100, width, label='Precip (mm/100)', color='blue', alpha=0.7)
    ax_weather.set_xticks(x)
    ax_weather.set_xticklabels([f[-6:] for f in weather_by_field.index], rotation=45, fontsize=8)
    ax_weather.set_title('Weather by Field (5-Year Avg)', fontsize=14, fontweight='bold')
    ax_weather.legend()
    
    # ========== Row 4: CDL by Year + Summary ==========
    # CDL by year
    ax_cdl = fig.add_subplot(gs[3, :2])
    cdl_by_year = cdl.groupby(['year', 'crop_name']).size().unstack(fill_value=0)
    cdl_by_year.plot(kind='bar', ax=ax_cdl, width=0.8, edgecolor='black')
    ax_cdl.set_title('CDL Crop Types by Year', fontsize=14, fontweight='bold')
    ax_cdl.set_xlabel('Year')
    ax_cdl.set_ylabel('Count')
    ax_cdl.legend(title='Crop', fontsize=8)
    ax_cdl.tick_params(axis='x', rotation=0)
    
    # Overall summary
    ax_summary = fig.add_subplot(gs[3, 2:])
    ax_summary.axis('off')
    
    total_acres = fields['area_acres'].sum()
    avg_gdd = gdd_by_field.mean()
    avg_precip = weather_by_field['PRECTOTCORR'].mean()
    avg_temp = weather_by_field['T2M'].mean()
    
    summary_text = f"""
    ╔═══════════════════════════════════════════════╗
    ║           OVERALL SUMMARY                      ║
    ╠═══════════════════════════════════════════════╣
    ║  Fields: {len(fields)}                                   ║
    ║  Total Acres: {total_acres:.0f}                          ║
    ║  Years Analyzed: 2021-2025 (weather)              ║
    ║                  2021-2024 (CDL)                   ║
    ╠═══════════════════════════════════════════════╣
    ║  Weather (5-year avg):                         ║
    ║    Temperature: {avg_temp:.1f}°C                         ║
    ║    Precipitation: {avg_precip:.0f} mm/yr                  ║
    ║    GDD (growing season): {avg_gdd:.0f}                    ║
    ╠═══════════════════════════════════════════════╣
    ║  Soils:                                        ║
    ║    Dominant: {soil_summary['dominant_soil'].mode().iloc[0][:20]}           ║
    ║    Avg pH: {soil_summary['avg_ph'].mean():.1f}                             ║
    ║    Avg OM: {soil_summary['avg_om_pct'].mean():.1f}%                            ║
    ╚═══════════════════════════════════════════════╝
    """
    
    ax_summary.text(0.5, 0.5, summary_text, fontsize=10, family='monospace',
                   ha='center', va='center', transform=ax_summary.transAxes,
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.savefig('data/EDA/iowa_aggregate_summary.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("✓ Aggregate summary saved to data/EDA/iowa_aggregate_summary.png")

if __name__ == "__main__":
    main()
