# Skill: eda-correlate

## Description

This skill analyzes correlations between variables in agricultural datasets. It calculates correlation coefficients, identifies significant relationships, and creates correlation matrices with heatmaps. Perfect for discovering which soil properties, field characteristics, and environmental factors are related without statistical coding.

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn

## Installation

```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

### analyze_correlations

Calculate correlation matrix for all numeric columns.

```python
from skills.eda_correlate import EDACorrelateSkill

skill = EDACorrelateSkill()
correlations = skill.analyze_correlations(
    data_path='data/soil_data.csv',
    output_path='data/correlation_matrix.csv',
    method='pearson'  # Options: 'pearson', 'spearman', 'kendall'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `output_path` (str): Path to save correlation matrix CSV
- `method` (str): Correlation method ('pearson', 'spearman', 'kendall')

Returns:

- pandas.DataFrame: Correlation matrix with all numeric column pairs

### get_strongest_correlations

Find the strongest correlations in the dataset.

```python
strong_correlations = skill.get_strongest_correlations(
    data_path='data/field_data.csv',
    threshold=0.5,  # Only correlations above this absolute value
    top_n=10  # Return top N correlations
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `threshold` (float): Minimum absolute correlation to include (0.0-1.0)
- `top_n` (int): Number of top correlations to return

Returns:

- list: Strongest correlations with variable pairs and coefficients

### analyze_pair

Analyze correlation between two specific variables.

```python
result = skill.analyze_pair(
    data_path='data/soil_data.csv',
    var1='ph_water',
    var2='organic_matter',
    create_plot=True,
    output_path='data/ph_om_correlation.png'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `var1` (str): First variable name
- `var2` (str): Second variable name
- `create_plot` (bool): Whether to create scatter plot with trend line
- `output_path` (str): Path to save plot (if create_plot=True)

Returns:

- dict: Correlation coefficient, p-value, and interpretation

## Examples

### Example 1: Full Correlation Analysis

```python
from skills.eda_correlate import EDACorrelateSkill

# Initialize skill
skill = EDACorrelateSkill()

# Analyze all correlations in soil data
correlations = skill.analyze_correlations(
    data_path='data/soil_properties.csv',
    output_path='data/analysis/correlation_matrix.csv',
    method='pearson'
)

print("Correlation Matrix:")
print(correlations)

# Show strongest relationships
strong = skill.get_strongest_correlations(
    data_path='data/soil_properties.csv',
    threshold=0.3,
    top_n=5
)

print("\nTop 5 Strongest Correlations:")
for item in strong:
    print(f"{item['var1']} ↔ {item['var2']}: {item['correlation']:.3f}")
```

### Example 2: Investigate Specific Relationship

```python
from skills.eda_correlate import EDACorrelateSkill

skill = EDACorrelateSkill()

# Analyze specific relationship with visualization
result = skill.analyze_pair(
    data_path='data/fields_complete.csv',
    var1='ph_water',
    var2='organic_matter',
    create_plot=True,
    output_path='data/analysis/ph_om_scatter.png'
)

print(f"Correlation: {result['correlation']:.3f}")
print(f"P-value: {result['p_value']:.4f}")
print(f"Interpretation: {result['strength']} {result['direction']} relationship")

if result['significant']:
    print("✓ Statistically significant")
else:
    print("✗ Not statistically significant")
```

### Example 3: Interpret Correlation Results

```python
from skills.eda_correlate import EDACorrelateSkill

skill = EDACorrelateSkill()

# Get all strong correlations
results = skill.get_strongest_correlations(
    data_path='data/agricultural_data.csv',
    threshold=0.5,
    top_n=10
)

print("Key Findings:")
for r in results:
    var1, var2 = r['var1'], r['var2']
    corr = r['correlation']

    # Interpret strength
    if abs(corr) >= 0.7:
        strength = "Strong"
    elif abs(corr) >= 0.4:
        strength = "Moderate"
    else:
        strength = "Weak"

    direction = "positive" if corr > 0 else "negative"

    print(f"\n{var1} ↔ {var2}:")
    print(f"  Correlation: {corr:.3f}")
    print(f"  Strength: {strength} {direction}")
    print(f"  Meaning: When {var1} increases, {var2} tends to {'increase' if corr > 0 else 'decrease'}")
```

### Example 4: Compare Multiple Datasets

```python
from skills.eda_correlate import EDACorrelateSkill

skill = EDACorrelateSkill()

# Analyze correlations in different regions
regions = ['corn_belt', 'great_plains', 'southeast']

for region in regions:
    print(f"\n=== {region.upper()} ===")

    correlations = skill.analyze_correlations(
        data_path=f'data/{region}_soil.csv',
        output_path=f'data/analysis/{region}_correlations.csv'
    )

    strong = skill.get_strongest_correlations(
        data_path=f'data/{region}_soil.csv',
        threshold=0.4,
        top_n=3
    )

    for item in strong:
        print(f"{item['var1']} ↔ {item['var2']}: {item['correlation']:.3f}")
```

## Data Source

- **Input**: CSV files with numeric columns
- **Output**: Correlation matrix CSV + optional scatter plots
- **Methods**: Pearson (linear), Spearman (rank-based), Kendall (ordinal)

## Output Files

- `correlation_matrix.csv` - Full correlation matrix
- `*_correlation.png` - Scatter plots with trend lines (when created)

## Correlation Interpretation Guide

**Strength:**

- 0.0 - 0.3: Weak correlation
- 0.3 - 0.7: Moderate correlation
- 0.7 - 1.0: Strong correlation

**Direction:**

- Positive (+): Both variables increase together
- Negative (-): One increases, other decreases

**Significance:**

- p-value < 0.05: Statistically significant
- p-value ≥ 0.05: Not statistically significant

## Notes

- Pearson correlation assumes linear relationships (most common)
- Spearman correlation works for monotonic relationships (rank-based)
- Kendall correlation for ordinal data or small samples
- Automatically excludes non-numeric columns
- Handles missing values via pairwise deletion
- Statistical significance tested automatically
- Correlation does not imply causation

## Resources

- [Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
- [Correlation vs Causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation)
- [Interpreting Correlations](https://www.statisticssolutions.com/correlation-pearson-kendall-spearman/)
