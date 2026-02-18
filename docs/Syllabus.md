# Course Syllabus

> Agricultural Data Analytics Course – High-Level Overview

This syllabus outlines the structure of the **Agricultural Data Analytics Course**, including classes, topics, and assignments. Each class has a corresponding slide deck and Markdown outline to support AI‑assisted iteration and slide generation.

---

## Course Structure

- **Format**: Multi‑week, cohort‑style course.
- **Focus**: Practical agricultural data workflows (field data, remote sensing, geospatial analytics, dashboards) built around a real toolkit: [`agri-data-toolkit`](https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit).
- **Deliverables**: A series of targeted assignments plus a **final project dashboard** for row‑crop intelligence.

---

## Classes at a Glance

| Class | Title                                                                           | Type                 |
| ----- | ------------------------------------------------------------------------------- | -------------------- |
| 00    | Welcome Class                                                                   | Orientation          |
| 01    | The New Farm Frontier: Inside the Agricultural Data Revolution                  | Lecture + Discussion |
| 02    | Gearing Up: Building Your Smart Farm Workspace + Demo                           | Lecture + Demo       |
| 03    | Navigating the US Agricultural Data Landscape + Workshop                        | Lecture + Workshop   |
| 04    | Clean Fields, Clean Data + Demo                                                 | Lecture + Demo       |
| 05    | Exploratory Data Analysis: Finding Farm Insights + Demo                         | Lecture + Demo       |
| 06    | Geospatial Analysis with Python + Workshop & Demo                               | Lecture + Workshop   |
| 07    | Watching from Above: Satellite & Drone Intelligence + Workshop & Demo           | Lecture + Workshop   |
| 08    | Weather Patterns & Climate Data Analysis                                        | Lecture + Demo       |
| 09    | Advanced Spatial Integration & Transformations + Workshop                       | Lecture + Workshop   |
| 10    | US Precision Agriculture Systems & Real Farm Data                               | Lecture + Case Study |
| 11    | Soil Health & Sustainability Metrics + Workshop                                 | Lecture + Workshop   |
| 12    | From Data to Decisions: Building Dashboards that Tell a Story + Workshop & Demo | Lecture + Workshop   |
| 13    | Ethics, Ownership & the Politics of US Farm Data + Guest Speaker                | Guest + Discussion   |
| 14    | The Future Farm: Trends, Careers & Final Reflections                            | Wrap‑up + Reflection |

---

## Assignment Structure

Assignments are attached to specific classes and designed to build toward the **final project**.

| Class | Assignment Title                                             | Points | Notes                                |
| ----- | ------------------------------------------------------------ | ------ | ------------------------------------ |
| 00    | No assignment                                                | –      | Orientation only                     |
| 01    | Field Data Acquisition and Documentation                     | xx     | Hands‑on field/ground‑truth data     |
| 02    | No assignment                                                | –      |                                      |
| 03    | Field Data Acquisition and Documentation                     | xx     | Extension / deeper documentation     |
| 04    | Data Cleaning and Integration with Python & SQL              | xx     | Core data wrangling + integration    |
| 05    | Exploratory Data Analysis of Row Crop Fields                 | xx     | EDA + feature discovery              |
| 06    | Geospatial Mapping and Field Variability Visualization       | xx     | Spatial visualization & map products |
| 07    | Vegetation Index (NDVI) Calculation and Crop Health Analysis | xx     | Remote sensing & plant health        |
| 08    | Weather and Climate Trend Analysis for Row Crops             | xx     | Climate + weather analytics          |
| 09    | Integrated Spatial Analysis and Zonal Statistics             | xx     | Advanced spatial analytics           |
| 10    | No assignment                                                | –      | Focus on systems & case studies      |
| 11    | Soil Health and Sustainability Metrics Assessment            | xx     | Soil metrics & sustainability        |
| 12    | Final Project: Row Crop Intelligence Data Dashboard          | xx     | Capstone dashboard                   |
| 13    | No assignment                                                | –      | Ethics + guest speaker               |
| 14    | No assignment                                                | –      | Final reflections                    |

