# 01 - The New Farm Frontier: Inside the Agricultural Data Revolution

_Agricultural Data Systems_

---

## 🏠 Housekeeping

- **Use the "Q&A" feature** in Zoom for questions
- Keep your **camera on** during class if possible
- Please **mute yourself** to avoid interruptions
- Use the **"Raise hand"** feature when you want to speak (and lower it when finished)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Before Class

- Verify all students completed Class 00 setup
- Check that data download script repository is accessible
- Prepare examples of agricultural data transformations

### Quick Reminders (2 minutes)

- "Welcome back! Hope you had time to set up your environment"
- "Today we dive into why agricultural data matters"
- "This is your first assignment class - we'll preview it at the end"

</details>

---

## 📋 Syllabus Review

Last week in Class 00, we introduced the course structure and got oriented. Today we begin our journey into the **agricultural data revolution** - exploring how data has transformed farming from intuition-based to evidence-driven decision-making.

This connects to Class 02 next week, where you'll build your smart farm workspace with the actual tools used in the industry.

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Connection to Previous (1 minute)

- "Last week was orientation - setup, tools, expectations"
- "Now we start the real content"
- Ask: "Who successfully cloned the repository?"

### Today's Focus (1 minute)

- "Today is about the 'why' before the 'how'"
- "Understanding the landscape before we build in it"
- "Real examples from my time at Monsanto and Climate Corp"

### Looking Ahead (30 seconds)

- "Next week: hands-on with your development environment"
- "Class 03: Deep dive into USDA and government data sources"

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Evolution of agricultural data (15 min)
- [ ] Key data types in modern farming (20 min)
- [ ] Real-world applications & case studies (20 min)
- [ ] Industry trends & challenges (10 min)
- [ ] Assignment preview (5 min)
- [ ] Q&A (5 min)

**Total:** 75 minutes

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- "Packed agenda today covering the full data landscape"
- "Mix of history, technical concepts, and real examples"
- "First assignment is introduced at the end"

### Pacing

