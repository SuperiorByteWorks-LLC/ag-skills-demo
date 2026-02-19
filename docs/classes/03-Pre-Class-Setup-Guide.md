# Pre-Class Setup Guide — Class 03

_Navigating the US Agricultural Data Landscape_

---

## ⚙️ What You Need Before Class

Complete these before Class 03 starts:

| Item                       | Status | Notes                                      |
| -------------------------- | ------ | ------------------------------------------ |
| VS Code installed          | ☐      | [Download](https://code.visualstudio.com/) |
| AI assistant connected     | ☐      | OpenCode, Claude Code, or GitHub Copilot   |
| Template repository cloned | ☐      | From Class 02                              |
| GitHub secrets configured  | ☐      | Cloudflare + OpenRouter tokens             |
| agri-toolkit installed     | ☐      | `poetry install`                           |
| ~200 fields downloaded     | ☐      | Run download script                        |

> **Why this matters:** Class 03 is knowledge-focused (no live coding), but the workshop at the end uses your downloaded field data. If you're still on setup, that's okay — focus on getting the data download working.

---

## 🔧 Technical Foundations

This section explains the key tools and concepts for Class 03. Review before class if you're new to any of these.

### The Data Pipeline

```
┌────────────┐   ┌─────────┐   ┌────────┐   ┌─────────┐   ┌──────┐   ┌────────┐
│   Local    │ → │Terminal │ → │  Git   │ → │ GitHub │ → │ API  │ → │Python │ → │ Output│
│  Machine   │   │         │   │        │   │        │   │      │   │       │   │       │
│ (your PC)  │   │(commands)│  │(version)│  │ (cloud) │  │(data) │  │(process)│  │(files)│
└────────────┘   └─────────┘   └────────┘   └─────────┘   └──────┘   └────────┘   └────────┘
```

**What each step does:**

| Step     | Tool            | What It Is               | Class 03 Connection        |
| -------- | --------------- | ------------------------ | -------------------------- |
| Local    | VS Code         | Your code editor         | Where you'll write prompts |
| Terminal | CLI             | Command line interface   | Run Python scripts         |
| Git      | Version control | Tracks changes to code   | Commit your work           |
| GitHub   | Cloud repo      | Online code storage      | Push your projects         |
| API      | Data request    | Programmatic data access | Pull USDA/NASA data        |
| Python   | Processing      | Data analysis            | Transform and analyze      |
| Output   | Files           | Results (CSV, GeoJSON)   | Your final dashboard       |

### Key Terms for This Class

| Term                               | Plain English Definition                                            |
| ---------------------------------- | ------------------------------------------------------------------- |
| **Vector data**                    | Shapes on a map — points, lines, polygons (like field boundaries)   |
| **Tabular data**                   | Rows and columns — like a spreadsheet or database table             |
| **Raster/Imagery data**            | Grid of pixels — satellite photos, NDVI maps                        |
| **Time series**                    | Data collected over time — daily weather, yearly yields             |
| **GeoJSON**                        | A file format that stores geographic shapes as text                 |
| **geopandas**                      | Python library for working with map data                            |
| **pandas**                         | Python library for tables and time series                           |
| **numpy**                          | Python library for numerical arrays (images)                        |
| **API**                            | Application Programming Interface — how programs talk to each other |
| **Crop Sequence Boundaries (CSB)** | USDA's dataset of actual field boundaries across the US             |

---

## 🗂️ Visual Workflow — Class 03 Activities

This shows where each activity fits in the data pipeline:

```
1. KNOWLEDGE BUILDING (no computer needed)
   └─→ Understanding the Four Data Types

2. DATA SOURCE EXPLORATION
   └─→ Browsing USDA/NASA/NOAA portals (web browser → API)

3. TOOLKIT STATUS REVIEW
   └─→ What works now, what's coming (GitHub → Python)

4. WORKSHOP: AI FIELD VIEWER
   └─→ Local (write prompt) → AI generates HTML → Browser (view result)
```

---

## 🚨 Troubleshooting

### Common Issues Before Class 03

| Problem                    | Solution                                                                                                                                           |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poetry install fails       | Run: `poetry install --no-root`, then `poetry install`                                                                                             |
| No fields downloaded       | Try downloading 10 first: `python -c "from agri_toolkit.downloaders import FieldBoundaryDownloader; FieldBoundaryDownloader().download(count=10)"` |
| AI assistant not connected | Check VS Code extensions panel; reconnect OpenRouter secret                                                                                        |
| GitHub secrets not working | Verify in GitHub repo Settings → Secrets → Actions                                                                                                 |

### Where to Get Help

1. **Your AI assistant** — Paste the error message and ask for a fix
2. **Office hours** — Before/after class
3. **Class 02 materials** — Review setup steps

---

## 📋 Prep Checklist

Before Class 03 starts, confirm:

- [ ] I can open VS Code and see my project
- [ ] My AI assistant is responding to prompts
- [ ] I've tried downloading at least a few field boundaries
- [ ] I understand the four data types (vector, tabular, imagery, time series)
- [ ] I know what each data source provides (NASS, NRCS, FSA, NASA, NOAA, Sentinel-2, Landsat)

---

## 🔗 Quick Reference Links

- [Class 03 Main Document](./03-Navigating-the-US-Agricultural-Data-Landscape.md)
- [Assignment 1 Instructions](./assignments/01-project-setup-data-acquisition.md)
- [Class 02 Setup Guide](./02-Gearing-Up-Building-Your-Smart-Farm-Workspace.md)
- [agri-toolkit Repository](https://github.com/borealBytes/agri-data-toolkit)

---

**Last Updated:** 2026-02-18
**For Class:** 03 — Navigating the US Agricultural Data Landscape
**Instructor:** Clayton Young
