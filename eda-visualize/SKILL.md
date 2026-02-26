# Skill: eda-visualize

## Description

This skill creates professional data visualizations automatically from agricultural datasets. Generate histograms, scatter plots, box plots, bar charts, and heatmaps with a single command. Perfect for understanding distributions, relationships, and patterns in field data, soil properties, and weather records without writing matplotlib code.

## Requirements

- Python 3.9+
- pandas
- matplotlib
- seaborn

## Installation

```bash
pip install pandas matplotlib seaborn
```

## Usage

### create_histogram

Create distribution histograms for numeric columns.

```python
from skills.eda_visualize import EDAVisualizeSkill

skill = EDAVisualizeSkill()
skill.create_histogram(
    data_path='data/soil_data.csv',
    column='ph_water',
    output_path='data/viz/ph_distribution.png',
    bins=20,
    title='Soil pH Distribution'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `column` (str): Column to visualize
- `output_path` (str): Path to save the chart
- `bins` (int): Number of histogram bins (default: auto)
- `title` (str): Chart title

### create_scatter

Create scatter plots to show relationships between two variables.

```python
skill.create_scatter(
    data_path='data/soil_data.csv',
    x_column='ph_water',
    y_column='organic_matter',
    output_path='data/viz/ph_vs_om.png',
    title='Soil pH vs Organic Matter',
    color_by='region'  # Optional: color points by category
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `x_column` (str): X-axis variable
- `y_column` (str): Y-axis variable
- `output_path` (str): Path to save the chart
- `title` (str): Chart title
- `color_by` (str): Optional column to color points by

### create_boxplot

Create box plots to compare distributions across categories.

```python
skill.create_boxplot(
    data_path='data/field_data.csv',
    value_column='field_size',
    category_column='region',
    output_path='data/viz/size_by_region.png',
    title='Field Size by Region'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `value_column` (str): Numeric column to visualize
- `category_column` (str): Categorical column for grouping
- `output_path` (str): Path to save the chart
- `title` (str): Chart title

### create_bar_chart

Create bar charts for categorical data.

```python
skill.create_bar_chart(
    data_path='data/crop_data.csv',
    category_column='crop_type',
    output_path='data/viz/crop_counts.png',
    title='Crop Type Distribution'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `category_column` (str): Categorical column to count
- `output_path` (str): Path to save the chart
- `title` (str): Chart title

### create_heatmap

Create correlation heatmaps for numeric columns.

```python
skill.create_heatmap(
    data_path='data/soil_data.csv',
    columns=['ph_water', 'organic_matter', 'clay', 'sand'],
    output_path='data/viz/correlation_heatmap.png',
    title='Soil Properties Correlation'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `columns` (list[str]): Numeric columns to include
- `output_path` (str): Path to save the chart
- `title` (str): Chart title

## Examples

### Example 1: Create Multiple Histograms

```python
from skills.eda_visualize import EDAVisualizeSkill

skill = EDAVisualizeSkill()

# Visualize soil properties
soil_columns = ['ph_water', 'organic_matter', 'clay_content']

for col in soil_columns:
    skill.create_histogram(
        data_path='data/soil_measurements.csv',
        column=col,
        output_path=f'data/viz/{col}_dist.png',
        title=f'{col.replace("_", " ").title()} Distribution'
    )
    print(f"Created: data/viz/{col}_dist.png")
```

### Example 2: Relationship Scatter Plot

```python
from skills.eda_visualize import EDAVisualizeSkill

skill = EDAVisualizeSkill()

# Show relationship with regional colors
skill.create_scatter(
    data_path='data/fields_with_soil.csv',
    x_column='ph_water',
    y_column='organic_matter',
    output_path='data/viz/ph_om_relationship.png',
    title='pH vs Organic Matter by Region',
    color_by='region'
)

print("Created relationship plot showing regional patterns")
```

### Example 3: Comparative Box Plots

```python
from skills.eda_visualize import EDAVisualizeSkill

skill = EDAVisualizeSkill()

# Compare soil pH across regions
skill.create_boxplot(
    data_path='data/soil_by_region.csv',
    value_column='ph_water',
    category_column='region',
    output_path='data/viz/ph_by_region.png',
    title='Soil pH Distribution by Region'
)

# Compare field sizes by crop type
skill.create_boxplot(
    data_path='data/fields.csv',
    value_column='area_acres',
    category_column='crop_type',
    output_path='data/viz/size_by_crop.png',
    title='Field Size by Crop Type'
)
```

### Example 4: Complete Visualization Suite

```python
from skills.eda_visualize import EDAVisualizeSkill

skill = EDAVisualizeSkill()

# Create a comprehensive visualization set
dataset = 'data/my_agricultural_data.csv'
output_dir = 'data/visualizations'

# 1. Distribution of numeric columns
skill.create_histogram(
    data_path=dataset,
    column='field_size',
    output_path=f'{output_dir}/field_size_dist.png',
    title='Field Size Distribution'
)

# 2. Categorical distribution
skill.create_bar_chart(
    data_path=dataset,
    category_column='crop_type',
    output_path=f'{output_dir}/crop_counts.png',
    title='Crop Types in Dataset'
)

# 3. Correlation heatmap
numeric_cols = ['field_size', 'ph_water', 'organic_matter', 'yield']
skill.create_heatmap(
    data_path=dataset,
    columns=numeric_cols,
    output_path=f'{output_dir}/correlations.png',
    title='Variable Correlations'
)

print(f"Created {len(output_dir)} visualizations in {output_dir}/")
```

## Data Source

- **Input**: Any CSV with numeric or categorical columns
- **Output**: PNG image files (300 DPI, publication quality)
- **Chart Types**: Histogram, scatter, box plot, bar chart, heatmap

## Output Files

All outputs are high-resolution PNG files:

- `*_distribution.png` - Histograms
- `*_scatter.png` - Scatter plots
- `*_boxplot.png` - Box plots
- `*_barchart.png` - Bar charts
- `*_heatmap.png` - Correlation heatmaps

## Notes

- All charts are 300 DPI for publication quality
- Color schemes are colorblind-friendly
- Large datasets are sampled for performance (max 10K points for scatter plots)
- Charts automatically adjust figure size based on data
- Missing values are handled gracefully (excluded from visualization)
- Font sizes are optimized for presentation slides

## Resources

- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Data Visualization Best Practices](https://clauswilke.com/dataviz/)
