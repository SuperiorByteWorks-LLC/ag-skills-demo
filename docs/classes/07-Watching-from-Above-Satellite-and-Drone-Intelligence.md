# 07 - Watching from Above: Satellite and Drone Intelligence + Workshop and Demo

_Agricultural Data Systems_

---

## 🏠 Housekeeping

- **Use the "Q&A" feature** in Zoom for questions
- Keep your **camera on** during class if possible
- Please **mute yourself** to avoid interruptions
- Use the **"Raise hand"** feature when you want to speak (and lower it when finished)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Confirm students can access imagery files or portals
- Remind students about large file sizes and download time

</details>

---

## 📋 Syllabus Review

Last class we built geospatial analysis skills in Python. Today we focus on remote sensing and imagery workflows that reveal crop health at scale.

_This connects to Class 08 next week, where we analyze weather and climate drivers alongside imagery._

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Reinforce that imagery is a core input in modern ag analytics
- Mention that vegetation indices return in later assignments

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Syllabus review
- [ ] Remote sensing fundamentals
- [ ] NDVI and vegetation indices for crop health
- [ ] Satellite imagery sources (Sentinel-2, Landsat)
- [ ] Drone data collection and processing
- [ ] Workshop: NDVI analysis on crop fields
- [ ] Case study: Crop health monitoring
- [ ] Demo: Processing satellite and drone imagery

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Prioritize the workshop and demo if time is tight
- Encourage questions about imagery licensing and usage rights

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Explain** core remote sensing concepts and spectral bands
- **Compute** NDVI and interpret vegetation signals
- **Locate** open satellite imagery for agricultural analysis
- **Describe** how drone data is captured and processed
- **Analyze** crop health trends using imagery time series

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Ask students where imagery could improve their final projects
- Emphasize interpretation, not just computation

</details>

---

## 📚 Content

### Remote Sensing Fundamentals

We introduce how sensors capture reflected light and why agriculture relies on spectral data.

Key points:

- Spectral bands and reflectance signatures
- Spatial and temporal resolution trade-offs
- Common agricultural use cases

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Keep the physics practical and tied to examples
- Use a simple diagram if available

</details>

---

### NDVI and Vegetation Indices for Crop Health

We compute NDVI and discuss how indices highlight plant vigor.

Key points:

- NDVI formula and inputs
- Interpreting high vs low index values
- Limitations such as clouds and soil background

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Show an NDVI map and explain what it means
- Mention cloud masking as a key preprocessing step

</details>

---

### Satellite Imagery Sources (Sentinel-2, Landsat)

We review open imagery sources and how to download them.

Key points:

- Sentinel-2 for higher frequency coverage
- Landsat for long historical records
- Access portals and file formats

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Mention that source choice depends on resolution and coverage needs
- Encourage recording acquisition dates in metadata

</details>

---

### Drone Data Collection and Processing

We cover how drones capture imagery and how orthomosaics are generated.

Key points:

- Flight planning and ground control
- Orthorectification and mosaicking
- When drones outperform satellites

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Explain that drones offer higher resolution but higher effort
- Mention common drone processing tools

</details>

---

### Workshop: NDVI Analysis on Crop Fields

Students compute NDVI and compare results across fields or dates.

Key points:

- Load imagery and calculate NDVI
- Mask clouds or low quality pixels
- Summarize field-level statistics

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage students to annotate insights as they work
- Emphasize saving outputs for later assignments

</details>

---

### Case Study: Crop Health Monitoring

We review a real-world example of using imagery for crop stress detection.

Key points:

- Time-series NDVI trends
- Linking imagery to management decisions
- Lessons learned from the case study

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Ask students to interpret one chart before revealing conclusions
- Connect this case study to their final projects

</details>

---

### Demo: Processing Satellite and Drone Imagery

We demonstrate a full imagery workflow using Python tools.

Key points:

- Download, preprocess, and visualize imagery
- Compute indices and export outputs
- Document parameters for reproducibility

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Narrate each processing step clearly
- Remind students to track coordinate systems and units

</details>

---

## ✍️ Assignment

### Task: Satellite Crop Health Analysis

**Objective:** Use satellite imagery to evaluate crop health over time.

**Instructions:**

1. Download Sentinel-2 or Landsat imagery for a crop field.
2. Compute NDVI and at least one additional vegetation index.
3. Create a time-series visualization and document insights.

**What to submit:** A notebook or report with imagery outputs and interpretation notes.

**Due:** TBD

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Encourage students to include cloud masking notes
- Remind them to cite imagery sources

</details>

---

## 🔗 Resources & References

### Official Sources

- [Copernicus Data Space](https://dataspace.copernicus.eu/) - Sentinel imagery access
- [USGS Landsat](https://www.usgs.gov/landsat-missions) - Landsat mission data

### Tools

- [Google Earth Engine](https://earthengine.google.com/) - Cloud-based imagery analysis
- [Rasterio](https://rasterio.readthedocs.io/) - Python raster processing library
- [OpenDroneMap](https://www.opendronemap.org/) - Drone imagery processing toolkit

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Mention Earth Engine for browser-based workflows
- Encourage students to record data source metadata

</details>

---
