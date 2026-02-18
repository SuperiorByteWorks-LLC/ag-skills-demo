# Class Documentation Guide

This guide shows you how to create consistent, professional class documents. Follow the structure below and use `TEMPLATE.md` to get started.

---

## Quick Start

1. Copy `TEMPLATE.md` to `classXX.md` (replace XX with class number)
2. Follow the 8-section structure below
3. Use the checklist at the end before publishing

---

## The 8-Section Structure

Every class has exactly these 8 sections in this order:

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

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Note 1
- Note 2

</details>

---
```

- H2 with exactly ONE emoji (🏠)
- Bullet points only
- Collapsible speaker notes (optional)
- Horizontal rule (---) after </details> for visual separation
- 3-4 items max

### 3. 📋 Syllabus Review

```
## 📋 Syllabus Review

Last class we covered [X]. Today we explore [Y].

This connects to [Z] next week.

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Connection to previous
- Bridge to today

</details>

---
```

- H2 with emoji (📋)
- 2-3 sentences max
- Connect previous → today → future
- Horizontal rule (---) after </details>

### 4. 📍 Agenda

```
## 📍 Agenda

- [x] Housekeeping
- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3
- [ ] Assignment preview

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Pacing notes
- Timing flexibility

</details>

---
```

- H2 with emoji (📍)
- Checkbox list
- First item checked
- 4-6 items total
- Horizontal rule (---) after </details>

### 5. 🎯 Learning Outcomes

```
## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Identify** [specific thing]
- **Analyze** [specific thing]
- **Create** [specific output]

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Assessment approach
- Success criteria

</details>

---
```

- H2 with emoji (🎯)
- Intro line: "After this class, you'll be able to:"
- 3-5 items
- Bold action verbs (Identify, Analyze, Create, Evaluate, Design)
- Specific, measurable outcomes
- Horizontal rule (---) after </details>

### 6. 📚 Content with Collapsible Speaker Notes

```
## 📚 Content

### Topic 1

Explanation and context here...

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Note 1
- Note 2
- Additional context
- Timing guidance

</details>

---

#### Subtopic 1.1
Details here

---

#### Subtopic 1.2
Details here

---

### Topic 2

![Description](images/class03_slide05_img01.png)
*Figure 1: What this shows*

More explanation...

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

Additional information:
- Key talking points
- Stories or examples
- Clarifications
- Transitions to next topic

</details>

---
```

- H2 with emoji (📚)
- H3 for each main topic (3-5 topics)
- H4 for subtopics only
- **Images inline with text** (place them where relevant to content)
- Italic caption below images: `*Figure N: Description*`
- **Collapsible speaker notes after content** (collapsed by default)
  - Use HTML `<details>` and `<summary>` tags
  - Summary text: `<strong>💬 Speaker Notes</strong>`
  - Can contain any formatted markdown (bullets, lists, links, code, etc.)
  - For any supplemental info: detailed notes, timing, stories, transitions, talking points
- **Horizontal rule (---) after EVERY </details> block for visual separation**
- **Horizontal rule (---) after subtopics** to clearly separate from next section
- 2000-3000 words total for content section
- Use **bold** for important terms
- Use `code` for technical terms
- Use tables for data
- Use blockquotes for definitions

### 7. ✍️ Assignment

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

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Grading rubric
- Common student issues

</details>

---
```

- H2 with emoji (✍️)
- H3 for task name
- Clear objective (one sentence)
- Numbered steps (not bullets)
- Explicit deliverable format
- Specific date and time
- Horizontal rule (---) after </details>

### 8. 🔗 Resources

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

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- How to use these resources
- Which are required vs optional

</details>

---
```

- H2 with emoji (🔗)
- Organize into subsections (Official, Reading, Tools, etc.)
- 5-10 links/resources total
- Meaningful link text (not "click here")
- Brief description for each
- Test all links before publishing
- Horizontal rule (---) after </details>

---

## Critical Formatting Rule: Horizontal Rules

**IMPORTANT:** Always add a horizontal rule (`---`) after EVERY `</details>` block to create clear visual separation between content sections.

### Why This Matters

- **Visual clarity** in both raw markdown and rendered view
- **Easier scanning** when editing or teaching from notes
- **Professional appearance** in documentation
- **Consistent separation** between major content sections

### Examples

#### ✅ CORRECT - With horizontal rule

```markdown
### Topic 1

Content about topic 1...

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

Teaching notes for topic 1...

</details>

---

### Topic 2

Content about topic 2...
```

**Result:** Clear visual break between Topic 1 and Topic 2

#### ❌ INCORRECT - Without horizontal rule

```markdown
### Topic 1

Content about topic 1...

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

Teaching notes for topic 1...

</details>

### Topic 2 ← Hard to see this is a new section!

