---
name: ssurgo-soil
description: Access USDA NRCS SSURGO (Soil Survey Geographic Database) soil data for agricultural fields. Use when the user needs soil properties (organic matter, pH, texture, drainage), soil maps, or soil health data for field analysis, crop planning, or agricultural modeling.
---

# SSURGO Soil Data

## Quick Start

Download soil data for field boundaries:

```python
from skills.ssurgo_soil import SSURGOSoilSkill

skill = SSURGOSoilSkill()
soil = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    attributes=['om_pct', 'ph_water', 'awc_r', 'drainagecl'],
    output_path='data/soil_EPSG4326.csv'
)
```

## Data Source

**USDA NRCS SSURGO** (Soil Survey Geographic Database)

- Coverage: Most agricultural areas in the US
- Resolution: 1:12,000 to 1:63,360 (detailed field-level)
- Attributes: 60+ soil properties
- Update: Periodic surveys

## Key Attributes

| Attribute      | Description               | Units       |
| -------------- | ------------------------- | ----------- |
| `om_pct`       | Organic matter percentage | %           |
| `ph_water`     | pH in water               | pH units    |
| `awc_r`        | Available water capacity  | inches/inch |
| `drainagecl`   | Drainage class            | categorical |
| `claytotal_r`  | Clay content              | %           |
| `sandtotal_r`  | Sand content              | %           |
| `silttotal_r`  | Silt content              | %           |
| `dbthirdbar_r` | Bulk density              | g/cm³       |
| `cec7_r`       | Cation exchange capacity  | meq/100g    |

## Usage

### download_for_fields

Query SSURGO soil data at field centroids.

```python
soil = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    attributes=['om_pct', 'ph_water', 'awc_r'],
    output_path='data/soil_EPSG4326.csv'
)
```

Parameters:

- `fields_geojson` (str): Path to GeoJSON file with field boundaries
- `attributes` (list[str]): Soil attributes to retrieve. See references/attributes.md for full list.
- `output_path` (str): Output CSV file path

Returns:

- DataFrame: Soil data with field_id and requested attributes

### plot_soil_map

Visualize soil properties on field map.

```python
skill.plot_soil_map(
    soil_data=soil,
    fields=fields_geojson,
    attribute='om_pct',
    title='Soil Organic Matter',
    save_path='data/soil_map.png'
)
```

### get_soil_health_score

Calculate composite soil health score.

```python
soil_with_scores = skill.get_soil_health_score(
    soil_data,
    weights={'om_pct': 0.3, 'awc_r': 0.25, 'ph_water': 0.2}
)
```

## Examples

### Example 1: Download and Visualize

```python
from skills.ssurgo_soil import SSURGOSoilSkill

skill = SSURGOSoilSkill()

# Get soil data for 20 fields
soil = skill.download_for_fields(
    fields_geojson='data/my_fields_EPSG4326.geojson',
    attributes=['om_pct', 'ph_water', 'awc_r', 'drainagecl'],
    output_path='data/soil_EPSG4326.csv'
)

# Display summary
print(f"Average pH: {soil['ph_water'].mean():.2f}")
print(f"Average OM: {soil['om_pct'].mean():.2f}%")

# Visualize organic matter
skill.plot_soil_map(
    soil_data=soil,
    fields='data/my_fields_EPSG4326.geojson',
    attribute='om_pct',
    title='Soil Organic Matter by Field',
    save_path='data/soil_om_map.png'
)
```

### Example 2: Soil Health Analysis

```python
from skills.ssurgo_soil import SSURGOSoilSkill
import pandas as pd

skill = SSURGOSoilSkill()

# Download with multiple attributes
soil = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    attributes=['om_pct', 'ph_water', 'awc_r', 'claytotal_r', 'drainagecl'],
    output_path='data/soil_detailed_EPSG4326.csv'
)

# Calculate soil health score
soil_scored = skill.get_soil_health_score(soil)

# Find fields with best soil health
best_fields = soil_scored.nlargest(5, 'soil_health_score')
print("Top 5 fields by soil health:")
print(best_fields[['field_id', 'soil_health_score', 'om_pct', 'ph_water']])

# Classify drainage
soil_classified = skill.classify_drainage(soil)
print(soil_classified['drainage_category'].value_counts())
```

## Output Files

- `soil_EPSG4326.csv` - Soil data with field_id for joining
- Columns: field_id, om_pct, ph_water, awc_r, drainagecl, etc.

## Notes

- Queries soil data at field centroids
- May return NULL for areas without soil surveys
- pH valid range: 3.5 - 10.0
- Organic matter typical range: 0-20%
- See references/attributes.md for complete attribute list

## Resources

- [USDA NRCS Soil Data Access](https://sdmdataaccess.nrcs.usda.gov/)
- [SSURGO Database](https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/)
- [references/attributes.md](references/attributes.md) - Complete attribute reference
