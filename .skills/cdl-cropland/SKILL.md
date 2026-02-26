---
name: cdl-cropland
description: Access USDA NASS Cropland Data Layer (CDL) for annual crop classifications. Use when the user needs crop type data, land cover classifications, or crop history for agricultural fields, carbon credit verification, or land use analysis.
---

# CDL Cropland Data

## Quick Start

Download annual crop classifications for fields:

```python
from skills.cdl_cropland import CDLCroplandSkill

skill = CDLCroplandSkill()
cdl = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    years=[2021, 2022, 2023],
    output_path='data/cdl_EPSG4326.csv'
)
```

## Data Source

**USDA NASS Cropland Data Layer (CDL)**

- Coverage: Contiguous United States
- Resolution: 30m (1 pixel = 30x30m)
- Classification: 130+ crop/land cover classes
- Time Period: 2008-present (annual)
- Accuracy: 90%+ for major crops

## Major Crop Classes

| Code | Crop         | Category     |
| ---- | ------------ | ------------ |
| 1    | Corn         | Row Crops    |
| 5    | Soybeans     | Row Crops    |
| 24   | Winter Wheat | Small Grains |
| 27   | Rye          | Small Grains |
| 36   | Alfalfa      | Forage       |
| 61   | Fallow/Idle  | Fallow       |

## Usage

### download_for_fields

Download CDL crop classifications for fields.

```python
cdl = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    years=[2021, 2022, 2023],
    output_path='data/cdl_EPSG4326.csv'
)
```

Parameters:

- `fields_geojson` (str): Path to field boundaries
- `years` (list[int]): Years to retrieve (2008-present)
- `output_path` (str): Output CSV path

Returns:

- DataFrame: Crop data with field_id, year, crop_code, crop_name

### analyze_rotation

Analyze crop rotation patterns.

```python
rotation = skill.analyze_rotation(cdl)
print(rotation.head())
```

### plot_crop_map

Visualize crop distribution on field map.

```python
skill.plot_crop_map(
    cdl_data=cdl,
    fields='data/fields_EPSG4326.geojson',
    year=2023,
    save_path='data/crop_map.png'
)
```

## Examples

### Example 1: Download and Visualize

```python
from skills.cdl_cropland import CDLCroplandSkill

skill = CDLCroplandSkill()

# Get 5 years of crop data
cdl = skill.download_for_fields(
    fields_geojson='data/my_fields_EPSG4326.geojson',
    years=[2019, 2020, 2021, 2022, 2023],
    output_path='data/cdl_5yr_EPSG4326.csv'
)

# See crop distribution
print(cdl['crop_name'].value_counts())

# Visualize 2023 crops
skill.plot_crop_map(
    cdl_data=cdl,
    fields='data/my_fields_EPSG4326.geojson',
    year=2023,
    title='2023 Crop Distribution',
    save_path='data/crop_2023_map.png'
)
```

### Example 2: Rotation Analysis

```python
from skills.cdl_cropland import CDLCroplandSkill

skill = CDLCroplandSkill()

# Download crop data
cdl = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    years=[2019, 2020, 2021, 2022, 2023]
)

# Analyze rotation patterns
rotation = skill.analyze_rotation(cdl)
print("Rotation Analysis:")
print(rotation[['field_id', 'rotation_count', 'crop_sequence']].head())

# Get most common crops
dominant = skill.get_dominant_crops(cdl, top_n=5)
print("\nTop 5 Crops:")
print(dominant)

# Classify into categories
cdl_classified = skill.classify_crop_type(cdl)
print("\nCrop Categories:")
print(cdl_classified['crop_category'].value_counts())
```

## Output Files

- `cdl_EPSG4326.csv` - Annual crop classifications
- Columns: field_id, year, crop_code, crop_name

## Notes

- CDL provides dominant crop per field
- 30m resolution may not capture small fields accurately
- Classifications based on satellite imagery (June-July)
- Double-cropped areas may show only primary crop
- See references/crop_codes.md for full classification list

## Resources

- [USDA NASS CDL](https://www.nass.usda.gov/Research_and_Science/Cropland/)
- [CropScape](https://nassgeodata.gmu.edu/CropScape/)
