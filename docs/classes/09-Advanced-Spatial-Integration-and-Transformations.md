# 09 - Advanced Spatial Integration and Transformations + Workshop

_Agricultural Data Systems_

---

## 🏠 Housekeeping

- **Use the "Q&A" feature** in Zoom for questions
- Keep your **camera on** during class if possible
- Please **mute yourself** to avoid interruptions
- Use the **"Raise hand"** feature when you want to speak (and lower it when finished)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Confirm students can load prior geospatial outputs
- Remind students to bring their field boundary datasets

</details>

---

## 📋 Syllabus Review

Last class we learned geospatial analysis foundations. Today we combine multiple spatial layers and perform advanced transformations to create richer insights.

_This connects to Class 10 next week, where we explore real precision agriculture systems and data._

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Emphasize that integration is where spatial insights become actionable
- Remind students to track CRS choices carefully

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Syllabus review
- [ ] Overlaying spatial datasets
- [ ] Coordinate transformations and reprojection
- [ ] Zonal statistics and spatial aggregation
- [ ] Buffer operations and proximity analysis
- [ ] Workshop: Integrated field analysis
- [ ] QGIS demo and workflow automation

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- If time is tight, shorten the QGIS demo and focus on the workshop
- Encourage students to ask questions about join logic

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Integrate** multiple spatial layers into a single analysis view
- **Transform** spatial datasets to align projections and datums
- **Compute** zonal statistics for agricultural zones
- **Apply** buffer and proximity analysis to spatial questions
- **Automate** spatial workflows using QGIS or Python

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Ask students which spatial layer combinations they expect to use most
- Tie outcomes to the final project spatial workflow

</details>

---

## 📚 Content

### Overlaying Spatial Datasets

We combine field boundaries, weather grids, soil maps, and imagery layers.

Key points:

- Choosing a primary layer and join logic
- Handling mismatched geometries
- Validating overlay results

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Use a simple overlay example to show intersection results
- Emphasize checking row counts and geometry validity

</details>

---

### Coordinate Transformations and Reprojection

We apply advanced CRS and datum transformations for accurate overlays.

Key points:

- Identifying transformation requirements
- Choosing projection for distance and area calculations
- Verifying alignment after reprojection

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Highlight the difference between geographic and projected CRS
- Remind students to document CRS decisions

</details>

---

### Zonal Statistics and Spatial Aggregation

We compute statistics within boundaries to summarize spatial layers.

Key points:

- Mean, median, and percentile summaries
- Aggregating rasters to polygons
- Comparing zones across fields or seasons

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Show a simple zonal stats example
- Mention common pitfalls with nodata values

</details>

---

### Buffer Operations and Proximity Analysis

We analyze spatial relationships using distance-based methods.

Key points:

- Buffering features to assess influence zones
- Proximity to waterways, roads, or storage facilities
- Decision support use cases

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Ask students how proximity could affect farm decisions
- Emphasize that buffer distance must be justified

</details>

---

### Workshop: Integrated Field Analysis

Students build an integrated spatial dataset using multiple layers.

Key points:

- Combine field boundaries with weather and soil layers
- Compute zonal summaries
- Export a clean analysis table

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage students to validate each join step
- Remind them to save intermediate outputs

</details>

---

### QGIS Demo and Workflow Automation

We demonstrate a spatial workflow in QGIS and discuss automation options.

Key points:

- Visual validation of overlays
- Using QGIS for quick inspection
- Automating steps with Python or QGIS models

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Keep the demo focused on a few key actions
- Encourage students to use QGIS as a debugging tool

</details>

---

## ✍️ Assignment

### Task: Integrated Spatial Analysis

**Objective:** Combine multiple spatial datasets and produce a summarized analysis output.

**Instructions:**

1. Integrate field boundaries with weather, soil, and satellite data.
2. Perform zonal statistics to summarize key metrics.
3. Create a short report describing spatial patterns and findings.

**What to submit:** A notebook or report with maps, outputs, and interpretation notes.

**Due:** TBD

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage clear tables and annotated maps
- Remind students to note CRS and data sources

</details>

---

## 🔗 Resources & References

### Official Sources

- [USGS National Map](https://www.usgs.gov/programs/national-geospatial-program/national-map) - Base layers and boundaries

### Tools

- [QGIS](https://qgis.org/) - GIS desktop toolkit
- [GeoPandas](https://geopandas.org/) - Python geospatial analysis
- [PostGIS](https://postgis.net/) - Spatial database extension

### Reading Materials

- [PROJ Documentation](https://proj.org/) - CRS and transformation reference

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage practice in both QGIS and Python
- Emphasize documenting CRS transformations

</details>

---
