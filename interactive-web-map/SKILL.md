---
name: interactive-web-map
description: Create interactive single-file HTML web maps for visualizing agricultural data. Use when the user needs to visualize field boundaries, soil data, weather patterns, crop distributions, or satellite imagery in an interactive web map with selectable layers and data tables.
---

# Interactive Web Map

## Quick Start

Create an interactive web map from field data:

```python
from skills.interactive_web_map import InteractiveWebMapSkill

skill = InteractiveWebMapSkill()

# Create map with multiple data sources
skill.create_map(
    fields_geojson='data/fields_EPSG4326.geojson',
    soil_csv='data/soil_EPSG4326.csv',
    weather_csv='data/weather.csv',
    cdl_csv='data/cdl_EPSG4326.csv',
    output_path='data/interactive_map.html'
)
```

## Description

Creates a fully self-contained, single-file HTML interactive web map for visualizing agricultural data. The map includes:

- Interactive field boundaries on a world map
- Clickable fields that show data tables
- Layer toggles for different data sources
- Zoom and pan controls
- Popups with field information
- Data tables that update based on selection
- Fully portable - works offline

## Features

- **Single File**: Everything embedded in one HTML file
- **Interactive**: Click fields to see data, toggle layers
- **Multi-Source**: Display soil, weather, crops together
- **Responsive**: Works on desktop and mobile
- **Offline**: No internet required after initial load
- **Portable**: Email, share, or archive the HTML file

## Usage

### create_map

Create an interactive web map from multiple data sources.

```python
skill.create_map(
    fields_geojson='data/fields_EPSG4326.geojson',
    soil_csv='data/soil_EPSG4326.csv',
    weather_csv='data/weather.csv',
    cdl_csv='data/cdl_EPSG4326.csv',
    sentinel2_dir='data/sentinel2',
    output_path='data/interactive_map.html'
)
```

Parameters:

- `fields_geojson` (str): Path to field boundaries GeoJSON
- `soil_csv` (str, optional): Path to soil data CSV
- `weather_csv` (str, optional): Path to weather data CSV
- `cdl_csv` (str, optional): Path to crop data CSV
- `sentinel2_dir` (str, optional): Directory with Sentinel-2 imagery
- `landsat_dir` (str, optional): Directory with Landsat imagery
- `output_path` (str): Output HTML file path

Returns:

- Path: Path to generated HTML file

### create_simple_map

Create a simple map with just field boundaries.

```python
skill.create_simple_map(
    fields_geojson='data/fields_EPSG4326.geojson',
    output_path='data/simple_map.html'
)
```

## Examples

### Example 1: Full Agricultural Data Map

```python
from skills.interactive_web_map import InteractiveWebMapSkill

skill = InteractiveWebMapSkill()

# Create comprehensive map with all data sources
map_path = skill.create_map(
    fields_geojson='data/my_fields_EPSG4326.geojson',
    soil_csv='data/soil_EPSG4326.csv',
    weather_csv='data/weather.csv',
    cdl_csv='data/cdl_EPSG4326.csv',
    output_path='data/agricultural_dashboard.html'
)

print(f"Map created: {map_path}")
print("Open in browser to explore your data interactively!")
```

### Example 2: Soil Analysis Map

```python
from skills.interactive_web_map import InteractiveWebMapSkill

skill = InteractiveWebMapSkill()

# Create map focused on soil data
map_path = skill.create_map(
    fields_geojson='data/fields_EPSG4326.geojson',
    soil_csv='data/soil_EPSG4326.csv',
    output_path='data/soil_analysis_map.html'
)

# Open in browser
import webbrowser
webbrowser.open(f'file://{map_path}')
```

### Example 3: Multi-Year Crop History

```python
from skills.interactive_web_map import InteractiveWebMapSkill

skill = InteractiveWebMapSkill()

# Create map with 5 years of crop data
map_path = skill.create_map(
    fields_geojson='data/fields_EPSG4326.geojson',
    cdl_csv='data/cdl_5yr_EPSG4326.csv',
    output_path='data/crop_rotation_map.html'
)
```

## Output File

**Single HTML file** containing:

- Interactive map (Leaflet.js)
- All data embedded (GeoJSON, CSV)
- Styling and JavaScript
- Responsive layout

Example: `interactive_map.html` (typically 1-5 MB)

## Map Interface

### Navigation

- **Zoom**: Mouse wheel or +/- buttons
- **Pan**: Click and drag
- **Reset**: Home button to see all fields

### Layers

- **Fields**: Toggle field boundaries
- **Soil**: Toggle soil data (if provided)
- **Weather**: Toggle weather stations
- **Crops**: Toggle crop classifications
- **Imagery**: Toggle satellite layers

### Interactions

- **Click field**: Show data table for that field
- **Hover**: Highlight field and show name
- **Table tabs**: Switch between data sources
- **Export**: Save data as CSV

## Data Requirements

### Required

- `fields_geojson`: GeoJSON with field_id column

### Optional (enhances map)

- `soil_csv`: Must have field_id column
- `weather_csv`: Must have field_id column
- `cdl_csv`: Must have field_id column
- `sentinel2_dir`: GeoTIFF files with field_id in filename

## Browser Compatibility

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Notes

- Large datasets (>100 fields) may load slowly
- Satellite imagery increases file size significantly
- All data is embedded - file is self-contained
- No server or internet required after creation
- Maps work offline once loaded

## Resources

- [Leaflet.js Documentation](https://leafletjs.com/)
- [GeoJSON Specification](https://geojson.org/)
- [HTML5 Offline Applications](https://developer.mozilla.org/en-US/docs/Web/HTML/Using_the_application_cache)
