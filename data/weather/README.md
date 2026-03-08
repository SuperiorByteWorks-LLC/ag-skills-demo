# Weather Data

This directory contains NASA POWER weather data for agricultural fields.

## Source

- **NASA Langley Research Center POWER Project**
- Data format: CSV
- Endpoint: <https://power.larc.nasa.gov/api/temporal/daily/point>

## Files

| File                                 | Description                                          |
| ------------------------------------ | ---------------------------------------------------- |
| `michigan_southern_weather_2024.csv` | Daily weather for 50 Southern Michigan fields (2024) |

## Weather Parameters

- T2M: Daily mean temperature (°C)
- T2M_MAX: Daily maximum temperature (°C)
- T2M_MIN: Daily minimum temperature (°C)
- PRECTOTCORR: Precipitation - bias-corrected (mm)
- ALLSKY_SFC_SW_DWN: Solar radiation (MJ/m²/day)
- RH2M: Relative humidity at 2 m (%)
- WS10M: Wind speed at 10 m (m/s)

## Usage

```python
import pandas as pd

weather = pd.read_csv('data/weather/michigan_southern_weather_2024.csv', parse_dates=['date'])
print(weather.groupby('field_id').agg({
    'T2M': 'mean',
    'PRECTOTCORR': 'sum'
}))
```

## Note

This data is NOT tracked in git. See .gitignore.
