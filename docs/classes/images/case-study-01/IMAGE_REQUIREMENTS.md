# Image Requirements for Case Study 1.01: Variable Rate Seeding in Corn

## Images Needed

### 1. FieldView Platform Screenshots
**Filename:** `fieldview-dashboard.png`
**Location in document:** After "Climate FieldView Platform Overview" section
**Specifications:**
- Resolution: 1920x1080 (Full HD for slide presentation)
- Format: PNG
- Content: Climate FieldView web dashboard showing field overview
**Source suggestion:** 
- Climate Corporation press kit: https://climate.com/media
- Screenshot from FieldView demo account
- Alternative: Search "Climate FieldView dashboard" on Unsplash or official Bayer press materials

### 2. FieldView Drive Hardware
**Filename:** `fieldview-drive-hardware.jpg`
**Location in document:** "FieldView Drive" subsection
**Specifications:**
- Resolution: 1200x800
- Format: JPG
- Content: FieldView Drive device plugged into tractor
**Source suggestion:**
- Climate Corporation product pages
- Agricultural equipment dealer websites
- Search: "FieldView Drive 2.0 device"

### 3. NDVI Corn Field Map
**Filename:** `corn-field-ndvi-zones.png`
**Location in document:** "Management Zone Delineation" section
**Specifications:**
- Resolution: 1600x1200
- Format: PNG
- Content: Corn field with NDVI color gradient showing productivity zones
**Source suggestion:**
- Sentinel Hub EO Browser examples
- Academic papers (ensure open license)
- Create from sample Sentinel-2 data

### 4. Variable Rate Prescription Map
**Filename:** `vrs-prescription-map.png`
**Location in document:** "Prescription Generation" section
**Specifications:**
- Resolution: 1600x1200
- Format: PNG
- Content: Field map with 3-5 zones showing different seeding rates
**Source suggestion:**
- University extension publications (Iowa State, Illinois)
- Academic paper figures (cite source)
- Generate from tutorial code in document

### 5. Corn Planter with VRA Equipment
**Filename:** `corn-planter-vra-equipment.jpg`
**Location in document:** "Equipment Upload & Application" section
**Specifications:**
- Resolution: 1600x1200
- Format: JPG
- Content: Modern corn planter showing precision planting monitor
**Source suggestion:**
- John Deere or Precision Planting press materials
- Agricultural equipment manufacturers
- Search: "precision planting 20|20 monitor"

### 6. Yield Map Comparison
**Filename:** `yield-map-uniform-vs-vrs.png`
**Location in document:** "Post-Season Analysis" section
**Specifications:**
- Resolution: 1920x1080 (side-by-side comparison)
- Format: PNG
- Content: Two yield maps side-by-side (uniform vs VRS year)
**Source suggestion:**
- Research papers with before/after data
- University on-farm trial results
- Generate from simulated data

### 7. Butler County Iowa Location Map
**Filename:** `butler-county-iowa-location.png`
**Location in document:** "Study Overview" section
**Specifications:**
- Resolution: 1200x900
- Format: PNG
- Content: Map showing Butler County location in Iowa
**Source suggestion:**
- Create using folium/matplotlib in Python
- USDA county maps
- Simple outline map from public domain sources

### 8. Soil Productivity Zones
**Filename:** `soil-productivity-zones.png`
**Location in document:** "Data Sources & Methodology" section
**Specifications:**
- Resolution: 1600x1200
- Format: PNG
- Content: Field with SSURGO soil types overlaid
**Source suggestion:**
- Web Soil Survey screenshot
- Create from SSURGO data download
- Tutorial code generates this

## Image Optimization Guidelines

### For Slide Presentation:
- **Minimum resolution:** 1200px on longest dimension
- **Ideal resolution:** 1920px (Full HD) for main figures
- **File size:** < 500KB per image (compress if needed)
- **Format:** PNG for maps/diagrams, JPG for photos
- **Color:** Ensure good contrast for projectors
- **Text:** Minimum 14pt font size if text in image

### Markdown Embedding Format:

```markdown
![Alt text description](images/case-study-01/filename.png)
*Figure X: Caption describing the image and its relevance*
```

## Copyright & Licensing

- **Preferred:** Creative Commons (CC-BY or CC-BY-SA)
- **Acceptable:** Fair use for educational purposes (cite source)
- **Generate original:** Use tutorial code where possible
- **Commercial sources:** Ensure proper licensing or permissions

## Next Steps

1. Search for images from suggested sources
2. Download at specified resolutions
3. Optimize file sizes (compress PNGs with pngquant, JPGs at 85% quality)
4. Rename according to specifications
5. Place in `/docs/classes/images/case-study-01/` directory
6. Update markdown document with proper image links
7. Test rendering in VS Code markdown preview
8. Verify images display correctly when exported to PDF/slides

