# Converting PowerPoint Slides to Markdown Classes

This guide explains how to transform existing PowerPoint presentations into standardized markdown class documents using the style guide.

## 🎯 Overview

**Goal:** Take a PowerPoint with slides and convert it into a full markdown class document.

**Why:** Markdown documents are:
- Version-controllable (GitHub)
- Searchable and indexable
- Easily updateable
- Convertible back to slides (Marp)
- Accessible to students
- Better for speaker notes integration

**Time required:** 2-4 hours depending on complexity

---

## 💻 The Conversion Process

### Phase 1: Analyze Your PowerPoint (15-30 minutes)

#### Step 1.1: Extract Slide Content

Open your PowerPoint and go through each slide:

1. **Title Slide**
   - Title
   - Subtitle (if present)
   - Date/semester
   - Instructor name (if shown)
   - **Note:** This becomes your H1 and metadata

2. **Content Slides** - For each, record:
   - Main heading (becomes H2 or H3)
   - Bullet points
   - Key details
   - Any visuals (images, charts, tables)
   - Speaker notes (if available)

3. **Images/Visuals**
   - Screenshots
   - Diagrams
   - Charts
   - Data visualizations
   - **Note:** Export at high quality (300 dpi if possible)

#### Step 1.2: Extract Images from PowerPoint

**Method A: Using PowerPoint Export**
1. In PowerPoint: File → Export → Change File Type → PNG/JPG
2. Select resolution (high quality preferred)
3. Export to folder
4. Rename: `class##_slide##_img##.png`

**Method B: Manual Screenshot**
1. View each slide full-screen
2. Use Print Screen or Cmd+Shift+4 (Mac)
3. Crop image to relevant area
4. Save as PNG: `class##_slide##_img##.png`
5. Optimize file size if needed (images shouldn’t exceed 500 KB each)

