# Welcome Class (Class 00)

> Agricultural Data Analytics Course  
> Instructor: Clayton Young

---

## Slide 1 – Welcome Class Title

- **Course**: Agricultural Data Analytics Course
- **Class**: 00 – Welcome Class
- **Instructor**: Clayton Young

---

## Slide 2 – Class Agenda

- **Instructor intro**
- **Course structure**
- **Assignments & final project overview**
- **Introduction to the data download script**

---

## Slide 3 – Instructor Intro: Clayton Young

- Lead Data Engineer with nearly two decades in AgriTech, shaping large-scale data ecosystems at Bayer, Monsanto, and The Climate Corporation.
- Led data engineering initiatives at Bayer — one of the world’s largest agricultural and life sciences companies (€22.3B revenue in 2024), driving innovation in sustainable farming and agri‑data systems.
- Built a foundation in agricultural data science as a research technician, turning academic insights into real‑world agricultural solutions.
- Spent 6 years at Monsanto and 4 at The Climate Corporation, developing data platforms that powered precision agriculture and climate‑resilient decision‑making.
- Guided data integration through major industry transitions, from Monsanto’s acquisition of The Climate Corporation to Bayer’s global consolidation, gaining a unique perspective across the full AgriTech ecosystem.

---

## Slide 4 – Product Management Partner (Placeholder)

> **Note**: Slide content to be added (PM/producer introduction).  
> Keep this slide reserved for the program manager / class company introduction.

- Placeholder title: **Program & Logistics Partner**
- Bullet ideas (to be refined later):
  - Who they are and their role in the cohort.
  - How communication, scheduling, and logistics will flow.
  - Where to go for non-technical support.

---

## Slide 5 – Housekeeping & Zoom Etiquette

- **Use the “Q&A” feature** in Zoom if you want to ask a question.
- Ensure Zoom is updated to the latest version to use all features.
- Keep your **camera on** during class if possible.
- Please **mute yourself** so you don’t accidentally interrupt the instructor.
- Use the **“Raise hand”** feature in Zoom when you want to ask a question.
- Don’t forget to **lower your hand** once finished.

---

## Slide 6 – Course Overview (Syllabus Snapshot)

> High-level view of where this Welcome Class fits in the overall course.

| Class | Title                                                                           |
| ----- | ------------------------------------------------------------------------------- |
| 01    | The New Farm Frontier: Inside the Agricultural Data Revolution                  |
| 02    | Gearing Up: Building Your Smart Farm Workspace + Demo                           |
| 03    | Navigating the US Agricultural Data Landscape + Workshop                        |
| 04    | Clean Fields, Clean Data + Demo                                                 |
| 05    | Exploratory Data Analysis: Finding Farm Insights + Demo                         |
| 06    | Geospatial Analysis with Python + Workshop & Demo                               |
| 07    | Watching from Above: Satellite & Drone Intelligence + Workshop & Demo           |
| 08    | Weather Patterns & Climate Data Analysis                                        |
| 09    | Advanced Spatial Integration & Transformations + Workshop                       |
| 10    | US Precision Agriculture Systems & Real Farm Data                               |
| 11    | Soil Health & Sustainability Metrics + Workshop                                 |
| 12    | From Data to Decisions: Building Dashboards that Tell a Story + Workshop & Demo |
| 13    | Ethics, Ownership & the Politics of US Farm Data + Guest Speaker                |
| 14    | The Future Farm: Trends, Careers & Final Reflections                            |

---

## Slide 7 – Assignments & Final Project (Overview)

> This slide sets expectations for assignments and the final project at a high level.

- You will complete **targeted assignments** aligned to specific classes (e.g., data cleaning, NDVI, weather analysis, spatial integration, EDA, soil health, dashboards).
- Several classes are **“no assignment”** sessions (e.g., orientation, ethics, final reflections).
- The **final project** brings everything together into a **Row Crop Intelligence Data Dashboard** built on real data and workflows used in class.

---

## Slide 8 – Assignment Structure (Per Class)

