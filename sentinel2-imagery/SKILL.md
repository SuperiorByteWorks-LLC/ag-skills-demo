---
name: sentinel2-imagery
description: Download and process Sentinel-2 satellite imagery for agricultural fields using standard Python libraries (sentinelsat, rasterio). Calculate NDVI, extract statistics, and visualize crop health.
version: 1.0.0
author: Boreal Bytes
tags: [sentinel-2, satellite, imagery, ndvi, remote-sensing, agriculture, copernicus]
---

# Skill: sentinel2-imagery

## Description

Download and process Sentinel-2 multispectral satellite imagery for agricultural analysis. This skill teaches you to use standard Python libraries (`sentinelsat` for data access, `rasterio` for raster processing) to acquire satellite data, calculate vegetation indices like NDVI, and extract field-level statistics.

## When to Use This Skill

- **Downloading satellite imagery**: Get Sentinel-2 data for specific fields and date ranges
- **Calculating NDVI**: Compute Normalized Difference Vegetation Index for crop health monitoring
- **Time series analysis**: Track vegetation changes throughout the growing season
- **Field-level statistics**: Extract mean, min, max NDVI values for agricultural fields
- **Cloud masking**: Filter imagery by cloud cover percentage

## Prerequisites

```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Example Data

Sample data is included in the `examples/` directory:

- `examples/sample_aoi.geojson` - Bounding box AOI derived from field-boundaries examples
- `examples/sample_ndvi_metadata.json` - Metadata for sample NDVI calculations
- `examples/sample_field_stats.csv` - Example field-level NDVI statistics (time series)

Use these for testing and development:

```python
import json

# Load example metadata
with open('examples/sample_ndvi_metadata.json') as f:
    metadata = json.load(f)
print(f"Sample acquisition date: {metadata['acquisition_date']}")
print(f"Cloud cover: {metadata['cloud_cover']}%")

# Output:
# Sample acquisition date: 2024-06-15
# Cloud cover: 12%
```

## Quick Start

```bash
# Run in isolated environment with required dependencies
uv run --with sentinelsat --with rasterio --with numpy --with geopandas python << 'EOF'
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import rasterio
from rasterio.mask import mask
import numpy as np

# Connect to Copernicus Data Space (free registration required)
api = SentinelAPI('your_username', 'your_password', 'https://dataspace.copernicus.eu')

# Search for Sentinel-2 imagery
footprint = geojson_to_wkt(read_geojson('examples/sample_aoi.geojson'))
products = api.query(
    footprint,
    date=('20240601', '20240630'),
    platformname='Sentinel-2',
    producttype='S2MSI2A',  # Level-2A (atmospherically corrected)
    cloudcoverpercentage=(0, 20)
)

print(f"Found {len(products)} products")
EOF
```

## Installation (Isolated Environment)

This skill runs in an isolated environment to avoid dependency conflicts:

```bash
# Create dedicated environment for this skill
cd .skills/sentinel2-imagery
uv venv .venv
source .venv/bin/activate

# Install dependencies
uv pip install sentinelsat rasterio numpy geopandas matplotlib
```

## Usage Examples

### Example 1: Search and Download Imagery

```python
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import geopandas as gpd

# Initialize API (get free account at dataspace.copernicus.eu)
api = SentinelAPI('username', 'password', 'https://dataspace.copernicus.eu')

# Load field boundaries (from field-boundaries skill)
fields = gpd.read_file('../field-boundaries/examples/sample_2_fields.geojson')

# Get bounding box of fields for search
bbox = fields.total_bounds  # [minx, miny, maxx, maxy]
footprint = f"POLYGON(({bbox[0]} {bbox[1]}, {bbox[2]} {bbox[1]}, {bbox[2]} {bbox[3]}, {bbox[0]} {bbox[3]}, {bbox[0]} {bbox[1]}))"

# Search for imagery
products = api.query(
    footprint,
    date=('20240601', '20240831'),  # Growing season
    platformname='Sentinel-2',
    producttype='S2MSI2A',
    cloudcoverpercentage=(0, 20)
)

# Convert to DataFrame
products_df = api.to_dataframe(products)
print(f"Found {len(products_df)} products")
print(products_df[['title', 'cloudcoverpercentage', 'beginposition']].head())

# Download first product
if len(products_df) > 0:
    product_id = products_df.index[0]
    api.download(product_id, directory_path='data/sentinel2')
```

### Example 2: Calculate NDVI with Rasterio

```python
import rasterio
import numpy as np
from rasterio.plot import show
import matplotlib.pyplot as plt

# Open Red (B04) and NIR (B08) bands
# Note: Update paths to your downloaded imagery
with rasterio.open('data/sentinel2/T33UUV_20240615_B04_10m.jp2') as red_src:
    red = red_src.read(1).astype(float)
    profile = red_src.profile

