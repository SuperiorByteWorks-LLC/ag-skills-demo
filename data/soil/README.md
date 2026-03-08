# Soil Data

This directory contains USDA NRCS SSURGO soil data for agricultural fields.

## Source

- **USDA NRCS Soil Data Access (SDA)** REST API
- Data format: CSV
- Endpoint: <https://sdmdataaccess.sc.egov.usda.gov/>

## Files

| File                         | Description                                     |
| ---------------------------- | ----------------------------------------------- |
| `michigan_southern_soil.csv` | Soil properties for 50 Southern Michigan fields |

## Soil Properties

- pH (ph1to1h2o_r)
- Organic matter (om_r) - percentage
- Available water capacity (awc_r)
- Drainage class
- Clay/Sand/Silt percentages
- Bulk density (dbthirdbar_r)
- Cation exchange capacity (cec7_r)

## Usage

```python
import pandas as pd

soil = pd.read_csv('data/soil/michigan_southern_soil.csv')
print(soil[['field_id', 'compname', 'om_r', 'ph1to1h2o_r']].head())
```

## Note

This data is NOT tracked in git. See .gitignore.
