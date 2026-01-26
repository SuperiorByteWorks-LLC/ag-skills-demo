# ✅ Agri-Data Toolkit: Class Content Style Guide v2.0

**Slide-Generation Ready**  
**Last Updated:** January 26, 2026

> This guide ensures all course materials are consistently formatted, easily converted to slides, and instructor-friendly with integrated speaker notes.

---

## 🎯 Overview

Your markdown files serve **dual purpose:**

1. **Student-facing content** - Full class notes they can study
2. **Slide template** - Auto-convertible to presentations (HTML, PowerPoint, PDF)

By writing once with speaker notes, you generate unlimited formats. This is **maximum efficiency.**

---

## 🏗️ Architecture: Slide Blocks + Speaker Notes

### Core Concept

Each class is structured as **slide blocks:**

- **One slide block** = One presentation slide
- **Visible content** = What students see on screen (concise)
- **Speaker notes** = What you present (detailed guidance)
- **Slide separators** = `---` on their own line
- **Notes format** = HTML comments: `<!-- NOTES ... -->`

### Why This Works

```
Markdown file (single source of truth)
    ↓
    ├─→ [Marp CLI] → HTML slides (browser, presenter mode)
    ├─→ [Pandoc] → PowerPoint (.pptx)
    ├─→ [reveal.js] → Interactive web presentation
    ├─→ [Print to PDF] → Student handout
    └─→ [Read as is] → Full class notes
```

---

## 📋 Full Class Template

This is your starting point for every class:

