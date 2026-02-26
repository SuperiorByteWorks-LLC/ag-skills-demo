# Skill: eda-compare

## Description

This skill compares groups and categories within agricultural datasets. Perform statistical comparisons between regions, crop types, soil classifications, or any categorical grouping. Create comparative visualizations and calculate statistical significance without writing comparison code.

## Requirements

- Python 3.9+
- pandas
- scipy
- matplotlib
- seaborn

## Installation

```bash
pip install pandas scipy matplotlib seaborn
```

## Usage

### compare_groups

Compare numeric values across different categories.

```python
from skills.eda_compare import EDACompareSkill

skill = EDACompareSkill()
comparison = skill.compare_groups(
    data_path='data/fields.csv',
    value_column='field_size',
    group_column='region',
    output_path='data/analysis/region_comparison.csv'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `value_column` (str): Numeric column to compare
- `group_column` (str): Categorical column defining groups
- `output_path` (str): Path to save comparison results

Returns:

- dict: Statistics for each group including mean, median, std, count

### statistical_test

Perform statistical significance tests between groups.

```python
results = skill.statistical_test(
    data_path='data/soil_data.csv',
    value_column='ph_water',
    group_column='region',
    test_type='anova',  # Options: 'anova', 't-test', 'mann-whitney'
    output_path='data/analysis/significance_test.csv'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `value_column` (str): Numeric column to test
- `group_column` (str): Categorical column defining groups
- `test_type` (str): Statistical test to perform
- `output_path` (str): Path to save results

Returns:

- dict: Test statistics, p-value, and interpretation

### create_comparison_plot

Generate comparative visualizations (box plots, violin plots, bar charts).

```python
skill.create_comparison_plot(
    data_path='data/crops.csv',
    value_column='yield',
    group_column='crop_type',
    plot_type='box',  # Options: 'box', 'violin', 'bar'
    output_path='data/viz/yield_by_crop.png',
    title='Yield Comparison by Crop Type'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `value_column` (str): Numeric column to visualize
- `group_column` (str): Categorical column for grouping
- `plot_type` (str): Type of plot ('box', 'violin', 'bar')
- `output_path` (str): Path to save the chart
- `title` (str): Chart title

### compare_multiple_metrics

Compare several metrics across groups simultaneously.

```python
results = skill.compare_multiple_metrics(
    data_path='data/fields.csv',
    metric_columns=['size', 'ph_water', 'organic_matter'],
    group_column='management_zone',
    output_path='data/analysis/multi_metric_comparison.csv'
)
```

Parameters:

- `data_path` (str): Path to CSV file
- `metric_columns` (list[str]): Multiple numeric columns to compare
- `group_column` (str): Categorical column defining groups
- `output_path` (str): Path to save results

Returns:

- pandas.DataFrame: Comparison table with all metrics by group

## Examples

### Example 1: Regional Comparison

```python
from skills.eda_compare import EDACompareSkill

skill = EDACompareSkill()

# Compare field sizes across regions
comparison = skill.compare_groups(
    data_path='data/all_fields.csv',
    value_column='area_acres',
    group_column='region',
    output_path='data/analysis/size_by_region.csv'
)

print("Field Size by Region:")
for region, stats in comparison.items():
    print(f"\n{region}:")
    print(f"  Count: {stats['count']} fields")
    print(f"  Mean: {stats['mean']:.1f} acres")
    print(f"  Median: {stats['median']:.1f} acres")
    print(f"  Std Dev: {stats['std']:.1f} acres")
```

### Example 2: Statistical Significance Testing

```python
from skills.eda_compare import EDACompareSkill

skill = EDACompareSkill()

# Test if soil pH differs significantly by region
test_result = skill.statistical_test(
    data_path='data/soil_by_region.csv',
    value_column='ph_water',
    group_column='region',
    test_type='anova',
    output_path='data/analysis/ph_significance.csv'
)

print(f"Test: {test_result['test_name']}")
print(f"Statistic: {test_result['statistic']:.3f}")
print(f"P-value: {test_result['p_value']:.4f}")

if test_result['significant']:
    print("✓ Significant difference between regions")
else:
    print("✗ No significant difference between regions")

print(f"\nInterpretation: {test_result['interpretation']}")
```

### Example 3: Crop Type Comparison

```python
from skills.eda_compare import EDACompareSkill

skill = EDACompareSkill()

# Compare yields across crop types
skill.create_comparison_plot(
    data_path='data/yield_data.csv',
    value_column='yield_bushels',
    group_column='crop_type',
    plot_type='box',
    output_path='data/viz/yield_comparison.png',
    title='Yield Distribution by Crop Type'
)

# Get detailed statistics
comparison = skill.compare_groups(
    data_path='data/yield_data.csv',
    value_column='yield_bushels',
    group_column='crop_type',
    output_path='data/analysis/yield_stats.csv'
)

print("\nYield Statistics by Crop:")
for crop, stats in comparison.items():
    print(f"{crop}: {stats['mean']:.1f} ± {stats['std']:.1f} bushels/acre")
```

### Example 4: Multi-Metric Analysis

```python
from skills.eda_compare import EDACompareSkill

skill = EDACompareSkill()

# Compare multiple soil properties by drainage class
results = skill.compare_multiple_metrics(
    data_path='data/soil_measurements.csv',
    metric_columns=['ph_water', 'organic_matter', 'clay_content', 'sand_content'],
    group_column='drainage_class',
    output_path='data/analysis/soil_by_drainage.csv'
)

print("Soil Properties by Drainage Class:")
print(results.to_string())

# Create comprehensive visualization
for metric in ['ph_water', 'organic_matter']:
    skill.create_comparison_plot(
        data_path='data/soil_measurements.csv',
        value_column=metric,
        group_column='drainage_class',
        plot_type='violin',
        output_path=f'data/viz/{metric}_by_drainage.png',
        title=f'{metric.replace("_", " ").title()} by Drainage Class'
    )
```

### Example 5: Before and After Comparison

```python
from skills.eda_compare import EDACompareSkill

skill = EDACompareSkill()

# Compare field performance before/after treatment
comparison = skill.compare_groups(
    data_path='data/treatment_results.csv',
    value_column='yield',
    group_column='treatment_group',  # 'before' or 'after'
    output_path='data/analysis/treatment_effect.csv'
)

print("Treatment Effect:")
for group, stats in comparison.items():
    print(f"{group}: {stats['mean']:.1f} bushels/acre (n={stats['count']})")

# Test significance
test = skill.statistical_test(
    data_path='data/treatment_results.csv',
    value_column='yield',
    group_column='treatment_group',
    test_type='t-test',
    output_path='data/analysis/treatment_significance.csv'
)

if test['significant']:
    improvement = comparison['after']['mean'] - comparison['before']['mean']
    print(f"\n✓ Significant improvement: +{improvement:.1f} bushels/acre")
else:
    print("\n✗ No significant difference")
```

## Data Source

- **Input**: CSV with numeric columns and categorical grouping columns
- **Output**: Comparison statistics, significance tests, visualizations
- **Tests Supported**: ANOVA (3+ groups), t-test (2 groups), Mann-Whitney (non-parametric)

## Output Files

- `*_comparison.csv` - Group statistics
- `*_significance.csv` - Statistical test results
- `*_comparison.png` - Box plots, violin plots, bar charts

## Statistical Test Guide

**Choose the right test:**

- **ANOVA** (Analysis of Variance): Compare 3+ groups
  - Example: Compare yields across 5 different regions
- **t-test**: Compare exactly 2 groups
  - Example: Compare treated vs untreated fields
- **Mann-Whitney U**: Non-parametric alternative (when data isn't normally distributed)
  - Example: Compare soil types with skewed distributions

**Interpreting results:**

- p-value < 0.05: Significant difference exists
- p-value ≥ 0.05: No significant difference
- Effect size: How large is the difference (practical significance)

## Notes

- Automatically handles unequal group sizes
- Reports both statistical and practical significance
- Box plots show median, quartiles, and outliers
- Violin plots show distribution shape
- All tests assume independence (different samples per group)
- Missing values excluded from comparisons
- Large group differences may be significant even if small

## Resources

- [Statistical Hypothesis Testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
- [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance)
- [T-Test](https://en.wikipedia.org/wiki/Student%27s_t-test)
- [Mann-Whitney U Test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
- [Box Plot Interpretation](https://en.wikipedia.org/wiki/Box_plot)