Content about topic 2...
```

**Result:** Topics visually run together, hard to distinguish sections

---

## Approved Emoji List

### Core Section Emoji (Required - One Per H2)

| Emoji | Use                           | Section   |
| ----- | ----------------------------- | --------- |
| 🏠    | Housekeeping & announcements  | Section 2 |
| 📋    | Syllabus review & connections | Section 3 |
| 📍    | Agenda & roadmap              | Section 4 |
| 🎯    | Learning outcomes & goals     | Section 5 |
| 📚    | Main content & concepts       | Section 6 |
| ✍️    | Assignments & tasks           | Section 7 |
| 🔗    | Resources & references        | Section 8 |

### Agricultural & Data Emoji (For Content/Notes)

| Emoji | Use                                      |
| ----- | ---------------------------------------- |
| 🌾    | Crops, agriculture, farming              |
| 🚜    | Equipment, machinery, farming            |
| 🌱    | Growth, seedlings, new concepts          |
| 🌍    | Global, geospatial, location             |
| 📊    | Data, charts, analytics, graphs          |
| 📈    | Trends, growth, increase, optimization   |
| 📉    | Decline, decrease, patterns              |
| 💾    | Data storage, databases, files           |
| 🗂️    | Organization, structure, systems         |
| 🔍    | Analysis, investigation, discovery       |
| 🔄    | Cycles, processes, workflows, repetition |
| ⚙️    | Systems, mechanics, configuration        |
| 🎨    | Design, visualization, UI/UX             |

### Code & Technical Emoji

| Emoji | Use                               |
| ----- | --------------------------------- |
| 💻    | Code, programming, development    |
| 🐍    | Python code, scripts              |
| 📝    | Scripts, code files               |
| 🔧    | Tools, utilities, configuration   |
| 🔨    | Setup, tools, implementation      |
| ⚡    | Performance, optimization, speed  |
| 🔐    | Security, authentication, privacy |
| 🌐    | Web, internet, APIs               |

### Positive & Constructive Emoji

| Emoji | Use                                      |
| ----- | ---------------------------------------- |
| ✅    | Correct, success, verification, complete |
| ✔️    | Approved, confirmed                      |
| 👍    | Good practice, recommended approach      |
| 💡    | Tips, insights, ideas, best practices    |
| 🎓    | Learning, education, knowledge           |
| 📌    | Important, pin, key point                |
| ⭐    | Excellent, standout, special             |
| 🎁    | Bonus, extra, gift, special resource     |
| ➕    | Additional, extra, add more              |

### Cautionary & Negative Emoji

| Emoji | Use                                            |
| ----- | ---------------------------------------------- |
| ⚠️    | Warning, caution, important notice             |
| ❌    | Wrong, incorrect, avoid, don't do this         |
| 🚫    | Prohibited, blocked, no                        |
| ❓    | Questions, uncertain, check your understanding |
| 🔴    | Critical, stop, alert                          |
| ⛔    | Do not, prohibited, blocked                    |
| ➖    | Decrease, subtract, remove                     |

### Context & Meta Emoji

| Emoji | Use                                      |
| ----- | ---------------------------------------- |
| 💬    | Speaker notes, comments, thoughts        |
| 📌    | Remember, important, bookmark            |
| 🎬    | Demo, example, walkthrough               |
| 📹    | Video reference, screen recording        |
| 📖    | Reading, literature, reference           |
| 🔎    | Explore, discover, research              |
| 💭    | Think about, reflection, deeper thought  |
| 🤔    | Questions to consider, critical thinking |
| 👥    | Group work, collaboration                |
| 🗣️    | Discussion, speaking points              |

### Usage Notes

- Use section emoji **only in H2 headings** (once per section)
- Use content emoji **sparingly in body text** - emphasize key points only
- Use in speaker notes naturally without overdoing it
- Never use emoji in: title, metadata, code blocks, links, list bullets
- All emoji are optional in body text - use when it adds clarity

---

## Formatting Rules

### Emoji

- **One per section** in H2 headings only
- **Sparingly in content** for emphasis
- **Nowhere else** - no emoji in title, metadata, code, or links

### Headings

- `# Title` - H1 (ONE ONLY)
- `## 🏠 Section` - H2 (EIGHT TOTAL)
- `### Topic` - H3 (CONTENT ONLY)
- `#### Subtopic` - H4 (CONTENT ONLY)
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

### Images

- **Inline with content text** where relevant
- `![alt text](images/class03_slide05_img01.png)`
- Italic caption below: `*Figure 1: Description*`
- Numbered figures if multiple

### Speaker Notes (Collapsible)

```html
<details>
  <summary><strong>💬 Speaker Notes</strong></summary>

  - Bullet point 1 - Bullet point 2 - **Bold text** for emphasis - [Links](https://example.com) work fine - Even code
  blocks work
</details>

---
```

- Collapsed by default
- Can contain any markdown
- Include timing, stories, transitions, clarifications
- **ALWAYS follow with horizontal rule (---)**

### Horizontal Rules

- Use `---` (three hyphens)
- After EVERY `</details>` block
- After each H2 section
- After subtopics to separate from next content
- Creates clear visual breaks

### Links

- `[Meaningful text](https://full-url.com)`
- Test before publishing
- Use meaningful text (not "click here")

### Spacing

- Blank line between sections
- Blank line between paragraphs
- No blank lines within lists
- `---` separator after each H2 section and after `</details>` blocks

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

### ❌ Missing separator lines after speaker notes