```markdown
---
marp: true
title: '03 - Class Title Here'
theme: default
---

# 03 - Class Title Here

_Agricultural Data Systems | Spring 2026_

<!-- NOTES
## Title Slide Notes

### Before Class (5 min before start)
- Check laptop/projector connection
- Test internet connectivity
- Have attendance sheet ready

### First 3 Minutes
- Welcome students as they arrive
- Take attendance
- Brief overview: "Today we're covering [topic], which connects to [previous] and leads to [future]"
- Set expectations: "By end of class, you'll be able to [outcome 1], [outcome 2], [outcome 3]"
- Announce: "We'll have a 10-minute break around 40-minute mark"

### Key Themes to Establish
- Topic is relevant to real agricultural work
- Builds on what they've learned
- Sets up for future applications
-->

---

## 🏠 Housekeeping

- Announcement or logistics item
- Reminder about upcoming deadline
- Office hours or resource update

<!-- NOTES
## Housekeeping Talking Points

- **Item 1:** Context is... This matters because...
- **Item 2:** Due date is... Submit to... Any questions?
- **Item 3:** This upcoming change affects... Here's how you'll adapt...

### Timing
- Allow 2-3 minutes for this section
- Pause after each item: "Any quick questions?"
- Note in gradebook if announcement requires action

### Student Engagement
- Make eye contact
- Ask if anyone didn't understand
- Clarify immediately if confused
-->

---

## 📋 Syllabus Review

Last class we covered **[Previous Concept]**. Today we'll explore **[Today's Topic]**, building on that foundation.

_This connects to [Future Topic] next week._

<!-- NOTES
## Syllabus Review Talking Points

### Connection to Previous Class (1 minute)
- "Two weeks ago we learned about [concept]"
- "Remember when we discussed [specific lesson]?"
- Ask: "Who can quickly recap what we covered?"
- Wait for response (30 seconds)

### Bridge to Today (1 minute)
- "That knowledge is the foundation for today"
- "Today we're adding the next layer: [today's topic]"
- "Here's why this matters in real agriculture: [specific scenario]"

### Preview of Connection (30 seconds)
- "Next week we'll apply this to [future topic]"
- "So by the end of today, you'll have the skills to..."

### Pacing
- Total time: 2-3 minutes
- Don't rush - let students think
- Pause for questions
-->

---

## 📍 Agenda

- [x] Housekeeping (5 min)
- [ ] Syllabus Review (3 min)
- [ ] Concept Introduction (10 min)
- [ ] Deep Dive + Example (15 min)
- [ ] Interactive Practice (15 min)
- [ ] Assignment Preview (10 min)
- [ ] Q&A and Wrap-up (10 min)

**Total:** 75 minutes

<!-- NOTES
## Agenda Talking Points

- "Here's how we'll structure our 75 minutes together"
- "We have a natural break around 40 minutes"
- "Our goal is to end by [specific time] sharp"
- Ask: "Any concerns about this schedule?"

### During Class
- Reference the agenda when transitioning topics
- "We're about 20 minutes in; moving to our next topic"
- Adjust timing if needed, but communicate changes

### Timing Flexibility
- If spending extra time on Q&A? Fine - cut from wrap-up
- If moving faster? Don't skip content - compress later sections
- Always prioritize student questions
-->

---

## 🎯 Learning Outcomes

After this class, you'll be able to:

- **Identify** [specific element/concept in agricultural context]
- **Analyze** [specific data/pattern/relationship relevant to field work]
- **Create** [specific output/visualization/solution students will produce]

<!-- NOTES
## Learning Outcomes Talking Points

### Present These Goals (2-3 minutes)
"These are our three main goals for today. By the end of the 75 minutes, I want you to feel confident doing each of these. If you don't, please let me know - we'll follow up."

### Reference These Throughout Class
- "This connects back to our first learning outcome..."
- "By doing this exercise, you're working on outcome 2..."
- "Your assignment today tests whether you've achieved outcome 3..."

### Assessment Strategy
- Outcome 1: Tested through discussion/engagement
- Outcome 2: Tested through guided practice
- Outcome 3: Tested through assignment

### Differentiation
- If student struggles with outcome 1, guide them with examples
- If student excels, challenge them with "What if...?" questions
-->

---

## 📊 Key Images

![NDVI map showing vegetation health variation across field](images/class03_slide05_img01.png)
_Figure 1: NDVI classification with color scale (red=poor vegetation, green=healthy)_

<!-- NOTES
## Key Images Teaching Notes

### Image 1: NDVI Map (2-3 minutes)

#### What to Point Out
- "Look at the color gradient"
- "Red areas = low vegetation health = might need intervention"
- "Green areas = healthy vegetation = maintaining current practices"
- "Notice the pattern - does it follow field boundaries?"

#### Why It Matters
- "This single image tells you more than 100 written descriptions"
- "Farmers use this weekly to monitor crop progress"
- "Early detection of problems saves money and time"

#### Interactive Element
- Ask: "What would cause the red zone in the upper left?"
- Possible answers: drainage issue, pest problem, compaction, etc.
- Discuss which most likely in Michigan agriculture

#### Real-World Connection
- "NDVI maps are generated from satellite imagery"
- "You can get them from [specific service] for your local fields"
- "Free tools available at [specific website]"
-->

---

## 📚 Content - Topic 1

### Soil Classification Systems

Soils can be classified by **physical properties**, **chemical composition**, or **biological activity**. Each system serves different purposes in agricultural management.

**Three Classification Approaches:**

- **Physical:** Texture, structure, porosity
- **Chemical:** pH, nutrients, contaminants
- **Biological:** Organisms, organic matter, decomposition

<!-- NOTES
## Topic 1 Teaching Notes

### Teaching Strategy (4-5 minutes)

#### Engage First (1 minute)
- "Open question: How would you categorize soil if I gave you a handful?"
- Take 2-3 answers (don't judge - good/bad answers help)
- "You just used intuition. Scientists use formal systems. Let me show you three approaches..."

#### Explain Physical Classification (1.5 minutes)
- Show soil texture triangle (if available)
- "This system categorizes by how it feels and holds water"
- "Farmers use this because it directly affects planting decisions"

#### Explain Chemical Classification (1 minute)
- "pH affects nutrient availability"
- "Nutrient levels determine what crops you can grow"
- "Contamination levels determine land use restrictions"

#### Explain Biological Classification (1 minute)
- "Healthy soil is alive with organisms"
- "These organisms break down organic matter"
- "Release nutrients plants can use"

#### Check Understanding
- Ask: "So if I have acidic sandy soil with low organisms, what should a farmer consider?"
- Listen for: Needs nutrient amendments, pH adjustment, organic matter addition

### Common Student Misconceptions

**Misconception 1:** "Soil is just dirt"
- **Reality:** Soil is a living ecosystem
- **How to address:** "Show" soil organisms under microscope or through image

**Misconception 2:** "All soil is the same"
- **Reality:** Soil varies dramatically across fields
- **How to address:** "Even in one field, upper and lower sections differ"

**Misconception 3:** "Classification is academic - farmers don't care"
- **Reality:** Farmers use classification every day (maybe unconsciously)
- **How to address:** "Soil classification = decision-making tool"

### Interactive Element
- "Bring in soil samples from Michigan fields (if possible)"
- "Let students feel the texture"
- "Ask them to classify without tools"
- "Then show formal classification"
- Creates muscle memory and relevance

### Pacing
- **Total for this slide:** 4-5 minutes
- **Explanation:** 3 min, **Questions:** 1-2 min

### Transition to Next Topic
- "Now that we understand HOW to classify soil..."
- "Let's look at WHY different soils matter for specific crops"
-->

---

## 📚 Content - Topic 2

### Soil-Crop Relationships

Different crops have different soil requirements:

| Crop     | Soil pH | Texture Preference | Drainage Need |
| -------- | ------- | ------------------ | ------------- |
| Corn     | 6.0-7.5 | Loam               | Moderate      |
| Soybeans | 6.0-7.0 | Loam-clay          | Moderate      |
| Alfalfa  | 6.5-7.5 | Well-drained       | High          |

**Key Point:** Selecting appropriate crops for existing soil = sustainable farming

<!-- NOTES
## Topic 2 Teaching Notes

### Teaching Strategy (5-6 minutes)

#### Introduce Table (1 minute)
- "This table summarizes what soil conditions each crop prefers"
- "Notice all three crops are common in Michigan"
- "But they have different requirements"

#### Walk Through Each Crop (1.5 minutes each = 4.5 total)

**Corn:**
- "Corn is flexible - grows in pH 6.0-7.5"
- "Prefers loam because it balances drainage + water retention"
- "Needs moderate drainage - not waterlogged but consistent moisture"

**Soybeans:**
- "Soybeans are similar to corn"
- "Slightly more tolerant of clay soils"
- "Same drainage requirements"

**Alfalfa:**
- "Alfalfa is pickier"
- "Needs higher pH (less acidic)"
- "Demands GOOD drainage - won't survive waterlogged conditions"
- "Why? Fungal diseases in wet soil"

#### Application (30 seconds)
- "So if you have wet, acidic soil..."
- "...corn/soybeans are better choices than alfalfa"
- "Different soil = different crop = same farm can be productive"

### Common Questions to Anticipate

**Q: Why can't I just amend soil to grow any crop?**
- A: You can, but it's expensive and sometimes impractical
- Example: "Raising pH costs $20/acre. Hard to justify for marginal land."

**Q: What if my soil doesn't match?**
- A: Three options: (1) Grow different crop, (2) Amend soil (expensive), (3) Use different field

**Q: Does this change year to year?**
- A: Soil properties are stable, but management can improve them over years

### Real-World Connection
- "Many Michigan farms have diverse soils"
- "They plant corn in loamy areas, soybeans in clay areas"
- "This matches crop to soil = better yields"

### Interactive Element
- Poll: "Who has crop experience?" (if applicable)
- "What soil did you notice worked best for corn on your farm/garden?"
- Connect their experience to the table

### Pacing
- **Total for this slide:** 5-6 minutes
- **Table explanation:** 4 min, **Interactive:** 1-2 min
-->

---

## 📚 Content - Topic 3

### Practical Soil Management

**Best Practices for Michigan Farmers:**

1. **Test soil annually** - Know your baseline before adjusting
2. **Rotate crops** - Different crops use different nutrients; rotation restores balance
3. **Add organic matter** - Cover crops, manure, compost improve soil health long-term
4. **Manage pH strategically** - Adjust based on crop choice, not tradition

<!-- NOTES
## Topic 3 Teaching Notes

### Teaching Strategy (6-7 minutes)

#### Practice 1: Soil Testing (1.5 minutes)
- "Most important first step"
- "You can't manage what you don't measure"
- Recommendation: "Test every 3-4 years minimum"
- Tools: Michigan State Extension offers affordable testing
- Cost: ~$10-20 per sample
- Turnaround: 2-3 weeks
- What you get: pH, nutrient levels (N, P, K), organic matter percentage
- Action items: "Based on test, decide if amendments needed"

#### Practice 2: Crop Rotation (1.5 minutes)
- "Corn heavily uses nitrogen"
- "After corn, soil is depleted of nitrogen"
- "Plant soybeans (legume) next year"
- "Soybeans partner with bacteria that fix nitrogen from air"
- "Soil nitrogen rebuilds naturally"
- Timeline: 2-3 year rotation is typical
- Benefit: Reduces fertilizer costs, improves soil health

#### Practice 3: Organic Matter Addition (1.5 minutes)
- "Organic matter = carbon-based material (plant/animal)"
- "Examples: Compost, cover crops, manure"
- "Why it matters: Improves water retention, aids microbes"
- "Long-term approach: Requires 5-10 years to see major changes"
- Options:
  - Cover crops: Plant after harvest, plow in spring
  - Compost: Available from many sources
  - Manure: If available from livestock farming

#### Practice 4: pH Management (1 minute)
- "Don't adjust pH randomly"
- "Base decisions on soil test + crop choice"
- "Raising pH: Add lime (~2 years to work)"
- "Lowering pH: Add sulfur (~faster than raising)"
- Cost: Significant, so do only when necessary

#### Check for Understanding
- "If your soil test shows low nitrogen and you're growing corn next year..."
- "What practice would you prioritize? Raise pH? Rotate crops?"
- Expected answer: Rotate crops (alfalfa/soybean) to rebuild nitrogen naturally

### Why This Matters
- "These practices = better yields, lower costs, healthier soil"
- "Sustainable farming isn't sacrifice - it's smart business"

### Real-World Example
- "A Michigan farmer spent $5,000 adding fertilizer to low-nitrogen field"
- "Alternative: Rotate soybeans for 2 years (~$1,500 cost)"
- "Same end result, but smarter approach"

### Common Mistakes to Avoid
- **Mistake 1:** Buying expensive amendments without soil test
  - Prevention: Test first, then decide what to add
- **Mistake 2:** Expecting quick results from organic matter
  - Prevention: Understand timeline, commit to multi-year strategy
- **Mistake 3:** Rotating same crop because it's profitable
  - Prevention: Diversify rotations despite market pressures

### Pacing
- **Total for this slide:** 6-7 minutes
- **Practice descriptions:** 4.5 min, **Real example:** 1 min, **Q&A:** 1-2 min

### Transition to Assignment
- "Now you understand soil classification, crop relationships, and management"
- "Your assignment today applies all three concepts"
-->

---

## ✍️ Assignment

### Task: Michigan Soil Analysis Project

**Objective:** Evaluate soil conditions in a Michigan field and recommend appropriate management practices based on soil classification and crop requirements.

**Your Challenge:**

You've been hired as an agricultural consultant. A Michigan farmer has a field with unclear soil characteristics. They want to know: What should they plant? What management practices should they use?

**Instructions:**

1. **Analyze** (15 min)
   - Download dataset from `docs/data/sample_soil_data.csv`
   - Calculate soil texture percentages: (sand + silt + clay = 100%)
   - Determine which soil classification the field falls into
   - Document findings in `Texture_Analysis.xlsx`

2. **Research** (10 min)
   - Using the Soil-Crop table from class, identify 2-3 suitable crops
   - For each crop, note requirements vs. your field's actual conditions
   - Record in `Crop_Recommendations.docx`

3. **Recommend** (10 min)
   - Choose ONE best crop for this field
   - Justify your choice (3-5 sentences)
   - List 2-3 management practices to implement
   - Estimate costs if applicable

4. **Present** (10 min)
   - Organize findings in 1-2 page document
   - Include: Analysis data, crop comparison table, recommendation with justification
   - Share with classmate for feedback (30 sec each, 1 min total)

**Deliverable:**

Submit to Canvas by [specific date]:

- File name: `LastName_SoilAnalysis_Assignment.pdf`
- Format: 2 pages maximum (analysis + recommendation)
- Include: Data analysis, table comparing crops, written recommendation, management practices
- References: Cite at least 2 sources (class notes, textbook, Extension website)

**Due:** [Specific date] at 11:59 PM EST

<!-- NOTES
## Assignment Teaching Notes

### Before Presenting Assignment (1 minute)

- "Let's look at your assignment for this topic"
- "This applies everything we discussed today"
- "You'll work individually, but you'll have peer feedback"

### Walking Through Assignment (4-5 minutes)

#### Step 1: Analyze (15 min)
- Show where data file is located
- Demonstrate opening the CSV file
- Walk through one calculation: "Sand is 40%, silt is 40%, clay is 20%"
- Show how to determine texture from percentages (use texture triangle image)
- Ask: "Any questions about the analysis step?"

#### Step 2: Research (10 min)
- Reference the Soil-Crop table from earlier slide
- "You're matching field conditions to crop requirements"
- Encourage students to: "Look up if you're uncertain"
- Reassure: "This isn't trick - there are often multiple right answers"

#### Step 3: Recommend (10 min)
- "You'll make a choice and defend it"
- "Good recommendations answer: Why this crop? Why not others? What now?"
- Show example: "Field has good drainage and neutral pH, so corn is excellent choice. Corn prefers loam and moderate drainage, which this field provides. Management: Annual soil testing and rotation with soybeans every 3 years."

#### Step 4: Present (10 min)
- "This is peer feedback - helps you think critically"
- "You're not grading each other, just reflecting on the recommendations"
- Pairing: "I'll assign partners; takes about 1 minute each"

### Grading Rubric

| Criterion | Points | Expectations |
|-----------|--------|--------------|
| Data Analysis | 20 | Correctly calculated soil texture, identified classification |
| Crop Comparison | 20 | Evaluated ≥2 crops against field conditions |
| Recommendation | 30 | Clear choice with 3-5 sentence justification |
| Management Plan | 15 | ≥2 practices with rationale |
| Presentation | 15 | Professional, organized, 2 pages max |
| **Total** | **100** | |

### Common Student Issues (Watch For These)

**Issue 1:** Choosing crop without analyzing field
- **Solution:** Guide them: "First, what's the soil texture? Then check if crop matches."

**Issue 2:** Not understanding why crop choice matters
- **Solution:** Connect to real farm: "If they planted alfalfa in wet soil, it would die. That's why analysis comes first."

**Issue 3:** Rushing the recommendation
- **Solution:** Ask: "You chose corn. But why NOT soybeans? Answer that, and you've written a good justification."

**Issue 4:** Missing management practices
- **Solution:** Prompt: "Now that you've chosen the crop, what should they do to maintain soil health?"

### After Assignment is Turned In

- Grade within 1 week
- Provide detailed feedback on recommendations (not just score)
- Note any recurring misconceptions for follow-up discussion
- Celebrate strong recommendations in next class: "Some excellent analysis this week..."

### Differentiation

**For struggling students:**
- Allow them to work with a partner
- Provide a partially filled analysis worksheet
- Reduce to 1 crop comparison instead of 2-3

**For advanced students:**
- Challenge: "What if climate change shifts rainfall patterns by 15%?"
- Extension: "Research actual carbon sequestration from cover crops"
- Real-world: "Find a real Michigan farm and analyze their soil"

### Time Management in Class

- Assignment presentation: 4-5 minutes
- Student questions: 2-3 minutes
- Demonstrate data access: 1-2 minutes
- Peer feedback setup: 1 minute
- **Total:** 8-11 minutes (built into 75-minute schedule)
-->

---

## 🔗 Resources & References

### Official Sources

- [Michigan State Extension Soil Testing](https://www.canr.msu.edu/services/soil-plant-pest-mgmt) - Soil test ordering and interpretation
- [NRCS Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/) - Local soil data by location
- [USDA Soil Taxonomy](https://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/survey/?cid=nrcs142p2_053587) - Official classification system

### Reading Materials

- Brady, N. C., & Weil, R. R. (2016). _The Nature and Properties of Soils_ (15th ed.). Pearson. _(Textbook reference)_
- "Soil Organic Matter: Importance and Measures for Improvement." Extension publication, MSU.

### External Tools

- [Soil Texture Triangle Calculator](http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054286) - Interactive tool to determine soil classification from sand/silt/clay percentages

### Optional Deep Dives

- [Precision Agriculture in Michigan](https://precision.agbiomech.msu.edu/) - For interested students
- [Cover Crop Case Studies](https://www.mda.state.mi.us/farmland-mgmt) - Real examples from Michigan farms

<!-- NOTES
## Resources Teaching Notes

### In Class

- "Here are the resources that best support today's content"
- Point out: "MSU Extension has free soil testing - I recommend it"
- Browse: "Soil Survey website together if you have time (5 min max)"

### For Students

- "Some of these are required, some are optional deep dives"
- "Use what's helpful for the assignment"
- "MSU Extension is free and local - reach out to them"

### Follow-Up

- If student asks: "Where do I find X?" → Point to Resources section
- Bookmark the key websites during class for easy reference
-->

---

## 📌 Class Metadata

**Duration:** 75 minutes  
**Preparation:** 10 minutes (tech check, datasets ready)

**Materials Needed:**

- Laptop with internet (to access soil survey website)
- Projector connected
- `sample_soil_data.csv` downloaded and ready

**Accessibility:**

- Large font size on slides (24pt minimum)
- High contrast: dark background, light text
- Speaker talks through all images and tables
- Closed captions available if video shown

**Tech Setup:**

- Have backup internet connection (hotspot)
- Pre-load web pages in tabs
- Test soil survey website before class

_Last Updated: January 26, 2026_

<!-- NOTES
## Class Closing Notes

### Final 5 Minutes of Class

**Summarize (1 minute):**
- "We covered three main ideas today: classification, crop relationships, management"
- "Each builds on the last: classify → choose crop → manage accordingly"

**Preview Next Class (1 minute):**
- "Next class we move from individual fields to farm-level systems"
- "Bring a photo of a field if you have one"

**Assignment Reminder (1 minute):**
- "Assignment due [date] by 11:59 PM"
- "Submit to Canvas"
- "Office hours Thursday 3-5 PM if you have questions"

**Open Floor (2 minutes):**
- "Any final questions?"
- Wait 30 seconds for responses
- "If you think of something later, email me or come to office hours"

### After Class

- Review attendance
- Note any students who seemed confused (follow-up one-on-one)
- Collect questions for FAQ document
- Update next semester's notes with what worked/didn't work
- Save any great student examples (with permission)
-->
```

