# Field Boundaries Data

This directory contains USDA NASS Crop Sequence Boundaries for agricultural fields.

## Source

- **USDA NASS Crop Sequence Boundaries** via Source Cooperative
- Data format: GeoParquet -> GeoJSON
- Year: 2023

## Files

| File                           | Description                                |
| ------------------------------ | ------------------------------------------ |
| `michigan_southern_50.geojson` | 50 field boundaries from Southern Michigan |

## Region

Southern Michigan includes:

- Thumb region (Huron, Tuscola, Sanilac, Saginaw)
- Mid-Michigan (Clinton, Gratiot, Isabella, Midland)
- Southwest (Berrien, Cass, St. Joseph, Branch)
- South-central (Jackson, Hillsdale, Lenawee, Monroe)

## Bounding Box

- North: 44.5° N
- South: 41.5° N
- East: 82.5° W
- West: 87.5° W

## Usage

```python
import geopandas as gpd

fields = gpd.read_file('data/field-boundaries/michigan_southern_50.geojson')
print(f"Loaded {len(fields)} fields")
```

## Note

This data is NOT tracked in git. See .gitignore.
