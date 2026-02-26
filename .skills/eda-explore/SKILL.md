# Skill: eda-explore

## Description

This skill provides automated exploratory data analysis (EDA) for agricultural datasets. It generates comprehensive statistical summaries, identifies data distributions, and creates descriptive statistics for any CSV or tabular dataset. Perfect for understanding field data, soil properties, weather records, and crop information without writing code.

## Requirements

- Python 3.9+
- pandas
- numpy

## Installation

```bash
pip install pandas numpy
```

## Usage

### analyze

Generate comprehensive statistical summary for a dataset.

```python
from skills.eda_explore import EDAExploreSkill

skill = EDAExploreSkill()
summary = skill.analyze(
    data_path='data/field_data.csv',
    output_path='data/eda_summary.csv'
)
```

Parameters:

- `data_path` (str): Path to CSV file containing your data
- `output_path` (str): Path to save summary statistics CSV

Returns:

- dict: Summary statistics including counts, means, medians, standard deviations, min/max, quartiles, and data types

### get_column_info

Get detailed information about each column in the dataset.

```python
column_info = skill.get_column_info(
    data_path='data/field_data.csv'
)
print(column_info['numeric_columns'])
print(column_info['categorical_columns'])
```

Parameters:

- `data_path` (str): Path to CSV file

Returns:

- dict: Column types, missing value counts, unique values for categorical columns

### identify_outliers

Find potential outliers in numeric columns.

```python
outliers = skill.identify_outliers(
    data_path='data/soil_data.csv',
    columns=['ph_water', 'organic_matter'],
    method='iqr'  # Options: 'iqr', 'zscore'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `columns` (list[str]): Columns to check for outliers
- `method` (str): Outlier detection method ('iqr' or 'zscore')

Returns:

- dict: Outlier records with values and row indices

## Examples

### Example 1: Basic Exploration

```python
from skills.eda_explore import EDAExploreSkill

# Initialize skill
skill = EDAExploreSkill()

# Analyze field data
summary = skill.analyze(
    data_path='data/my_fields.csv',
    output_path='data/exploration/summary.csv'
)

print("Dataset Overview:")
print(f"Total records: {summary['total_records']}")
print(f"Numeric columns: {summary['numeric_count']}")
print(f"Categorical columns: {summary['categorical_count']}")

# Show sample statistics
for col, stats in summary['numeric_stats'].items():
    print(f"\n{col}:")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Median: {stats['median']:.2f}")
    print(f"  Range: {stats['min']:.2f} - {stats['max']:.2f}")
```

### Example 2: Check for Outliers

```python
from skills.eda_explore import EDAExploreSkill

skill = EDAExploreSkill()

# Find unusual values in soil data
outliers = skill.identify_outliers(
    data_path='data/soil_measurements.csv',
    columns=['ph_water', 'organic_matter', 'clay_content'],
    method='iqr'
)

print(f"Found {len(outliers)} potential outliers:")
for col, records in outliers.items():
    print(f"\n{col}: {len(records)} outliers")
    for record in records[:3]:  # Show first 3
        print(f"  Row {record['row']}: {record['value']:.2f}")
```

### Example 3: Column Information

```python
from skills.eda_explore import EDAExploreSkill

skill = EDAExploreSkill()

# Get column details
info = skill.get_column_info('data/weather_data.csv')

print("Data Structure:")
print(f"Total columns: {info['total_columns']}")
print(f"Numeric: {len(info['numeric_columns'])}")
print(f"Categorical: {len(info['categorical_columns'])}")

print("\nMissing Values:")
for col, count in info['missing_values'].items():
    if count > 0:
        print(f"  {col}: {count} missing")
```

## Data Source

- **Input**: Any CSV or tabular dataset
- **Output**: Statistical summaries in CSV format
- **Compatible With**: Field boundaries, soil data, weather records, crop data

## Output Files

- `eda_summary.csv` - Complete statistical summary
- Column statistics (mean, median, std, min, max, quartiles)
- Data type information
- Missing value counts
- Outlier identification

## Notes

- Automatically detects numeric vs categorical columns
- Handles missing values gracefully
- Provides IQR (Interquartile Range) outlier detection by default
- Suitable for datasets of any size (tested up to 100K records)
- Results are saved as CSV for easy viewing in Excel
- All numeric calculations use pandas/numpy for accuracy

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Exploratory Data Analysis Guide](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
- [Descriptive Statistics](https://en.wikipedia.org/wiki/Descriptive_statistics)
