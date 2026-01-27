# 04 - Clean Fields, Clean Data + Demo

_Agricultural Data Systems_

---

## 🏠 Housekeeping

- **Use the "Q&A" feature** in Zoom for questions
- Keep your **camera on** during class if possible
- Please **mute yourself** to avoid interruptions
- Use the **"Raise hand"** feature when you want to speak (and lower it when finished)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Confirm students have a sample dataset downloaded from Class 03
- Remind them to save scripts for reuse in later assignments

</details>

---

## 📋 Syllabus Review

Last class we mapped the data landscape and pulled sample datasets. Today we focus on cleaning, validating, and integrating those datasets for analysis.

_This connects to Class 05 next week, where we run exploratory data analysis on cleaned data._

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Reinforce that cleaning decisions affect every downstream result
- Mention that every assignment from here forward assumes clean inputs

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Syllabus review
- [ ] Data wrangling fundamentals
- [ ] Intro to SQL
- [ ] Merging and joining datasets
- [ ] USDA and weather data integration
- [ ] AI assistants for data cleaning
- [ ] Demo: Python and SQL cleaning workflow

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Keep the demo flexible to absorb extra time
- If time is short, compress the AI section

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Identify** common data quality issues in agricultural datasets
- **Apply** SQL filters and joins for cleaning tasks
- **Merge** multiple sources into a unified table
- **Validate** cleaned data with repeatable checks
- **Use** AI tools to accelerate routine cleaning steps

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Ask students which data issues they saw in their downloads
- Tie outcomes to the assignment deliverable

</details>

---

## 📚 Content

### Data Wrangling Fundamentals

We cover the core cleaning steps that make data usable for analysis.

Key points:

- Missing values, duplicates, and inconsistent units
- Standardizing column names and categories
- Logging assumptions and transformations

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Use a quick before and after example to show impact
- Emphasize that documentation is part of cleaning

</details>

---

### Intro to SQL

We use SQL to filter, join, and summarize agricultural datasets.

Key points:

- `SELECT`, `WHERE`, `GROUP BY`, `JOIN`
- Data type casting and validation
- Saving queries for reuse

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Show a simple query on a crop dataset
- Explain where SQL fits alongside Python

</details>

---

### Merging and Joining Datasets

We combine multiple sources into a consistent analytical view.

Key points:

- Join keys and row alignment
- Left vs inner joins in agricultural contexts
- Avoiding accidental duplication

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Remind students to check row counts after joins
- Note that mismatches often signal data issues

</details>

---

### USDA and Weather Data Integration

We align USDA data with NOAA weather series for analysis.

Key points:

- Temporal alignment (daily vs monthly)
- Geographic identifiers and crosswalks
- Unit conversions and normalization

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Highlight the importance of documenting alignment decisions
- Mention time zone and calendar year pitfalls

</details>

---

### AI Assistants for Data Cleaning

We use AI tools to generate boilerplate cleaning scripts and checks.

Key points:

- Use specific prompts and sample schema
- Validate AI outputs against expectations
- Keep a log of AI-assisted decisions

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Share a prompt template that works well for cleaning tasks
- Reinforce that AI does not replace verification

</details>

---

### Demo: Python and SQL Cleaning Workflow

We walk through a complete cleaning pipeline on a real dataset.

Key points:

- Load raw files and standardize columns
- Run SQL checks to validate merges
- Export a clean, analysis-ready table

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Narrate decisions and trade-offs as you go
- Pause for questions at each major step

</details>

---

## ✍️ Assignment

### Task: Data Cleaning Pipeline

**Objective:** Build a repeatable cleaning workflow for raw agricultural datasets.

**Instructions:**

1. Download raw data from multiple sources.
2. Clean, validate, and merge the datasets using Python and or SQL.
3. Document data quality issues and how you resolved them.

**What to submit:** A notebook or script with a short write-up of cleaning decisions.

**Due:** TBD

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage students to include before and after row counts
- Suggest a short data log at the top of the notebook

</details>

---

## 🔗 Resources & References

### Official Sources

- [USDA NASS QuickStats](https://quickstats.nass.usda.gov/) - Crop and livestock data
- [NOAA NCEI](https://www.ncei.noaa.gov/) - Climate and weather archives

### Reading Materials

- [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf) - Core framework for clean datasets

### Tools

- [pandas](https://pandas.pydata.org/) - Data cleaning library
- [SQLBolt](https://sqlbolt.com/) - SQL refresher and practice

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Point students to SQLBolt if they need a refresher
- Encourage bookmarking pandas docs for quick reference

</details>

---