---

## 🎯 Key Formatting Rules for Slide Conversion

### Slide Separators

- **`---`** = Slide boundary (MUST be on own line)
- Creates new slide in HTML, PowerPoint, and PDF
- Marp recognizes this as page break

### Speaker Notes Structure

- **Location:** After slide content, before next `---`
- **Format:** `<!-- NOTES [content] -->`
- **Visibility:** Only visible in presenter mode (Alt+P)
- **Content:** Teaching strategy, timing, common questions, tips

### Content Density (CRITICAL FOR SLIDES)

- **Visible content:** 3-6 lines maximum per slide
- **Bullet points:** 3-5 per slide maximum
- **Tables:** Only if essential, max 3×3
- **Images:** One per slide (large) or two small

### Typography

- **H1 (`#`):** Title only (first slide)
- **H2 (`##`):** Slide heading (one per slide)
- **H3 (`###`):** Subsections only (rarely used)
- **Bold:** Key concepts, action verbs
- **Code blocks:** Technical terms only
- **No emoji:** Removed from v2.0 for cleaner slides

---

## 🔄 Conversion Workflow

### From Markdown to Multiple Formats

```bash
# Install tools
npm install -g @marp-team/marp-cli
brew install pandoc

# Convert to HTML slides (with speaker notes in presenter mode)
marp class03.md -o class03.html

# Convert to PDF (handout format, no speaker notes)
marp class03.md -o class03.pdf

# Convert to PowerPoint
pandoc class03.md -o class03.pptx \
  --from markdown \
  --to pptx \
  --slide-level 2

# Watch file and auto-convert (development mode)
marp class03.md -w
```

