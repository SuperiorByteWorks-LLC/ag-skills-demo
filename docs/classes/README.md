# Agricultural Data Systems - Class Documentation

This directory contains standardized markdown documentation for all Agricultural Data Systems courses, including a comprehensive style guide, reference examples, and templates.

## 📚 Files in This Directory

### Core Documentation

#### 1. **`STYLE_GUIDE.md`** - The Complete Reference
The authoritative guide for formatting all class documents. Use this when you need to understand:
- Exact structure and heading hierarchy
- Emoji usage and placement rules
- Formatting conventions (bold, italic, lists, tables, code blocks)
- Content density requirements
- Image and link guidelines
- Professional tone standards

**When to use:** Before creating any new class document or when editing existing content.

**Key sections:**
- 🏗️ Class Structure Template - The exact format to follow
- 🎨 Formatting Checklist - Detailed rules for text, lists, tables
- ✏️ Content Quality Checklist - Clarity, completeness, engagement standards
- 🔍 Final Review - Pre-publishing verification

---

#### 2. **`STYLE_REFERENCE_EXAMPLE.md`** - Real Example to Copy
A completely formatted example class document showing:
- Proper heading hierarchy
- Correct emoji placement (one per H2 section)
- Fully populated sections with appropriate content
- Realistic housekeeping items, learning outcomes, assignments
- Proper list and table formatting
- Correct resource section structure

**When to use:** As a template - literally copy its structure and replace content.

**Key features:**
- Shows all 9 required sections
- Demonstrates proper spacing and separators
- Includes example assignments with clear deliverables
- Shows resource organization patterns
- Uses realistic content for an agricultural data course

---

#### 3. **`STYLE_IMPLEMENTATION_CHECKLIST.md`** - Your Working Document
A practical, actionable checklist for applying the style guide:
- Before-you-start verification
- Section-by-section templates
- Formatting quick-checks
- Content quality verification
- Common mistakes to avoid (with fixes)
- Pro tips for professional results

**When to use:** While creating or updating class documents. Keep it open on a second screen.

**Key features:**
- Checkbox format - mark off as you complete each section
- Quick reference tables for statistics and formatting
- Visual examples of right vs. wrong approaches
- Step-by-step workflow for new and existing classes

---

#### 4. **`TEMPLATE.md`** - Ready-to-Use Starting Point
A blank template with:
- Marp frontmatter for slide integration
- Comprehensive speaker notes (in HTML comments)
- All 9 required sections pre-formatted
- Placeholder text clearly marked for replacement
- Teaching notes explaining what goes in each section

**When to use:** Starting a new class document from scratch.

**Key features:**
- Marp YAML frontmatter (convertible to slides)
- Extensive speaker notes for instructors
- Pre-formatted section headers with correct emoji
- Guidance text explaining what content belongs where
- Real teaching tips for classroom delivery

---

## 🚀 Quick Start Workflows

### Creating a New Class Document

**Option A: Fast Track (Using Template)**

1. Copy `TEMPLATE.md` to a new file: `class03.md`
2. Replace placeholders:
   - Title and course info
   - Housekeeping items
   - Syllabus review content
   - Learning outcomes
   - Main content sections
3. Add images from `images/` folder
4. Write assignment
5. Gather resources
6. Use `STYLE_IMPLEMENTATION_CHECKLIST.md` to verify
7. Save and commit

**Estimated time:** 2-3 hours

---

**Option B: From Example (Learning Mode)**

1. Open `STYLE_REFERENCE_EXAMPLE.md`
2. Study how each section is formatted
3. Create new file based on example structure
4. Adapt example content to your topic
5. Follow all emoji and formatting rules
6. Use `STYLE_GUIDE.md` for clarification
7. Run `STYLE_IMPLEMENTATION_CHECKLIST.md`
8. Save and commit

**Estimated time:** 3-4 hours (includes learning time)

---

**Option C: Using AI/Copilot (Scalable)**

1. Get student data/images from slide extraction
2. Provide these files to AI with instructions:
   ```
   Create a class document following STYLE_GUIDE.md.
   
   Use STYLE_REFERENCE_EXAMPLE.md as the structural template.
   Use TEMPLATE.md for the content outline.
   
   Topic: [Your Topic]
   Key Points: [Your Points]
   Images: [Your Image Files]
   
   Ensure:
   - All 9 sections included
   - Exact emoji usage (one per H2)
   - Proper heading hierarchy (H1 > H2 > H3 > H4)
   - Content density: 3-5 topics, 3-5 outcomes, 3-5 resources
   - Learning outcomes use specific action verbs
   ```
