# Work Plan: Merge ssurgo-poster-cards Skill

## TL;DR

Merge the `ssurgo-poster-cards` skill into `ag-skills-demo` as a new discoverable skill package plus standalone script. This skill generates poster-ready soil profile cards from SSURGO SQLite databases.

**Deliverables:**

- `.opencode/skills/ssurgo-poster-cards/` - skill package with SKILL.md, README.md, requirements.txt
- `.opencode/skills/ssurgo-poster-cards/examples/` - example invocations
- `.opencode/skills/ssurgo-poster-cards/templates/` - reusable templates
- `scripts/build_ssurgo_poster_cards.py` - standalone executable script

---

## Context

This merge adds a reusable repo skill for generating poster-ready soil profile cards from SSURGO data stored in a local SQLite database. The workflow is packaged as both a discoverable skill for agent use and a normal Python script for direct CLI execution.

**Source:** Handoff summary from external contribution with complete specifications.

---

## Work Objectives

### Core Objective

Create a complete skill package and standalone script for SSURGO poster card generation.

### Concrete Deliverables

1. Skill definition (SKILL.md) with YAML frontmatter
2. User-facing README with setup and usage
3. Python dependencies list (requirements.txt)
4. Example invocation documentation
5. Reusable handoff summary template
6. Standalone Python script at `scripts/build_ssurgo_poster_cards.py`

### Definition of Done

- [ ] All files created in correct locations
- [ ] Script runs from repo root with `python scripts/build_ssurgo_poster_cards.py --help`
- [ ] Skill documentation is complete and accurate
- [ ] Output naming convention matches documentation

---

## Execution Strategy

### File Structure

```
ag-skills-demo/
  .opencode/skills/
    ssurgo-poster-cards/
      SKILL.md                    # Agent-facing skill definition
      README.md                   # Human-facing usage guide
      requirements.txt            # Python dependencies
      examples/
        example_invocation.md     # Usage examples
      templates/
        handoff_summary.md        # Reusable template
  scripts/
    build_ssurgo_poster_cards.py  # Standalone executable
```

### Parallel Execution

All file creation tasks are independent and can run in parallel:

**Wave 1 - Skill Package Files (parallel):**

- Create SKILL.md
- Create README.md
- Create requirements.txt
- Create examples/example_invocation.md
- Create templates/handoff_summary.md

**Wave 2 - Script (sequential after Wave 1):**

- Create scripts/build_ssurgo_poster_cards.py

**Wave 3 - Verification (parallel):**

- Verify script runs
- Verify file structure
- Verify documentation completeness

---

## TODOs

- [ ] 1. Create SKILL.md with YAML frontmatter

  **What to do:**
  Create `.opencode/skills/ssurgo-poster-cards/SKILL.md` with the following exact content:

  ```yaml
  ---
  name: ssurgo-poster-cards
  description: Generate poster-ready SSURGO soil profile cards from a local SQLite database, including single-profile, comparison, texture-color, and clustered layouts.
  version: 1.0.0
  author: Boreal Bytes
  tags: [agriculture, soil, ssurgo, visualization, poster]
  ---
  ```

  Followed by the full skill definition from the handoff summary (Use this skill when, Inputs, Expected tables, Required fields, Optional fields, Outputs, Behavior, Notes, Script entrypoint).

  **Must NOT do:**
  - Change the YAML frontmatter structure
  - Omit any required fields from the skill definition

  **Acceptance Criteria:**
  - [ ] File exists at `.opencode/skills/ssurgo-poster-cards/SKILL.md`
  - [ ] YAML frontmatter is valid
  - [ ] All skill sections from handoff are included

  **Commit:** NO (group with final verification)

- [ ] 2. Create README.md

  **What to do:**
  Create `.opencode/skills/ssurgo-poster-cards/README.md` with the exact content from the handoff summary.

  **Content:**
  - Title: # ssurgo-poster-cards
  - Brief description
  - Generates list (4 card types)
  - Run section with bash command example
  - Typical use description
  - Dependencies section
  - Data expectations section

  **Acceptance Criteria:**
  - [ ] File exists at `.opencode/skills/ssurgo-poster-cards/README.md`
  - [ ] Contains all sections from specification
  - [ ] Command example is copy-paste ready

  **Commit:** NO (group with final verification)

- [ ] 3. Create requirements.txt

  **What to do:**
  Create `.opencode/skills/ssurgo-poster-cards/requirements.txt` with:

  ```
  pandas>=2.0.0
  matplotlib>=3.7.0
  numpy>=1.24.0
  scikit-learn>=1.3.0
  ```

  **Acceptance Criteria:**
  - [ ] File exists at `.opencode/skills/ssurgo-poster-cards/requirements.txt`
  - [ ] All 4 dependencies listed with version constraints

  **Commit:** NO (group with final verification)

