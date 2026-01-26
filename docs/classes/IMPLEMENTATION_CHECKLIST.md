# 📋 Implementation Checklist: From PPTX to Markdown + Slides

**Version 2.0 - Slide-Generation Ready**  
**Last Updated:** January 26, 2026

> This checklist guides you through converting each PowerPoint into a slide-ready markdown file with speaker notes.

---

## 🚀 Quick Start

### One-Time Setup (5 minutes)

```bash
# Install required tools
npm install -g @marp-team/marp-cli
brew install pandoc  # macOS, or use package manager for Linux/Windows

# Verify installation
marp --version
pandoc --version
```

---

## 📱 Phase 1: Image Extraction (Per Class)

**Time:** 10-15 minutes per class

### Step 1: Extract Images from PowerPoint

```bash
# Navigate to PowerPoint file location
cd "3. Navigating the US Agricultural Data Landscape + Workshop.pptx"

# Extract using Python script (see script below)
python extract_pptx_images.py

# Output: Creates docs/classes/images/class03_slide##_img##.png
```

### Step 2: Organize Extracted Images

- [ ] All images extracted to `docs/classes/images/`
- [ ] Filenames follow pattern: `class##_slide##_img##.png`
- [ ] Create subfolder for class if needed: `class_03/`
- [ ] Remove duplicate or blank images
- [ ] Verify image quality (readable, relevant)

### Python Script: Extract Images from PPTX

Create file: `scripts/extract_pptx_images.py`

```python
import os
from pptx import Presentation
from pathlib import Path

def extract_images(pptx_path, output_dir):
    """
    Extract all images from PowerPoint file.

    Args:
        pptx_path: Path to .pptx file
        output_dir: Directory to save images
    """
    prs = Presentation(pptx_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Extract class number from filename
    pptx_name = Path(pptx_path).stem
    class_num = pptx_name.split('. ')[0].zfill(2)

    image_count = 0
    slide_num = 0

    for slide_idx, slide in enumerate(prs.slides, 1):
        slide_num = slide_idx
        img_in_slide = 0

        for shape_idx, shape in enumerate(slide.shapes):
            if shape.has_image:
                image = shape.image
                image_bytes = image.blob
                extension = image.ext

                filename = f"class{class_num}_slide{slide_num:02d}_img{img_in_slide:02d}.{extension}"
                filepath = output_path / filename

                with open(filepath, 'wb') as f:
                    f.write(image_bytes)

                print(f"Extracted: {filename}")
                image_count += 1
                img_in_slide += 1

    print(f"\nTotal images extracted: {image_count}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python extract_pptx_images.py <pptx_file> [output_dir]")
        sys.exit(1)

    pptx_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "docs/classes/images"

    extract_images(pptx_file, output_dir)
```

---

## 📋 Phase 2: Markdown Creation (Per Class)

**Time:** 45-60 minutes per class

### Step 1: Prepare Base Template

```bash
# Copy template for new class
cp docs/classes/TEMPLATE.md docs/classes/class_03.md
```

### Step 2: Fill in Metadata

- [ ] Update frontmatter: title, course, semester
- [ ] Add class number to filename: `class_03.md`
- [ ] Update last modified date

### Step 3: Extract Content from PowerPoint

**For each slide in PPTX:**

