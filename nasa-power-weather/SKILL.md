---
name: nasa-power-weather
description: Access NASA POWER meteorological data for agricultural fields. Use when the user needs weather data, temperature records, precipitation, solar radiation, or Growing Degree Days (GDD) for agricultural analysis, crop modeling, or irrigation planning.
---

# NASA POWER Weather Data

## Quick Start

Download daily weather for agricultural fields:

```python
from skills.nasa_power_weather import NASAPowerWeatherSkill

skill = NASAPowerWeatherSkill()
weather = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2023-01-01',
    end_date='2023-12-31',
    parameters=['T2M_MIN', 'T2M_MAX', 'PRECTOTCORR'],
    output_path='data/weather.csv'
)
```

## Data Source

**NASA POWER** (Prediction of Worldwide Energy Resources)

- Coverage: Global (0.5° grid resolution)
- Resolution: Daily, 0.5° x 0.5°
- Time Period: 1981-present
- Source: Satellite observations + reanalysis

## Key Parameters

| Parameter           | Description               | Units     |
| ------------------- | ------------------------- | --------- |
| `T2M_MIN`           | Daily minimum temperature | °C        |
| `T2M_MAX`           | Daily maximum temperature | °C        |
| `T2M`               | Daily mean temperature    | °C        |
| `PRECTOTCORR`       | Daily precipitation       | mm        |
| `ALLSKY_SFC_SW_DWN` | Solar radiation           | MJ/m²/day |
| `RH2M`              | Relative humidity         | %         |
| `WS10M`             | Wind speed at 10m         | m/s       |

## Usage

### download_for_fields

Download daily weather data for field centroids.

```python
weather = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2023-01-01',
    end_date='2023-12-31',
    parameters=['T2M_MIN', 'T2M_MAX', 'PRECTOTCORR'],
    output_path='data/weather.csv'
)
```

Parameters:

- `fields_geojson` (str): Path to GeoJSON file with field boundaries
- `start_date` (str): Start date 'YYYY-MM-DD'
- `end_date` (str): End date 'YYYY-MM-DD'
- `parameters` (list[str]): Weather parameters to retrieve
- `output_path` (str): Output CSV file path

Returns:

- DataFrame: Daily weather time series with field_id

### calculate_growing_degree_days

Calculate Growing Degree Days (GDD) for crop development.

```python
gdd = skill.calculate_growing_degree_days(
    weather,
    base_temp=10.0,  # °C
    max_temp=30.0   # Cap temperature
)
```

### plot_weather_timeseries

Plot weather time series for one or more fields.

```python
skill.plot_weather_timeseries(
    weather,
    field_id='field_001',
    parameters=['T2M_MIN', 'T2M_MAX'],
    save_path='data/weather_plot.png'
)
```

## Examples

### Example 1: Download and Calculate GDD

```python
from skills.nasa_power_weather import NASAPowerWeatherSkill

skill = NASAPowerWeatherSkill()

# Download 2023 weather data
weather = skill.download_for_fields(
    fields_geojson='data/my_fields_EPSG4326.geojson',
    start_date='2023-01-01',
    end_date='2023-12-31',
    parameters=['T2M_MIN', 'T2M_MAX', 'PRECTOTCORR'],
    output_path='data/weather_2023.csv'
)

# Calculate GDD for corn (base 10°C)
gdd = skill.calculate_growing_degree_days(weather, base_temp=10.0)

# Plot cumulative GDD for first field
field_id = gdd['field_id'].unique()[0]
field_gdd = gdd[gdd['field_id'] == field_id]

import matplotlib.pyplot as plt
plt.plot(field_gdd['date'], field_gdd['gdd_cumulative'])
plt.title(f'Cumulative GDD - {field_id}')
plt.xlabel('Date')
plt.ylabel('GDD (°C)')
plt.savefig('data/gdd_plot.png')
```

### Example 2: Seasonal Weather Analysis

```python
from skills.nasa_power_weather import NASAPowerWeatherSkill

skill = NASAPowerWeatherSkill()

# Download weather
weather = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2020-01-01',
    end_date='2023-12-31',
    parameters=['T2M_MIN', 'T2M_MAX', 'PRECTOTCORR', 'ALLSKY_SFC_SW_DWN'],
    output_path='data/weather_multi_year.csv'
)

# Get growing season summary
growing_summary = skill.get_seasonal_summary(weather, season='growing')
print(growing_summary.head())

# Calculate accumulated precipitation
weather_with_accum = skill.calculate_accumulated_precipitation(
    weather, window_days=30
)

# Plot temperature comparison
skill.plot_temperature_comparison(
    weather,
    save_path='data/temp_comparison.png'
)
```

## Output Files

- `weather.csv` - Daily weather time series
- Columns: field_id, date, T2M_MIN, T2M_MAX, PRECTOTCORR, etc.

## GDD Calculation

Formula: `GDD = ((Tmin + Tmax) / 2) - Tbase`

Capped at `max_temp` if specified.

## Notes

- Weather is queried at field centroids
- Data interpolated from 0.5° grid
- Missing days rare but possible
- GDD accumulation starts at planting date
- Precipitation accumulated over growing season

## Resources

- [NASA POWER API](https://power.larc.nasa.gov/api/)
- [NASA POWER Documentation](https://power.larc.nasa.gov/docs/)
- [Growing Degree Days](https://www.extension.umn.edu/agriculture/climate/growing-degree-days/)