- [ ] 4. Create examples/example_invocation.md

  **What to do:**
  Create `.opencode/skills/ssurgo-poster-cards/examples/example_invocation.md` showing:
  - Agent-facing usage example
  - CLI-facing usage example
  - Expected outputs list

  **Acceptance Criteria:**
  - [ ] File exists at correct path
  - [ ] Contains both agent and CLI examples
  - [ ] Lists all 4 output card types

  **Commit:** NO (group with final verification)

- [ ] 5. Create templates/handoff_summary.md

  **What to do:**
  Create `.opencode/skills/ssurgo-poster-cards/templates/handoff_summary.md` as a reusable template for future soil-data skills.

  Template should include:
  - Merge target placeholder
  - Layout structure
  - Handoff summary sections (PR title, Purpose, What is being added)
  - Skill definition template
  - Script merge notes
  - README text template
  - Merge criteria checklist

  **Acceptance Criteria:**
  - [ ] File exists at correct path
  - [ ] Contains all template sections
  - [ ] Uses placeholder syntax for customization

  **Commit:** NO (group with final verification)

- [ ] 6. Create scripts/build_ssurgo_poster_cards.py

  **What to do:**
  Create the standalone Python script at `scripts/build_ssurgo_poster_cards.py`.

  **Requirements:**
  - Shebang: `#!/usr/bin/env python3`
  - Module docstring describing inputs and exported card types
  - argparse CLI with:
    - `--db` - Path to SSURGO SQLite database (required)
    - `--out` - Output directory (default: outputs/cards)
    - `--dominant-only` - Flag to keep only dominant components
    - `--max-profiles` - Limit number of profiles (default: 6)
    - `--mukeys` - Optional list of MUKEYs to filter

  **Core functionality:**
  1. Connect to SQLite database
  2. Query and join mapunit/component/chorizon tables
  3. Filter to valid horizon depths
  4. Optionally filter to dominant components
  5. Generate 4 card types:
     - Single profile visualization
     - Multi-profile comparison
     - Texture RGB coloring
     - Clustered profiles
  6. Export to SVG, PDF, and PNG formats

  **Must NOT do:**
  - Embed the script inside the skill folder
  - Change the filename from build_ssurgo_poster_cards.py
  - Remove the `if __name__ == "__main__": main()` block

  **Acceptance Criteria:**
  - [ ] File exists at `scripts/build_ssurgo_poster_cards.py`
  - [ ] Script has proper shebang and docstring
  - [ ] All argparse arguments implemented
  - [ ] Creates outputs/cards/ directory if needed
  - [ ] Generates all 4 card types

  **Commit:** NO (group with final verification)

- [ ] 7. Verify script runs from repo root

  **What to do:**
  Test the script with: `python scripts/build_ssurgo_poster_cards.py --help`

  **Acceptance Criteria:**
  - [ ] Script executes without import errors
  - [ ] Help text displays all arguments
  - [ ] Script returns exit code 0

  **Evidence:** Screenshot or terminal output showing successful execution

  **Commit:** YES - "feat(ssurgo-poster-cards): add SSURGO poster card skill and script"

- [ ] 8. Verify complete file structure

  **What to do:**
  List all created files and verify structure matches specification.

  **Acceptance Criteria:**
  - [ ] All 7 files exist in correct locations
  - [ ] SKILL.md has valid YAML frontmatter
  - [ ] README.md matches handoff specification
  - [ ] requirements.txt has all dependencies

  **Evidence:** Directory tree output

---

## Success Criteria

### Verification Commands

```bash
# Verify script runs
python scripts/build_ssurgo_poster_cards.py --help

# Verify file structure
find .opencode/skills/ssurgo-poster-cards -type f | sort
ls -la scripts/build_ssurgo_poster_cards.py

# Verify SKILL.md frontmatter
head -10 .opencode/skills/ssurgo-poster-cards/SKILL.md
```

### Final Checklist

- [ ] SKILL.md exists with valid YAML frontmatter
- [ ] README.md contains all required sections
- [ ] requirements.txt lists all dependencies
- [ ] examples/ contains example_invocation.md
- [ ] templates/ contains handoff_summary.md
- [ ] scripts/build_ssurgo_poster_cards.py exists and runs
- [ ] Script outputs to outputs/cards/ by default
- [ ] All output naming conventions match documentation
