# 02 - Gearing Up: Building Your Smart Farm Workspace

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

- Verify your own development environment is working
- Have the agri-data-toolkit repository cloned and ready
- Test screen sharing for live demo
- Prepare backup plan if demo fails (recorded video)

### Quick Reminders (2 minutes)

- "Welcome to Class 02! Today is all hands-on setup"
- "This is a no-assignment class - focus is on getting your environment ready"
- "Everyone will leave with a working workspace today"

### Common Technical Issues

- Python version conflicts
- PATH environment variables
- Git authentication problems
- VS Code extension installation

</details>

---

## 📋 Syllabus Review

Last week in Class 01, we explored the agricultural data revolution and why data matters in modern farming. Today we shift from theory to practice - setting up the development environment you'll use throughout this course.

This connects to Class 03 next week, where you'll use these tools to navigate and download real US agricultural datasets.

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Connection to Previous (1 minute)

- "Last week: the 'why' of agricultural data"
- "This week: the 'how' - building your toolkit"
- Ask: "Who completed the setup checklist from Class 00?"

### Today's Focus (1 minute)

- "Today is 100% practical and hands-on"
- "We're building the foundation for every future assignment"
- "Think of this as setting up your digital farm equipment"

### Looking Ahead (30 seconds)

- "Next week: using these tools to download USDA data"
- "Class 04: your first Python data cleaning assignment"
- "Everything builds on today's setup"

</details>

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Python environment setup (15 min)
- [ ] Essential data science libraries (10 min)
- [ ] Git & GitHub workflow (15 min)
- [ ] VS Code & AI assistant integration (15 min)
- [ ] Live demo: Complete workspace setup (15 min)
- [ ] Q&A and troubleshooting (5 min)

**Total:** 75 minutes

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- "Packed agenda with lots of hands-on work"
- "Follow along on your computer as we go"
- "Don't worry if you fall behind - we'll pause for questions"

### Pacing