> **Note**: Replace `xx` with final point values once grading is locked in. The “No assignment” slots are intentionally open to allow for breathing room, catch‑up, and deeper in‑class work.

---

## Tools & Repositories

Students will work primarily from the **Agri Data Toolkit** and related docs:

- Main repository: [`SuperiorByteWorks-LLC/agri-data-toolkit`](https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit)
- Data sources overview: [`docs/data_sources.md`](https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit/blob/feature/ssurgo-soil-integration/docs/data_sources.md)

Key workflows include:

- Running data download scripts.
- Cleaning and integrating multi‑source datasets (field, USDA, weather, satellite, soils).
- Performing exploratory and geospatial analysis.
- Building a **row‑crop intelligence dashboard** that tells a coherent story.

---

## AI Usage Expectations

AI tools are **integrated into the course** as part of the professional workflow.

- **Primary AI tools**:
  - **Perplexity** (with GitHub integration) for research, API docs, code context, lightweight code edits, and GitHub project management tasks.
  - **VS Code + agent plugins** (e.g., Copilot, Roo Code) for inline assistance, structured refactors, and debugging.
- **Your responsibilities with AI**:
  - Provide high‑signal context in each prompt (code, errors, requirements).
  - Treat AI output as **drafts**, not ground truth.
  - Verify, test, and document any AI‑generated code or analysis before submitting.

> You’ll learn to **steer** models effectively, retry with different models, and design prompts that produce verifiable, reproducible work.

---

## Grading & Final Project

A detailed grading rubric can be added later once all point values are finalized, but at a high level:

- **Assignments**:
  - Reinforce individual skills (data wrangling, EDA, geospatial analysis, NDVI, weather, soil metrics, dashboards).
  - Typically graded for correctness, clarity, reproducibility, and documentation.
- **Final Project – Row Crop Intelligence Dashboard**:
  - Integrates:
    - Field and observational data.
    - Remote sensing and NDVI.
    - Weather and climate signals.
    - Soil health and sustainability metrics.
  - Evaluated on:
    - Data quality and pipeline robustness.
    - Insightfulness of metrics and visuals.
    - Quality of narrative (can a non‑technical stakeholder understand the story?).
    - Use of AI tools in a **disciplined, auditable** way.

---

## Per‑Class Markdown Files

Each class has (or will have) its own Markdown outline under `docs/classes/` to support AI‑driven slide iteration:

- `docs/classes/00-Welcome-Class.md` – Welcome, instructor intro, assignments structure, AI guidelines.
- `docs/classes/01-*.md` – The New Farm Frontier.
- `docs/classes/02-*.md` – Gearing Up: Smart Farm Workspace.
- `docs/classes/03-*.md` – US Agricultural Data Landscape.
- `docs/classes/04-*.md` – Clean Fields, Clean Data.
- `docs/classes/05-*.md` – Exploratory Data Analysis.
- `docs/classes/06-*.md` – Geospatial Analysis with Python.
- `docs/classes/07-*.md` – Satellite & Drone Intelligence.
- `docs/classes/08-*.md` – Weather Patterns & Climate Data.
- `docs/classes/09-*.md` – Advanced Spatial Integration.
- `docs/classes/10-*.md` – US Precision Agriculture Systems.
- `docs/classes/11-*.md` – Soil Health & Sustainability.
- `docs/classes/12-*.md` – Dashboards & Storytelling.
- `docs/classes/13-*.md` – Ethics & Farm Data Politics.
- `docs/classes/14-*.md` – Future Farm & Careers.

> As you flesh out later decks, mirror the **per‑slide numbered sections** used in `00-Welcome-Class.md` to keep things AI‑friendly and slide‑rendering‑friendly.