### Recommended Flow

1. **Write markdown** with visible content + speaker notes
2. **Convert to HTML** with `marp class03.md -o class03.html`
3. **Review in browser** - Use presenter mode (Alt+P) to see speaker notes
4. **Teach with HTML** - Display in browser, use presenter view
5. **Share as PDF** - Print or email to students
6. **Archive both** - Keep markdown + generated formats

---

## ✅ Pre-Publication Checklist

### Frontmatter (Line 1-3)

- [ ] `---` starts file
- [ ] `marp: true` included
- [ ] `title:` matches class number and name
- [ ] `---` closes frontmatter

### Slide Structure

- [ ] Title slide is first
- [ ] Each slide separated by `---`
- [ ] Each slide has exactly ONE H2 heading
- [ ] No stacked content on single slide

### Speaker Notes

- [ ] Each slide has `<!-- NOTES ... -->` block
- [ ] Notes follow format: `<!-- NOTES [content] -->`
- [ ] Notes include: strategy, timing, common questions
- [ ] Notes are 150-300 words (concise but complete)

### Content Verification

- [ ] All learning outcomes are specific and measurable
- [ ] Assignment is clear and achievable in stated time
- [ ] All resources/links are current and tested
- [ ] No placeholder text (TODOs, [INSERT X])
- [ ] Spelling and grammar checked

