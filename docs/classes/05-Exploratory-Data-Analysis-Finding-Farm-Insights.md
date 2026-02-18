# 05 - Exploratory Data Analysis: Finding Farm Insights + Demo

_Agricultural Data Systems_

---

## 🏠 Housekeeping

- **Use the "Q&A" feature** in Zoom for questions
- Keep your **camera on** during class if possible
- Please **mute yourself** to avoid interruptions
- Use the **"Raise hand"** feature when you want to speak (and lower it when finished)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Confirm students have a cleaned dataset ready for exploration
- Remind students to save charts for later dashboard work

</details>

---

## 📋 Syllabus Review

Last class we cleaned and integrated raw datasets. Today we explore the data to uncover patterns, outliers, and questions for deeper analysis.

_This connects to Class 06 next week, where we add geospatial analysis to our workflow._

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Emphasize that EDA shapes every modeling decision later
- Encourage curiosity and experimentation

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Syllabus review
- [ ] DataFrames and EDA fundamentals
- [ ] Pandas and Polars operations with time series
- [ ] Descriptive statistics for farm data
- [ ] Visualization and correlation analysis
- [ ] AI for alternative metrics or visualizations
- [ ] Demo: Python EDA notebook walkthrough
- [ ] Peer share

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Keep peer share short and focused on insights
- If time is short, blend AI prompts into the demo

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Profile** agricultural datasets using descriptive statistics
- **Apply** key pandas and Polars operations for exploration
- **Visualize** distributions, trends, and relationships
- **Interpret** correlations and outliers with agricultural context
- **Generate** alternative metrics or charts using AI assistance

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Ask students to name one question they want to answer with EDA
- Tie outcomes to the assignment deliverable

</details>

---

## 📚 Content

### DataFrames and EDA Fundamentals

We review how to inspect datasets quickly and understand their structure.

Key points:

- Shape, schema, and missing values
- Basic summaries and sanity checks
- Building an exploration checklist

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Demonstrate `df.info()` and `df.describe()` on a sample dataset
- Encourage students to log questions as they explore

</details>

---

### Pandas and Polars Operations with Time Series

We focus on grouping, filtering, and resampling time-based agricultural data.

Key points:

- Grouping by geography or season
- Resampling daily data to weekly or monthly
- Handling missing timestamps

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Show a quick resampling example and discuss trade-offs
- Note differences between pandas and Polars APIs

</details>

---

### Descriptive Statistics for Farm Data

We calculate metrics that help explain yield, inputs, and environmental impacts.

Key points:

- Mean, median, variance, and percentiles
- Outlier detection and validation
- Comparing distributions across regions

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Use a histogram to show skewed yield data
- Remind students that outliers can be real events

</details>

---

### Visualization and Correlation Analysis

We turn statistical results into visual stories and relationships.

Key points:

- Histograms, scatter plots, line charts, heatmaps
- Correlation vs causation in agriculture
- Matching chart type to the question

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage clear labeling and consistent units
- Mention common visualization pitfalls to avoid

</details>

---

### AI for Alternative Metrics or Visualizations

We use AI tools to brainstorm new metrics or chart ideas.

Key points:

- Provide AI with schema and sample rows
- Validate AI output with domain knowledge
- Document AI-assisted insights

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Show a sample prompt and discuss why it works
- Reinforce that AI does not replace verification

</details>

---

### Demo: Python EDA Notebook Walkthrough

We walk through a full EDA notebook using row crop data.

Key points:

- Combine text, charts, and insights
- Build a reproducible notebook structure
- Export visuals for dashboards

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage students to save the notebook as a template
- Pause after each section so students can follow along

</details>

---

### Peer Share

Students share one insight and one visualization from their exploration.

Key points:

- Keep shares brief and focused
- Ask one follow-up question per share
- Capture ideas for future analysis

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Call on 3 to 5 volunteers
- Reinforce positive feedback and curiosity

</details>

---

## ✍️ Assignment

### Task: Row Crop Exploratory Data Analysis

**Objective:** Conduct a structured EDA and communicate insights with visuals.

**Instructions:**

1. Run EDA on a row crop yield or soil health dataset.
2. Create at least five visualizations that support key insights.
3. Summarize findings, correlations, and open questions.

**What to submit:** A Jupyter notebook with markdown commentary and embedded charts.

**Due:** TBD

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Emphasize quality of insights over number of charts
- Suggest a short insights section at the end of the notebook

</details>

---

## 🔗 Resources & References

### Official Sources

- [USDA NASS QuickStats](https://quickstats.nass.usda.gov/) - Baseline crop statistics for EDA

### Reading Materials

- [Exploratory Data Analysis](https://www.itl.nist.gov/div898/handbook/eda/eda.htm) - NIST EDA reference

### Tools

- [pandas](https://pandas.pydata.org/) - Data analysis toolkit
- [Polars](https://pola.rs/) - Fast DataFrame library
- [seaborn](https://seaborn.pydata.org/) - Statistical visualization library

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage students to compare pandas and Polars performance
- Point students to the NIST guide for deeper context

</details>

---