- Python setup: 15 min (most critical, don't rush)
- Libraries: 10 min (quick overview)
- Git: 15 min (important for assignments)
- VS Code: 15 min (demo-heavy)
- Live demo: 15 min (full workflow)
- Keep Q&A flexible

### Backup Plan

- If many students have issues, extend Q&A
- Offer post-class office hours for setup help
- Have troubleshooting documentation ready

</details>

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Install** and configure Python 3.9+ with virtual environments for agricultural data projects
- **Integrate** essential data science libraries (pandas, geopandas, rasterio) into your workflow
- **Execute** Git version control commands for cloning, committing, and pushing code to GitHub
- **Configure** VS Code with AI assistants (Copilot, Roo Code) for enhanced productivity

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

"By end of class, you should have:

1. A working Python environment
2. All required libraries installed
3. The course repository cloned locally
4. VS Code configured with AI tools"

### Assessment Approach

- Outcome 1: Tested through Python version check and venv creation
- Outcome 2: Tested through successful library imports
- Outcome 3: Tested through repository clone and first commit
- Outcome 4: Tested through VS Code AI assistant demonstration

### Success Criteria

- Students can run `python --version` successfully
- Students can import pandas and geopandas
- Students have cloned agri-data-toolkit repository
- Students can generate code with Copilot

</details>

---

## 📚 Content

### Python Environment Setup

**Why Python for Agricultural Data?**

Python is the industry standard for agricultural data analysis because:

- Extensive geospatial libraries (GeoPandas, Rasterio, Shapely)
- Data manipulation tools (Pandas, NumPy)
- Machine learning frameworks (scikit-learn, TensorFlow)
- API integrations for USDA, NOAA, satellite providers
- Used by Climate Corp, John Deere, Bayer, Indigo Ag

**Installation Requirements:**

- **Python Version:** 3.9 or higher (3.10 or 3.11 recommended)
- **Package Manager:** pip (included with Python) or conda
- **Virtual Environment Tool:** venv (built-in) or conda

**Step-by-Step Installation:**

**Option 1: Direct Python Installation (Recommended for Beginners)**

1. **Download Python:**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Download Python 3.11 for your operating system
   - **Windows:** Use the installer, check "Add Python to PATH"
   - **Mac:** Use the installer or `brew install python@3.11`
   - **Linux:** `sudo apt install python3.11 python3.11-venv`

2. **Verify Installation:**

   ```bash
   python --version
   # Should show: Python 3.11.x

   pip --version
   # Should show: pip 23.x or higher
   ```

3. **Create Virtual Environment:**

   ```bash
   # Navigate to your projects folder
   cd ~/projects/agri-data

   # Create virtual environment
   python -m venv ag-env

   # Activate it
   # Windows:
   ag-env\Scripts\activate

   # Mac/Linux:
   source ag-env/bin/activate

   # Verify activation (prompt should show (ag-env))
   ```

**Option 2: Anaconda Installation (For Advanced Users)**

1. **Download Anaconda:**
   - Visit [anaconda.com](https://www.anaconda.com/download)
   - Download for your operating system
   - Install with default settings

2. **Create Conda Environment:**

   ```bash
   # Create environment with Python 3.11
   conda create -n ag-env python=3.11

   # Activate it
   conda activate ag-env

   # Verify
   python --version
   ```

**Why Virtual Environments Matter:**

- Isolate project dependencies
- Avoid version conflicts between projects
- Easy to recreate environments
- Industry best practice
- Required for reproducible research

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (15 minutes)

#### Set Context (2 minutes)

- "Python powers almost every agricultural data platform"
- "Climate Corp, John Deere Operations Center, Indigo Ag - all Python backends"
- "The tools we're installing today are what industry uses"

#### Walk Through Installation (8 minutes)

**For Direct Python (5 min):**

- Share screen, show python.org
- Download installer (or show previously downloaded)
- Walk through installation options
- Emphasize "Add to PATH" checkbox
- Run `python --version` to verify
- Create virtual environment live

**For Anaconda (3 min):**

- Quick overview: "Anaconda includes data science packages"
- "Easier for some, heavier installation"
- "Either approach works - pick what fits you"

#### Demonstrate venv Creation (3 minutes)

- Create project folder
- Run `python -m venv ag-env`
- Activate it (show prompt change)
- Explain: "This is your isolated workspace"

#### Interactive Check (2 minutes)

- Pause: "Everyone successfully installed Python?"
- Screen share issues
- Quick troubleshoot or note for office hours

### Common Student Issues

**Issue 1: Python not found in PATH**

- **Windows:** Reinstall, check "Add to PATH"
- **Mac/Linux:** Check `.bashrc` or `.zshrc`
- **Quick fix:** Use full path to python.exe

**Issue 2: Multiple Python versions**

- **Solution:** Use `python3` or `python3.11` explicitly
- Check: `which python` to see what's running

**Issue 3: Permission errors**

- **Mac/Linux:** May need `sudo` for global installs (avoid global)
- **Better:** Use virtual environments (no sudo needed)

### Real-World Connection

- "At Bayer, every data scientist has multiple virtual environments"
- "One per project, sometimes one per client"
- "Prevents 'it works on my machine' problems"

</details>

---

### Essential Data Science Libraries

**Core Libraries for Agricultural Data:**

#### 1. Pandas 🐼

**Purpose:** Data manipulation and analysis

```python
import pandas as pd

# Read crop yield data
yields = pd.read_csv('yield_data.csv')

# Calculate average yield by field
avg_yield = yields.groupby('field_id')['yield_bu_acre'].mean()
```

**Use Cases:**

- Loading CSV files from USDA NASS
- Cleaning and filtering agricultural data
- Calculating statistics (mean yield, total acres)
- Merging datasets (yields + weather + soil)

#### 2. GeoPandas 🌍

**Purpose:** Geospatial data analysis

```python
import geopandas as gpd

# Read field boundaries
fields = gpd.read_file('field_boundaries.geojson')

# Calculate field areas
fields['area_acres'] = fields.geometry.area / 4046.86

# Spatial join with soil data
fields_with_soil = gpd.sjoin(fields, soil_data, how='left')
```

**Use Cases:**

- Working with field boundary shapefiles
- Calculating field areas and perimeters
- Spatial joins (fields + soil types)
- Creating maps of agricultural data

#### 3. Rasterio 🛰️

**Purpose:** Satellite imagery and raster analysis

```python
import rasterio

# Open Sentinel-2 band (e.g., Red band)
with rasterio.open('sentinel2_red.tif') as src:
    red_band = src.read(1)
    transform = src.transform

# Calculate statistics
mean_reflectance = red_band.mean()
```

**Use Cases:**

- Reading satellite imagery (Sentinel-2, Landsat)
- Calculating NDVI from multispectral bands
- Extracting pixel values for field zones
- Analyzing drone imagery

#### 4. Matplotlib & Plotly 📊

**Purpose:** Visualization

```python
import matplotlib.pyplot as plt
import plotly.express as px

# Simple plot
plt.plot(dates, yields)
plt.xlabel('Date')
plt.ylabel('Yield (bu/acre)')
plt.title('Corn Yield Over Time')

# Interactive dashboard
fig = px.scatter(df, x='ndvi', y='yield', color='field')
fig.show()
```

**Use Cases:**

- Plotting yield trends over time
- Creating NDVI heatmaps
- Building interactive dashboards
- Presenting analysis results

#### 5. NumPy & SciPy 🔢

**Purpose:** Numerical computation

```python
import numpy as np
from scipy import stats

# Calculate growing degree days
gdd = np.maximum(0, (temp_data - 50) / 2)

# Statistical analysis
correlation = stats.pearsonr(ndvi_values, yield_values)
```

**Use Cases:**

- Growing degree day calculations
- Statistical analysis of yields
- Array operations on large datasets
- Mathematical transformations

**Installation:**

```bash
# Activate your virtual environment first
source ag-env/bin/activate  # or ag-env\Scripts\activate on Windows

# Install core libraries
pip install pandas geopandas rasterio matplotlib plotly numpy scipy

# Install geospatial dependencies
pip install shapely fiona pyproj

# Install additional tools
pip install jupyter notebook requests python-dotenv

# Verify installations
python -c "import pandas; print('Pandas:', pandas.__version__)"
python -c "import geopandas; print('GeoPandas:', geopandas.__version__)"
python -c "import rasterio; print('Rasterio:', rasterio.__version__)"
```

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (10 minutes)

#### Overview Libraries (2 minutes)

- "These 5 library categories cover 90% of ag data work"
- "You'll use all of them in this course"
- "Same stack used at major ag companies"

#### Walk Through Each Library (6 minutes total, ~1 min each)

**Pandas:**

- Show quick example: loading yield CSV
- "Think Excel, but programmable and much faster"
- "Industry standard for tabular data"

**GeoPandas:**

- Show field boundary visualization
- "Pandas + geometry = GeoPandas"
- "Critical for field-level analysis"

**Rasterio:**

- Show satellite image loaded
- "How we work with imagery pixels"
- "Used in Assignment 07 for NDVI"

**Matplotlib/Plotly:**

- Show quick plot example
- "Matplotlib: static, publication-quality"
- "Plotly: interactive dashboards"

**NumPy/SciPy:**

- Show GDD calculation
- "Math backbone of everything else"
- "Fast array operations"

#### Live Installation (2 minutes)

- Run pip install commands
- Show progress bars
- Address any errors immediately
- Verify with import statements

### Common Student Issues

**Issue: GeoPandas installation fails**

- **Cause:** Missing GDAL/GEOS libraries
- **Solution (Windows):** Use conda instead: `conda install geopandas`
- **Solution (Mac):** `brew install gdal geos`
- **Solution (Linux):** `sudo apt install libgdal-dev libgeos-dev`

**Issue: ImportError despite installation**

- **Cause:** Wrong Python environment active
- **Solution:** Deactivate/reactivate venv
- **Check:** `which python` should point to venv

**Issue: Slow installation**

- **Cause:** Large dependencies (especially geospatial)
- **Solution:** Be patient, let it finish
- **Alternative:** Use conda (pre-compiled binaries)

### Real-World Examples

**Climate Corp Stack:**

- "We used all these libraries"
- "Plus custom internal tools built on them"
- "Pandas for farmer data, GeoPandas for fields, Rasterio for satellites"

**Typical Workflow:**

- Load field boundaries (GeoPandas)
- Load yield data (Pandas)
- Load satellite imagery (Rasterio)
- Calculate NDVI (NumPy)
- Visualize results (Matplotlib/Plotly)

</details>

---

### Git & GitHub Workflow

**Why Version Control for Agricultural Data Projects?**

- Track changes to analysis code over time
- Collaborate with team members
- Revert to previous working versions
- Document your analytical process
- Required for professional data science work
- Enables reproducible research

**Git Basics:**

**Installing Git:**

- **Windows:** Download from [git-scm.com](https://git-scm.com/)
- **Mac:** `brew install git` or included with Xcode
- **Linux:** `sudo apt install git`

**Verify:** `git --version`

**Essential Git Commands:**

```bash
# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Clone a repository
git clone https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit.git
cd agri-data-toolkit

# Check status
git status

# Add files to staging
git add filename.py
git add .  # Add all changes

# Commit changes
git commit -m "Add yield analysis script"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Create a branch
git branch feature/new-analysis
git checkout feature/new-analysis
# Or combined:
git checkout -b feature/new-analysis

# View commit history
git log --oneline
```

**GitHub Workflow for Assignments:**

1. **Clone the course repository:**

   ```bash
   git clone https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit.git
   ```

2. **Create assignment folder:**

   ```bash
   cd agri-data-toolkit
   mkdir -p assignments/02-workspace-setup
   cd assignments/02-workspace-setup
   ```

3. **Work on your assignment** (write code, analyze data)

4. **Stage and commit:**

   ```bash
   git add .
   git commit -m "Complete workspace setup assignment"
   ```

5. **Push to your fork or branch:**

   ```bash
   git push origin main
   ```

6. **Submit repository URL to Canvas**

**Best Practices:**

- ✅ Commit often with clear messages
- ✅ Use descriptive commit messages ("Add NDVI calculation" not "Update")
- ✅ Pull before you push to get latest changes
- ✅ Don't commit large data files (use `.gitignore`)
- ✅ Create branches for experimental work
- ❌ Don't commit API keys or passwords
- ❌ Don't commit generated outputs (plots, CSVs) unless necessary

**GitHub Authentication:**

GitHub now requires **Personal Access Tokens (PAT)** instead of passwords:

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `workflow`
4. Copy token (save it securely!)
5. Use token as password when pushing

**Alternative:** Use SSH keys (more secure, one-time setup)

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (15 minutes)

#### Why Git Matters (2 minutes)

- "Version control is non-negotiable in data science"
- "Every company uses Git - it's expected"
- "Saves you from 'final_v2_FINAL_REALLY.py' situations"

#### Live Git Demo (8 minutes)

**Setup Git (2 min):**

- Show `git config` commands
- Explain username/email purpose
- Check: `git config --list`

**Clone Repository (2 min):**

- Clone agri-data-toolkit live
- Show directory structure
- Explain: "This is your starting point"

**Make a Change (2 min):**

- Create test file: `test_setup.py`
- Add simple print statement
- Run `git status` - show untracked file

**Commit & Push (2 min):**

- `git add test_setup.py`
- `git commit -m "Test commit from Class 02"`
- Explain commit message importance
- `git push` (or show how to set upstream)

#### GitHub Authentication (3 minutes)

- Explain: "Passwords deprecated in 2021"
- Show PAT generation process
- Or demonstrate SSH key setup
- Recommend: Use GitHub Desktop as alternative

#### Best Practices (2 minutes)

- Show good vs bad commit messages
- Demonstrate `.gitignore` for data files
- Explain: "Commit code, not data"

### Common Student Issues

**Issue: "fatal: not a git repository"**

- **Cause:** Not in a Git-initialized folder
- **Solution:** `git clone` or `git init`

**Issue: Authentication failed**

- **Cause:** Using password instead of PAT
- **Solution:** Generate and use Personal Access Token

**Issue: Merge conflicts**

- **Cause:** Changes in same file from different sources
- **Solution:** Carefully resolve conflicts in editor
- **Prevention:** Pull before making changes

**Issue: Accidentally committed API keys**

- **Cause:** Didn't use .gitignore
- **Solution:** Remove from history, rotate keys
- **Prevention:** Use `.env` files and `.gitignore`

### Real-World Git Workflow

**At Bayer/Climate Corp:**

- Feature branches for all work
- Pull requests for code review
- CI/CD pipelines run tests automatically
- Commit messages link to task IDs
- "Your Git history tells the story of your project"

### Interactive Element

- Ask: "Who's used Git before?"
- Take questions about specific scenarios
- "What would you do if...?" scenarios

</details>

---

### VS Code & AI Assistant Integration

**Why VS Code for Agricultural Data Science?**

- Most popular editor for Python development
- Extensive extension ecosystem
- Integrated terminal and Git support
- Jupyter notebook integration
- AI assistants (Copilot, Roo Code) built-in
- Free and open-source

**Installing VS Code:**

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install with default settings
3. Launch VS Code

**Essential Extensions:**

**For Python Development:**

- **Python** (Microsoft) - IntelliSense, linting, debugging
- **Pylance** (Microsoft) - Fast language server
- **Jupyter** (Microsoft) - Notebook support in VS Code

**For Data Science:**

- **Data Wrangler** - Visual data exploration
- **Rainbow CSV** - Color-coded CSV viewing

**For AI Assistance:**

- **GitHub Copilot** - AI pair programmer (paid)
- **Roo Code** - Alternative AI coding assistant
- **IntelliCode** (Microsoft) - AI-assisted IntelliSense (free)

**For Version Control:**

- **GitLens** - Enhanced Git visualization
- **GitHub Pull Requests** - Review PRs in VS Code

**Installing Extensions:**

1. Click Extensions icon (left sidebar) or press `Ctrl+Shift+X`
2. Search for extension name
3. Click "Install"
4. Reload VS Code if prompted

**Configuring GitHub Copilot:**

1. **Get Copilot Access:**
   - Students: Free via [GitHub Student Pack](https://education.github.com/pack)
   - Others: $10/month subscription

2. **Install Extension:**
   - Search "GitHub Copilot" in Extensions
   - Install both "GitHub Copilot" and "GitHub Copilot Chat"

3. **Sign In:**
   - Click Copilot icon in bottom bar
   - Authorize with GitHub account

4. **Test It:**

   ```python
   # Type this comment:
   # Function to calculate NDVI from red and NIR bands

   # Copilot will suggest:
   def calculate_ndvi(red, nir):
       return (nir - red) / (nir + red)
   ```

**Using Copilot Effectively:**

**Good Prompts:**

```python
# Load field boundary shapefile and calculate area in acres
# Copilot suggests full code block

# Create a scatter plot of yield vs NDVI with matplotlib
# Copilot generates plotting code
```

**Copilot Chat:**

- Open with `Ctrl+I`
- Ask questions: "How do I read a GeoJSON file in Python?"
- Get inline explanations and code suggestions

**Configuring Roo Code (Alternative):**

1. Install "Roo Code" extension
2. Sign up at [roocode.ai](https://roocode.ai/)
3. Connect to your preferred AI model
4. Similar usage to Copilot

**VS Code Tips for Agricultural Data Work:**

**Integrated Terminal:**

- Open: `` Ctrl+` ``
- Run Python scripts directly
- Activate virtual environments
- Execute Git commands

**Jupyter Notebooks in VS Code:**

- Create `.ipynb` file
- Select Python interpreter (your venv)
- Run cells interactively
- View plots inline

**Debugging:**

- Set breakpoints (click left margin)
- Press `F5` to start debugging
- Inspect variables during execution

**Multi-File Editing:**

- Split editor: `Ctrl+\`
- View data file + code side-by-side

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (15 minutes)

#### Why VS Code (2 minutes)

- "Industry standard for data science"
- "Used by developers at Climate Corp, John Deere, everywhere"
- "Free, powerful, extensible"

#### Live VS Code Setup (8 minutes)

**Installation & First Look (2 min):**

- Show download page
- Quick install walkthrough
- Tour interface: explorer, search, git, extensions

**Install Extensions (3 min):**

- Open Extensions panel
- Install Python extension (show IntelliSense)
- Install Jupyter (show .ipynb support)
- Install Copilot (if students have access)

**Demonstrate Copilot (3 min):**

- Create new Python file
- Write comment: "Function to load yield CSV and calculate average"
- Show Copilot suggestion
- Accept it (`Tab`)
- Explain: "AI wrote this based on your comment"
- Show Copilot Chat for questions

#### Jupyter in VS Code (3 minutes)

- Create new notebook: `test.ipynb`
- Select Python interpreter (show venv)
- Run simple cell:

  ```python
  import pandas as pd
  print(pd.__version__)
  ```

- Show inline output
- Explain: "No need to leave VS Code for notebooks"

#### Best Practices (2 minutes)

- Use virtual environment interpreter
- Organize files in folders (data/, scripts/, notebooks/)
- Commit `.vscode/settings.json` for team settings
- Don't commit `.vscode/` folder to Git (add to `.gitignore`)

### Common Student Issues

**Issue: Python extension not finding interpreter**

- **Solution:** `Ctrl+Shift+P` → "Python: Select Interpreter"
- Choose your virtual environment

**Issue: Copilot not suggesting**

- **Check:** Signed in to GitHub?
- **Check:** Extension enabled?
- **Solution:** Restart VS Code

**Issue: Jupyter kernel won't start**

- **Cause:** ipykernel not installed in venv
- **Solution:** `pip install ipykernel`

**Issue: Terminal shows wrong environment**

- **Solution:** Close and reopen terminal after activating venv
- Or manually activate: `source ag-env/bin/activate`

### Real-World VS Code Usage

**At Climate Corp:**

- Entire team used VS Code or similar IDE
- Shared settings via Git for consistency
- Extensions standardized across team
- Remote development to cloud instances

**Professional Workflow:**

1. Open VS Code
2. Activate virtual environment (integrated terminal)
3. Open Jupyter notebook or .py file
4. Write code with Copilot assistance
5. Debug with breakpoints
6. Commit via Git panel
7. Push to GitHub

### Interactive Demo Ideas

**Live Coding with Copilot:**

- Ask students: "What should we build?"
- Suggestion: "Load sample yield data and plot it"
- Write comment, let Copilot generate code
- Run it live, show results
- Emphasize: "Verify AI code before running"

**Debugging Demo:**

- Intentionally introduce bug
- Set breakpoint
- Step through code
- Show variable inspection
- Fix bug

</details>

---

### Live Demo: Complete Workspace Setup

**End-to-End Workflow Demonstration:**

This section brings together everything from today's class in one continuous workflow.

**Step 1: Create Project Directory**

```bash
mkdir ~/agri-data-projects
cd ~/agri-data-projects
```

**Step 2: Create and Activate Virtual Environment**

```bash
python -m venv ag-env
source ag-env/bin/activate  # Mac/Linux
# or
ag-env\Scripts\activate  # Windows
```

**Step 3: Install Required Libraries**

```bash
pip install pandas geopandas rasterio matplotlib plotly numpy scipy jupyter
pip install shapely fiona pyproj requests python-dotenv
```

**Step 4: Clone Course Repository**

```bash
git clone https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit.git
cd agri-data-toolkit
```

**Step 5: Open in VS Code**

```bash
code .
```

**Step 6: Select Python Interpreter in VS Code**

- Press `Ctrl+Shift+P`
- Type "Python: Select Interpreter"
- Choose your `ag-env` virtual environment

**Step 7: Create Test Notebook**

- Create new file: `test_setup.ipynb`
- Add cell:

  ```python
  import pandas as pd
  import geopandas as gpd
  import rasterio
  import matplotlib.pyplot as plt

  print("✅ Pandas version:", pd.__version__)
  print("✅ GeoPandas version:", gpd.__version__)
  print("✅ Rasterio version:", rasterio.__version__)
  print("\n🎉 All libraries loaded successfully!")
  ```

- Run cell, verify output

**Step 8: Test Copilot (if available)**

- Create new file: `test_copilot.py`
- Write comment: `# Function to calculate growing degree days`
- Let Copilot suggest code
- Review and accept suggestion

**Step 9: Commit Your Work**

```bash
git add test_setup.ipynb test_copilot.py
git commit -m "Class 02: Verify workspace setup"
git push origin main
```

**Step 10: Verify Everything Works**

- ✅ Python 3.9+ installed
- ✅ Virtual environment created and activated
- ✅ Libraries import without errors
- ✅ VS Code recognizes interpreter
- ✅ Copilot or AI assistant working
- ✅ Git commits and pushes successfully

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Teaching Strategy (15 minutes)

#### Set Expectations (1 minute)

- "I'm going to do the entire setup from scratch"
- "Follow along on your computer"
- "Pause and ask questions anytime"

#### Execute Demo (10 minutes)

- Go slowly through each step
- Narrate what you're doing: "Now I'm creating the venv..."
- Show each command in terminal
- Display output after each step
- Pause after major steps: "Everyone with me?"

#### Troubleshoot Common Issues (2 minutes)

- Intentionally show 1-2 common errors
- Example: Import error → "Forgot to activate venv"
- Fix it live: "See how I diagnosed that?"

#### Verify Success (2 minutes)

- Run test imports
- Show green checkmarks
- "If you see this, you're ready for Class 03"

### Backup Plan

**If Live Demo Fails:**

- Have pre-recorded video ready
- Or use screenshots in slides
- Still walk through steps verbally

**If Many Students Have Issues:**

- "Let's pause and troubleshoot together"
- Screen share student issue
- Solve it collaboratively
- Document for others

### Post-Demo Actions

- Share terminal command history
- Post screenshots to discussion forum
- Announce office hours for setup help
- "If it didn't work, don't panic - we'll fix it"

### Real-World Connection

"This exact workflow:

- Is what I use every day
- Is what you'd do at Climate Corp, John Deere, any ag data company
- Is what employers expect you to know
- Is now YOUR workflow for this course"

### Interactive Element

**Checkpoint Questions:**

- "Show of hands: who has Python installed?"
- "Who successfully created a virtual environment?"
- "Who imported pandas without errors?"
- "Who has VS Code open?"

### Encouragement

- "Setup is always the hardest part"
- "Once it's working, it just works"
- "You now have professional-grade tools"
- "Same stack powering billion-dollar ag companies"

</details>

---

## ✍️ Assignment

**No Assignment for Class 02**

This is a setup class with no graded assignment. Your focus should be on:

**Checklist for Next Class:**

- ✅ Python 3.9+ installed and verified
- ✅ Virtual environment created (`ag-env` or similar)
- ✅ All required libraries installed (pandas, geopandas, rasterio, matplotlib, etc.)
- ✅ Git installed and configured
- ✅ Course repository cloned locally
- ✅ VS Code installed with Python and Jupyter extensions
- ✅ GitHub authentication configured (PAT or SSH)
- ✅ AI assistant (Copilot or alternative) set up (optional but recommended)

**Test Your Setup:**

Create a file called `test_setup.py` and run:

```python
import sys
import pandas as pd
import geopandas as gpd
import rasterio
import matplotlib.pyplot as plt

print(f"Python version: {sys.version}")
print(f"Pandas: {pd.__version__}")
print(f"GeoPandas: {gpd.__version__}")
print(f"Rasterio: {rasterio.__version__}")
print("\n✅ All systems ready for agricultural data analysis!")
```

Expected output: No errors, version numbers displayed

**If You Encounter Issues:**

1. Review class demo recording (posted to Canvas)
2. Check troubleshooting guide in course repository
3. Ask in discussion forum
4. Attend office hours this week
5. Use AI assistant to debug error messages

**Recommended (Optional):**

- Explore VS Code features and shortcuts
- Practice Git commands (clone, commit, push)
- Try Copilot with simple Python exercises
- Browse the agri-data-toolkit repository structure

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### Emphasize No Assignment (1 minute)

- "No graded assignment this week"
- "But setup is critical - don't skip it"
- "Class 03 assumes everything is working"

### Offer Support (1 minute)

- "Office hours this week: [times]"
- "Post issues in forum - help each other"
- "I'm available for troubleshooting"

### Set Expectations for Class 03 (1 minute)

- "Next week: hands-on with USDA data"
- "We'll download real agricultural datasets"
- "Everyone needs working setup by then"

</details>

---

## 🔗 Resources & References

### Installation Guides

- [Python Official Download](https://www.python.org/downloads/) - Get Python 3.11
- [Anaconda Distribution](https://www.anaconda.com/download) - Alternative Python distribution
- [Git Download](https://git-scm.com/downloads) - Version control system
- [VS Code Download](https://code.visualstudio.com/) - Code editor

### Documentation

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - Official venv guide
- [Pandas Documentation](https://pandas.pydata.org/docs/) - Data manipulation library
- [GeoPandas Documentation](https://geopandas.org/) - Geospatial data in Python
- [Rasterio Documentation](https://rasterio.readthedocs.io/) - Raster data access
- [Git Handbook](https://guides.github.com/introduction/git-handbook/) - Git basics

### VS Code Resources

- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial) - Getting started
- [VS Code Jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) - Notebook support
- [GitHub Copilot Docs](https://docs.github.com/en/copilot) - AI pair programming
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks) - Productivity guide

### GitHub Resources

- [GitHub Student Pack](https://education.github.com/pack) - Free Copilot for students
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) - Authentication
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) - Common commands

### Troubleshooting

- [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - Python questions
- [GeoPandas Install Issues](https://geopandas.org/en/stable/getting_started/install.html) - Platform-specific help
- [VS Code Python Issues](https://github.com/microsoft/vscode-python/issues) - Bug tracker

### Course Repository

- [agri-data-toolkit](https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit) - Main course repository
- [Setup Troubleshooting Guide](https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit/blob/main/docs/troubleshooting.md) - Common issues

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

### In Class (2 minutes)

- "Bookmark these resources"
- "Python and GeoPandas docs are essential references"
- "Troubleshooting guides save hours of frustration"

### Post-Class

- Verify all links work
- Update if any resources have moved
- Add new resources based on student questions

</details>

---
