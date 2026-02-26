---
name: sentinel2-imagery
description: Access and visualize Sentinel-2 satellite imagery for agricultural fields. Use when the user needs satellite images, NDVI calculations, crop health monitoring, or remote sensing data for agricultural analysis from Sentinel-2 satellites.
---

# Sentinel-2 Imagery

## Quick Start

Download Sentinel-2 imagery for agricultural fields:

```python
from skills.sentinel2_imagery import Sentinel2ImagerySkill

skill = Sentinel2ImagerySkill()
imagery = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2024-06-01',
    end_date='2024-08-31',
    bands=['B4', 'B8'],
    cloud_cover_max=20,
    output_dir='data/sentinel2'
)
```

## Data Source

**Sentinel-2** (ESA Copernicus Program)

- Coverage: Global
- Resolution: 10m (B2, B3, B4, B8), 20m (other bands)
- Revisit: 5 days
- Bands: 13 spectral bands (10-60m)
- Time Period: 2015-present

## Key Bands

| Band | Wavelength     | Resolution | Use                    |
| ---- | -------------- | ---------- | ---------------------- |
| B2   | 490 nm (Blue)  | 10m        | Water penetration      |
| B3   | 560 nm (Green) | 10m        | Vegetation vigor       |
| B4   | 665 nm (Red)   | 10m        | Chlorophyll absorption |
| B8   | 842 nm (NIR)   | 10m        | Vegetation biomass     |
| B11  | 1610 nm (SWIR) | 20m        | Moisture content       |

## Usage

### download_for_fields

Download Sentinel-2 imagery for field boundaries.

```python
imagery = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2024-06-01',
    end_date='2024-08-31',
    bands=['B4', 'B8'],
    cloud_cover_max=20,
    output_dir='data/sentinel2'
)
```

Parameters:

- `fields_geojson` (str): Path to field boundaries
- `start_date` (str): Start date 'YYYY-MM-DD'
- `end_date` (str): End date 'YYYY-MM-DD'
- `bands` (list[str]): Sentinel-2 bands to download
- `cloud_cover_max` (float): Maximum cloud cover %
- `output_dir` (str): Output directory

Returns:

- DataFrame: Metadata for downloaded imagery

### calculate_ndvi

Calculate NDVI from Red and NIR bands.

```python
ndvi_path = skill.calculate_ndvi(
    red_band_path='data/sentinel2/field_001_20240615_B4_EPSG4326.tif',
    nir_band_path='data/sentinel2/field_001_20240615_B8_EPSG4326.tif',
    output_path='data/sentinel2/field_001_ndvi_EPSG4326.tif'
)
```

### plot_imagery

Visualize satellite imagery.

```python
skill.plot_imagery(
    image_path='data/sentinel2/field_001_ndvi_EPSG4326.tif',
    title='NDVI - Field 001',
    save_path='data/sentinel2/ndvi_plot.png'
)
```

## Examples

### Example 1: Download and Calculate NDVI

```python
from skills.sentinel2_imagery import Sentinel2ImagerySkill

skill = Sentinel2ImagerySkill()

# Download imagery for growing season
imagery = skill.download_for_fields(
    fields_geojson='data/my_fields_EPSG4326.geojson',
    start_date='2024-05-01',
    end_date='2024-09-30',
    bands=['B4', 'B8'],
    cloud_cover_max=20,
    output_dir='data/sentinel2'
)

print(f"Downloaded {len(imagery)} images")

# Calculate NDVI for first image
if len(imagery) > 0:
    red_path = imagery[imagery['band'] == 'B4']['file_path'].iloc[0]
    nir_path = imagery[imagery['band'] == 'B8']['file_path'].iloc[0]

    ndvi_path = skill.calculate_ndvi(red_path, nir_path)
    print(f"NDVI saved to: {ndvi_path}")

    # Plot NDVI
    skill.plot_imagery(ndvi_path, title='NDVI',
                      save_path='data/sentinel2/ndvi_plot.png')
```

### Example 2: Extract Statistics

```python
from skills.sentinel2_imagery import Sentinel2ImagerySkill

skill = Sentinel2ImagerySkill()

# Download NDVI for all fields
imagery = skill.download_for_fields(
    fields_geojson='data/fields_EPSG4326.geojson',
    start_date='2024-06-01',
    end_date='2024-08-31',
    bands=['B4', 'B8'],
    output_dir='data/sentinel2'
)

# Calculate NDVI for each field
ndvi_files = []
for field_id in imagery['field_id'].unique():
    field_imagery = imagery[imagery['field_id'] == field_id]
    red = field_imagery[field_imagery['band'] == 'B4']['file_path'].iloc[0]
    nir = field_imagery[field_imagery['band'] == 'B8']['file_path'].iloc[0]
    ndvi_path = skill.calculate_ndvi(red, nir)
    ndvi_files.append(ndvi_path)

# Extract statistics
stats = skill.extract_statistics(
    ndvi_files[0],
    'data/fields_EPSG4326.geojson'
)
print(stats)
```

## Output Files

- `sentinel2_field_001_20240615_B4_EPSG4326.tif` - Individual bands
- `sentinel2_field_001_20240615_NDVI_EPSG4326.tif` - Calculated NDVI
- `sentinel2_manifest_EPSG4326.csv` - Metadata

## NDVI Calculation

Formula: `NDVI = (NIR - Red) / (NIR + Red)`

Range: -1 to 1

- < 0.2: Water, bare soil
- 0.2-0.4: Sparse vegetation
- 0.4-0.6: Moderate vegetation
- > 0.6: Dense vegetation

## Notes

- Downloads clipped to field boundaries (not full scenes)
- 10m resolution for RGB+NIR bands
- 5-day revisit time
- Requires Copernicus Data Space account
- Cloud-free images recommended (<20%)

## Resources

- [Copernicus Data Space](https://dataspace.copernicus.eu/)
- [Sentinel-2 User Guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi)
