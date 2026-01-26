# 🌾 Agricultural Data Course - Style Guide

**Version:** 1.0  
**Last Updated:** January 25, 2026  
**Purpose:** Ensure all 15 class notes maintain a professional, clean, and consistent aesthetic

---

## 📑 Quick Navigation

- [Overview](#overview)
- [Design Principles](#design-principles)
- [Standard Class Structure](#standard-class-structure)
- [Visual Hierarchy](#visual-hierarchy)
- [Typography & Formatting](#typography--formatting)
- [Emoji Usage Guide](#emoji-usage-guide)
- [Markdown Components](#markdown-components)
- [Class Template](#class-template)
- [Implementation Checklist](#implementation-checklist)
- [Examples](#examples)

---

## Overview

This style guide ensures all class materials are:

- **Clear** - Easy navigation with logical hierarchy
- **Consistent** - Uniform structure across all 15 classes
- **Professional** - Appropriate for academic and industry use
- **Scannable** - Quick to read and focused on learning
- **Accessible** - Works across all markdown viewers and platforms

### Design Philosophy

**Professional but approachable.** Use minimal, purposeful emoji (1 per section). Maintain academic tone while remaining engaging. Prioritize clarity over decoration.

---

## Design Principles

### 1. One Main Topic per Section

Each class covers ONE coherent topic. If content exceeds 3000 words, split into multiple sections.

### 2. Scannable Structure

Use clear headings, bullet points, and visual breaks. Readers should grasp content at a glance.

### 3. Progressive Disclosure

Start with overview, move to details. Use hierarchy to show relationships.

### 4. Learning-Focused

Every class clearly indicates:

- What students will learn (Learning Outcomes)
- How content connects (Syllabus Review)
- What they'll do (Assignments)

### 5. Consistent Navigation

Students should always know where to find agenda, assignments, and resources in every class.

---

## Standard Class Structure

Every class follows this 9-section template:

```markdown
# Class Number - Title

_Course Name | Semester_

## 🏠 Housekeeping

## 📋 Syllabus Review

## 📍 Agenda

## 🎯 Learning Outcomes

## 📊 Key Images & Resources

## 📚 Content

## ✍️ Assignment

## 🔗 Resources & References

## 📝 Instructor Notes (optional)
```

### Section Descriptions

| Section                  | Purpose                      | Length         | Required        |
| ------------------------ | ---------------------------- | -------------- | --------------- |
| **Title**                | Class number and topic       | 1 line         | ✅              |
| **🏠 Housekeeping**      | Announcements, logistics     | 2-4 bullets    | ✅              |
| **📋 Syllabus Review**   | Connection to course arc     | 2-3 sentences  | ✅              |
| **📍 Agenda**            | Session outline              | 4-6 checkboxes | ✅              |
| **🎯 Learning Outcomes** | What students will learn     | 3-5 bullets    | ✅              |
| **📊 Key Images**        | Visual resources from slides | Variable       | If images exist |
| **📚 Content**           | Main teaching material       | Variable       | ✅              |
| **✍️ Assignment**        | What to do, when due         | Variable       | ✅              |
| **🔗 Resources**         | Links and references         | 5-10 links     | ✅              |
| **📝 Notes**             | Instructor reminders         | Variable       | Optional        |

---

## Visual Hierarchy

### Heading Structure

```
# Class Title                    ← H1 (ONE per document)
## Section Name                   ← H2 (9 standard sections)
### Major Topic                   ← H3 (content subsections)
#### Detailed Subtopic            ← H4 (specific concepts)
```

**Rules:**

- Exactly ONE H1 per document (the class title)
- H2 for the 9 standard sections only
- H3 for major content topics
- H4 for detailed explanations within topics
- Never skip heading levels

### Spacing Standards

```markdown
## Section Heading

Content paragraph here.

---

## Next Section
```

- **Between sections:** Three blank lines (separator + blank + heading)
- **Between paragraphs:** One blank line
- **Within lists:** No blank lines between items
- **Separator:** `---` after each H2 section

---

## Typography & Formatting

### Text Styles

| Style    | Usage                      | Example                      |
| -------- | -------------------------- | ---------------------------- |
| **Bold** | Emphasis, key terms        | `**precision agriculture**`  |
| _Italic_ | Definitions, emphasis      | `*per hectare*`              |
| `Code`   | Technical terms, variables | `` `NDVI` ``, `` `Python` `` |
| > Quote  | Definitions, key concepts  | `> **Definition:** ...`      |

### When to Use Each

**Bold:**

- First mention of important terms
- Action verbs in learning outcomes
- Section labels ("Objective:", "Due:")

**Italic:**

- Foreign words or phrases
- Book/article titles
- Figure captions

**Code formatting:**

- Programming language names
- File names and paths
- Data formats (CSV, GeoTIFF)
- Technical acronyms (NDVI, SQL)

**Blockquotes:**

- Definitions
- Important warnings or tips
- Key takeaways

---

## Emoji Usage Guide

### ✅ DO: Minimal, Purposeful Emoji

Use **exactly one emoji per H2 section** for visual organization:

| Emoji | Section           | Purpose              |
| ----- | ----------------- | -------------------- |
| 🏠    | Housekeeping      | Administrative items |
| 📋    | Syllabus Review   | Course connection    |
| 📍    | Agenda            | Navigation/structure |
| 🎯    | Learning Outcomes | Goals/objectives     |
| 📊    | Key Images        | Data/visuals         |
| 📚    | Content           | Main material        |
| ✍️    | Assignment        | Tasks/activities     |
| 🔗    | Resources         | Links/references     |
| 📝    | Notes             | Instructor info      |

### ❌ DON'T: Excessive Emoji

**Wrong:**

```markdown
## 📚📊📈 Content & Data Analysis 🎉

This section 📊 covers data 🌾 visualization 📈
```

**Right:**

```markdown
## 📚 Content

This section covers data visualization for agricultural datasets.
```

**Emoji Rules:**

1. One emoji per H2 heading only
2. No emoji in body text
3. No emoji in links or code
4. No emoji in lists or tables
5. Use from approved list above

---

## Markdown Components

### Lists

#### Unordered (Bullet Points)

Use for non-sequential items:

```markdown
- First concept
- Second concept
- Third concept
```

#### Ordered (Numbered)

Use for sequential steps:

```markdown
1. Download data
2. Clean and validate
3. Perform analysis
```

#### Checkbox (Tasks)

Use for agenda and task lists:

```markdown
- [x] Completed item
- [ ] Upcoming item
- [ ] Another upcoming item
```

### Tables

Use for structured comparisons:

```markdown
| Data Source | Coverage | Access |
| ----------- | -------- | ------ |
| USDA NASS   | National | Free   |
| NRCS Soils  | National | Free   |
```

**Table Guidelines:**

- Always include header row
- Use pipes `|` for columns
- Align with dashes `---`
- Keep cell content concise

### Code Blocks

Use triple backticks with language:

````markdown
```python
import pandas as pd
df = pd.read_csv('harvest_data.csv')
```
````

**Supported languages:**

- `python`, `r`, `sql`, `bash`, `json`, `yaml`

### Blockquotes

Use for definitions and important notes:

```markdown
> **Definition:** Precision agriculture uses data to optimize field management.

> 💡 **Tip:** Always validate data before analysis.

> ⚠️ **Important:** Missing values affect results.
```

### Images

Use descriptive alt text and figure captions:

```markdown
![NDVI map showing vegetation health variation](images/class03_slide05_img01.png)
_Figure 1: NDVI classification with color scale (red=poor, green=healthy)_
```

**Image Guidelines:**

- Store in `docs/classes/images/` folder
- Use semantic naming: `class##_slide##_img##.ext`
- Always include alt text
- Add italic caption below
- Number figures sequentially

---

## Class Template

Copy this template for each new class:

````markdown
# 03 - Class Title Here

_Agricultural Data Systems | Spring 2026_

---

## 🏠 Housekeeping

- Announcement or logistics item
- Reminder about upcoming deadline
- Office hours or resource update

---

## 📋 Syllabus Review

Last class we covered [previous concept]. Today we'll explore [new concept],
which builds on that foundation and prepares us for [future topic].

---

## 📍 Agenda

- [x] Housekeeping
- [ ] Main topic 1
- [ ] Main topic 2
- [ ] Main topic 3
- [ ] Assignment preview

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Verb** specific, measurable outcome
- **Verb** another clear objective
- **Verb** third learning goal

_Use action verbs: Identify, Analyze, Create, Evaluate, Apply, Understand_

---

## 📊 Key Images & Resources

![Descriptive alt text](images/class03_slide02_img01.png)
_Figure 1: What this image shows_

---

## 📚 Content

### Major Topic 1

Introduction and overview of the topic...

#### Subtopic 1.1

Detailed explanation...

#### Subtopic 1.2

More details with examples...

### Major Topic 2

Next major concept...

> **Key Concept:** Important definition or principle here.

| Item | Description | Example  |
| ---- | ----------- | -------- |
| Data | What it is  | Instance |

```python
# Code example if relevant
import library
result = function()
```
````

---

## ✍️ Assignment

### Task: Descriptive Title

**Objective:** One sentence describing the goal

**Instructions:**

1. First step with clear action
2. Second step
3. Third step

**Deliverable:**

- What to submit
- Expected format
- File naming convention

**Due:** Specific date and time

**Grading Criteria:**

- Completeness (40%)
- Quality (40%)
- Presentation (20%)

---

## 🔗 Resources & References

### Official Sources

- [USDA NASS QuickStats](https://quickstats.nass.usda.gov/) - Agricultural statistics
- [NRCS Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/) - Soil data

### Reading Materials

- Author, Title (Year)
- Another Reference (Year)

### Tools & Datasets

- [Tool Name](URL) - Brief description

---

## 📝 Instructor Notes

_Optional section for teaching tips, common student questions, or prep notes_

- Note about difficult concept
- Suggestion for demonstration
- Reminder about class timing

---

**Class Duration:** 75 minutes  
**Preparation:** 10 minutes  
**Last Updated:** January 25, 2026

````

---

## Implementation Checklist

Use this checklist when creating or updating a class:

### Structure ✅
- [ ] H1 title with class number
- [ ] All 9 sections present
- [ ] Sections in correct order
- [ ] One emoji per H2 section
- [ ] Separator lines after sections

### Content ✅
- [ ] Housekeeping relevant and current
- [ ] Syllabus review connects to course arc
- [ ] Agenda has 4-6 checkbox items
- [ ] Learning outcomes use action verbs
- [ ] 3-5 specific outcomes listed
- [ ] Content organized with H3/H4 hierarchy
- [ ] Assignment clearly explained
- [ ] Due date specified
- [ ] Resources organized by category

### Formatting ✅
- [ ] Bold used for key terms
- [ ] Code blocks have language tags
- [ ] Tables have headers
- [ ] Images have alt text and captions
- [ ] Links use descriptive text
- [ ] No excessive emoji
- [ ] Consistent spacing throughout

### Quality ✅
- [ ] Spelling and grammar checked
- [ ] All links tested and active
- [ ] Images display correctly
- [ ] Tone is professional but approachable
- [ ] Content flows logically
- [ ] No orphaned sections

---

## Examples

### ✅ Good Example

```markdown
## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Identify** major US agricultural data sources
- **Evaluate** dataset quality for research needs
- **Access** USDA QuickStats platform effectively
- **Understand** common agricultural data formats

---

## 📚 Content

### Understanding Agricultural Data Sources

The US agricultural data ecosystem includes government, commercial,
and research sources. Each serves different purposes.

**Government sources** provide:
- Long historical records
- Official statistics
- Free public access

> **Key Insight:** Public data is free but may lack field-level detail.

### USDA NASS Overview

**What it is:** National agricultural statistics service

| Feature | Description |
|---------|-------------|
| Coverage | National, state, county |
| Update | Annual (some monthly) |
| Access | Free via QuickStats |

```python
# Example: Load NASS data
import pandas as pd
data = pd.read_csv('nass_corn_yield.csv')
````

````

### ❌ Bad Example

```markdown
## 📚📊🎯 Learning and Content!!! 🎉🌾

We'll learn stuff about data! 😊

- maybe identify some things
- look at datasets 📊
- do analysis 🔬
- create visualizations 📈

The USDA 🏛️ has data 📊 that farmers 🚜 use for crops 🌽!

Sources:
USDA - click here
NRCS - link
data.gov - somewhere
````

**Problems:**

- Multiple emoji in heading
- Emoji throughout body text
- Vague learning outcomes
- No action verbs or specificity
- Unprofessional tone
- Links not descriptive or formatted
- Missing structure elements

---

## Common Mistakes to Avoid

### 1. Inconsistent Heading Hierarchy

❌ Wrong:

```markdown
## Content

### Topic 1

##### Subtopic (skipped H4)
```

✅ Right:

```markdown
## 📚 Content

### Topic 1

#### Subtopic
```

### 2. Missing Separators

❌ Wrong:

```markdown
## 🏠 Housekeeping

Items here

## 📋 Syllabus Review
```

✅ Right:

```markdown
## 🏠 Housekeeping

Items here

---

## 📋 Syllabus Review
```

### 3. Vague Learning Outcomes

❌ Wrong:

```markdown
- Understand some concepts
- Learn about data
```

✅ Right:

```markdown
- **Analyze** agricultural datasets using Python pandas
- **Create** geospatial visualizations of field data
```

### 4. Poor Link Formatting

❌ Wrong:

```markdown
Click here: https://longurl.com/path/to/resource
```

✅ Right:

```markdown
[USDA NASS QuickStats](https://quickstats.nass.usda.gov/) - Agricultural statistics database
```

---

## Pro Tips

1. **Draft content first, format second** - Get ideas down, then apply style
2. **Use blockquotes for definitions** - Makes key concepts stand out
3. **Bold action verbs in outcomes** - Improves scannability
4. **Table for comparisons** - Cleaner than long paragraphs
5. **Test all links before committing** - Broken links hurt credibility
6. **Keep line length under 100 chars** - Easier to read and diff
7. **Version control** - Commit often with clear messages
8. **Get peer review** - Fresh eyes catch errors

---

## Questions & Adjustments

If you need to deviate from this guide:

1. **Document the reason** at the top of the file
2. **Explain why** it's necessary
3. **Consider updating** this guide if it's a good pattern

**Example note:**

```markdown
_Note: This class uses additional H4 headings due to topic complexity.
See STYLE_GUIDE.md for rationale._
```

---

## Version History

| Version | Date         | Changes             |
| ------- | ------------ | ------------------- |
| 1.0     | Jan 25, 2026 | Initial style guide |

---

## Quick Reference Card

**Structure:** Title → 🏠 → 📋 → 📍 → 🎯 → 📊 → 📚 → ✍️ → 🔗 → 📝

**Emoji:** One per H2 section, from approved list only

**Headings:** H1 (title) → H2 (sections) → H3 (topics) → H4 (details)

**Spacing:** 3 lines between sections, 1 between paragraphs

**Bold:** Key terms, action verbs, labels

**Code:** Technical terms, file names, languages

**Images:** Alt text + relative path + figure caption

**Links:** `[Descriptive text](URL)` with context

---

**Questions?** Open an issue in the repository or contact course team.

**Last Updated:** January 25, 2026