> This mirrors the slide table structure, with placeholders where the original deck uses “xx points.”

| Class | Assignment Title                                             | Points |
| ----- | ------------------------------------------------------------ | ------ |
| 00    | No assignment                                                | –      |
| 01    | Field Data Acquisition and Documentation                     | xx     |
| 02    | No assignment                                                | –      |
| 03    | Field Data Acquisition and Documentation                     | xx     |
| 04    | Data Cleaning and Integration with Python & SQL              | xx     |
| 05    | Exploratory Data Analysis of Row Crop Fields                 | xx     |
| 06    | Geospatial Mapping and Field Variability Visualization       | xx     |
| 07    | Vegetation Index (NDVI) Calculation and Crop Health Analysis | xx     |
| 08    | Weather and Climate Trend Analysis for Row Crops             | xx     |
| 09    | Integrated Spatial Analysis and Zonal Statistics             | xx     |
| 10    | No assignment                                                | –      |
| 11    | Soil Health and Sustainability Metrics Assessment            | xx     |
| 12    | Final Project: Row Crop Intelligence Data Dashboard          | xx     |
| 13    | No assignment                                                | –      |
| 14    | No assignment                                                | –      |

> **Note**: Replace `xx` with specific point values once the grading scheme is finalized.

---

## Slide 9 – Introduction to the Data Download Script

- Repository: [`borealBytes/agri-data-toolkit`](https://github.com/borealBytes/agri-data-toolkit)
- Key documentation: [`docs/data_sources.md`](https://github.com/borealBytes/agri-data-toolkit/blob/feature/ssurgo-soil-integration/docs/data_sources.md)
- You’ll use the script to:
  - Download core datasets used throughout the course.
  - Explore metadata and understand what each source contributes.
  - Establish a **repeatable, automated pipeline** for data access.

---

## Slide 10 – AI Concepts to Keep in Mind

> This slide sets expectations for how AI tools will be used and where their limits are.

- You’ll use AI to:
  - Troubleshoot code errors.
  - Understand documentation and APIs.
  - Generate test data.
  - Draft analysis explanations.
  - Iterate on dashboard requirements.
- **AI tools we’re using:**
  - **Perplexity** (with GitHub integration) for research, API docs, code context, basic code edits, and GitHub project management.
  - **VS Code + agent plugins** (Copilot, Roo Code, and possibly others) for inline assistance while coding and debugging, reviewing code, making complex edits, testing, and other development activities.
- **AI model limits:**
  - Can hallucinate or give inconsistent answers.
  - Do not remember context between sessions.
- **Your job:**
  - Use AI to speed you up, but **you verify everything**.
  - Produce outputs you can **trust, cite, and turn in with confidence**.

---

## Slide 11 – AI Use Key Fundamentals: Context Is Everything

- Every time you ask an AI tool a question, it starts fresh — it does **not** remember previous messages in a persistent way.
- **What to do:**
  - Paste the full error message.
  - Include the relevant code.
  - Include assignment requirements.
  - Describe what you expected to happen.
- **Why it matters:**
  - High‑signal, concrete context reduces hallucinations.
  - Noisy or incomplete context leads to generic, low‑value answers.
- **In practice:**
  - ❌ “How do I fix this error?”
  - ✅ _\[error message + code snippet + “I’m trying to download Sentinel‑2 data but getting a timeout after 10 seconds”\]_

---

## Slide 12 – AI Use Key Fundamentals: Retry, and with Different Models

- If a model (GPT‑4, Claude, an open‑source model, etc.) doesn’t give you a useful answer, **try a different one**.
- Different models have different strengths — one might miss a bug that another catches immediately.
- In practice:
  - Perplexity lets you select among multiple models.
  - VS Code agents may have different backends / plugins. Try both.
- Why it matters:
  - Models are trained differently. What’s obvious to one may not be to another.
  - Retrying catches issues you’d otherwise miss.

> Additional depth (for instructor notes): You can briefly mention “temperature” and model randomness here — higher temperature = more variation across retries; lower temperature = more deterministic.
