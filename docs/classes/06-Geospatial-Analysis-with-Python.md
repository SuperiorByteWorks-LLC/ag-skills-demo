# 06 - Geospatial Analysis with Python + Workshop and Demo

_Agricultural Data Systems_

---

## 🏠 Housekeeping

- **Use the "Q&A" feature** in Zoom for questions
- Keep your **camera on** during class if possible
- Please **mute yourself** to avoid interruptions
- Use the **"Raise hand"** feature when you want to speak (and lower it when finished)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Confirm students can open sample geospatial files
- Remind students to keep outputs in a dedicated geospatial folder

</details>

---

## 📋 Syllabus Review

Last class we explored datasets and surfaced patterns through EDA. Today we add spatial analysis in Python to map and interpret field-level data.

_This connects to Class 07 next week, where we work with satellite and drone imagery._

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Reinforce that most agricultural insights have a spatial dimension
- Note that CRS errors are common and worth double-checking

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Syllabus review
- [ ] GeoDataFrames and spatial data structures
- [ ] Shapefiles, geometries, and coordinate systems
- [ ] Reprojection and coordinate transformations
- [ ] Mapping and spatial visualization
- [ ] Workshop: Field boundary analysis
- [ ] Demo: Mapping US row crop fields

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Emphasize the workshop as the key hands-on component
- If time is short, compress the visualization section

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Create** GeoDataFrames and inspect spatial datasets
- **Explain** coordinate reference systems and why they matter
- **Reproject** data to align spatial layers accurately
- **Visualize** geospatial data for agricultural insights
- **Perform** basic spatial analysis on field boundaries

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Ask students to share one spatial question they want to answer
- Tie outcomes to the assignment map deliverable

</details>

---

## 📚 Content

### GeoDataFrames and Spatial Data Structures

We introduce GeoPandas and the data structures used to store spatial features.

Key points:

- Geometry columns and attribute tables
- Vector features: points, lines, polygons
- Common file inputs and outputs

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Show a quick `gdf.head()` and plot example
- Emphasize the link between geometry and attributes

</details>

---

### Shapefiles, Geometries, and Coordinate Systems

We review file formats and how coordinate systems define location and scale.

Key points:

- Shapefile components and alternatives
- CRS basics and EPSG codes
- Consequences of mismatched CRS

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Use a quick CRS mismatch example to show misalignment
- Encourage students to record CRS in their notes

</details>

---

### Reprojection and Coordinate Transformations

We convert datasets to compatible CRS for analysis and mapping.

Key points:

- When to reproject and why
- Choosing projections by region and purpose
- Verifying results after transformation

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Demonstrate a simple `to_crs` step
- Remind students to document original CRS

</details>

---

### Mapping and Spatial Visualization

We create maps that highlight spatial patterns in agricultural data.

Key points:

- Static vs interactive map options
- Color scales and readability
- Annotating maps for clarity

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Show a map with a clear legend and units
- Discuss how color choices affect interpretation

</details>

---

### Workshop: Field Boundary Analysis

Students work with field boundary data and perform spatial queries.

Key points:

- Load boundaries and intersect with other layers
- Calculate area and basic metrics
- Save outputs for downstream use

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage students to ask for help early if stuck
- Reinforce that errors are common in geospatial work

</details>

---

### Demo: Mapping US Row Crop Fields

We demonstrate a complete map workflow from raw boundaries to visualization.

Key points:

- Data loading, CRS checks, and plotting
- Adding contextual layers such as counties or states
- Exporting map visuals for reports

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Narrate each step and highlight best practices
- Encourage students to reuse the demo as a template

</details>

---

## ✍️ Assignment

### Task: Geospatial Field Analysis

**Objective:** Analyze field boundaries and produce a map-based summary.

**Instructions:**

1. Load and visualize field boundaries for your region.
2. Join boundaries with weather or soil data for context.
3. Create a map highlighting key spatial patterns.

**What to submit:** A notebook or report with maps, code, and interpretation notes.

**Due:** TBD

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage clear map titles, legends, and captions
- Remind students to document CRS choices

</details>

---

## 🔗 Resources & References

### Official Sources

- [USGS National Map](https://www.usgs.gov/programs/national-geospatial-program/national-map) - Base layers and boundaries

### Tools

- [GeoPandas](https://geopandas.org/) - Python geospatial library
- [Shapely](https://shapely.readthedocs.io/) - Geometry operations
- [QGIS](https://qgis.org/) - Desktop GIS for validation

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Recommend QGIS for troubleshooting spatial issues
- Point students to GeoPandas docs for examples

</details>

---
