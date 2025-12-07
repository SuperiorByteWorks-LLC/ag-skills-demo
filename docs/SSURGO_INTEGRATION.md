# SSURGO Soil Data Integration

## Overview

This document tracks the integration of USDA NRCS SSURGO (Soil Survey Geographic Database) data into the agri-data-toolkit.

## SSURGO Background

SSURGO is the most detailed level of soil mapping produced by the USDA Natural Resources Conservation Service (NRCS). It provides:

- **Soil Properties**: Texture, depth, drainage, pH, organic matter, cation exchange capacity
- **Hydraulic Properties**: Infiltration rates, saturated hydraulic conductivity, available water capacity
- **Physical Properties**: Bulk density, particle size distribution, rock fragments
- **Chemical Properties**: pH, salinity, sodium adsorption ratio
- **Interpretive Data**: Land capability class, crop yield estimates, drainage class

## Data Access Methods

### 1. Soil Data Access (SDA) REST API
- Primary interface for programmatic access
- SQL-like queries against the SSURGO database
- Returns JSON or XML responses
- Endpoint: `https://SDMDataAccess.nrcs.usda.gov/`

### 2. Web Soil Survey
- Interactive web interface
- Area of Interest (AOI) definition
- Export capabilities for detailed reports

### 3. Bulk Downloads
- State-level SSURGO datasets
- File geodatabase or Shapefile format
- Updated quarterly

## Implementation Plan

### Phase 2.1: Basic SSURGO Queries
- Point location soil property lookup
- Map unit and component retrieval
- Basic soil texture and drainage class

### Phase 2.2: Advanced Queries
- Polygon/field boundary soil analysis
- Multi-layer soil profile data
- Hydraulic property calculations

### Phase 2.3: Analysis Tools
- Soil suitability assessment
- Available water capacity calculations
- Aggregated field-level statistics

## Data Model

### Hierarchy
```
Survey Area
  └─ Map Unit
      └─ Component (soil type)
          └─ Layer/Horizon
              └─ Properties
```

### Key Tables
- `mapunit`: Soil map unit polygons
- `component`: Soil components within map units (e.g., different soil types)
- `chorizon`: Soil horizon/layer data
- `chtexturegrp`: Texture information by horizon

## API Rate Limits and Caching

- SDA has no published rate limits but reasonable use is expected
- Implement local caching to minimize redundant queries
- Cache duration: 90 days (SSURGO quarterly update cycle)

## References

- [SSURGO Data Access](https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo)
- [Soil Data Access User Guide](https://sdmdataaccess.nrcs.usda.gov/)
- [SSURGO Metadata](https://www.nrcs.usda.gov/resources/data-and-reports/ssurgo/stats)

## Status

🚧 **In Progress** - Phase 2.1 implementation underway
