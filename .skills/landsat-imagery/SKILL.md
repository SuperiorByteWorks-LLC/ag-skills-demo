---
name: landsat-imagery
description: Access and visualize Landsat 8/9 satellite imagery for agricultural fields. Use when the user needs historical satellite images, NDVI/EVI calculations, or long-term remote sensing data for agricultural analysis from Landsat satellites.
---

# Landsat Imagery

## Quick Start

Download Landsat 8/9 imagery for agricultural fields:

```python
from skills.landsat_imagery import LandsatImagerySkill

skill = LandsatImagerySkill()
imagery = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2024-06-01',
    end_date='2024-08-31',
    bands=['B4', 'B5'],
    cloud_cover_max=20,
    output_dir='data/landsat'
)
```

## Data Source

**Landsat 8/9** (USGS/NASA)

- Coverage: Global
- Resolution: 30m (multispectral), 15m (panchromatic)
- Revisit: 16 days
- Time Period: 2013-present (L8), 2021-present (L9)
- Archive: 1984-present (Landsat 4-9)

## Key Bands

| Band | Wavelength          | Resolution | Use                    |
| ---- | ------------------- | ---------- | ---------------------- |
| B2   | 450-510 nm (Blue)   | 30m        | Water penetration      |
| B3   | 530-590 nm (Green)  | 30m        | Vegetation vigor       |
| B4   | 640-670 nm (Red)    | 30m        | Chlorophyll absorption |
| B5   | 850-880 nm (NIR)    | 30m        | Vegetation biomass     |
| B6   | 1570-1650 nm (SWIR) | 30m        | Moisture content       |
| B10  | 1060-1119 nm (TIRS) | 100m       | Surface temperature    |

## Usage

### download_for_fields

Download Landsat imagery for field boundaries.

```python
imagery = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2024-06-01',
    end_date='2024-08-31',
    bands=['B4', 'B5'],
    cloud_cover_max=20,
    output_dir='data/landsat'
)
```

Parameters:

- `fields_geojson` (str): Path to field boundaries
- `start_date` (str): Start date 'YYYY-MM-DD'
- `end_date` (str): End date 'YYYY-MM-DD'
- `bands` (list[str]): Landsat bands to download
- `cloud_cover_max` (float): Maximum cloud cover %
- `output_dir` (str): Output directory

Returns:

- DataFrame: Metadata for downloaded imagery

### calculate_ndvi

Calculate NDVI from Red and NIR bands.

```python
ndvi_path = skill.calculate_ndvi(
    red_band_path='data/landsat/field_001_20240615_B4_EPSG4326.tif',
    nir_band_path='data/landsat/field_001_20240615_B5_EPSG4326.tif',
    output_path='data/landsat/field_001_ndvi_EPSG4326.tif'
)
```

### calculate_evi

Calculate Enhanced Vegetation Index (EVI).

```python
evi_path = skill.calculate_evi(
    red_band_path='data/landsat/field_001_20240615_B4_EPSG4326.tif',
    nir_band_path='data/landsat/field_001_20240615_B5_EPSG4326.tif',
    blue_band_path='data/landsat/field_001_20240615_B2_EPSG4326.tif',
    output_path='data/landsat/field_001_evi_EPSG4326.tif'
)
```

## Examples

### Example 1: Download Historical Data

```python
from skills.landsat_imagery import LandsatImagerySkill

skill = LandsatImagerySkill()

# Download 5 years of data
imagery = skill.download_for_fields(
    fields_geojson='data/my_fields_EPSG4326.geojson',
    start_date='2019-01-01',
    end_date='2023-12-31',
    bands=['B4', 'B5'],
    cloud_cover_max=20,
    output_dir='data/landsat'
)

print(f"Downloaded {len(imagery)} images")

# Calculate NDVI for first image
if len(imagery) > 0:
    red_path = imagery[imagery['band'] == 'B4']['file_path'].iloc[0]
    nir_path = imagery[imagery['band'] == 'B5']['file_path'].iloc[0]

    ndvi_path = skill.calculate_ndvi(red_path, nir_path)
    print(f"NDVI saved to: {ndvi_path}")
```

### Example 2: Long-term Trend Analysis

```python
from skills.landsat_imagery import LandsatImagerySkill

skill = LandsatImagerySkill()

# Download multiple years
imagery = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2018-06-01',
    end_date='2023-08-31',
    bands=['B2', 'B4', 'B5'],
    output_dir='data/landsat'
)

# Calculate NDVI for all
ndvi_files = []
for field_id in imagery['field_id'].unique():
    field_imagery = imagery[imagery['field_id'] == field_id]

    for date in field_imagery['date'].unique():
        date_imagery = field_imagery[field_imagery['date'] == date]
        red = date_imagery[date_imagery['band'] == 'B4']['file_path'].iloc[0]
        nir = date_imagery[date_imagery['band'] == 'B5']['file_path'].iloc[0]

        ndvi_path = skill.calculate_ndvi(red, nir)
        ndvi_files.append({'field_id': field_id, 'date': date, 'path': ndvi_path})

# Compare with Sentinel-2 (if available)
# stats = skill.compare_with_sentinel2(landsat_ndvi, sentinel2_ndvi, fields_geojson)
```

## Output Files

- `landsat_field_001_20240615_B4_EPSG4326.tif` - Individual bands
- `landsat_field_001_20240615_NDVI_EPSG4326.tif` - Calculated NDVI
- `landsat_manifest_EPSG4326.csv` - Metadata

## Comparison with Sentinel-2

| Feature    | Landsat 8/9      | Sentinel-2                 |
| ---------- | ---------------- | -------------------------- |
| Resolution | 30m              | 10-60m                     |
| Revisit    | 16 days          | 5 days                     |
| Archive    | 1984-present     | 2015-present               |
| Best for   | Long-term trends | High-resolution monitoring |

## Notes

- Downloads clipped to field boundaries
- 30m resolution for multispectral bands
- 16-day revisit time
- Excellent for long-term trend analysis
- Requires USGS EarthExplorer account

## Resources

- [USGS EarthExplorer](https://earthexplorer.usgs.gov/)
- [Landsat Missions](https://landsat.gsfc.nasa.gov/)
