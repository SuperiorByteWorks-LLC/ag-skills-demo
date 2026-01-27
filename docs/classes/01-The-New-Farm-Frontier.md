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
- Have case study files 01.01 and 01.02 ready for detailed discussion

### Quick Reminders (2 minutes)

- "Welcome back! Hope you had time to set up your environment"
- "Today we dive into why agricultural data matters"
- "We'll look at real case studies showing data driving actual farm decisions"
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
- "Real examples from actual research papers and my time at Climate Corp"
- "Two detailed case studies with real numbers"

### Looking Ahead (30 seconds)

- "Next week: hands-on with your development environment"
- "Class 03: Deep dive into USDA and government data sources"

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Evolution of agricultural data (15 min)
- [ ] Key data types in modern farming (20 min)
- [ ] Real-world case studies with numbers (20 min)
- [ ] Industry trends & challenges (10 min)
- [ ] Assignment preview (5 min)
- [ ] Q&A (5 min)

**Total:** 75 minutes

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- "Packed agenda today covering the full data landscape"
- "Mix of history, technical concepts, and real case study examples"
- "The case studies will show you actual research findings with numbers"
- "First assignment is introduced at the end"

### Pacing

- Evolution: 15 min (don't rush - sets context)
- Data types: 20 min (core learning)
- Case studies: 20 min (engagement and relevance - this is the new stuff)
- Trends: 10 min (quick overview)
- Assignment: 5 min (clear and actionable)

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Trace** the evolution of agricultural data from manual records to real-time IoT systems
- **Identify** the six major data types used in precision agriculture and their sources
- **Analyze** real-world case studies demonstrating data-driven farming decisions with quantified outcomes
- **Evaluate** current industry trends and challenges in agricultural data systems

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

"By end of class, you should understand:

1. Where ag data came from and where it's going
2. What types of data power modern farms
3. How real farms use this data to make decisions (with numbers)
4. What challenges the industry faces"

### Assessment Approach

- Outcome 1: Historical timeline discussion
- Outcome 2: Data type identification exercise
- Outcome 3: Case study analysis with quantification
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
- "By 2020, we managed data for 100+ million acres"

**Modern Era (2 min):**

- "Now: terabytes of data per farm per season"
- "The challenge isn't getting data - it's making sense of it"
- "That's where you come in"

#### Interactive Element (3 minutes)

- Ask: "Anyone here from a farming family?"
- Ask: "What kind of data did your parents/grandparents track?"
- Compare to what's tracked now

### Real-World Example

- "Climate Corp growth shows adoption velocity: 30M acres (2015) → 100M acres (2020)"

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

### Real-World Integration

- "We combined all six types in FieldView"
- "Farmer opens one dashboard, sees everything"
- "That's what you're building toward in Class 12"

</details>

---

### Real-World Applications & Case Studies

#### Case Study 01.03: NASA Harvest - Satellite Data for Global Food Security

**Focus:** 🛰️ **Global → Commercial → Local analysis of satellite agricultural data**  
**Program:** NASA Harvest (2017-present), 40+ countries  
**Core Question:** When data is technically free but practically inaccessible, who benefits?

**The Three-Scale Challenge:**

Satellite data seems like the perfect public good - NASA provides petabytes of imagery free to everyone. But the reality is more complex:

```mermaid
graph TB
    subgraph "🌍 **Global Scale**"
        A[**Free Satellite Data**<br/>Landsat, Sentinel-2, MODIS<br/>128+ petabytes archived]
    end
    
    subgraph "🏢 **Commercial Users**"
        B[**Commodity Traders**<br/>Yield forecasts<br/>3-6 week lead time]
        C[**Insurance Companies**<br/>Automated claims<br/>Parametric products]
    end
    
    subgraph "👨‍🌾 **Farmer Access**"
        D[**U.S. Farmer**<br/>30-40% adoption<br/>Direct satellite access]
        E[**Smallholder Farmer**<br/>5% access<br/>Infrastructure barriers]
    end
    
    A --> B
    A --> C
    A --> D
    A -.Multiple Barriers.-> E
    
    classDef global fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    classDef commercial fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef farmer fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    classDef barrier fill:#ffebee,stroke:#c62828,stroke-width:2px
    
    class A global
    class B,C commercial
    class D farmer
    class E barrier
```

**Key Statistics:**

- **Global Level:** 200+ million hectares monitored, 8+ million users, 4.5 billion files downloaded annually
- **Commercial Level:** $200-300M annual satellite analytics market, major users include Cargill, Archer Daniels Midland
- **U.S. Farmers:** 30-40% use satellite-based crop monitoring (integrated into farm management platforms)
- **Smallholder Farmers:** <5% have meaningful satellite data access despite representing majority of global farmers

**The Digital Divide:**

| Access Metric                    | U.S. Farmers | Sub-Saharan Africa Smallholders | Gap    |
| -------------------------------- | ------------ | ------------------------------- | ------ |
| Smartphone ownership             | 85%+         | 30-50%                          | **40%pts**  |
| Satellite data adoption          | 30-40%       | <5%                             | **30%pts**  |
| Mobile data cost (% of income)   | 1-2%         | 5-15%                           | **8x higher** |
| Agricultural extension access    | High         | 1:1000-5000 agent:farmer ratio  | **10-50x worse** |

**Speaker Note Detail:** This case study shifts focus from technical precision ag to examining how the same "public" data infrastructure creates vastly different outcomes for different farmers globally.

<details>
<summary><strong>💬 Speaker Notes - NASA Harvest Overview</strong></summary>

### Setup (2 minutes)

- "NASA provides free satellite data - Landsat, Sentinel-2, MODIS, all public domain"
- "Sounds democratic: same data available to everyone"
- "Reality: access barriers turn 'free' data into unequal outcomes"

### The Three Scales (2 minutes)

**Global:**
- "NASA Harvest: 40+ countries, petabytes of data"
- "GEOGLAM Crop Monitor: monthly global crop assessments"
- "FEWS NET: famine early warning for 40 countries"

**Commercial:**
- "Trading firms use satellite data for yield forecasts weeks before USDA reports"
- "Insurance companies automate claims with satellite vegetation indices"
- "$200-300M market for satellite analytics services"

**Local (the gap):**
- "U.S. farmer: checks satellite alerts on smartphone over morning coffee"
- "Ugandan smallholder: heard about 'the satellite that tells when rain comes' but can't access it"
- "Same satellites, completely different farmer experiences"

### Why This Matters (1 minute)

- "Data infrastructure isn't neutral - it reflects and amplifies existing inequalities"
- "You'll work with satellite data in Module 04 and Assignment 4-2"
- "But consider: who benefits from the tools you build?"

**Full case study:** See `docs/classes/01.03-case-study-nasa-harvest.md` for 15,000-word deep dive

</details>

---

#### Case Study 01.03 (cont.): Global Satellite Infrastructure

**The Satellite Systems Behind Agricultural Monitoring:**

Four key satellites provide different agricultural capabilities:

| Satellite      | Resolution | Revisit Time | Key Agriculture Use              |
| -------------- | ---------- | ------------ | -------------------------------- |
| **Landsat 8/9**    | 30 meters  | 16 days      | Field-level mapping, 50-year historical record |
| **Sentinel-2 A/B** | 10 meters  | 5 days       | Active crop monitoring, frequent updates |
| **MODIS**          | 250-500m   | 1-2 days     | Regional yield forecasting, daily coverage |
| **SMAP**           | 9-36 km    | 2-3 days     | Soil moisture, irrigation planning |

**The Data Flow:**

```mermaid
flowchart LR
    subgraph Space["🛰️ **Space**"]
        S1[**Satellites**<br/>Continuous imaging]
    end
    
    subgraph Processing["☁️ **NASA Processing**"]
        P1[**Atmospheric<br/>Correction**]
        P2[**Index Calculation**<br/>NDVI, EVI, NDWI]
    end
    
    subgraph Products["📊 **Products**"]
        PR1[**Crop Type Maps**]
        PR2[**Yield Forecasts**]
        PR3[**Drought Indices**]
    end
    
    subgraph Users["👥 **Users**"]
        U1[**Governments**<br/>USDA, FAO]
        U2[**Commercial**<br/>Traders, Insurers]
        U3[**NGOs**<br/>FEWS NET, WFP]
        U4[**Farmers**<br/>via intermediaries]
    end
    
    S1 --> P1
    P1 --> P2
    P2 --> PR1
    P2 --> PR2
    P2 --> PR3
    
    PR1 --> U1
    PR2 --> U2
    PR3 --> U3
    PR1 -.Limited Access.-> U4
    
    classDef space fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef process fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef product fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef user fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    
    class S1 space
    class P1,P2 process
    class PR1,PR2,PR3 product
    class U1,U2,U3,U4 user
```

**Global Programs Using This Data:**

- **GEOGLAM (Group on Earth Observations):** G20-backed monthly crop assessments for wheat, maize, rice, soybeans
- **AMIS (Agricultural Market Information System):** Market transparency to prevent food price crises
- **FEWS NET:** Famine early warning in 40 countries, operated since 1985
- **NASA Harvest:** Coordinates satellite ag monitoring across 40+ countries

**Speaker Note Detail:** The infrastructure is impressive - billions invested in satellites and processing. But notice the user types: governments, commercial companies, NGOs. Individual farmers are "via intermediaries" - they don't directly access this system.

<details>
<summary><strong>💬 Speaker Notes - Global Infrastructure</strong></summary>

### The Satellite Constellation (2 minutes)

- "Four satellites, four different capabilities"
- "Landsat: best historical record (50 years)"
- "Sentinel-2: best for active monitoring (5-day revisit)"
- "MODIS: daily global coverage, coarser resolution"
- "SMAP: soil moisture through clouds"

### Processing Pipeline (2 minutes)

- "Raw satellite data is useless - needs atmospheric correction, cloud masking"
- "NASA processes this automatically - 128+ petabytes archived"
- "Output: vegetation indices (NDVI), crop type maps, yield forecasts"
- "8 million users download 4.5 billion files per year"

### Global Programs (1 minute)

- "GEOGLAM: G20 created this after 2007-08 food price spikes"
- "FEWS NET: predicts famines months in advance"
- "These programs inform international policy - not individual farms"

### The Question (30 seconds)

- "All this infrastructure exists"
- "How does it actually reach a farmer in Uganda?"
- "That's the last-mile problem we'll examine next"

</details>

---

#### Case Study 01.03 (cont.): Commercial Applications

**How Companies Monetize Free Public Data:**

Satellite data is free, but actionable intelligence is not. Commercial firms add value through processing, modeling, and delivery:

**Commercial Use Case 1: Commodity Trading**

- **Before satellite monitoring:** Traders relied on USDA monthly reports (delayed), weather stations (sparse), ground scouts (expensive)
- **With satellite monitoring:** Daily crop condition assessments, 3-6 week yield forecast lead time before official reports
- **Economic value:** Better forecasts → strategic futures positions → millions in trading advantage
- **Market size:** $200-300M annually for satellite analytics services

**Commercial Use Case 2: Crop Insurance**

Traditional insurance requires expensive field visits ($100-300 per claim). Satellite monitoring enables:

- **Automated loss assessment:** Satellite vegetation indices verify crop damage without field visits
- **Parametric insurance:** Automatic payout when satellite NDVI drops below threshold - no claim filing required
- **Example product (Kenya):** $10-20/hectare premium, automatic payout within 2 weeks if NDVI < 0.4 during grain fill

**Commercial Use Case 3: Water Management**

- **OpenET (western U.S.):** Field-level evapotranspiration estimates from Landsat/Sentinel-2
- **Economic impact:** $20M water savings in Idaho (2023), paid for by water districts and state agencies
- **Business model:** Free to farmers, funded by water management agencies

**The Pattern: Privatizing Public Data Insights**

```mermaid
graph LR
    subgraph Public["**Public Investment**"]
        A[**NASA Satellites**<br/>Billions in public funds]
        B[**Free Data Distribution**<br/>No access fees]
    end
    
    subgraph Private["**Private Value Capture**"]
        C[**Processing Infrastructure**<br/>Cloud computing<br/>Storage<br/>Bandwidth]
        D[**Analytical Models**<br/>Machine learning<br/>Crop models<br/>Forecasting]
        E[**Domain Expertise**<br/>Agronomists<br/>Data scientists<br/>Software engineers]
    end
    
    subgraph Revenue["**Revenue Streams**"]
        F[**Subscriptions**<br/>$200-300M market]
        G[**Platform Fees**<br/>API access charges]
        H[**Consulting Services**<br/>Custom analytics]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G
    E --> H
    
    classDef public fill:#e8f5e9,stroke:#388e3c,stroke-width:3px
    classDef private fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef revenue fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    
    class A,B public
    class C,D,E private
    class F,G,H revenue
```

**Speaker Note Detail:** This isn't necessarily wrong - companies add real value. But it shows that "free" data only benefits those who can afford the $hundreds of thousands in infrastructure to process it.

<details>
<summary><strong>💬 Speaker Notes - Commercial Applications</strong></summary>

### Commodity Trading (2 minutes)

- "Before satellites: traders flew scouts over fields, counted trucks at grain elevators"
- "Now: daily MODIS imagery, machine learning models predict yields"
- "Key advantage: 3-6 week lead time before USDA reports"
- "That information advantage is worth millions in futures markets"

### Crop Insurance (2 minutes)

- "Traditional: adjuster drives to field, assesses damage, $200 cost per claim"
- "Satellite: check NDVI index, automatic payout if below threshold"
- "Example: Kenya drought insurance - NDVI drops below 0.4 → automatic payment in 2 weeks"
- "This only works because NASA already pays for the satellites"

### The Value Chain (1 minute)

- "Public pays for satellites (billions)"
- "Companies pay for processing and expertise (millions)"
- "Companies charge farmers and agribusinesses ($$$ subscriptions)"
- "Is this technology transfer working? Or is it privatizing public goods?"

### Discussion Questions

- "Should companies pay royalties when building businesses on public data?"
- "Is this different from building a business using public roads or public education?"

</details>

---

#### Case Study 01.03 (cont.): Local Farmer Access & Barriers

**Two Farmer Realities:**

**U.S. Farmer (Representative Pattern):**

- **Equipment:** 800-hectare operation, $1.5M in machinery, GPS-guided tractors
- **Technology:** $2,000-3,000/year farm management software that automatically processes Sentinel-2 imagery
- **Daily workflow:** Email alerts for crop stress detected in satellite imagery → check soil sensors → decide irrigation
- **Experience:** Satellite data is one layer among many (yield maps, weather, equipment telemetry) - seamlessly integrated

**Ugandan Smallholder Farmer (Representative Barriers):**

- **Equipment:** 2-hectare operation, hand tools, no mechanization
- **Technology:** Basic mobile phone (not smartphone), unreliable electricity for charging
- **Access barriers:**
  - Smartphone: 30-50% penetration in rural Sub-Saharan Africa
  - Data costs: $1-2/month = 5-15% of monthly income
  - Extension services: 1:1000-5000 agent-to-farmer ratio (vs. 1:100-300 in developed countries)
  - Digital literacy: Understanding satellite-derived maps requires education rarely available
- **Experience:** Heard about "the satellite that tells when rain comes" but cannot access it

**The Last-Mile Problem:**

```mermaid
graph TD
    subgraph Satellite["**Satellite Data Available**"]
        A[**Free Public Data**<br/>Landsat, Sentinel-2<br/>Global coverage]
    end
    
    subgraph Barriers["**Infrastructure Barriers**"]
        B1[**Smartphone Access**<br/>30-50% penetration]
        B2[**Internet Data**<br/>$1-2/month<br/>5-15% of income]
        B3[**Electricity**<br/>Unreliable charging]
        B4[**Digital Literacy**<br/>Map reading skills]
        B5[**Extension Services**<br/>1:1000+ farmer ratio]
    end
    
    subgraph Outcome["**Farmer Outcome**"]
        C1[**U.S. Farmer**<br/>Direct access<br/>30-40% adoption]
        C2[**Smallholder Farmer**<br/>No access<br/>5% adoption]
    end
    
    A -.Easy Path.-> C1
    A --> B1
    A --> B2
    A --> B3
    A --> B4
    A --> B5
    
    B1 -.Blocks.-> C2
    B2 -.Blocks.-> C2
    B3 -.Blocks.-> C2
    B4 -.Blocks.-> C2
    B5 -.Blocks.-> C2
    
    classDef satellite fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    classDef barrier fill:#ffebee,stroke:#c62828,stroke-width:2px
    classDef outcome fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    
    class A satellite
    class B1,B2,B3,B4,B5 barrier
    class C1,C2 outcome
```

**Bridging Attempts:**

- **HarvestNow app (Kenya/Ethiopia):** Low-literacy mobile app with visual icons, ~5,000 users by 2023
- **Extension service training:** NASA Harvest trains national ag extension to interpret satellite data
- **Community access points:** Shared tablets at cooperatives, input dealers
- **SMS/Radio:** Simplified satellite-derived forecasts via text message or community radio

**Farmer Quote (Uganda Study, 2018):**

> "We heard about the satellite that can tell when rain comes, but we don't have the phones that work with it. The agricultural officer came one time and showed us pictures from space, but he doesn't come often enough." — Beatrice, smallholder farmer

**Speaker Note Detail:** The contrast is stark. Same satellites, same "free" data, completely different farmer experiences. The barrier isn't the technology - it's infrastructure, education, and economic access.

<details>
<summary><strong>💬 Speaker Notes - Local Access</strong></summary>

### The Two Realities (2 minutes)

**U.S. Farmer:**
- "Checks satellite crop stress alerts on smartphone"
- "Software costs $3,000/year but makes economic sense at 800 hectares"
- "Satellite data just one tool among many"
- "Never directly downloads a Sentinel-2 image - service handles everything"

**Ugandan Smallholder:**
- "Operates 2 hectares - same size as my backyard"
- "Has basic phone, not smartphone (30-50% smartphone penetration)"
- "If she had smartphone, $2/month data plan = 5-15% of income"
- "Extension officer visited once, showed satellite images, hasn't returned"

### The Barriers Stack (2 minutes)

- "It's not just one problem - it's five overlapping barriers"
- "Fix smartphones → still need data plan → still need electricity → still need literacy"
- "This is why bridging attempts (HarvestNow app) reach 5,000 farmers, not 5 million"

### Real Quote (1 minute)

- "Read Beatrice's quote carefully"
- "She understands value: 'If I knew when rain comes, I'd plant on exactly the right day'"
- "The barrier isn't interest or understanding - it's access infrastructure"

### Discussion Questions

- "Is this a solvable problem? Or fundamental limit of technology diffusion?"
- "Who is responsible for building last-mile infrastructure?"

**Full analysis:** See `docs/classes/01.03-case-study-nasa-harvest.md` Section 4

</details>

---

#### Case Study 01.03 (cont.): The Central Tension & Course Connections

**The Ethical Question: Who Benefits from "Free" Data?**

When data is technically free but practically inaccessible, we must ask:

**Stakeholder Benefit Analysis:**

| Stakeholder                  | Access Level | Economic Benefit         | Why?                                   |
| ---------------------------- | ------------ | ------------------------ | -------------------------------------- |
| **U.S./European Governments**    | ✅ Direct     | High (policy decisions)  | Full processing capability, expertise  |
| **Commercial Companies**         | ✅ Direct     | $200-300M annual revenue | Monetize public data                   |
| **Large-Scale Farmers**          | ✅ Via services | Strong ROI (~$10-20/ha) | Affordable subscriptions, infrastructure |
| **Developing Country Govts**     | ⚠️ Partial    | Medium (limited capacity) | Data access, limited processing        |
| **NGOs & Extension**             | ⚠️ Partial    | Medium (intermediary role) | Funding dependent, scaling challenges  |
| **Smallholder Farmers**          | ❌ Minimal    | Very low (<5% access)    | Infrastructure barriers, cost prohibitive |

**Multiple Perspectives:**

- **NASA/Space agencies:** "We provide the data - that's our mission. We can't solve all infrastructure and development challenges."
- **Commercial companies:** "We add value - processing, expertise, software. Farmers who pay see strong ROI. We're not exploiting public resources."
- **Developing country governments:** "Satellite data helps national monitoring, but we can't reach individual farmers due to extension limitations."
- **Technology critics:** "'Free' data primarily benefits wealthy farmers and companies. We're using public resources to amplify existing inequalities."
- **Smallholder farmer:** "I need to know when rain comes and when to plant, but that information doesn't reach me."

**Course Connections:**

This case study connects to several course modules:

- **Module 02 (Data Collection):** Satellite remote sensing as automated data collection system; sensor trade-offs (spatial vs. temporal resolution)
- **Module 04 (Data Processing):** Atmospheric correction, cloud masking, NDVI calculation
- **Module 07 (Data Integration):** Combining satellite data with weather, soil, yield data
- **Module 10 (Decision Support):** Different delivery models (direct vs. intermediated farmer access)
- **Module 12 (Data Ethics):** Access inequality, data sovereignty, benefit distribution
- **Assignment 4-2:** Implement basic satellite image preprocessing workflow
- **Assignment 7-1:** Integrate Sentinel-2 imagery with field boundaries and weather data

**Key Takeaways:**

1. **Infrastructure is not neutral** - "Free" data + unequal infrastructure = unequal outcomes
2. **Multiple delivery models needed** - No single approach works for all contexts
3. **Technology alone doesn't solve development challenges** - Requires broader infrastructure investment
4. **Consider beneficiaries when building systems** - Who gains from the tools you create?

**Full case study:** `docs/classes/01.03-case-study-nasa-harvest.md` (14,000 words, 23 discussion questions, Python/SQL examples)

<details>
<summary><strong>💬 Speaker Notes - Tensions & Takeaways</strong></summary>

### The Core Question (1 minute)

- "Satellite data is 'free' in legal sense"
- "But requires expensive infrastructure to use"
- "Result: benefits concentrate among those with existing resources"
- "Is this technology amplifying inequality?"

### Different Perspectives (2 minutes)

- "NASA: 'We provide the data - that's our job'"
- "Companies: 'We add real value through processing and expertise'"
- "Critics: 'You're privatizing public goods'"
- "Smallholder farmer: 'The information exists but doesn't reach me'"
- "None of these perspectives is entirely wrong"

### Course Relevance (2 minutes)

- "You'll work with satellite data in Module 04"
- "You'll integrate it with other data types in Module 07"
- "But always ask: who will actually use what you build?"
- "Technology choices aren't neutral - they have distributional consequences"

### Looking Forward

- "Next case study: John Deere Operations Center"
- "Different tension: When farmers generate data, who owns it?"
- "Same theme: data infrastructure and power dynamics"

**Discussion questions:** See full case study for 23 provocative, balanced, and applied questions

</details>

---

#### Case Study 01.04: John Deere Operations Center - Equipment Data & Farmer Agency

**Focus:** 🚜 **Equipment-generated agricultural data ecosystems**  
**Platform:** John Deere Operations Center, 200M+ hectares managed globally  
**Core Question:** When equipment generates farm data, who owns it and controls access?

**The Connected Equipment Revolution:**

Modern farm equipment doesn't just plant and harvest - it collects thousands of data points per hour. GPS position, yield monitoring, planting rates, fertilizer applications, machine performance - all flowing automatically from tractor to cloud.

```mermaid
graph TB
    subgraph Equipment["🚜 **Connected Equipment**"]
        A[**Tractor/Combine**<br/>GPS, sensors<br/>yield monitors]
    end
    
    subgraph Network["📡 **JDLink Network**"]
        B[**Cellular Modem**<br/>Real-time transmission<br/>Automatic upload]
    end
    
    subgraph Platform["☁️ **Operations Center**"]
        C[**Free Tier**<br/>Data storage<br/>Basic visualization]
        D[**PRO Service**<br/>Remote diagnostics<br/>Advanced analytics<br/>💰 $2-5K/year]
    end
    
    subgraph Farmer["👨‍🌾 **Farmer Experience**"]
        E[**Daily Use**<br/>Field planning<br/>Progress monitoring]
        F[**Dependencies**<br/>Historical data trapped<br/>Repair restrictions<br/>Platform lock-in]
    end
    
    A --> B
    B --> C
    B --> D
    C --> E
    D --> E
    E --> F
    
    classDef equipment fill:#e8f5e9,stroke:#388e3c,stroke-width:3px
    classDef network fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef platform fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef farmer fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef tension fill:#ffebee,stroke:#c62828,stroke-width:3px
    
    class A equipment
    class B network
    class C,D platform
    class E farmer
    class F tension
```

**Key Statistics:**

- **Global reach:** 200+ million hectares managed (equivalent to all EU agricultural land)
- **Platform economics:** $1.5B+ annual technology/precision ag revenue for Deere (2023)
- **Subscription model:** Free basic tier + paid PRO Service ($2,000-5,000/year estimated)
- **Adoption:** 60-70% of Operations Center users rely primarily on free tier
- **Equipment integration:** Works best (sometimes only) with all-Deere fleets

**The Business Model Evolution:**

| Traditional Model (pre-2010)                         | Technology Platform Model (2015-present)                   |
| ---------------------------------------------------- | ---------------------------------------------------------- |
| Revenue: Equipment sales + parts + service           | Revenue: Equipment + parts + service + **subscriptions + data** |
| Customer relationship: Transactional (ends after sale) | Customer relationship: Ongoing (yearly subscription renewal) |
| Competitive advantage: Product performance, dealer network | Competitive advantage: Product + network + **platform ecosystem** |

**Speaker Note Detail:** This case study examines data ownership and farmer agency. Unlike NASA Harvest (public data, access barriers), here farmers generate the data through their own farming operations - but don't fully control it.

<details>
<summary><strong>💬 Speaker Notes - John Deere Overview</strong></summary>

### Setup (2 minutes)

- "Modern tractor = sophisticated data collection system"
- "GPS position every second, yield monitor readings, planting rates, all captured automatically"
- "Data flows wirelessly: equipment → JDLink modem → Operations Center cloud"
- "Farmer never manually enters a number - it's all automatic"

### The Platform (2 minutes)

- "Operations Center: free basic tier (60-70% of users)"
- "PRO Service: $2-5K/year subscription for advanced features"
- "200+ million hectares managed globally"
- "Nearly 20 years of development - this is a mature system"

### The Tension (1 minute)

- "Farmer paid $500,000 for the combine"
- "But data flows through Deere's platform - can't access directly from equipment"
- "Historical data trapped in Operations Center - hard to export"
- "Plus repair restrictions: can't fix equipment without dealer diagnostic access"
- "Question: Do farmers own their data? Their equipment?"

### Why This Matters

- "You'll work with equipment data in Module 08 (security/privacy)"
- "Module 11: analyze business models like this freemium platform"
- "Module 12: data ethics - ownership, agency, power"

**Full case study:** See `docs/classes/01.04-case-study-john-deere.md` for 15,000-word analysis

</details>

---

#### Case Study 01.04 (cont.): Daily Farmer Workflow & Platform Value

**Representative Farmer:** 1,200-hectare corn/soybean operation, Iowa, all-Deere fleet ($1.5M equipment value)

**Spring Workflow - Planning & Planting:**

- **March-April:** Reviews last year's yield maps in Operations Center, overlays soil data, generates variable-rate seeding prescriptions
- **System recommendation:** PRO Service algorithm suggests seeding rates based on 8+ years of field history plus anonymized data from "similar" fields
- **Work plans:** Creates plans in Operations Center → sends wirelessly to employee's tractor → appears automatically on display
- **Real-time monitoring:** During planting, watches from office: which field (42% complete), actual vs. target population (31,800 vs. 32,000 seeds/acre - within tolerance)
- **Automatic alerts:** Smartphone notification if planter skips detected → calls employee before turning around

**Summer Workflow - Monitoring & Management:**

- **Morning:** Check dashboard over coffee - equipment locations, fuel levels, yesterday's progress
- **Mid-season:** Satellite imagery integrated (third-party service) shows potential stress → visits field → creates variable-rate nitrogen application prescription
- **Automatic execution:** Prescription transfers wirelessly to sprayer, automatically adjusts rates as it crosses field zones

**Fall Workflow - Harvest & Analysis:**

- **Real-time yield data:** Appears on smartphone as harvest progresses → inform grain marketing decisions
- **Harvest logistics:** Track which fields harvested, storage bin inventory, moisture levels
- **End-of-season analysis:** Profitability by field, input effectiveness, equipment performance, multi-year trends

**The Value Proposition:**

- **Time savings:** 200-300 hours annually vs. paper recordkeeping (worth $10,000-15,000 at $50/hour opportunity cost)
- **Better decisions:** Multi-year historical data reveals patterns invisible in paper records
- **Team coordination:** Employees access work plans, farmer monitors remotely, everyone works from same data
- **Compliance:** Export reports for crop insurance, conservation programs in minutes vs. searching filing cabinets

**But Also: The Constraints:**

- **Software bugs:** "During peak planting, Operations Center was down for 6 hours. We couldn't access work plans. We just kept planting with last year's rates and hoped it would come back."
- **Forced updates:** "Deere pushes software updates automatically. Sometimes features move. I've trained employees on one workflow, then an update changes it."
- **Subscription cost escalation:** "Features that used to be free now require PRO Service. Feels like bait-and-switch."
- **Data export limitations:** "Export is technically possible, but format is clunky. It's clear they don't want data leaving their ecosystem."
- **Multi-brand challenges:** "Bought one Case IH sprayer because Deere was backordered. Getting it to work was a nightmare."

<details>
<summary><strong>💬 Speaker Notes - Daily Workflow</strong></summary>

### Setup (1 minute)

- "Representative pattern, not specific farm"
- "1,200 hectares = medium-large U.S. Midwest operation"
- "All-Deere fleet - this is important because multi-brand is harder"

### Walk Through Workflow (3 minutes)

**Spring:**
- "Reviews last year's performance → generates prescriptions"
- "PRO Service recommendation algorithm: 8 years her data + anonymous 'similar farms'"
- "Sends plans wirelessly to equipment - no paper maps, no manual entry"
- "Monitors in real-time from office"

**Summer:**
- "Check dashboard over morning coffee"
- "Satellite alerts → field visit → create prescription → automatic execution"

**Fall:**
- "Real-time yield data helps marketing decisions"
- "End-of-season: Which fields made money? Which lost money?"

### The Value (1 minute)

- "200-300 hours saved annually"
- "That's $10-15K in opportunity cost"
- "Better decisions from historical patterns"
- "Team coordination seamless"

### But Also Constraints (2 minutes)

- "Read the farmer quotes - these are real frustrations from forums and interviews"
- "Platform downtime during critical operations - 'dead in the water'"
- "Forced updates changing UI - training problem"
- "Subscription creep - free features moving to PRO"
- "Data export intentionally difficult"
- "Multi-brand 'compatibility' technically exists, functionally problematic"

### Discussion

- "High value AND high dependency - both true simultaneously"
- "Farmer values platform but resents feeling trapped"

</details>

---

#### Case Study 01.04 (cont.): Data Ownership Tensions

**The Core Question: Who Owns Farm Data?**

Deere's official position: **"Farmers own their data."**

But what does "ownership" mean when:

- Farmers can't directly download data from equipment - must flow through Operations Center
- Export functionality is intentionally limited (functional but not user-friendly)
- Historical context is non-exportable (data points yes, analytical insights no)
- Third-party integrations require Deere's API permission and ongoing access fees

**Legal Ownership vs. Practical Control:**

| Aspect                     | Deere's Position                                   | Farmer Reality                                |
| -------------------------- | -------------------------------------------------- | --------------------------------------------- |
| **Data access**                | "Farmers control who can view data"                | Must use Deere's platform - no direct equipment access |
| **Data export**                | "Farmers can export their data"                    | Export formats are clunky, historical context lost |
| **Third-party use**            | "Farmers authorize third-party access"             | But Deere controls API terms and can restrict access |
| **Aggregate data use**         | "We use anonymized data to improve products"       | Farmers contribute data but aren't compensated |
| **Equipment diagnostic data**  | Deere owns machine telemetry (engine, maintenance) | Farmers need this to repair equipment they own |

**Deere's Retained Rights (from Terms of Service):**

- License to use farmer data to "improve products and services"
- Right to create "aggregate, anonymized" datasets from farmer data
- Ownership of all machine-generated diagnostic data
- Control over data access methods and infrastructure
- Right to modify terms unilaterally (farmers must accept or lose access)

**The Right-to-Repair Controversy:**

Modern equipment software controls mechanical functions, but Deere restricts diagnostic access:

- **Farmer complaint:** "I own a $500,000 combine, but when it breaks during harvest, I can't fix it myself. Deere locks diagnostic software behind dealer-only tools. I wait hours/days for $300+ dealer visit to diagnose problems I could troubleshoot if I had access to my equipment's data."
- **Deere's response:** PRO Service now offers remote diagnostics - dealers diagnose remotely, reducing wait time
- **Farmer counter:** "That's another subscription, and I still can't repair myself. It doesn't address the fundamental issue."
- **Legislative status:** 20+ U.S. states have considered right-to-repair legislation; few have passed comprehensive laws (as of 2024)

**Who Economically Benefits from Farm-Generated Data?**

```mermaid
graph TD
    subgraph Source["📊 **Data Source**"]
        A[**Farm Operations**<br/>Farmer decisions<br/>+ Equipment capture<br/>= Combined dataset]
    end
    
    subgraph Deere["🏢 **Deere Value Extraction**"]
        B[**Machine Learning**<br/>Train models on<br/>millions of fields]
        C[**Product Development**<br/>Design better<br/>equipment/software]
        D[**Platform Lock-in**<br/>Switching costs<br/>drive equipment sales]
    end
    
    subgraph Revenue["💰 **Revenue Streams**"]
        E[**Subscriptions**<br/>$1.5B+ technology<br/>revenue annually]
        F[**Equipment Sales**<br/>Data platform drives<br/>equipment preference]
        G[**API Fees**<br/>Third-party<br/>access charges]
    end
    
    subgraph Farmer["👨‍🌾 **Farmer Value**"]
        H[**Better Decisions**<br/>Data-informed<br/>management]
        I[**Time Savings**<br/>Automated<br/>recordkeeping]
        J[**No Compensation**<br/>Contribute data<br/>but not paid]
    end
    
    A --> B
    A --> C
    A --> D
    B --> E
    C --> F
    D --> F
    B --> G
    
    A -.Free Use.-> H
    A -.Free Use.-> I
    A -.No Payment.-> J
    
    classDef source fill:#e8f5e9,stroke:#388e3c,stroke-width:3px
    classDef deere fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef revenue fill:#fff3e0,stroke:#f57c00,stroke-width:3px
    classDef farmer fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    
    class A source
    class B,C,D deere
    class E,F,G revenue
    class H,I,J farmer
```

<details>
<summary><strong>💬 Speaker Notes - Data Ownership</strong></summary>

### The Official Position (1 minute)

- "Deere says 'farmers own their data'"
- "True in narrow legal sense: farmers control who else can see it"
- "But what about practical control?"

### Legal vs. Practical (2 minutes)

- "Can't download data directly from equipment"
- "Export functionality exists but is intentionally difficult"
- "Historical context non-exportable - just raw data points"
- "Third-party access gated by Deere's API terms"

### Right-to-Repair (2 minutes)

- "$500,000 combine breaks during harvest"
- "Farmer has tools, mechanical skills, could fix it"
- "But can't access diagnostic codes - dealer-only software"
- "$300 dealer visit just to diagnose"
- "PRO Service 'solution': remote diagnostics for another subscription"

### Who Benefits? (2 minutes)

- "Farmers: better decisions, time savings"
- "Deere: $1.5B tech revenue, equipment sales driven by platform lock-in"
- "Farmers contribute data → Deere trains ML models → Deere sells those insights back to farmers"
- "Is this fair exchange? Or extraction?"

### Discussion Questions

- "If you can't meaningfully take data elsewhere, do you really 'own' it?"
- "Should farmers be compensated when their data trains commercial ML models?"
- "Where should law draw the line on repair access?"

</details>

---

#### Case Study 01.04 (cont.): Multiple Perspectives & Power Dynamics

**Stakeholder Perspectives on Data Ownership:**

**Farmer perspective:**  
"I paid for the equipment. The data describes my farming decisions on my land. I should have complete control - ability to access data directly from machines, export in any format, use with any third-party service, repair equipment without manufacturer permission. Current restrictions feel like Deere holding my data hostage to sell subscriptions."

**Deere perspective:**  
"Farmers do control their data - they decide who can see it and can export it. We need certain rights to use aggregate data to improve products that benefit all farmers. The machine learning models that power PRO Service only work because we pool anonymized data from millions of fields. Equipment repair restrictions protect safety, intellectual property, and emissions compliance."

**Dealer perspective:**  
"Remote diagnostics and controlled repair access protect the dealer network that provides service in rural areas. If farmers could repair everything themselves, dealers couldn't afford service infrastructure. When truly complex repairs are needed, farmers would be out of luck."

**Third-party platform perspective:**  
"Deere's control over API access means they decide what tools farmers can use. If we build competing farm management software, Deere can restrict our API access or charge prohibitive fees. This gatekeeping limits innovation and farmer choice."

**Agricultural economist perspective:**  
"There's legitimate value in aggregate data that justifies Deere retaining some rights. But the current balance tips too far toward manufacturer control. Farmers contribute data that generates substantial value but capture little of that value. Better policy would ensure farmers are either compensated for data contributions or have truly unrestricted data portability."

**The Power Asymmetry:**

Deere is a $50+ billion corporation. Individual farmers are price-takers who must accept offered terms.

**Farmer bargaining power:**
- Can choose competitors (Case IH, AGCO, Claas) - but they have similar data practices
- Can collectively organize (Farm Bureau, Farmers Union) - but limited policy success
- Can refuse to adopt technology - but lose competitive advantage

**Deere bargaining power:**
- Controls access to equipment farmers depend on for livelihood
- Can modify terms of service unilaterally (farmers must accept or lose access)
- Leverages switching costs (historical data, workflow integration) for customer retention
- Lobbies effectively against regulatory intervention

**Potential Policy Solutions:**

| Approach                        | Description                                              | Status                          |
| ------------------------------- | -------------------------------------------------------- | ------------------------------- |
| **Data portability requirements**   | Mandate easy export in standard formats                  | Discussed but not implemented   |
| **Aggregate data compensation**     | Pay farmers royalties when using their data commercially | Proposed in some farm organizations |
| **Farmer data cooperatives**        | Enable collective negotiation of data terms              | Emerging (limited scale)        |
| **Right-to-repair legislation**     | Require manufacturers provide diagnostic access          | 20+ states considering, few passed |
| **Open data standards**             | Industry-wide standards like ISOBUS                      | ISOBUS exists but limited scope |

<details>
<summary><strong>💬 Speaker Notes - Perspectives & Power</strong></summary>

### The Perspectives (3 minutes)

- "Read through each perspective carefully"
- "None is entirely wrong - there are legitimate interests on all sides"
- "Farmer: 'I bought it, I should control it'"
- "Deere: 'Aggregate data creates value that requires some manufacturer rights'"
- "Dealer: 'Restrict repairs too much, rural service infrastructure collapses'"
- "Economist: 'Current balance tips too far toward manufacturer'"

### The Power Imbalance (2 minutes)

- "Deere: $50B corporation, armies of lawyers"
- "Individual farmer: price-taker, must accept offered terms"
- "Even when Deere's position has economic logic, farmers can't negotiate"

### What Could Change This? (2 minutes)

**Data portability:**
- "Reduce switching costs → increase farmer bargaining power"

**Aggregate data compensation:**
- "If Deere profits from farmer data → farmers get royalty"

**Farmer cooperatives:**
- "10,000 farmers collectively negotiate better terms"

**Right-to-repair:**
- "Farmers and independent shops get diagnostic access"

### Discussion

- "Which approach is most feasible?"
- "Which addresses root problem vs. symptoms?"
- "Should government intervene or let market sort it out?"

</details>

---

#### Case Study 01.04 (cont.): Course Connections & Key Takeaways

**Course Connections:**

This case study integrates with multiple course modules:

- **Module 01 (Introduction):** Equipment-generated data as foundational agricultural data source
- **Module 03 (Data Standards):** ISOBUS standards vs. proprietary protocols; interoperability challenges
- **Module 06 (Cloud Computing):** Operations Center as cloud-based agricultural data platform; edge computing in equipment
- **Module 08 (Security & Privacy):** Team access controls; dealer/third-party data sharing; data breach risks
- **Module 11 (Business Models):** Freemium model (free basic + paid PRO); platform economics; subscription vs. ownership
- **Module 12 (Data Ethics):** Data ownership tensions; farmer agency vs. manufacturer control; power asymmetries
- **Module 13 (Policy & Regulation):** Right-to-repair legislation; data portability requirements; antitrust concerns
- **Assignment 8-1:** Evaluate Operations Center security model and access controls
- **Assignment 11-2:** Compare data monetization models across agricultural equipment manufacturers
- **Assignment 12-1:** Analyze John Deere case through farmer autonomy and power dynamics ethics frameworks

**Key Takeaways:**

**1. Data ownership is multifaceted:**
- Legal ownership (who has legal title to data)
- Practical control (who can actually access and use data)
- Economic benefit (who captures value from data)

These three aspects can diverge significantly.

**2. Platform lock-in is cumulative:**
- Year 1: Easy to leave
- Years 2-3: Some switching costs
- Years 6+: Practically impossible without major disruption

**3. Business model shifts risk:**
- Traditional: One-time equipment purchase → farmer owns
- Modern: Equipment purchase + ongoing subscriptions → features become services

**4. Power asymmetries shape outcomes:**
- Individual farmers have limited bargaining power
- Collective action or regulatory intervention may be necessary for balance

**5. No simple answers:**
- Aggregate data does create legitimate value
- Platform infrastructure does require investment
- But current arrangements may tip too far toward manufacturer control

**Comparison: NASA Harvest vs. John Deere**

| Dimension           | NASA Harvest                      | John Deere Operations Center         |
| ------------------- | --------------------------------- | ------------------------------------ |
| **Data source**         | Government satellites (public)    | Farmer equipment operations (private) |
| **Core tension**        | Access inequality despite "free" data | Ownership ambiguity despite farmer-generated data |
| **Primary barrier**     | Infrastructure & economic access  | Platform control & switching costs   |
| **Who benefits most**   | Governments & commercial companies | Manufacturer & large-scale farmers   |
| **Policy question**     | How to bridge last-mile gap?      | How to ensure farmer data rights?    |
| **Your role**           | Consider access when building systems | Consider ownership when designing platforms |

**Discussion Questions for Both Case Studies:**

1. Is "free" data that requires expensive infrastructure to access actually free?
2. When farmers generate data through farming activities, who should control it?
3. What obligations do companies have when building profitable businesses on public data (NASA) or farmer-generated data (Deere)?
4. Where should law draw the line between legitimate business interests and anticompetitive platform control?
5. As a data systems developer, what principles should guide your design choices?

**Full case studies:**
- NASA Harvest: `docs/classes/01.03-case-study-nasa-harvest.md` (14,000 words)
- John Deere: `docs/classes/01.04-case-study-john-deere.md` (15,000 words)

Each includes comprehensive analysis, technical appendices with code examples, and 20+ discussion questions.

<details>
<summary><strong>💬 Speaker Notes - Takeaways & Transition</strong></summary>

### Synthesize the Two Cases (3 minutes)

- "Two very different data ecosystems"
- "NASA: public data, access barriers"
- "Deere: farmer-generated data, ownership ambiguity"
- "Common theme: infrastructure and power shape who benefits"

### Key Principles (2 minutes)

**For both cases:**
- "Data infrastructure is not neutral"
- "Legal rights don't ensure practical control"
- "Economic value often concentrates with intermediaries"
- "Individual users (farmers) have limited bargaining power"

### Your Role (1 minute)

- "You'll build agricultural data systems"
- "Your choices shape who can access and benefit"
- "Technology design is never just technical - it's also political and ethical"

### Looking Forward

- "Next section: Industry trends"
- "Then we'll look at specific data types and technologies"
- "But keep these case studies in mind throughout the course"

### Assignment Preview

- "Module 12: Ethics analysis assignment"
- "You'll choose one of these case studies and analyze through ethical frameworks"
- "Start thinking about which perspective you find most compelling"

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

**2. Variable Rate Everything**

- Not just seed and N - now extending to:
  - VR phosphorus & potassium (VRP, VRK)
  - VR fungicides and insecticides
  - VR irrigation
  - VR tillage depth

**3. Carbon & Sustainability Verification**

- Data-driven carbon credit programs (Nori, Indigo, Truterra)
- Automated ESG reporting for food companies
- Blockchain for supply chain transparency
- Regenerative agriculture measurement

**4. In-Season Sensor-Based Decisions**

- **Canopy sensors:** Real-time crop color analysis
- **Drone imagery:** Weekly N status monitoring
- **Satellite indices:** NDVI-based sidedress recommendations
- **Soil moisture sensors:** Irrigation timing optimization

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
- "The case studies we just saw (VRS, VRN) are TODAY"
- "But the industry is moving even faster"

**Walk Through Trends (3 min):**

- AI/ML: "Every company is adding AI features - some useful, some hype"
- Variable rate: "If it moves, someone's making it variable"
- Carbon: "Huge money in carbon credits - but requires data"
- In-season: "Real-time decisions, not just pre-season planning"
- Open data: "Finally happening after years of farmer advocacy"

**Personal Experience (1 min):**

- "At Climate Corp, we were early to AI"
- "Learned: farmers trust data they can verify"
- "Transparency beats fancy algorithms"

#### Challenges (5 minutes)

**Set Realistic Expectations (1 min):**

- "It's not all sunshine and precision"
- "Real problems that affect adoption"
- "Your generation needs to solve these"

**Walk Through Challenges (3 min):**

- Interop: "I dealt with this daily - nightmare"
- Ownership: "Hotly debated - farmers are winning"
- Digital divide: "Real barrier for many rural operations"
- Data overload: "More isn't always better"
- Trust: "Explainability is crucial"

**Your Role (1 min):**

- "You're learning to solve these problems"
- "The industry needs people who understand both data AND agriculture"

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
- [Case Study 01.01: Variable Rate Seeding](./01.01-case-study-variable-rate-seeding-corn.md) - Climate FieldView Seeds Pro, McNunn et al. (2019)
- [Case Study 01.02: Variable Rate Nitrogen](./01.02-case-study-variable-rate-nitrogen.md) - Grid soil sampling + optimization, Bongiovanni & Lowenberg-DeBoer (2004)

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

### Companies & Platforms Mentioned

- [Climate FieldView](https://climate.com/fieldview) - Bayer digital agriculture platform
- [John Deere Operations Center](https://www.deere.com/en/technology-products/precision-ag-technology/operations-center/) - Farm management platform
- [Indigo Ag](https://www.indigoag.com/) - Carbon credits and marketplace

### Key Research Papers (Speaker Reference)

- **Bongiovanni, R., & Lowenberg-DeBoer, J. (2004).** Precision Agriculture and Sustainability. _Precision Agriculture_, 5(4), 359-387. <https://doi.org/10.1023/B:PRAG.0000040806.39604.aa>

- **McNunn, G., Heaton, E., Archontoulis, S., Licht, M., & VanLoocke, A. (2019).** Using a crop modeling framework for precision cost-benefit analysis of variable seeding and nitrogen application rates. _Frontiers in Sustainable Food Systems_, 3, 108. <https://doi.org/10.3389/fsufs.2019.00108>

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Resource Guidance (2 minutes)

- "Required reading gives you broader context"
- "The two case studies (01.01 and 01.02) are SHORT versions of the deep dives"
- "If you want full detail on research methodology, economics, etc., read the full case study files"
- "But for slides/presentations, the critical insights are all here"
- "Industry reports show where money and jobs are"
- "Data sources - you'll use all of these in assignments"
- "Company links - explore what they're building"

### Encourage Exploration

- "Not all resources are required for assignment"
- "But they'll help you understand the industry"
- "Especially useful if you're interested in ag careers"
- "The research papers are dense but worth reading once you have data science context"

</details>

---