- Evolution: 15 min (don't rush - sets context)
- Data types: 20 min (core learning)
- Case studies: 20 min (engagement and relevance)
- Trends: 10 min (quick overview)
- Assignment: 5 min (clear and actionable)

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Trace** the evolution of agricultural data from manual records to real-time IoT systems
- **Identify** the six major data types used in precision agriculture and their sources
- **Analyze** real-world case studies demonstrating data-driven farming decisions
- **Evaluate** current industry trends and challenges in agricultural data systems

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

"By end of class, you should understand:

1. Where ag data came from and where it's going
2. What types of data power modern farms
3. How real farms use this data to make decisions
4. What challenges the industry faces"

### Assessment Approach

- Outcome 1: Historical timeline discussion
- Outcome 2: Data type identification exercise
- Outcome 3: Case study analysis
- Outcome 4: Trends discussion and assignment

</details>

---

## 📚 Content

### The Evolution of Agricultural Data

**Pre-Digital Era (Before 1980s):**

- Manual record-keeping in notebooks and ledgers
- Visual field observations and farmer intuition
- Regional knowledge passed down through generations
- County extension agents collecting survey data
- Limited data sharing between farms

**Early Digital Age (1980s-1990s):**

- First computerized farm management systems
- GPS technology introduced to agriculture (1990s)
- Yield monitors on combines tracking harvest data
- Basic desktop software for record-keeping
- Still largely farm-specific, minimal integration

**Precision Agriculture Era (2000s-2010s):**

- Variable rate technology for inputs (seed, fertilizer)
- Remote sensing from satellites becomes accessible
- John Deere, Case IH, and others develop telematics
- Cloud platforms emerge (Climate FieldView, 2015)
- Data standardization efforts begin
- Integration across equipment manufacturers

**Modern Data Ecosystem (2020s-Present):**

- Real-time IoT sensors throughout fields
- AI/ML models predicting yield and detecting disease
- Digital twins of entire farm operations
- Drone imagery processed daily
- API-driven data sharing across platforms
- Sustainability and carbon credit verification
- Blockchain for supply chain transparency

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (15 minutes)

#### Set the Stage (2 minutes)

- "Let's go back 50 years"
- "Farmer walks their field, sees a problem, makes a decision"
- "Fast forward to today: sensors detect the problem before visible, AI recommends action, equipment auto-adjusts"

#### Walk Through Timeline (8 minutes)

**Pre-Digital (2 min):**

- Show example: old farm notebook (if image available)
- "Everything was observation-based"
- "Knowledge was local and experiential"

**Early Digital (2 min):**

- "GPS was game-changing - knowing exactly where you are in the field"
- "Yield monitors showed variability farmers knew existed but couldn't quantify"

**Precision Ag (2 min):**

- "This is when I entered the industry"
- "Climate Corp launched in 2006 - I joined in 2013"
- "We were building the platforms that are standard today"

**Modern Era (2 min):**

- "Now: terabytes of data per farm per season"
- "The challenge isn't getting data - it's making sense of it"
- "That's where you come in"

#### Interactive Element (3 minutes)

- Ask: "Anyone here from a farming family?"
- Ask: "What kind of data did your parents/grandparents track?"
- Compare to what's tracked now

#### Real-World Example (2 minutes)

- **Climate Corp Story:**
  - "In 2015, we processed data for 30 million acres"
  - "By 2020, over 100 million acres"
  - "That growth shows how fast adoption happened"

### Common Misconceptions

**Myth:** "Big farms use data, small farms don't"
**Reality:** "Adoption varies by crop and region, not just farm size. Many small specialty farms are data-intensive."

**Myth:** "Older farmers don't use technology"
**Reality:** "Age matters less than crop type and profitability. Corn/soy farmers of all ages adopted quickly."

</details>

---

### Key Data Types in Modern Farming

Modern precision agriculture relies on six primary data types, each providing unique insights:

#### 1. Field & Crop Data 🌾

**What It Is:**

- Planting dates and seed varieties
- Growth stage observations
- Harvest dates and yields
- Field boundaries and management zones
- Historical crop rotations

**Sources:**

- Farm management software (John Deere Operations Center, Climate FieldView)
- Yield monitors on combines
- Manual farmer observations
- USDA Farm Service Agency (FSA) records

**Why It Matters:**

- Establishes baseline performance
- Tracks year-over-year trends
- Enables zone-based management
- Required for crop insurance and USDA programs

#### 2. Remote Sensing Data 🛰️

**What It Is:**

- Satellite imagery (Sentinel-2, Landsat, Planet)
- Drone/UAV imagery
- Vegetation indices (NDVI, EVI, NDRE)
- Thermal imaging for water stress
- Multispectral and hyperspectral data

**Sources:**

- Free: Sentinel-2 (5-day revisit), Landsat (16-day)
- Commercial: Planet (daily), Maxar, Airbus
- Farm-owned drones
- Aerial imagery services

**Why It Matters:**

- Monitors crop health across entire fields
- Detects problems before visible to human eye
- Tracks growth patterns over time
- Validates field scouting
- Supports insurance claims

#### 3. Weather & Climate Data ⛅

**What It Is:**

- Historical weather (temperature, precipitation, humidity)
- Real-time conditions from on-farm weather stations
- Forecasts (7-day, seasonal, long-term)
- Growing degree days (GDD)
- Evapotranspiration (ET) estimates

**Sources:**

- NOAA (National Weather Service, Climate Data Online)
- On-farm IoT weather stations (Davis, Onset, Campbell Scientific)
- Commercial APIs (OpenWeatherMap, Weather Underground)
- University extension services

**Why It Matters:**

- Critical for planting and harvest timing
- Irrigation scheduling
- Disease pressure prediction
- Yield forecasting
- Crop insurance triggers

#### 4. Soil Data 🌱

**What It Is:**

- Soil type classifications (USDA SSURGO)
- Texture (sand, silt, clay percentages)
- Organic matter content
- pH and nutrient levels (N, P, K)
- Soil moisture (sensors or models)
- Compaction and drainage characteristics

**Sources:**

- USDA NRCS SSURGO database
- Lab tests (university labs, commercial services)
- On-farm soil moisture sensors
- Electromagnetic induction (EM) surveys
- Traditional soil sampling grids

**Why It Matters:**

- Determines management zones
- Guides fertilizer and lime application
- Predicts water-holding capacity
- Identifies problem areas (compaction, drainage)
- Required for conservation program compliance

#### 5. Equipment & IoT Data 🚜

**What It Is:**

- Tractor/combine GPS tracks
- Fuel consumption and efficiency
- Equipment health and maintenance alerts
- As-applied maps (seed, fertilizer, pesticide)
- Real-time implement performance

**Sources:**

- Telematics from John Deere, Case IH, AGCO
- Third-party IoT platforms (Raven, Trimble)
- CAN bus data from equipment
- Aftermarket sensors and trackers

**Why It Matters:**

- Verifies what was applied where
- Optimizes equipment utilization
- Reduces downtime through predictive maintenance
- Improves operator efficiency
- Documentation for sustainability reporting

#### 6. Market & Economic Data 📊

**What It Is:**

- Commodity prices (corn, soy, wheat, cotton)
- Futures and options data
- Basis (local vs futures price difference)
- Input costs (seed, fertilizer, fuel)
- Government program payments and subsidies

**Sources:**

- USDA NASS (prices, production reports)
- Chicago Board of Trade (CBOT)
- Local grain elevators
- DTN, FarmMarket ID, Barchart
- Farm Credit institutions

**Why It Matters:**

- Marketing decisions (when to sell grain)
- Input purchasing timing
- Profitability analysis
- Cash flow planning
- Risk management (insurance, hedging)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (20 minutes)

#### Overview First (2 minutes)

- "Six major data types power modern farms"
- "You'll work with all six in this course"
- "Each answers different questions"

#### Walk Through Each Type (3 min per type = 18 min)

For each data type:

1. Define it clearly
2. Show real example (screenshot, chart, map)
3. Explain a specific use case
4. Connect to upcoming assignments

**Field Data:**

- Show: Operations Center screenshot
- Example: "This farm planted corn on April 15, 2024"
- Assignment: "You'll document field data in Assignment 01"

**Remote Sensing:**

- Show: NDVI map progression
- Example: "See how green this field was in June, then stressed in July"
- Assignment: "Assignment 07 calculates NDVI"

**Weather:**

- Show: Precipitation chart
- Example: "Dry spell in July explains the stress we just saw"
- Assignment: "Assignment 08 analyzes weather trends"

**Soil:**

- Show: SSURGO soil type map
- Example: "Different soil types = different water-holding capacity"
- Assignment: "Assignment 11 uses SSURGO data"

**Equipment:**

- Show: As-applied fertilizer map
- Example: "Variable rate application - more N where soil is sandier"
- Connection: "This data proves sustainability claims"

**Market:**

- Show: Corn price chart
- Example: "Farmer decides when to sell based on price forecasts"
- Connection: "Economic data drives all management decisions"

### Interactive Elements

**After Each Type, Ask:**

- "Who has experience with this type of data?"
- "What questions could this data answer?"
- "What's a limitation of this data type?"

### Real-World Integration

**Climate Corp Example:**

- "We combined all six types in FieldView"
- "Farmer opens one dashboard, sees everything"
- "That's what you're building toward in Class 12"

</details>

---

### Real-World Applications & Case Studies

#### Case Study 1: Yield Optimization in Iowa Corn 🌽

**Farm Profile:**

- 2,000 acres in central Iowa
- Corn-soybean rotation
- Rolling terrain with variable soils

**The Challenge:**

- Yield varied 80-180 bu/acre across fields
- Couldn't explain why with just visual observations
- Applying uniform inputs across all acres

**Data-Driven Solution:**

1. **Soil Data:** SSURGO analysis identified 5 distinct soil types
2. **Historical Yield:** 10 years of yield maps showed consistent patterns
3. **Remote Sensing:** NDVI confirmed vegetation differences
4. **Created Management Zones:** Divided fields into 3 productivity zones
5. **Variable Rate Application:** Adjusted seed population and N rates by zone

**Results:**

- Average yield increased 8 bu/acre
- Reduced fertilizer costs by 12% (less N on low-yield zones)
- ROI: $45/acre profit increase
- 3-year payback on investment in precision equipment

#### Case Study 2: Water Management in California Almonds 🌱

**Farm Profile:**

- 640 acres of almonds in Central Valley
- Expensive water due to drought
- High-value crop requiring precision

**The Challenge:**

- Over-irrigation wasted water and leached nutrients
- Under-irrigation reduced yield and nut quality
- Uniform irrigation didn't account for soil variability

**Data-Driven Solution:**

1. **Soil Moisture Sensors:** Installed 30 sensors across orchard
2. **Weather Data:** Real-time ET calculation
3. **Remote Sensing:** Thermal imaging to detect water stress
4. **Soil Mapping:** EM survey identified zones with different water-holding capacity
5. **Variable Rate Irrigation:** Adjusted irrigation by zone

**Results:**

- Water use reduced 22%
- Yield maintained (no loss from reduced water)
- Water cost savings: $85,000/year
- Improved sustainability certification
- Better drought resilience

#### Case Study 3: Disease Detection in Minnesota Wheat 🌾

**Farm Profile:**

- 3,500 acres spring wheat
- Fusarium head blight (FHB) is major concern
- Large fields make scouting difficult

**The Challenge:**

- FHB can devastate yield and quality
- Traditional scouting catches problems too late
- Preventive fungicide expensive ($25/acre)
- Need to target application only where needed

**Data-Driven Solution:**

1. **Weather Modeling:** FHB risk model using temp + humidity data
2. **Drone Imagery:** Weekly flights during critical growth stages
3. **Multispectral Analysis:** Early detection of stressed areas
4. **Ground Truthing:** Targeted scouting of flagged zones
5. **Precision Application:** Fungicide only in high-risk areas (35% of field)

**Results:**

- Reduced fungicide costs by $44,000
- Maintained grain quality (no FHB damage)
- Yield protected in treated zones
- Reduced environmental impact of pesticides

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (20 minutes total)

#### Introduce Case Studies (1 minute)

- "Let's see how this plays out on real farms"
- "Three different crops, three different problems"
- "All solved with data"

#### Case Study 1: Iowa Corn (6 minutes)

**Set the Scene (1 min):**

- "Typical Midwest operation"
- "Problem: some areas yield great, others terrible"
- "Why? And what to do about it?"

**Walk Through Solution (3 min):**

- Show: side-by-side yield map + soil map
- Point out: "See how yield follows soil patterns?"
- Explain: "Once you see the pattern, you can manage differently"

**Discuss Results (1 min):**

- "8 bu/acre = $35,000 extra revenue on 2000 acres"
- "Paid for equipment in 3 years"
- "Now they use this every year"

**Connect to Class (1 min):**

- "You'll do this analysis in Class 06 and 09"
- "Same tools, same workflow"

#### Case Study 2: California Almonds (6 minutes)

**Set the Scene (1 min):**

- "California context: water is expensive and scarce"
- "Can't afford to waste it"
- "But almonds need precise water management"

**Walk Through Solution (3 min):**

- Show: soil moisture sensor data graph
- Show: thermal image showing water stress
- Explain: "Combining real-time sensors with remote sensing"

**Discuss Results (1 min):**

- "22% less water = $85K savings"
- "Plus sustainability benefits"
- "This is future of western agriculture"

**Connect to Class (1 min):**

- "Assignment 08: weather and ET"
- "Assignment 07: thermal imagery analysis"

#### Case Study 3: Minnesota Wheat (6 minutes)

**Set the Scene (1 min):**

- "Disease is farmers' nightmare"
- "Can wipe out a field in days"
- "Prevention is expensive"

**Walk Through Solution (3 min):**

- Show: FHB risk map from weather model
- Show: drone multispectral image highlighting stress
- Explain: "Data caught it early, saved the crop"

**Discuss Results (1 min):**

- "Treated 35% of field instead of 100%"
- "$44K savings in one season"
- "Yield protected where it mattered"

**Connect to Class (1 min):**

- "Assignment 07: vegetation indices for health monitoring"
- "This is exactly what you'll learn to calculate"

#### Wrap-Up (2 minutes)

- "Three crops, three problems, one solution: data"
- Ask: "What do these cases have in common?"
- Answer: "Targeted management based on spatial variability"
- "That's precision agriculture"

### Interactive Questions

**After Case 1:**
"What would happen if they applied MORE fertilizer to low-yield zones?"
(Answer: Waste money, environmental risk, still limited by soil)

**After Case 2:**
"Could this work in humid climates where water is abundant?"
(Answer: Yes - still saves costs and prevents over-irrigation damage)

**After Case 3:**
"Why not just treat the whole field to be safe?"
(Answer: Cost, environmental impact, fungicide resistance risk)

</details>

---

### Industry Trends & Challenges

#### Current Trends 📈

**1. Artificial Intelligence & Machine Learning**

- Yield prediction models (Climate Corp, Granular, Indigo Ag)
- Disease and pest detection from imagery
- Automated weed identification and spot-spraying
- Predictive maintenance for equipment
- Market forecasting and decision support

**2. Digital Twins & Simulation**

- Virtual replicas of farms for scenario testing
- "What if" analysis before making decisions
- Climate adaptation strategy modeling
- Used by Bayer, Syngenta, Corteva

**3. Carbon & Sustainability Verification**

- Data-driven carbon credit programs (Nori, Indigo, Truterra)
- Automated ESG reporting for food companies
- Blockchain for supply chain transparency
- Regenerative agriculture measurement

**4. Edge Computing & 5G**

- On-farm processing of sensor data
- Real-time decision-making without cloud latency
- Autonomous equipment coordination
- Enhanced connectivity in rural areas

**5. Open Data & Interoperability**

- AgGateway standards for data exchange
- APIs replacing proprietary silos
- Farmer data ownership initiatives
- Cross-platform data portability

#### Persistent Challenges ⚠️

**1. Data Interoperability**

- Different manufacturers use different formats
- Difficult to combine John Deere + Case IH data
- No universal standard (yet)
- Costs farmers time and money

**2. Data Ownership & Privacy**

- Who owns farm data? Farmer or platform provider?
- Concerns about data being used against farmers
- Antitrust issues with agribusiness consolidation
- Need for clear data contracts

**3. Digital Divide**

- Rural broadband gaps limit cloud platform use
- Older farmers less comfortable with technology
- Small farms can't afford precision equipment
- Unequal access to technical support

**4. Data Overload**

- Farmers drowning in data but starved for insights
- Too many dashboards and platforms
- Difficult to know what data actually matters
- Analysis paralysis

**5. Trust & Validation**

- AI recommendations sometimes don't match farmer experience
- "Black box" models reduce trust
- Need for transparent, explainable AI
- Importance of ground-truthing

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (10 minutes)

#### Trends (5 minutes)

**Set the Stage (1 min):**

- "Let's look at where the industry is heading"
- "These are the hot topics in agribusiness right now"

**Walk Through Trends (3 min):**

- AI/ML: "Every company is adding AI features - some useful, some hype"
- Digital twins: "Bayer uses these for product testing before field trials"
- Carbon: "Huge money in carbon credits - but requires data verification"
- Edge computing: "Solving the rural broadband problem"
- Open data: "Finally happening after years of farmer advocacy"

**Personal Experience (1 min):**

- "At Climate Corp, we were early to AI-driven recommendations"
- "Learned: farmers trust data they can verify"
- "Transparency beats fancy algorithms"

#### Challenges (5 minutes)

**Set Realistic Expectations (1 min):**

- "It's not all sunshine and precision"
- "Real problems that affect adoption"

**Walk Through Challenges (3 min):**

- Interoperability: "I dealt with this daily at Bayer - nightmare"
- Ownership: "Hotly debated - farmers are winning, slowly"
- Digital divide: "Real barrier for many rural operations"
- Data overload: "More isn't always better"
- Trust: "Explainability is crucial for adoption"

**Your Role (1 min):**

- "You're learning to solve these problems"
- "The industry needs people who understand both sides"
- "Technical skills + agricultural context = valuable"

### Discussion Questions

**Q: "Should farmers own their data?"**

- Take 2-3 opinions
- Nuance: "It's complicated - who creates value? Farmer or platform?"

**Q: "Is AI making decisions or just recommending?"**

- Discuss autonomy vs augmentation
- Farmer always has final say (for now)

</details>

---

## ✍️ Assignment

### Assignment 01: Field Data Acquisition and Documentation

**Objective:** Establish a foundational dataset for a study field by documenting key agricultural data points and creating a repeatable workflow for field observations.

**Your Challenge:**

You'll select a real or simulated agricultural field and document core field data that will be used throughout the course. This establishes your "ground truth" for all future analyses.

**Instructions:**

1. **Select Your Study Field** (30 min)
   - Choose a real field if you have farm access, or select from provided sample fields
   - Define field boundaries (lat/lon coordinates or shapefile)
   - Document field size (acres), location (county, state), and primary crop

2. **Gather Field Information** (1 hour)
   - Planting date and crop variety
   - Historical crop rotation (last 3 years minimum)
   - Management practices (tillage, irrigation if applicable)
   - Any known issues (drainage problems, pest pressure, etc.)

3. **Create Data Documentation** (1 hour)
   - Build a structured markdown or CSV file with all field data
   - Include data sources and collection dates
   - Add relevant images or maps if available
   - Follow provided template structure

4. **Push to GitHub** (30 min)
   - Create folder in your repository: `assignments/01-field-data/`
   - Commit your documentation file
   - Include README explaining your field selection

**Deliverable:**

Submit to Canvas:

- GitHub repository URL containing `assignments/01-field-data/` folder
- Must include:
  - Field documentation file (markdown or CSV)
  - Field boundary file (GeoJSON, shapefile, or coordinates)
  - README with field description and data sources
  - At least one image or map of the field

**Due:** [Check Canvas for specific date and time]

**Grading Criteria:**

- Completeness of field documentation (40%)
- Data accuracy and proper sourcing (30%)
- File organization and GitHub structure (20%)
- Documentation clarity and professionalism (10%)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Assignment Overview (5 minutes)

#### Introduce Purpose (1 minute)

- "This field becomes your case study for the entire course"
- "Every future assignment builds on this"
- "Choose carefully - you'll work with it for 14 weeks"

#### Walk Through Steps (2 minutes)

- Step 1: "Pick a field - real if possible, simulated if not"
- Step 2: "Document what's there - crop, practices, history"
- Step 3: "Structure it properly - we provide templates"
- Step 4: "Get it into GitHub - practice your workflow"

#### Address Common Questions (1 minute)

**Q: "What if I don't have access to a real field?"**
A: "Sample fields are provided from Iowa, Illinois, California"

**Q: "How detailed does documentation need to be?"**
A: "As much as you can gather. More is better, but minimum requirements in rubric."

**Q: "Can I change fields later?"**
A: "Possible but not recommended. Pick one you can stick with."

#### Show Example (1 minute)

- Display sample field documentation
- Point out key elements
- Show what good structure looks like

### Grading Notes

- Looking for effort and completeness, not perfection
- Real field > simulated field (bonus points for real data)
- Good documentation now saves time later
- This is your foundation - take it seriously

</details>

---

## 🔗 Resources & References

### Required Reading

- [Precision Agriculture in the 21st Century](https://www.usda.gov/sites/default/files/documents/precision-agriculture-report.pdf) - USDA overview of precision ag technologies
- [The Climate Corporation: Data Science in Agriculture](https://climate.com/about-us) - Company background and approach

### Industry Reports

- [Precision Agriculture Market Size Report 2024](https://www.grandviewresearch.com/industry-analysis/precision-farming-market) - Market trends and growth projections
- [Farm Data Ownership and Privacy](https://www.fb.org/issues/technology/data-privacy) - American Farm Bureau perspective

### Historical Context

- [History of Precision Agriculture](https://extension.psu.edu/the-evolution-of-precision-agriculture) - Penn State Extension
- [GPS in Agriculture Timeline](https://www.precisionag.com/market-watch/the-evolution-of-gps-in-agriculture/) - Technology adoption history

### Data Sources Introduced Today

- [USDA NASS](https://www.nass.usda.gov/) - National Agricultural Statistics Service
- [Sentinel-2 Data](https://scihub.copernicus.eu/) - Free satellite imagery
- [SSURGO Soil Data](https://websoilsurvey.nrcs.usda.gov/) - USDA soil survey database
- [NOAA Climate Data](https://www.ncdc.noaa.gov/) - Historical weather data

### Companies Mentioned

- [Climate FieldView](https://climate.com/fieldview) - Bayer digital agriculture platform
- [John Deere Operations Center](https://www.deere.com/en/technology-products/precision-ag-technology/operations-center/) - Farm management platform
- [Indigo Ag](https://www.indigoag.com/) - Carbon credits and marketplace

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Resource Guidance (2 minutes)

- "Required reading gives you broader context"
- "Industry reports show where money and jobs are"
- "Data sources - you'll use all of these in assignments"
- "Company links - explore what they're building"

### Encourage Exploration

- "Not all resources are required for assignment"
- "But they'll help you understand the industry"
- "Especially useful if you're interested in ag careers"

</details>

---