**Method C: Using Online Converter**
1. Upload PowerPoint to [CloudConvert](https://cloudconvert.com) or similar
2. Convert to PNG format
3. Download all images
4. Rename and organize

#### Step 1.3: Identify Structure

As you review slides, categorize them:

```
Slide 1: Title → H1 + Metadata
Slides 2-3: Announcements/Housekeeping → 🏠
Slide 4: Review of Previous → 📋
Slide 5: Agenda → 📍
Slide 6: Learning Outcomes → 🎯
Slides 7-9: Images → 📊
Slides 10-18: Main Content → 📚 (with H3 subtopics)
Slides 19-20: Activity/Practice → 📚 continued or interactive section
Slide 21: Assignment → ✍️
Slide 22: Resources → 🔗
Slide 23: Q&A/Closing → Optional section
```

**Note:** Your PowerPoint may not have all these elements. That's OK—create what's missing.

---

### Phase 2: Extract Detailed Content (30-60 minutes)

#### Step 2.1: Create Content Inventory

Make a spreadsheet or text document with:

| Element | Source Slide | Content | Format |
|---------|-------------|---------|--------|
| Title | 1 | "03 - Class Title" | H1 |
| Course | 1 | "Agricultural Data Systems \| Spring 2026" | Metadata |
| Housekeeping | 2-3 | "Reminder about deadlines..." | Bullet list |
| Previous Concept | 4 | "Last class we covered X" | Paragraph |
| Today's Topic | 4 | "Today we'll explore Y" | Paragraph |
| Image 1 | 7 | Field data visualization | PNG file |
| Learning Outcome 1 | 6 | "Identify field variables" | Action verb |
| Content Topic 1 | 10-12 | Multiple slides | H3 with bullet points |
| Assignment | 21 | Task description | Numbered steps |
| Resources | 22 | Links and references | Organized list |

Use this inventory as your roadmap.

#### Step 2.2: Extract Hierarchical Structure

For content slides, determine hierarchy:

```
Slide 10: "Soil Analysis Fundamentals"  → H3
  - Bullet 1                             → Bullet
  - Bullet 2                             → Bullet
Slide 11: "Soil Types"                   → H4
  - Type A with explanation              → Bullet
  - Type B with explanation              → Bullet
Slide 12: "Testing Methods"              → H4
  - Method 1                             → Bullet
  - Method 2                             → Bullet
```

Group related slides:
- Slides belong to same topic? Same H3
- Slides show subtopics? Use H4 for each
- Long list across multiple slides? Combine into one section

#### Step 2.3: Note Speaker Content

If your PowerPoint has speaker notes:

1. Export speaker notes as text (File → Export → Outline View)
2. Review each note
3. Flag key teachable points
4. Identify misconceptions to address
5. Note real-world examples mentioned

These notes become HTML comments in your markdown.

---

### Phase 3: Organize and Plan (15-30 minutes)

#### Step 3.1: Create Your Outline

```markdown
# 03 - Class Title
Metadata

## 🏠 Housekeeping
- Item 1
- Item 2

## 📋 Syllabus Review
Previous concept + today's topic

## 📍 Agenda
Checklist of 5-6 items

## 🎯 Learning Outcomes
3-5 specific outcomes with action verbs

## 📊 Key Images
Images from slides with captions

## 📚 Content
### Topic 1
Content from slides 10-12

### Topic 2  
Content from slides 13-15

### Topic 3
Content from slides 16-18

## ✍️ Assignment
Task and deliverable from slide 21

## 🔗 Resources
Links and references from slide 22
```

#### Step 3.2: Identify Missing Pieces

Your PowerPoint might not include:
- Housekeeping items (create relevant ones)
- Explicit learning outcomes (extract from content)
- Speaker notes (write based on content)
- Assignment due date (determine)
- Resource list (compile)

**Action:** Add these now during planning, not during writing.

#### Step 3.3: Set Your Content Budget

Refer to style guide statistics:
- Total: 2000-3500 words
- Content section: 1500-2000 words (3-5 topics)
- Each topic: 300-500 words
- Images: 2-5 total
- Resources: 5-10 links

Do your PowerPoint slides fit? If not:
- Too much? Condense or split into multiple classes
- Too little? Research and add depth

---

### Phase 4: Write the Markdown (90-120 minutes)

#### Step 4.1: Copy the Template

1. Copy `TEMPLATE.md`
2. Name it `classXX.md` where XX is your class number
3. Open in your markdown editor

#### Step 4.2: Fill Metadata

Replace:
```markdown
---
marp: true
title: "XX - Class Title Here"
theme: default
---

# XX - Class Title Here

*Agricultural Data Systems | Spring 2026*
```

With your actual information.

#### Step 4.3: Write Each Section

**🏠 Housekeeping** (5 min)
- Current announcements
- Reminders about dates
- Administrative updates
- 3-4 bullet points

**📋 Syllabus Review** (5 min)
- Sentence about previous class
- Sentence about today
- Sentence about future connection
- Extract from PowerPoint slide if present

**📍 Agenda** (5 min)
- Copy template checklist
- 5-6 items
- First is always "Housekeeping"
- Last is always "Q&A and Wrap-up"
- Include time estimates

**🎯 Learning Outcomes** (10 min)
- 3-5 specific outcomes
- Start with action verb: Identify, Analyze, Create, Evaluate, etc.
- Include specific object: "field variables," "data patterns," etc.
- Reference what outcome accomplishes

**📊 Key Images** (10 min)
- Export images from PowerPoint
- Place in `images/` folder
- Name: `class##_slide##_img##.png`
- Add markdown: `![Description](images/...)`
- Add italic caption: `*Figure 1: What this shows*`

**📚 Content** (45 min)
- Extract content from slides
- Organize into 3-5 H3 topics
- Use H4 for subtopics
- Follow style guide formatting
- Use tables for structured data
- Include blockquotes for definitions
- Max 3000 words total
- Reference images in this section

**✍️ Assignment** (15 min)
- Clear objective (one sentence)
- 2-3 steps numbered
- Specific deliverable
- Exact due date and time
- Optional: Grading rubric
- Submission instructions

**🔗 Resources** (10 min)
- Organize by type
- Use meaningful link text
- Add brief description
- Verify all links active
- 5-10 resources total

**Metadata** (5 min)
- Duration: 75 minutes
- Prep time: 10 minutes
- Materials needed: [your list]
- Last updated: [today's date]

#### Step 4.4: Add Speaker Notes

In HTML comments (after each H2 section), add:

```html
<!-- NOTES
## Section Notes

### Teaching Strategy
- What to emphasize
- How long to spend
- What students should do

### Real-World Examples
- Specific scenario
- Why it matters

### Common Misconceptions
- What students often think
- How to address
-->
```

---

### Phase 5: Verify and Polish (30-45 minutes)

#### Step 5.1: Structure Check

Use `STYLE_IMPLEMENTATION_CHECKLIST.md`:

- [ ] All 9 sections present?
- [ ] Each H2 has exactly one emoji?
- [ ] Heading hierarchy correct (H1 > H2 > H3 > H4)?
- [ ] Separator lines after each section?
- [ ] No more than 4 levels of heading?
- [ ] Images load correctly?
- [ ] All links active?

#### Step 5.2: Content Quality Check

- [ ] Learning outcomes are specific and measurable?
- [ ] Assignment has clear deliverable?
- [ ] Content fits in 2000-3500 word range?
- [ ] No spelling or grammar errors?
- [ ] Images have captions?
- [ ] Resources are current?
- [ ] Tone is consistent and professional?

#### Step 5.3: Formatting Check

- [ ] Bold for emphasis and important terms?
- [ ] Italic for definitions?
- [ ] Code blocks for technical content?
- [ ] Bullet points for lists?
- [ ] Tables for structured data?
- [ ] Blockquotes for definitions/tips?
- [ ] Consistent spacing throughout?

#### Step 5.4: Accessibility Check

- [ ] Images have descriptive alt text?
- [ ] Tables have headers?
- [ ] Links have meaningful text?
- [ ] High contrast text/background?
- [ ] No color-only meaning?
- [ ] Font size readable?

#### Step 5.5: Quick Proofread

1. Read through once for flow
2. Check each learning outcome
3. Verify assignment is doable
4. Confirm resources are current
5. Check metadata dates

---

## 📃 Mapping PowerPoint Slides to Markdown Sections

### Common PowerPoint Structures

#### Pattern 1: Standard Lecture Slides

```
PowerPoint Structure          → Markdown Structure

Slide 1: Title                → H1 + Metadata
Slide 2: Agenda               → 📍 Agenda
Slides 3-5: Learning Goals    → 🎯 Learning Outcomes
Slides 6-15: Content          → 📚 Content (3-5 H3 topics)
Slide 16: Case Study          → 📚 Content section or 📊 Key Images
Slide 17: Assignment          → ✍️ Assignment
Slide 18: Resources           → 🔗 Resources
Slide 19: Q&A                 → Covered in closing remarks
```

#### Pattern 2: Data-Heavy Slides

```
PowerPoint Structure          → Markdown Structure

Slide 1: Title                → H1 + Metadata
Slides 2-3: Data Overview     → 📋 Syllabus Review + 📍 Agenda
Slides 4-6: Dataset Details   → 📚 Content (with tables)
Slides 7-9: Analysis Methods  → 📚 Content (with code blocks)
Slides 10-13: Visualizations  → 📊 Key Images + 📚 Content
Slide 14: Interpretation      → 📚 Content section
Slide 15: Application         → ✍️ Assignment
Slide 16: Resources           → 🔗 Resources
```

#### Pattern 3: Short Demo Slides

```
PowerPoint Structure          → Markdown Structure

Slide 1: Title                → H1 + Metadata
Slide 2: Demo Outline         → 📍 Agenda
Slides 3-8: Live Demo         → 📚 Content with step-by-step instructions
Slide 9: Results              → 📊 Key Images
Slide 10: Practice Task       → ✍️ Assignment
Slide 11: Resources           → 🔗 Resources
```

---

## 📦 File Organization

### After Conversion, You'll Have:

```
classXX.md                           # Main markdown document
images/
  ├── classXX_slide02_img01.png    # Images extracted from slides
  ├── classXX_slide05_img01.png
  ├── classXX_slide08_img02.png
  └── ...
```

### Naming Convention

**Format:** `class##_slide##_img##.png`

- `##` (first): Class number (01, 02, 03, etc.)
- `##` (second): Source slide number
- `##` (third): Image number on that slide (01, 02, etc.)

**Examples:**
- `class03_slide05_img01.png` - First image from slide 5 of class 3
- `class05_slide12_img02.png` - Second image from slide 12 of class 5

---

## 🗣️ Speaker Notes Conversion

If your PowerPoint has speaker notes, convert them to HTML comments in markdown:

### PowerPoint Notes

```
Slide 10 notes:
"Start by asking students what variables affect soil health.
Wait for responses, then explain three main factors: moisture,
temperature, and pH. Show graph comparing different soils.
Common mistake: students think only pH matters."
```

### Becomes This in Markdown

```html
<!-- NOTES
## Content - Soil Health Factors

### Teaching Strategy (5 minutes)
1. Open with question: "What variables affect soil health?"
   - Wait 30 seconds for student responses
   - Affirm good answers: "Good thinking, yes..."
2. Present three main factors
   - Moisture: why it matters (plant availability)
   - Temperature: why it matters (biological activity)
   - pH: why it matters (nutrient availability)
3. Show comparison graph
   - Point out different soil profiles
   - Ask: "What do you notice?"

### Common Student Mistakes
- **Misconception:** "pH is the only thing that matters"
  **Reality:** All three factors interact
  **Fix:** "pH is important, AND moisture and temperature are equally critical"

### Real-World Example
Farm in Michigan experienced poor yield.
Tested soil: pH was good, but moisture management was poor.
After implementing drainage: yield increased 20%.
-->
```

---

## ⚠️ Common Conversion Mistakes

### ❌ Mistake 1: Too Many Bullet Points

**PowerPoint:** One slide with 10 bullet points

**Wrong approach:** Copy all 10 bullets into one markdown section

**Right approach:**
- Group related bullets into subtopics (H4)
- Reduce to 4-5 key bullets per topic
- Move others to supporting content
- Consider splitting into multiple sections

### ❌ Mistake 2: Image Names Don't Match

**Wrong:** `image1.png`, `soildata.jpg`, `Figure_A.png`

**Right:** `class03_slide05_img01.png`, `class03_slide07_img02.png`

### ❌ Mistake 3: Missing Metadata

**Wrong:** Title, no course/semester info

**Right:** "03 - Soil Analysis Fundamentals" with course/semester on second line

### ❌ Mistake 4: No Speaker Notes

**Wrong:** Just copy slide text, lose instructor insights

**Right:** Add HTML comment notes with teaching strategy

### ❌ Mistake 5: Incomplete Assignment

**Wrong:** "Do the exercise on page 10"

**Right:** 
- Clear objective
- Step-by-step instructions
- What to submit
- When it's due
- Grading criteria

### ❌ Mistake 6: Emoji Overuse

**Wrong:** Emojis in title, in bullet text, scattered everywhere

**Right:** Exactly one emoji per H2 section heading, nowhere else

### ❌ Mistake 7: Dead Links in Resources

**Wrong:** Copy links without verifying they work

**Right:** Test every link before publishing

---

## 🎶 Workflow Summary

### Quick Checklist

**Phase 1: Analyze (15-30 min)**
- [ ] Open PowerPoint
- [ ] Extract slide content
- [ ] Export images
- [ ] Identify structure

**Phase 2: Extract (30-60 min)**
- [ ] Create content inventory
- [ ] Extract hierarchy
- [ ] Note speaker content
- [ ] Flag missing pieces

**Phase 3: Organize (15-30 min)**
- [ ] Create outline
- [ ] Identify missing sections
- [ ] Set content budget
- [ ] Organize images

**Phase 4: Write (90-120 min)**
- [ ] Copy template
- [ ] Fill each section
- [ ] Add speaker notes
- [ ] Include images

**Phase 5: Polish (30-45 min)**
- [ ] Structure check
- [ ] Content quality check
- [ ] Formatting check
- [ ] Accessibility check
- [ ] Final proofread

**Total Time:** 3-5 hours

---

## 🏗️ Tools That Help

### For Converting PowerPoint
- **LibreOffice Impress** - Export slides as images
- **CloudConvert** - Batch convert slides to images
- **Pandoc** - Convert between document formats

### For Editing Markdown
- **VS Code** - Markdown preview built-in
- **Typora** - Dedicated markdown editor
- **Obsidian** - Knowledge management with markdown

### For Quality Checking
- **Grammarly** - Spelling and grammar
- **Hemingway Editor** - Sentence clarity
- **URL Checker** - Verify links are valid

---

## 🏣 Examples

See `STYLE_REFERENCE_EXAMPLE.md` for a complete converted class showing:
- Proper structure from PowerPoint slides
- Well-formatted content sections
- Clear learning outcomes
- Complete assignment section
- Organized resources

---

## 📞 Questions?

- Review `STYLE_GUIDE.md` for detailed formatting rules
- Check `STYLE_REFERENCE_EXAMPLE.md` for structural patterns
- Use `STYLE_IMPLEMENTATION_CHECKLIST.md` during conversion
- Reference `TEMPLATE.md` for section templates

---

**Remember:** The conversion takes time, but results in professional, version-controlled, student-friendly class documentation.

*Last Updated: January 26, 2026*