### Formatting

- [ ] Bold used for key concepts, action verbs
- [ ] Code blocks have language specified: ` ```python `
- [ ] Tables have headers
- [ ] Images have descriptive alt text: `![Description]`
- [ ] All links are full URLs: `https://...`
- [ ] No emoji outside of notes

### Metadata

- [ ] Class number in title
- [ ] Course name listed
- [ ] Semester/year included
- [ ] Duration noted (75 minutes)
- [ ] Materials listed
- [ ] Last updated date is current

---

## 📊 Template Statistics

When following this structure, expect:

| Metric                        | Expected Range | Reasoning                                     |
| ----------------------------- | -------------- | --------------------------------------------- |
| **Total Slides**              | 9-12 slides    | 75-min class ÷ 6-8 min/slide                  |
| **Visible Content per Slide** | 80-150 words   | Forces conciseness for presentations          |
| **Speaker Notes per Slide**   | 200-400 words  | Detailed guidance without overwhelming slides |
| **Content Slides**            | 4-6 slides     | Usually 3+ topics × 1-2 slides each           |
| **Images**                    | 2-4 total      | Mix of concepts, data, real-world             |
| **Learning Outcomes**         | 3-5 outcomes   | Specific, measurable objectives               |

---

## 💡 Pro Tips

1. **Write visible content first** - Force brevity and clarity
2. **Add speaker notes second** - Add depth without cluttering slides
3. **Test conversion** - See how it looks as HTML/PowerPoint before teaching
4. **Use presenter mode** - Show speaker notes while students see clean slides
5. **Record timing** - Note how long each section actually takes
6. **Gather feedback** - Ask students what worked, what didn't
7. **Iterate yearly** - Improve based on classroom reality
8. **Version control** - Commit markdown files to git
9. **Template copies** - Copy-paste structure for consistency
10. **Backup originals** - Keep PowerPoint source files for reference