```
<details>
<summary><strong>💬 Speaker Notes</strong></summary>
Notes here
</details>
### Next Topic  ← No --- between
```

✅ Fix: Add `---` after `</details>`

```
<details>
<summary><strong>💬 Speaker Notes</strong></summary>
Notes here
</details>

---

### Next Topic  ← Clear separation
```

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

### ❌ Images in separate section

```
## 📚 Content
[content here]
## 📊 Key Images  ← Separate section
[images here]
```

✅ Fix: Place images inline where relevant

```
## 📚 Content

### Topic 1
Explanation...
![Image](images/class03_slide05_img01.png)
*Figure 1: Description*
```

### ❌ Missing collapsible speaker notes

```
### Topic
Content here
[no speaker notes]
```

✅ Fix: Add speaker notes section

```
### Topic
Content here

<details>
<summary><strong>💬 Speaker Notes</strong></summary>

- Key talking points
- Timing guidance

</details>

---
```

---

## Before Publishing - Checklist

### Structure

- [ ] All 8 sections present in order
- [ ] Each H2 has exactly ONE emoji
- [ ] Separator lines (---) after each section
- [ ] Horizontal rules (---) after EVERY </details> block
- [ ] No missing required sections

### Content

- [ ] Learning outcomes are specific and measurable
- [ ] Assignment has exact due date/time
- [ ] All links tested and working
- [ ] Speaker notes present under major topics
- [ ] Images are inline with relevant content
- [ ] No spelling or grammar errors

### Formatting

- [ ] Heading hierarchy correct (H1 → H2 → H3 → H4)
- [ ] Emoji count correct (7 in H2s)
- [ ] Spacing consistent throughout
- [ ] Bold, italic, code used correctly
- [ ] Horizontal rules after all </details> blocks

### Images

- [ ] Image paths correct (relative paths)
- [ ] Alt text descriptive
- [ ] Captions present and numbered
- [ ] Images load correctly
- [ ] Images are positioned inline with related content

### Speaker Notes

- [ ] Collapsible sections under major topics
- [ ] Using proper `<details>` and `<summary>` tags
- [ ] Notes are collapsed by default
- [ ] Notes are well-formatted markdown
- [ ] Horizontal rule (---) after each </details> block

### Metadata

- [ ] Class number in title
- [ ] Course and semester listed

---

## Statistics to Aim For

| Metric              | Target          |
| ------------------- | --------------- |
| Total length        | 2000-3500 words |
| Content topics (H3) | 3-5             |
| Images              | 2-5 (inline)    |
| Learning outcomes   | 3-5             |
| Resources           | 5-10            |
| Section emoji       | 7 (one per H2)  |

---

## Tips for Success

1. **Use TEMPLATE.md** - Copy and customize, don't start from scratch
2. **Check one section at a time** - Don't try to verify everything at once
3. **Test all links** - Broken links destroy credibility
4. **Use bold and italic** - Scannability matters for students
5. **Be specific in assignments** - Vague = confused students
6. **Keep learning outcomes focused** - 3-5 is perfect
7. **Add speaker notes** - Helps with live teaching preparation
8. **Place images inline** - They should relate to nearby content
9. **Always add horizontal rules after </details>** - Visual clarity matters
10. **Get feedback** - Have someone else review before publishing

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

### The 8 H2 Sections

1. 🏠 Housekeeping
2. 📋 Syllabus Review
3. 📍 Agenda
4. 🎯 Learning Outcomes
5. 📚 Content (with inline images & speaker notes)
6. ✍️ Assignment
7. 🔗 Resources
8. (Metadata - no H2, just text)

### Heading Levels

- `# Title` - H1 (ONE ONLY)
- `## 🏠 Section` - H2 (EIGHT TOTAL)
- `### Topic` - H3 (CONTENT ONLY)
- `#### Subtopic` - H4 (CONTENT ONLY)

### Speaker Notes HTML

```html
<details>
  <summary><strong>💬 Speaker Notes</strong></summary>

  [Your formatted markdown content here]
</details>

---
```

**Always follow with horizontal rule!**

### Action Verbs for Outcomes

Identify, Analyze, Create, Evaluate, Design, Interpret, Describe, Compare, Explain, Apply, Develop, Build, Implement, Test, Deploy

---

## Questions?

**How do I add images?**
Create `images/` folder, export images from PowerPoint as PNG, rename using convention above, add inline where relevant: `![alt text](images/class03_slide05_img01.png)` with `*Figure 1: Description*` below.

**How do I add speaker notes?**
After any major content section, add a collapsible details block:

```html
<details>
  <summary><strong>💬 Speaker Notes</strong></summary>

  - Your notes here - Timing guidance - Stories or examples
</details>

---
```

**Don't forget the horizontal rule after!**

**How long should this take?**
Small class: 2-3 hours | Large class: 5-7 hours | Updating: 30 min - 1 hour

**Can I skip a section?**
No - all 8 sections are required.

**What if my content doesn't fit?**
If over 3500 words, split into multiple classes. If under 2000 words, add more depth or combine related topics.

---

**Remember:** Consistency makes it easier for students to learn. Follow this structure for every class.

_Last Updated: January 26, 2026_