3. Review output against `STYLE_IMPLEMENTATION_CHECKLIST.md`
4. Make corrections
5. Save and commit

**Estimated time:** 1-2 hours

---

### Updating an Existing Class Document

1. Open the class markdown file
2. Check structure against `STYLE_GUIDE.md` - all 9 sections present?
3. Verify emoji usage - one emoji per H2 only?
4. Run through `STYLE_IMPLEMENTATION_CHECKLIST.md` section by section
5. Add missing sections
6. Fix formatting issues
7. Update content as needed
8. Refresh resources and links
9. Update "Last Updated" date
10. Commit with message: "Update class XX - [what changed]"

**Estimated time:** 45 minutes - 1 hour

---

## 📊 Directory Structure

```
docs/classes/
├── README.md                           # This file - overview and workflows
├── STYLE_GUIDE.md                      # Complete style rules (reference)
├── STYLE_REFERENCE_EXAMPLE.md          # Fully formatted example class
├── STYLE_IMPLEMENTATION_CHECKLIST.md   # Practical working checklist
├── TEMPLATE.md                         # Blank template to copy
│
├── class01.md                          # Individual class documents
├── class02.md                          # (created from template)
├── class03.md                          # (follow style guide)
├── class04.md                          # (verify with checklist)
├── ...
│
└── images/                             # Image subdirectory
    ├── class01_slide02_img01.png       # Organized by class and slide
    ├── class01_slide03_img01.png
    ├── class02_slide01_img01.png
    ├── class02_slide04_img02.png
    └── ...
```

---

## 🎯 Key Principles of the Style Guide

### Consistency
Every class follows the same structure, making content predictable for students and instructors.

**Structure (every class has):**
- Title & metadata
- Housekeeping announcements
- Connection to previous content
- Today's agenda
- 3-5 learning outcomes
- 2-5 key images
- 3-5 main content topics
- Clear assignment with due date
- 5-10 resources

### Clarity
Content is organized hierarchically with clear signposting.

**Hierarchy:**
- One H1 title
- 9 H2 sections (marked with emojis for quick navigation)
- H3 for content subtopics
- H4 for detailed points
- No deeper nesting

### Scannability
Students should understand the structure in 30 seconds.

**Visual cues:**
- One emoji per H2 section (indicates section type)
- Separator lines between sections (clear breaks)
- Bold for important terms
- Lists instead of paragraphs for multiple items

### Completeness
Every document has all necessary elements.

**Required sections:**
1. 🏠 Housekeeping
2. 📋 Syllabus Review  
3. 📍 Agenda
4. 🎯 Learning Outcomes
5. 📊 Key Images (if images available)
6. 📚 Content
7. ✍️ Assignment
8. 🔗 Resources
9. Metadata (duration, materials, last updated)

---

## 📝 Emoji Reference

Each section has exactly one emoji. Use these consistently:

| Emoji | Section | Meaning |
|-------|---------|----------|
| 🏠 | Housekeeping | Announcements, logistics, important info |
| 📋 | Syllabus Review | Connection to previous class |
| 📍 | Agenda | Plan for the 75 minutes |
| 🎯 | Learning Outcomes | Specific, measurable goals |
| 📊 | Key Images | Visual support (slides, diagrams, charts) |
| 📚 | Content | Main teaching material |
| ✍️ | Assignment | Work students will submit |
| 🔗 | Resources | Links, references, external materials |

**Rule:** One emoji per H2 section, nowhere else in the document.

---

## 🔄 Content Flow & Teaching Strategy

Each class follows this engagement pattern:

### Opening (First 10 minutes)
- **Housekeeping** (5 min) - Logistics, announcements
- **Syllabus Review** (3 min) - Connection to previous content
- **Learning Outcomes** (2 min) - Set expectations

### Main Content (35 minutes)
- **Content Section 1** - Introduce, explain, show example
- **Content Section 2** - Deepen understanding
- **Content Section 3** - Extend or apply concepts
- **Break point** (around 40 minutes in)

### Practice & Application (25 minutes)
- **Interactive practice** (10 min) - Guided exercises
- **Assignment introduction** (10 min) - Explain deliverable
- **Q&A and wrap-up** (5 min) - Address questions