---

## 🚀 Implementation Timeline

### Phase 1: Template Creation (NOW)

- [ ] Finalize this style guide ✅
- [ ] Create template class file
- [ ] Test Marp conversion

### Phase 2: Pilot One Class (Week 1-2)

- [ ] Choose Class 03 as pilot
- [ ] Write markdown with speaker notes
- [ ] Extract images from original PowerPoint
- [ ] Convert to HTML, PDF, PowerPoint
- [ ] Teach one live class with new format
- [ ] Document what worked, what needs adjustment

### Phase 3: Update Guide (Week 3)

- [ ] Incorporate learnings from pilot
- [ ] Update style guide based on real classroom experience
- [ ] Create improved template

### Phase 4: Scale to All Classes (Week 4-12)

- [ ] Convert remaining 14 classes
- [ ] Maintain consistency across all
- [ ] Build conversion scripts to automate

### Phase 5: Automation (Ongoing)

- [ ] Script for image extraction from PowerPoint
- [ ] Script for template generation
- [ ] Automated conversion pipeline

---

## ❓ FAQ

**Q: Do students need to see speaker notes?**  
A: No. In presenter mode (Alt+P), speaker notes are hidden from students - they only see the clean slide content.

**Q: What if I want complex animations or transitions?**  
A: Marp supports limited CSS animations. For PowerPoint features, convert to .pptx and edit there. HTML/Reveal.js supports more complexity.

