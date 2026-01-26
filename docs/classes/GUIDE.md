# Class Documentation Guide

This guide shows you how to create consistent, professional class documents. Follow the structure below and use `TEMPLATE.md` to get started.

---

## Quick Start

1. Copy `TEMPLATE.md` to `classXX.md` (replace XX with class number)
2. Follow the 9-section structure below
3. Use the checklist at the end before publishing

---

## The 9-Section Structure

Every class has exactly these 9 sections in this order:

### 1. Title & Metadata

```
# 03 - Class Title Here

*Agricultural Data Systems | Spring 2026*

---
```

- One H1 with class number
- Course and semester
- Separator line (---)

### 2. 🏠 Housekeeping

```
## 🏠 Housekeeping

- Announcement 1
- Announcement 2

---
```

- H2 with exactly ONE emoji (🏠)
- Bullet points only
- Separator line
- 3-4 items max

### 3. 📋 Syllabus Review

```
## 📋 Syllabus Review

Last class we covered [X]. Today we explore [Y].

This connects to [Z] next week.

---
```

- H2 with emoji (📋)
- 2-3 sentences max
- Connect previous → today → future
- Separator line

### 4. 📍 Agenda

```
## 📍 Agenda

- [x] Housekeeping
- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3
- [ ] Assignment preview

---
```

- H2 with emoji (📍)
- Checkbox list
- First item checked
- 4-6 items total
- Separator line

### 5. 🎯 Learning Outcomes

```
## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Identify** [specific thing]
- **Analyze** [specific thing]
- **Create** [specific output]

---
```

- H2 with emoji (🎯)
- Intro line: "After this class, you'll be able to:"
- 3-5 items
- Bold action verbs (Identify, Analyze, Create, Evaluate, Design)
- Specific, measurable outcomes
- Separator line

### 6. 📊 Key Images (optional)

```
## 📊 Key Images

![Description](images/class03_slide05_img01.png)
*Figure 1: What this shows*

![Another](images/class03_slide08_img01.png)
*Figure 2: Another concept*

---
```

- H2 with emoji (📊)
- Markdown image syntax with alt text
- Relative paths: `images/classXX_slideYY_imgZZ.png`
- Italic caption below each: `*Figure N: Description*`
- Separator line
- **Skip this section if no images**

### 7. 📚 Content

```
## 📚 Content

### Topic 1

Explanation and context here...

#### Subtopic 1.1
Details here

#### Subtopic 1.2
Details here

### Topic 2

More explanation...

---
```

- H2 with emoji (📚)
- H3 for each main topic (3-5 topics)
- H4 for subtopics only
- 2000-3000 words total for content section
- Use **bold** for important terms
- Use `code` for technical terms
- Use tables for data
- Use blockquotes for definitions
- Separator line at end

### 8. ✍️ Assignment

```
## ✍️ Assignment

### Task Name

**Objective:** One sentence goal

**Instructions:**
1. Step 1 - specific action
2. Step 2 - specific action
3. Step 3 - specific action

**What to submit:** Format and details

**Due:** Monday, March 3, 2026 at 11:59 PM EST

---
```

- H2 with emoji (✍️)
- H3 for task name
- Clear objective (one sentence)
- Numbered steps (not bullets)
- Explicit deliverable format
- Specific date and time
- Separator line

### 9. 🔗 Resources

```
## 🔗 Resources

### Official
- [Resource Name](https://example.com) - Why it matters
- [Another](https://example.com) - What it provides

### Reading
- Title (Author, Year)
- Another (Author, Year)

### Tools
- [Tool Name](https://example.com) - Purpose

---
```

- H2 with emoji (🔗)
- Organize into subsections (Official, Reading, Tools, etc.)
- 5-10 links/resources total
- Meaningful link text (not "click here")
- Brief description for each
- Test all links before publishing
- Separator line

### 10. Footer

```
**Class Duration:** 75 minutes
**Prep Time:** 10 minutes
**Materials:** Laptop, [specific software]

*Last Updated: January 26, 2026*
```

- Class duration
- Prep/setup time
- What students need
- Last update date

---

## Formatting Rules

### Emoji

- **One per section** (one 🏠, one 📋, etc.)
- **Nowhere else** - no emoji in body text, lists, or content
- Approved emojis: 🏠 📋 📍 🎯 📊 📚 ✍️ 🔗

### Headings

- **H1:** Exactly one (title only)
- **H2:** Nine sections (housekeeping through resources)
- **H3:** Content topics only
- **H4:** Subtopics only
- Never use H5 or deeper

### Text

- **Bold** for emphasis and important terms: `**term**`
- _Italic_ for definitions: `*term*`
- `Code` for technical: `` `command` ``
- > Blockquotes for definitions: `> Quote`

### Lists

- Bullets for non-sequential: `- item`
- Numbers for steps: `1. step`
- Checkboxes for agenda: `- [ ] item`
- Consistent indentation (2 spaces)

### Links

- `[Meaningful text](https://full-url.com)`
- Test before publishing
- Use meaningful text (not "click here")