1. **Note the slide content** (text, bullet points)
2. **Identify key concepts** (what students see)
3. **Plan speaker notes** (what you'll explain)
4. **Mark images** (which images belong where)

### Step 4: Structure Visible Content (3-6 lines per slide)

For each slide in the PPTX:

```markdown
## 📚 [Slide Topic]

[Concise visible content - 80-150 words max]

[Bullet points or key facts]

<!-- NOTES
[Teaching notes for this slide]
-->
```

**Rule:** If visible content exceeds 150 words, split into multiple slides.

### Step 5: Write Speaker Notes (200-400 words per slide)

Each speaker notes section should include:

- **Teaching Strategy** - How to present this
- **Timing** - How long this section takes
- **Common Questions** - Anticipated student questions
- **Interactive Elements** - Engagement prompts
- **Real-World Connection** - Why it matters in agriculture
- **Watch-Out Areas** - Common misconceptions

### Step 6: Add Images with Captions

For each extracted image:

```markdown
![Descriptive alt text about what the image shows](images/class03_slide05_img01.png)
_Figure 1: What this visualization demonstrates_
```

- [ ] Images are referenced with relative paths
- [ ] Alt text is descriptive (20-30 words)
- [ ] Captions are italic and numbered sequentially
- [ ] Images placed near relevant text

### Step 7: Verify Slide Structure

- [ ] Frontmatter present (marp, title, theme)
- [ ] Each slide separated by `---`
- [ ] Each slide has exactly ONE H2 heading
- [ ] No emoji in content (clean for slide display)
- [ ] Visible content is concise (80-150 words)
- [ ] All speaker notes wrapped in `<!-- NOTES ... -->`

---

## 🔄 Phase 3: Conversion Testing (Per Class)

**Time:** 5-10 minutes per class

### Step 1: Convert to HTML

```bash
# Convert markdown to HTML slides
marp docs/classes/class_03.md -o docs/classes/slides/class_03.html

# Watch mode (auto-convert on save)
marp docs/classes/class_03.md -w
```

### Step 2: Test HTML Presentation

- [ ] Open `class_03.html` in browser
- [ ] Navigate through slides (arrow keys)
- [ ] View presenter mode (Alt+P)
- [ ] Verify speaker notes visible in presenter mode
- [ ] Check image rendering
- [ ] Test links

### Step 3: Convert to PDF

```bash
# Create PDF version (for printing/handouts)
marp docs/classes/class_03.md -o docs/classes/slides/class_03.pdf
```

### Step 4: Convert to PowerPoint (Optional)

```bash
# Create PowerPoint if needed for sharing
pandoc docs/classes/class_03.md -o docs/classes/slides/class_03.pptx \
  --from markdown \
  --to pptx \
  --slide-level 2
```

### Step 5: Quality Checklist

- [ ] All slides display correctly in HTML
- [ ] Images render properly
- [ ] Text is readable (font size, contrast)
- [ ] Presenter notes appear in Alt+P mode
- [ ] Links work
- [ ] No formatting errors
- [ ] PDF prints correctly
- [ ] PowerPoint conversion is acceptable (some formatting may shift)

---

## 📋 Phase 4: Content Review (Per Class)

**Time:** 15-20 minutes per class

### Content Verification

- [ ] Learning outcomes are specific and measurable
- [ ] Assignment is clear and achievable
- [ ] Resources are current and tested
- [ ] No placeholder text ([INSERT X], TODO)
- [ ] Spelling and grammar checked
- [ ] All links are active (https://)
- [ ] Real-world examples are relevant to agriculture

### Formatting Verification

- [ ] Heading hierarchy is correct (H1 title → H2 sections)
- [ ] Bold used for key terms and action verbs
- [ ] Code blocks have language specified
- [ ] Tables have headers
- [ ] Lists are properly formatted (bullets or numbers)
- [ ] No inconsistent spacing

### Speaker Notes Verification

- [ ] Each slide has speaker notes
- [ ] Notes follow format: `<!-- NOTES ... -->`
- [ ] Notes include teaching strategy, timing, questions
- [ ] Notes are 200-400 words (concise but complete)
- [ ] No markdown formatting in notes (plain text)

### Accessibility Verification

- [ ] All images have descriptive alt text
- [ ] Tables have clear headers
- [ ] Links have meaningful text (not "click here")
- [ ] High contrast between text and background
- [ ] Font sizes are readable (18pt+ for body, 24pt+ for slide titles)

---

## 🏗️ Phase 5: Finalization (Per Class)

**Time:** 5 minutes per class

### File Organization

```
docs/classes/
├── class_00.md           # Markdown master file
├── class_01.md
├── ...
├── class_14.md
├── slides/
│   ├── class_00.html     # HTML presentation
│   ├── class_00.pdf      # PDF handout
│   ├── class_01.html
│   └── ...
└── images/
    ├── class00_slide01_img01.png
    ├── class01_slide02_img01.png
    └── ...
```

### Git Commit

```bash
# Add class files
git add docs/classes/class_03.md
git add docs/classes/slides/class_03.html
git add docs/classes/slides/class_03.pdf
git add docs/classes/images/class03_*.png

# Commit with clear message
git commit -m "Add Class 03 markdown with slide generation + speaker notes

- Extracted 8 images from PowerPoint
- Created markdown with Marp frontmatter
- Added comprehensive speaker notes for all sections
- Generated HTML, PDF presentations
- Verified all links and images"

# Push to branch
git push origin slide-md-extraction
```

### Documentation

- [ ] Update main README with class availability
- [ ] Add to conversion status table (see below)
- [ ] Link to HTML slides in course materials
- [ ] Share PDF with students if using as handout

---

## 📋 Conversion Status Tracker

Use this table to track progress across all 15 classes:

| Class | Title            | Images Extracted | Markdown Created | HTML Generated | PDF Generated | Status      | Last Updated |
| ----- | ---------------- | ---------------- | ---------------- | -------------- | ------------- | ----------- | ------------ |
| 00    | Welcome          | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 01    | Farm Frontier    | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 02    | Gearing Up       | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 03    | US Ag Data       | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 04    | Clean Data       | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 05    | EDA              | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 06    | Geospatial       | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 07    | Satellite        | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 08    | Weather          | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 09    | Advanced Spatial | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 10    | Precision Ag     | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 11    | Soil Health      | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 12    | Dashboards       | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 13    | Ethics           | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |
| 14    | Future Farm      | ⬜               | ⬜               | ⬜             | ⬜            | Not Started | -            |

**Legend:**

- ⬜ = Not started
- 🟡 = In progress
- ✅ = Complete
- ❌ = Issues found

---

## 📊 Section-by-Section Guidance

### 🏠 Housekeeping Slide

**Extract from PPTX:**

- Bullet points about announcements, dates, reminders
- Usually 2-4 items

**Markdown Structure:**

```markdown
## 🏠 Housekeeping

- Announcement 1
- Announcement 2

<!-- NOTES
## Housekeeping Notes

- Item 1: [Context and why students should care]
- Item 2: [Due date, where to submit, any deadline info]
- Item 3: [Why this change affects them]

### Timing
- Allow 2-3 minutes for this section
- Pause after each item for questions

### Student Engagement
- Make eye contact
- Ask: "Does everyone understand X?"
- Answer immediately if confused
-->
```

### 📋 Syllabus Review Slide

**Extract from PPTX:**

- Connection to previous class
- Preview of today's topic
- Why it matters

**Markdown Structure:**

```markdown
## 📋 Syllabus Review

Last class we covered **[Previous Topic]**. Today we explore **[Today's Topic]**.

_This connects to [Future Topic] next week._

<!-- NOTES
## Syllabus Review Notes

### Connection Strategy (1 minute)
- "Two weeks ago we learned about [concept]"
- Ask: "Who recalls...?" - wait for response
- "That foundation is key for today"

### Bridge to Today (1 minute)
- "Today we're adding..."
- "Here's why this matters: [real-world example]"

### Pacing
- Total time: 2-3 minutes
- Don't rush
- Allow thinking time
-->
```

### 📍 Agenda Slide

**Extract from PPTX:**

- List of topics for the class
- Usually 5-7 items

**Markdown Structure:**

```markdown
## 📍 Agenda

- [x] Housekeeping (5 min)
- [ ] Syllabus Review (3 min)
- [ ] Topic 1 (15 min)
- [ ] Topic 2 (20 min)
- [ ] Assignment Preview (10 min)
- [ ] Q&A (10 min)

**Total:** 75 minutes

<!-- NOTES
## Agenda Notes

- "Here's how we'll structure our 75 minutes"
- "We'll have a break around 40 minutes in"
- Point out timing: "Our goal is to finish by [time]"

### Pacing Reminders
- Reference agenda when transitioning
- Adjust if needed, but communicate changes
- Prioritize questions over strict timing
-->
```

### 🎯 Learning Outcomes Slide

**Extract from PPTX:**

- 3-5 specific, measurable learning objectives
- Action verbs (Identify, Analyze, Create, Evaluate, etc.)

**Markdown Structure:**

```markdown
## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Identify** [specific element]
- **Analyze** [specific data/relationship]
- **Create** [specific output/solution]

<!-- NOTES
## Learning Outcomes Notes

- "These are our three goals for today"
- "If you don't feel confident with any of these, tell me"
- Reference throughout class: "This tests outcome 2..."

### Pacing
- 2-3 minutes to present
-->
```

### 📊 Key Images Slide

**Extract from PPTX:**

- Important diagrams, charts, photos
- Usually 1-3 images per class

**Markdown Structure:**

```markdown
## 📊 Key Images

![Description of what the image shows](images/class03_slide05_img01.png)
_Figure 1: What this demonstrates_

<!-- NOTES
## Key Images Notes

### Image 1 Teaching (2-3 minutes)
- "Look at [specific element]"
- "This shows [what to notice]"
- "Why it matters: [real-world application]"
- Ask: "What patterns do you see?"

### Real-World Connection
- "[Specific farm/company] uses this because..."
- "The result was..."
-->
```

### 📚 Content Slides (Multiple)

**Extract from PPTX:**

- Main teaching content
- Usually 3-5 slides of content
- Split into logical topics

**Markdown Structure (per content slide):**

```markdown
## 📚 [Topic Name]

### [Subtopic]

[Concise explanation - 80-150 words]

- Key point 1
- Key point 2
- Key point 3

<!-- NOTES
## [Topic Name] Notes

### Teaching Strategy (4-5 minutes)

#### Engage First (1 minute)
- "Open question: [Question for students]"
- Take 2-3 answers
- "Let me show you the formal approach..."

#### Explain Core Concept (2 minutes)
- Step-by-step explanation
- Use real example
- Show how it connects to agriculture

#### Interactive Element (1 minute)
- Ask: "What would happen if...?"
- Guide them toward the answer
- Affirm correct thinking

#### Check Understanding
- "Who has questions?"
- Address misconceptions
- Connect to next topic

### Common Misconceptions
- **Misconception:** [What students might think]
  **Reality:** [What's actually true]
  **How to address:** [Teaching strategy]

### Real-World Example
- [Specific farm, company, or situation]
- [How they use this concept]
- [The result or impact]

### Transition
- "Now that we understand [concept]..."
- "Let's look at [next topic]..."
-->
```

### ✍️ Assignment Slide

**Extract from PPTX:**

- Task name and objective
- Instructions
- Deliverable format
- Due date

**Markdown Structure:**

```markdown
## ✍️ Assignment

### [Assignment Title]

**Objective:** One sentence goal

**Your Challenge:** [Scenario or context]

**Instructions:**

1. [First step] (X min)
2. [Second step] (X min)
3. [Third step] (X min)

**Deliverable:**

Submit to Canvas:

- File: `LastName_Assignment.pdf`
- Format: [Description]
- Include: [What to include]

**Due:** [Date] at [Time]

<!-- NOTES
## Assignment Notes

### Presentation (4-5 minutes)

- "Let's look at your assignment"
- Walk through each step
- Show an example
- Clarify expectations

### Common Student Issues
- **Issue:** [What students struggle with]
  **Solution:** [How to help]

### After Assignment Turned In
- Grade within 1 week
- Provide detailed feedback
- Note recurring misconceptions

### Differentiation
- **For struggling:** [Modified version]
- **For advanced:** [Challenge version]
-->
```

### 🔗 Resources Slide

**Extract from PPTX:**

- Links to tools, articles, datasets
- Usually organized by category

**Markdown Structure:**

```markdown
## 🔗 Resources & References

### Official Sources

- [Resource Name](https://url) - Why this is useful
- [Another Resource](https://url) - Specific application

### Reading Materials

- Author, A. (Year). "Title." _Journal_, Vol.

### External Tools

- [Tool Name](https://url) - What it provides

<!-- NOTES
## Resources Notes

### In Class
- Mention 1-2 key resources
- Show how to access
- Bookmark in course materials

### For Students
- Required vs. optional
- Why each resource matters
- How to use each one
-->
```

---

## 💡 Pro Tips for Efficient Conversion

1. **Work batch-style** - Extract all images, then create all markdown, then convert all
2. **Use template** - Copy-paste structure for consistency
3. **Speaker notes first** - Write teaching strategy while fresh
4. **Test early** - Convert to HTML after first few slides to catch issues
5. **Real-world examples** - Add specific Michigan agriculture connections
6. **Timing is key** - Note actual time spent presenting each section
7. **Record feedback** - What students asked, what worked
8. **Version control** - Commit after each class conversion
9. **Keep backups** - Archive original PowerPoint files
10. **Iterate** - Improve based on classroom experience

---

## 🚀 Recommended Sequence

### Week 1: Setup

- [ ] Install Marp CLI and Pandoc
- [ ] Create extraction script
- [ ] Test on one class (Class 03 recommended)

### Week 2-4: Pilot Conversion

- [ ] Convert Class 03 fully
- [ ] Teach with new format
- [ ] Document what works
- [ ] Update style guide based on learnings

### Week 5-8: Scale

- [ ] Convert remaining 14 classes
- [ ] Maintain consistency
- [ ] Build automation scripts

### Week 9+: Optimization

- [ ] Create conversion pipeline
- [ ] Automate image extraction
- [ ] Automate markdown template generation
- [ ] Build continuous deployment

---

## ❔ Troubleshooting

### Images don't extract

**Problem:** PowerPoint images not found  
**Solution:** Verify PPTX file is not corrupted; try opening in PowerPoint first

### Marp conversion fails

**Problem:** HTML won't generate  
**Solution:** Check frontmatter syntax; verify `marp: true` and `---` separators

### Speaker notes invisible in HTML

**Problem:** Notes don't appear in presenter mode  
**Solution:** Use Alt+P to activate presenter mode; ensure notes in `<!-- NOTES ... -->` format

### PowerPoint conversion removes formatting

**Problem:** Pandoc output doesn't match markdown  
**Solution:** This is expected; use HTML for best presentation, PowerPoint for sharing only

### Images not found in presentation

**Problem:** Image paths broken in converted files  
**Solution:** Use relative paths; ensure images/ folder exists in output directory

---

## 📚 Resources

### Tools

- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Pandoc](https://pandoc.org)
- [python-pptx](https://python-pptx.readthedocs.io/)

### Documentation

- [Marp Markdown Syntax](https://marpit.marp.app/markdown)
- [Markdown Guide](https://www.markdownguide.org/)
- [Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

---

**Remember:** The goal is ONE source of truth (markdown) that generates unlimited formats. This checklist ensures consistency and efficiency across all 15 classes. 🌾

_Last Updated: January 26, 2026_