### Closing
- Remind of learning outcomes achieved
- Preview next class
- Confirm assignment deadline
- Open for questions

---

## 🛠️ Using Speaker Notes (in TEMPLATE.md)

The template includes extensive speaker notes in HTML comments:

```html
<!-- NOTES
## Section Title Notes

### Key Teaching Points
- How long to spend (minutes)
- What to say (talking points)
- What students should do
- Common misconceptions to address

### Real-World Examples
- Specific scenarios
- Farm examples
- Industry applications
-->
```

**How to use:**
1. Copy template
2. Replace notes with YOUR speaking points
3. Keep during class (your notes on slide view)
4. Update after class with what worked
5. Reference when teaching again

Notes don't appear in converted slides - they're instructor-only.

---

## 📋 Before Publishing Checklist

### Quick Verification (2 minutes)
- [ ] All 9 sections present?
- [ ] Each H2 has exactly one emoji?
- [ ] Separator lines (---) after each section?
- [ ] No spelling/grammar errors?
- [ ] All links active?
- [ ] Images load correctly?
- [ ] Assignment has clear due date?
- [ ] Learning outcomes are specific?
- [ ] Metadata updated (date, materials)?

### Detailed Check (5 minutes)
Use `STYLE_IMPLEMENTATION_CHECKLIST.md` for comprehensive verification.

### Peer Review (Optional)
Have a colleague verify:
- Content accuracy
- Clear learning outcomes
- Realistic assignment timeline
- Working resources

---

## 📚 Learning Resources

### For New Users
1. Start with this `README.md`
2. Read `STYLE_GUIDE.md` thoroughly (15 min)
3. Study `STYLE_REFERENCE_EXAMPLE.md` (10 min)
4. Review `STYLE_IMPLEMENTATION_CHECKLIST.md` (5 min)
5. Copy `TEMPLATE.md` and start editing

**Total learning time:** ~45 minutes

### For Experienced Users
- Keep `STYLE_IMPLEMENTATION_CHECKLIST.md` open
- Reference `STYLE_GUIDE.md` for specifics
- Use `TEMPLATE.md` for new classes

### For Questions
- Check `STYLE_GUIDE.md` FAQ section
- Compare with `STYLE_REFERENCE_EXAMPLE.md`
- Review common mistakes section of `STYLE_IMPLEMENTATION_CHECKLIST.md`

---

## 🎓 Teaching Tips

### Making Classes Engaging
- Start each section with a question
- Use real agricultural examples
- Connect content to students' future work
- Include interactive elements (practice, discussion)
- Make assignments meaningful and doable

### Pacing (75 minutes)
- Housekeeping + Review: 8 minutes
- Content introduction: 10 minutes
- Deep dive + examples: 15 minutes
- Interactive practice: 15 minutes
- Assignment explanation: 10 minutes
- Q&A + wrap-up: 15 minutes

### Student Success
- Learning outcomes guide your teaching
- Assignment tests whether outcomes met
- Resources support students who need help
- Housekeeping keeps everyone on same page

---

## 📊 Statistics to Expect

When following this style guide, your classes will have:

| Metric | Target Range | Why |
|--------|------|-----|
| **Total Length** | 2000-3500 words | Comprehensive without overwhelming |
| **H2 Sections** | 9 sections | Consistent structure |
| **H3 Topics** | 3-5 per Content section | Focused, digestible content |
| **Learning Outcomes** | 3-5 | Specific, measurable goals |
| **Images** | 2-5 | Visual support without clutter |
| **Resources** | 5-10 | Enough support without overwhelming |
| **Assignment Time** | 4-6 hours | Realistic workload outside class |
| **Emoji Count** | 9 total | One per section, nowhere else |

---

## ✨ Version History

- **v1.0** (Jan 25, 2026) - Initial release with complete style guide, example, checklist, and template
- Future: Will evolve based on instructor feedback

---

## 📞 Questions or Suggestions?

- Review the relevant documentation file first
- Compare with `STYLE_REFERENCE_EXAMPLE.md`
- Check the common mistakes section of `STYLE_IMPLEMENTATION_CHECKLIST.md`
- Reach out to the course team with suggestions for improving the guide

---

**Remember:** The goal is to make course content consistent, clear, and professional. Following this style guide helps students learn better. 📚

*Last Updated: January 26, 2026*