### Spacing

- Blank line between sections
- Blank line between paragraphs
- No blank lines within lists
- `---` separator after each H2 section

---

## Common Mistakes to Avoid

### ❌ Multiple emoji per section

```
## 📚📊📈 Content Topics  ← WRONG
```

✅ Fix: Use one emoji

```
## 📚 Content  ← RIGHT
```

### ❌ Missing separator lines

```
## 🏠 Housekeeping
- Item
## 📋 Syllabus Review  ← No --- between
```

✅ Fix: Add `---` after each section

### ❌ Vague learning outcomes

```
- We'll look at some data
- Maybe discuss analysis
```

✅ Fix: Be specific and measurable

```
- **Analyze** field data using Python
- **Create** visualizations of patterns
```

### ❌ Generic assignment

```
**Due:** Next week
**Deliverable:** Something about the topic
```

✅ Fix: Be specific

```
**Due:** Friday, March 7, 2026 at 5:00 PM EST
**Deliverable:** PDF with analysis and written responses
```

### ❌ Broken or untested links

✅ Fix: Click every link before publishing

### ❌ Inconsistent heading hierarchy

```
## 📚 Content
### Topic
#### Detail
### Topic 2
##### Wrong level ← Too deep
```

✅ Fix: H3 for topics, H4 for details max

---

## Before Publishing - Checklist

### Structure

- [ ] All 9 sections present in order
- [ ] Each H2 has exactly ONE emoji
- [ ] Separator lines (---) after each section
- [ ] No missing required sections

### Formatting

- [ ] Heading hierarchy correct (H1 → H2 → H3 → H4)
- [ ] Emoji count correct (9 total, one per section)
- [ ] Spacing consistent throughout
- [ ] Bold, italic, code used correctly

### Content Quality

- [ ] Learning outcomes are specific and measurable
- [ ] Assignment is clear with exact due date/time
- [ ] All links are tested and working
- [ ] No spelling or grammar errors
- [ ] Resources are current

### Images (if included)

- [ ] Image paths correct
- [ ] Alt text descriptive
- [ ] Captions present and numbered
- [ ] Images load correctly

### Metadata

- [ ] Class number in title
- [ ] Course and semester listed
- [ ] Duration noted (typically 75 min)
- [ ] Last updated date current

---

## Statistics to Aim For

| Metric            | Target              |
| ----------------- | ------------------- |
| Total length      | 2000-3500 words     |
| Content topics    | 3-5                 |
| Images            | 2-5 (optional)      |
| Learning outcomes | 3-5                 |
| Resources         | 5-10                |
| Emoji count       | 9 (one per section) |

---

## Tips for Success

1. **Use TEMPLATE.md** - Copy and customize, don't start from scratch
2. **Check one section at a time** - Don't try to verify everything at once
3. **Test all links** - Broken links destroy credibility
4. **Use bold and italic** - Scannability matters for students
5. **Be specific in assignments** - Vague = confused students
6. **Keep learning outcomes focused** - 3-5 is perfect
7. **Update metadata** - Current dates show you care
8. **Get feedback** - Have someone else review before publishing

---

## File Naming Convention

**Classes:** `classXX.md` where XX is the class number (01, 02, 03, etc.)

**Images:** `classXX_slideYY_imgZZ.png`

- `XX` = class number
- `YY` = source slide number
- `ZZ` = image number on that slide

**Examples:**

- `class03_slide05_img01.png`
- `class05_slide12_img02.png`

---

## Quick Reference

### The 9 Emoji

1. 🏠 Housekeeping
2. 📋 Syllabus Review
3. 📍 Agenda
4. 🎯 Learning Outcomes
5. 📊 Key Images
6. 📚 Content
7. ✍️ Assignment
8. 🔗 Resources
9. (Footer - no emoji)

### Heading Levels

- `# Title` - H1 (ONE ONLY)
- `## 🏠 Section` - H2 (NINE TOTAL)
- `### Topic` - H3 (CONTENT ONLY)
- `#### Subtopic` - H4 (CONTENT ONLY)

### Action Verbs for Outcomes

Identify, Analyze, Create, Evaluate, Design, Interpret, Describe, Compare, Explain, Apply, Develop, Build, Implement, Test, Deploy

---

## Questions?

**How do I add images?**
Create `images/` folder, export images from PowerPoint as PNG, rename using convention above, add markdown: `![alt text](images/class03_slide05_img01.png)`

**How long should this take?**
Small class: 2-3 hours | Large class: 5-7 hours | Updating: 30 min - 1 hour

**Can I skip a section?**
No - all 9 sections are required except Key Images (optional if no images).

**What if my content doesn't fit?**
If over 3500 words, split into multiple classes. If under 2000 words, add more depth or combine related topics.

**Should I include speaker notes?**
Optionally in HTML comments: `<!-- NOTES section here -->`

---

**Remember:** Consistency makes it easier for students to learn. Follow this structure for every class.

_Last Updated: January 26, 2026_