with rasterio.open('data/sentinel2/T33UUV_20240615_B08_10m.jp2') as nir_src:
    nir = nir_src.read(1).astype(float)

# Calculate NDVI
# NDVI = (NIR - Red) / (NIR + Red)
ndvi = np.divide(
    nir - red,
    nir + red,
    out=np.zeros_like(nir),
    where=(nir + red) != 0
)

# Save NDVI raster
profile.update(dtype=rasterio.float32, count=1)
with rasterio.open('data/sentinel2/ndvi_20240615.tif', 'w', **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

print(f"NDVI range: {np.nanmin(ndvi):.2f} to {np.nanmax(ndvi):.2f}")
```

### Example 3: Clip to Field Boundaries

```python
from rasterio.mask import mask
import geopandas as gpd
import json

# Load field boundaries
fields = gpd.read_file('../field-boundaries/examples/sample_2_fields.geojson')

# Open NDVI raster
with rasterio.open('data/sentinel2/ndvi_20240615.tif') as src:
    # Clip to first field
    field_geom = [fields.iloc[0].geometry.__geo_interface__]
    out_image, out_transform = mask(src, field_geom, crop=True)
    out_meta = src.meta.copy()

# Update metadata
out_meta.update({
    'driver': 'GTiff',
    'height': out_image.shape[1],
    'width': out_image.shape[2],
    'transform': out_transform
})

# Save clipped NDVI
with rasterio.open('data/sentinel2/field_001_ndvi.tif', 'w', **out_meta) as dst:
    dst.write(out_image)

print("Clipped NDVI saved to field_001_ndvi.tif")
```

### Example 4: Extract Field Statistics

```python
import rasterio
from rasterio.mask import mask
import geopandas as gpd
import pandas as pd
import numpy as np

# Load fields
fields = gpd.read_file('../field-boundaries/examples/sample_2_fields.geojson')

# Open NDVI raster
with rasterio.open('data/sentinel2/ndvi_20240615.tif') as src:
    stats = []

    for idx, field in fields.iterrows():
        # Clip to field
        geom = [field.geometry.__geo_interface__]
        out_image, _ = mask(src, geom, crop=True, nodata=np.nan)

        # Calculate statistics
        ndvi_values = out_image[0]
        valid_pixels = ndvi_values[~np.isnan(ndvi_values)]

        if len(valid_pixels) > 0:
            stats.append({
                'field_id': field['field_id'],
                'mean_ndvi': np.mean(valid_pixels),
                'min_ndvi': np.min(valid_pixels),
                'max_ndvi': np.max(valid_pixels),
                'std_ndvi': np.std(valid_pixels),
                'pixel_count': len(valid_pixels)
            })

# Create statistics DataFrame
stats_df = pd.DataFrame(stats)
print(stats_df)

# Save to CSV
stats_df.to_csv('data/sentinel2/field_ndvi_stats.csv', index=False)
```

### Example 5: Visualize NDVI

```python
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Open NDVI raster
with rasterio.open('data/sentinel2/ndvi_20240615.tif') as src:
    ndvi = src.read(1)

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Define NDVI colormap (red to green)
cmap = colors.LinearSegmentedColormap.from_list(
    'ndvi', ['brown', 'yellow', 'lightgreen', 'darkgreen']
)

# Plot NDVI
im = ax.imshow(ndvi, cmap=cmap, vmin=-0.2, vmax=1.0)
ax.set_title('NDVI - June 15, 2024', fontsize=14)
ax.axis('off')

# Add colorbar
cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('NDVI', rotation=270, labelpad=20)

# Add interpretation labels
cbar.ax.text(0.5, 0.15, 'Bare Soil', ha='center', va='center', fontsize=9)
cbar.ax.text(0.5, 0.85, 'Healthy Veg', ha='center', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('data/sentinel2/ndvi_visualization.png', dpi=150, bbox_inches='tight')
plt.show()
```

## Python API Reference

### `SentinelAPI(username, password, api_url)`

Initialize connection to Copernicus Data Space.

**Parameters:**

- `username` (str): Your Copernicus Data Space username
- `password` (str): Your Copernicus Data Space password
- `api_url` (str): API endpoint URL ('https://dataspace.copernicus.eu')

**Returns:** SentinelAPI instance

### `api.query(footprint, date, platformname, producttype, cloudcoverpercentage)`

Search for Sentinel-2 products.

**Parameters:**

- `footprint` (str): WKT geometry string defining search area
- `date` (tuple): (start_date, end_date) in 'YYYYMMDD' format
- `platformname` (str): 'Sentinel-2'
- `producttype` (str): 'S2MSI2A' (Level-2A) or 'S2MSI1C' (Level-1C)
- `cloudcoverpercentage` (tuple): (min, max) cloud cover percentage

**Returns:** Dictionary of product metadata

### `api.download(product_id, directory_path)`

Download a Sentinel-2 product.

**Parameters:**

- `product_id` (str): Product UUID from query results
- `directory_path` (str): Directory to save downloaded files

**Returns:** Downloaded file path

### `api.to_dataframe(products)`

Convert query results to pandas DataFrame.

**Parameters:**

- `products` (dict): Query results from `api.query()`

**Returns:** DataFrame with product metadata

### `rasterio.open(path)`

Open raster file for reading or writing.

**Parameters:**

- `path` (str): Path to raster file (.jp2, .tif, etc.)

**Returns:** DatasetReader object

### `mask(src, shapes, crop=True)`

Clip raster to geometry.

**Parameters:**

- `src` (DatasetReader): Opened rasterio dataset
- `shapes` (list): List of GeoJSON-like geometry dictionaries
- `crop` (bool): Whether to crop to extent of shapes

**Returns:** (clipped_array, transform)

## Data Source

- **Source**: ESA Copernicus Sentinel-2
- **Coverage**: Global
- **Resolution**: 10m (B2, B3, B4, B8), 20m (other bands)
- **Revisit**: 5 days
- **Bands**: 13 spectral bands
- **Time Period**: 2015-present
- **Access**: Free with registration at [Copernicus Data Space](https://dataspace.copernicus.eu/)

## Key Sentinel-2 Bands

| Band | Wavelength     | Resolution | Use                    |
| ---- | -------------- | ---------- | ---------------------- |
| B2   | 490 nm (Blue)  | 10m        | Water penetration      |
| B3   | 560 nm (Green) | 10m        | Vegetation vigor       |
| B4   | 665 nm (Red)   | 10m        | Chlorophyll absorption |
| B8   | 842 nm (NIR)   | 10m        | Vegetation biomass     |
| B11  | 1610 nm (SWIR) | 20m        | Moisture content       |

## NDVI Calculation

Formula: `NDVI = (NIR - Red) / (NIR + Red)`

Range: -1 to 1

| NDVI Value | Interpretation      |
| ---------- | ------------------- |
| < 0.2      | Water, bare soil    |
| 0.2-0.4    | Sparse vegetation   |
| 0.4-0.6    | Moderate vegetation |
| > 0.6      | Dense vegetation    |

## Output Files

- `*_B04_10m.jp2` - Red band (10m resolution)
- `*_B08_10m.jp2` - NIR band (10m resolution)
- `ndvi_*.tif` - Calculated NDVI raster
- `field_*_ndvi.tif` - Field-clipped NDVI
- `field_ndvi_stats.csv` - Field-level statistics

## Environment Variables

```bash
# Optional: Store credentials in environment variables
export COPERNICUS_USERNAME="your_username"
export COPERNICUS_PASSWORD="your_password"
```

Then in Python:

```python
import os
from sentinelsat import SentinelAPI

api = SentinelAPI(
    os.getenv('COPERNICUS_USERNAME'),
    os.getenv('COPERNICUS_PASSWORD'),
    'https://dataspace.copernicus.eu'
)
```

## Integration with field-boundaries Skill

This skill is designed to work with the `field-boundaries` skill. Use field
boundaries as your area of interest (AOI) for Sentinel-2 searches:

```python
import geopandas as gpd
from sentinelsat import SentinelAPI, geojson_to_wkt, read_geojson

# Load field boundaries from field-boundaries skill examples
fields = gpd.read_file('../field-boundaries/examples/sample_2_fields.geojson')

# Create bounding box AOI from fields
bbox = fields.total_bounds  # [minx, miny, maxx, maxy]
footprint = (
    f'POLYGON(({bbox[0]} {bbox[1]}, {bbox[2]} {bbox[1]}, '
    f'{bbox[2]} {bbox[3]}, {bbox[0]} {bbox[3]}, {bbox[0]} {bbox[1]}))'
)

# Or use the pre-built AOI (1km buffer around field 271623002471299)
footprint = geojson_to_wkt(read_geojson('examples/sample_aoi.geojson'))

# Search for imagery over the AOI
api = SentinelAPI('user', 'pass', 'https://dataspace.copernicus.eu')
products = api.query(
    footprint,
    date=('20240601', '20240831'),
    platformname='Sentinel-2',
    producttype='S2MSI2A',
    cloudcoverpercentage=(0, 20)
)
```

## Resources

- [Copernicus Data Space](https://dataspace.copernicus.eu/) - Free registration and data access
- [Sentinel-2 User Guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi)
- [sentinelsat Documentation](https://sentinelsat.readthedocs.io/)
- [rasterio Documentation](https://rasterio.readthedocs.io/)
- [field-boundaries Skill](../field-boundaries/SKILL.md) - For getting field AOI data
