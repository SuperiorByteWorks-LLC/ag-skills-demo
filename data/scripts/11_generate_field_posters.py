#!/usr/bin/env python3
"""
Comprehensive Field Poster Generator

Creates detailed poster cards for each field showing:
- Full SSURGO breakdown (all horizons)
- 5-year weather stacked
- 4-year CDL history
- GDD accumulation by year
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

def main():
    print("=" * 60)
    print("Creating Comprehensive Field Posters")
    print("=" * 60)
    
    # Load all data
    fields = gpd.read_file('data/field-boundaries/iowa_10_fields.geojson')
    soil_full = pd.read_csv('data/soil/iowa_full_ssurgo.csv')
    soil_summary = pd.read_csv('data/soil/iowa_ssurgo_summary.csv')
    weather = pd.read_csv('data/weather/iowa_weather_2021_2025.csv', parse_dates=['date'])
    cdl = pd.read_csv('data/cdl/iowa_cdl_2021_2024.csv')
    
    fields['centroid'] = fields.geometry.centroid
    fields['lon'] = fields.centroid.x
    fields['lat'] = fields.centroid.y
    
    Path('data/EDA/field_cards').mkdir(parents=True, exist_ok=True)
    
    # Create poster for each field
    for idx, field in fields.iterrows():
        field_id = field['field_id']
        print(f"Creating poster for {field_id}...")
        
        field_soil = soil_full[soil_full['field_id'] == field_id]
        field_weather = weather[weather['field_id'] == field_id]
        field_cdl = cdl[cdl['field_id'] == field_id]
        field_summary = soil_summary[soil_summary['field_id'] == field_id].iloc[0]
        
        fig = plt.figure(figsize=(20, 16))
        fig.suptitle(f'Field Analysis: {field_id[-6:]} | {field["area_acres"]:.1f} acres | Iowa Corn Belt', 
                     fontsize=18, fontweight='bold', y=0.98)
        
        gs = fig.add_gridspec(4, 4, hspace=0.35, wspace=0.3)
        
        # ========== Row 1: Field Info + SSURGO Profile ==========
        # Field info
        ax_info = fig.add_subplot(gs[0, :2])
        ax_info.axis('off')
        info_text = f"""
        FIELD: {field_id}
        Area: {field['area_acres']:.1f} acres
        Location: ({field['lat']:.4f}, {field['lon']:.4f})
        OSM Land Use: {field.get('crop_name', 'N/A')}
        """
        ax_info.text(0.1, 0.5, info_text, fontsize=12, va='center',
                    bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
        
        # SSURGO Components
        ax_ssurgo = fig.add_subplot(gs[0, 2:])
        ax_ssurgo.axis('off')
        ax_ssurgo.set_title('SSURGO Profile', fontsize=12, fontweight='bold', loc='left')
        
        components = field_soil.groupby('compname').first().reset_index()
        comp_text = f"Dominant: {field_summary['dominant_soil']}\n"
        comp_text += f"Components: {field_summary['n_components']}\n"
        comp_text += f"Horizons: {field_summary['n_horizons']}\n"
        comp_text += f"Avg OM: {field_summary['avg_om_pct']:.1f}%\n"
        comp_text += f"Avg pH: {field_summary['avg_ph']:.1f}\n"
        comp_text += f"CEC: {field_summary['avg_cec']} meq/100g\n"
        comp_text += f"Total AWS: {field_summary['total_aws_inches']:.1f} in\n"
        comp_text += f"Drainage: {field_summary['drainage_class']}\n"
        comp_text += f"Erosion Risk: {field_summary['erosion_risk']}"
        ax_ssurgo.text(0.05, 0.95, comp_text, fontsize=10, va='top', transform=ax_ssurgo.transAxes)
        
        # ========== Row 2: Weather 5-Year Stacked ==========
        # Temperature time series (stacked by year)
        ax_temp = fig.add_subplot(gs[1, :2])
        for year in sorted(field_weather['date'].dt.year.unique()):
            year_data = field_weather[field_weather['date'].dt.year == year].sort_values('date')
            ax_temp.plot(year_data['date'], year_data['T2M'], label=str(year), linewidth=1, alpha=0.7)
        ax_temp.set_title('Temperature (5-Year Stacked)', fontsize=12, fontweight='bold')
        ax_temp.set_ylabel('Temp (°C)')
        ax_temp.legend(loc='upper right', fontsize=8, ncol=5)
        ax_temp.grid(True, alpha=0.3)
        
        # Precipitation bars by year
        ax_precip = fig.add_subplot(gs[1, 2:])
        field_weather['month'] = field_weather['date'].dt.month
        monthly = field_weather.groupby([field_weather['date'].dt.year, 'month'])['PRECTOTCORR'].sum()
        
        years = sorted(field_weather['date'].dt.year.unique())
        months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
        x = np.arange(12)
        width = 0.15
        
        for i, year in enumerate(years):
            if year in monthly.index.get_level_values(0):
                year_monthly = monthly[year].reindex(range(1, 13), fill_value=0)
                ax_precip.bar(x + i*width - 2*width, year_monthly.values, width, label=str(year), alpha=0.8)
        
        ax_precip.set_xticks(x)
        ax_precip.set_xticklabels(months)
        ax_precip.set_title('Monthly Precipitation (5-Year Stacked)', fontsize=12, fontweight='bold')
        ax_precip.set_ylabel('mm')
        ax_precip.legend(loc='upper right', fontsize=8, ncol=5)
        ax_precip.grid(True, alpha=0.3, axis='y')
        
        # ========== Row 3: GDD + CDL History ==========
        # GDD accumulation by year
        ax_gdd = fig.add_subplot(gs[2, :2])
        
        def calc_gdd(row):
            return max(0, (row['T2M_MAX'] + row['T2M_MIN']) / 2 - 10)
        
        for year in years:
            year_data = field_weather[field_weather['date'].dt.year == year].copy()
            year_data['GDD'] = year_data.apply(calc_gdd, axis=1)
            year_data['GDD_cumsum'] = year_data['GDD'].cumsum()
            # Growing season (Apr-Oct)
            gs_data = year_data[(year_data['date'].dt.month >= 4) & (year_data['date'].dt.month <= 10)]
            ax_gdd.plot(gs_data['date'], gs_data['GDD_cumsum'], label=str(year), linewidth=2)
        
        ax_gdd.set_title('GDD Accumulation (Growing Season)', fontsize=12, fontweight='bold')
        ax_gdd.set_ylabel('GDD (base 10°C)')
        ax_gdd.legend(loc='upper left', fontsize=8, ncol=5)
        ax_gdd.grid(True, alpha=0.3)
        
        # CDL History
        ax_cdl = fig.add_subplot(gs[2, 2:])
        ax_cdl.axis('off')
        ax_cdl.set_title('CDL Crop History (2021-2024)', fontsize=12, fontweight='bold', loc='left')
        
        cdl_text = ""
        for _, row in field_cdl.sort_values('year').iterrows():
            cdl_text += f"{row['year']}: {row['crop_name']} ({row['dominant_pct']:.0f}%)\n"
        
        # Rotation pattern
        crops = field_cdl.sort_values('year')['crop_name'].tolist()
        if len(crops) >= 2:
            rotations = [f"{crops[i]} → {crops[i+1]}" for i in range(len(crops)-1)]
            cdl_text += f"\nRotations: {', '.join(set(rotations))}"
        
        ax_cdl.text(0.05, 0.95, cdl_text, fontsize=10, va='top', transform=ax_cdl.transAxes)
        
        # ========== Row 4: Soil Horizon Profile + Summary ==========
        # OM by depth
        ax_om = fig.add_subplot(gs[3, :2])
        
        horizons = field_soil.sort_values('hzdept_r')
        if not horizons.empty:
            depths = horizons['hzdept_r'].values
            om_vals = horizons['om_r'].values
            ax_om.barh(depths, om_vals, height=5, color='green', alpha=0.7, edgecolor='black')
            ax_om.set_xlabel('Organic Matter (%)')
            ax_om.set_ylabel('Depth (cm)')
            ax_om.set_title('OM Profile by Depth', fontsize=12, fontweight='bold')
            ax_om.invert_yaxis()
        
        # Summary stats
        ax_summary = fig.add_subplot(gs[3, 2:])
        ax_summary.axis('off')
        
        # Weather summary
        weather_summary = field_weather.groupby(field_weather['date'].dt.year).agg({
            'T2M': 'mean',
            'PRECTOTCORR': 'sum'
        })
        
        summary_text = "Weather Summary (Avg across years):\n"
        summary_text += f"  Temp: {weather_summary['T2M'].mean():.1f}°C\n"
        summary_text += f"  Precip: {weather_summary['PRECTOTCORR'].mean():.0f} mm/yr\n\n"
        
        # Soil constraints
        summary_text += "Soil Constraints:\n"
        if field_summary['ph_constraint']:
            summary_text += f"  pH: {field_summary['ph_constraint']}\n"
        if field_summary['erosion_risk']:
            summary_text += f"  Erosion: {field_summary['erosion_risk']}\n"
        
        ax_summary.text(0.05, 0.95, summary_text, fontsize=10, va='top', transform=ax_summary.transAxes)
        
        # Save
        card_num = idx + 1
        plt.savefig(f'data/EDA/field_cards/iowa_field_poster_{card_num:02d}.png', dpi=150, bbox_inches='tight')
        plt.close()
    
    print(f"\n✓ All {len(fields)} field posters saved to data/EDA/field_cards/")

if __name__ == "__main__":
    main()