**Q: How do I update content for next semester?**  
A: Edit the markdown file, regenerate slides. Everything updates automatically - single source of truth.

**Q: Can students learn from just the markdown?**  
A: Yes! Print the markdown as PDF (without conversion) or let them read it directly. Includes all content + learning outcomes.

**Q: What's the conversion quality?**  
A: HTML/PDF = excellent. PowerPoint = very good (some formatting may shift). Test beforehand.

---

## 📚 Resources

### Marp Documentation

- [Marp Official Site](https://marp.app) - Getting started
- [Marp Markdown Syntax](https://marpit.marp.app/markdown) - Detailed reference
- [Marp CLI](https://github.com/marp-team/marp-cli) - Command-line tool

### Markdown Editors

- [VS Code](https://code.visualstudio.com) with [Marp extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
- [Marp Desktop](https://github.com/marp-team/marp/releases) - Standalone app
- [HackMD](https://hackmd.io) - Collaborative online editor

### Conversion Tools

- [Pandoc](https://pandoc.org) - Universal document converter
- [reveal.js](https://revealjs.com) - Interactive HTML presentations
- [Slidev](https://sli.dev) - Modern slide framework for developers

---

**Remember:** Writing once in markdown with speaker notes = unlimited presentation formats. Maximum efficiency. 🌾

**Version 2.0 - Slide-Generation Ready**  
_Last Updated: January 26, 2026_
