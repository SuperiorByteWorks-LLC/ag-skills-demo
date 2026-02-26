# Skill: field-boundaries

Download and visualize USDA field boundary data for agricultural analysis.

## Description

This skill provides access to the USDA NASS Crop Sequence Boundaries dataset, allowing you to download agricultural field boundaries for specific regions and crops. It includes built-in visualization capabilities and summary statistics.

## Requirements

- Python 3.9+
- geopandas
- matplotlib
- shapely

## Installation

```bash
pip install geopandas matplotlib shapely
```

## Usage

### download

Download field boundaries from USDA Crop Sequence Boundaries.

```python
from skills.field_boundaries import FieldBoundariesSkill

skill = FieldBoundariesSkill()
fields = skill.download(
    count=20,  # Number of fields (keep small: 20-50)
    regions=['corn_belt'],  # Options: 'corn_belt', 'great_plains', 'southeast'
    crops=['corn', 'soybeans'],  # Options: 'corn', 'soybeans', 'wheat', 'cotton'
    output_path='data/fields_EPSG4326.geojson'
)
```

Parameters:

- `count` (int): Number of fields to download. Keep small (20-50) for efficient local processing.
- `regions` (list[str]): Regions to sample from. Options: 'corn_belt', 'great_plains', 'southeast'.
- `crops` (list[str]): Crop types to include. Options: 'corn', 'soybeans', 'wheat', 'cotton'.
- `output_path` (str): Output file path. Should include CRS (e.g., 'fields_EPSG4326.geojson').

Returns:

- GeoDataFrame: Field boundaries with attributes including field_id, area_acres, region, crop_name.

### plot_fields

Create a visualization of field boundaries on a map.

```python
skill.plot_fields(
    fields,
    title="My Agricultural Fields",
    color_by="crop_name",  # Color fields by crop type
    save_path="data/fields_map.png"
)
```

Parameters:

- `fields` (GeoDataFrame): Field boundaries to visualize.
- `title` (str): Plot title.
- `color_by` (str): Column to color by (e.g., 'crop_name', 'region').
- `save_path` (str): Optional path to save the figure.

### get_summary

Get summary statistics for field boundaries.

```python
summary = skill.get_summary(fields)
print(f"Total fields: {summary['total_fields']}")
print(f"Average size: {summary['avg_field_size']:.1f} acres")
```

Parameters:

- `fields` (GeoDataFrame): Field boundaries.

Returns:

- dict: Summary statistics including total_fields, total_area_acres, avg_field_size, size_range, regions, crops.

### export

Export fields to file with proper CRS naming.

```python
skill.export(
    fields,
    output_path='data/fields_EPSG4326.geojson',
    format='geojson'  # Options: 'geojson', 'geoparquet'
)
```

Parameters:

- `fields` (GeoDataFrame): Field boundaries.
- `output_path` (str): Output file path with CRS (e.g., 'fields_EPSG4326.geojson').
- `format` (str): Export format. Options: 'geojson', 'geoparquet'.

Returns:

- Path: Path to exported file.

## Examples

### Example 1: Download and Visualize

```python
from skills.field_boundaries import FieldBoundariesSkill

# Initialize skill
skill = FieldBoundariesSkill()

# Download 20 fields from Corn Belt
fields = skill.download(
    count=20,
    regions=['corn_belt'],
    crops=['corn', 'soybeans'],
    output_path='data/my_fields_EPSG4326.geojson'
)

# Get summary
summary = skill.get_summary(fields)
print(f"Downloaded {summary['total_fields']} fields")
print(f"Total area: {summary['total_area_acres']:.1f} acres")

# Visualize
skill.plot_fields(
    fields,
    title="Iowa Corn and Soybean Fields",
    color_by='crop_name',
    save_path='data/fields_map.png'
)
```

### Example 2: Filter and Export

```python
from skills.field_boundaries import FieldBoundariesSkill

skill = FieldBoundariesSkill()
fields = skill.download(count=50)

# Filter large fields (>100 acres)
large_fields = skill.filter_by_size(fields, min_acres=100)
print(f"Large fields: {len(large_fields)}")

# Export in multiple formats
skill.export(large_fields, 'data/large_fields_EPSG4326.geojson', 'geojson')
skill.export(large_fields, 'data/large_fields_EPSG4326.parquet', 'geoparquet')
```

## Data Source

- **Source**: USDA NASS Crop Sequence Boundaries
- **Coverage**: Contiguous United States
- **Update Frequency**: Annual
- **Format**: GeoJSON (vector)
- **CRS**: EPSG:4326 (WGS84)

## Output Files

All output files include the CRS in the filename:

- `fields_EPSG4326.geojson` - Field boundaries in GeoJSON format
- `fields_EPSG4326.parquet` - Field boundaries in GeoParquet format (cloud-optimized)

## Notes

- Keep field count small (20-50) for efficient local processing
- All coordinates are in EPSG:4326 (WGS84)
- Field boundaries are approximate and may not match legal property lines
- Data is sourced from satellite imagery and may have classification errors
- NO shapefiles - use GeoJSON or GeoParquet only

## Resources

- [USDA NASS Crop Sequence Boundaries](https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/)
- [GeoPandas Documentation](https://geopandas.org/)
- [EPSG:4326 - WGS 84](https://epsg.io/4326)
