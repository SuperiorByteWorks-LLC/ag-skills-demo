# PR Record: Assignment Template and First Assignment

**Date:** 2026-02-15  
**Author:** Clay (AI Agent)  
**Status:** Ready for Review

---

## Summary

Create an assignment template and first assignment for the Agricultural Data Systems course. The first assignment covers project setup, Git workflow, AI assistant configuration, secrets setup (Cloudflare + OpenRouter), website deployment, and field data acquisition.

---

## Changes

### New Files

- `docs/classes/assignment_template.md` - Reusable template for future assignments
- `docs/classes/assignments/01-project-setup-data-acquisition.md` - First assignment (5 points)
- `docs/project/issues/issue-00000002-document-cloudflare-token-setup.md` - Issue tracking

### Updated Files

- `docs/preview-deployment-custom-domain.md` - Added exact Cloudflare API token permissions and step-by-step instructions
- `docs/classes/02-Gearing-Up-Building-Your-Smart-Farm-Workspace.md` - Added Cloudflare deployment and Google OAuth sections

### Content

1. **Assignment Template**
   - Reusable structure with objectives, instructions, deliverables, grading criteria
   - Follows markdown style guide

2. **Assignment 1: Project Setup and Field Data Acquisition**
   - Environment setup (Codespaces/WSL/Local)
   - Template repository cloning
   - AI assistant installation (OpenCode/Roo Code)
   - **Secrets configuration** (Cloudflare + OpenRouter) ← NEW
   - Local CI execution
   - Feature branch creation
   - **Website deployment (Cloudflare Pages)** ← NEW
   - Data download (~200 fields)
   - Field boundary visualization
   - Data vs. code best practices

3. **Cloudflare Token Documentation** ← NEW
   - Exact permissions required:
     - Account:Cloudflare Pages:Edit
     - Zone:DNS:Edit
     - Zone:Zone:Read
   - Step-by-step token creation
   - How to get Account ID
   - How to verify token works

---

## Testing

- [x] Template follows markdown style guide
- [x] Assignment has clear objectives
- [x] Instructions are step-by-step
- [x] Deliverables are clearly defined
- [x] Grading criteria are explicit
- [x] Cloudflare token documentation is accurate

---

## Notes

- Assignment aligns with Class 2 content (VS Code, AI assistants, Git workflow, deployment)
- Follows AI-assisted workflow (describe in English, AI creates Mermaid)
- Emphasizes data ≠ code (data not committed to Git)
- Includes required screenshots for verification (2 screenshots: dev env + deployed website)
- All 3 secrets required: CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID, OPENROUTER_API_KEY

---

## PR Requirements

- [ ] Human reviews and approves
- [ ] Tests pass (N/A - documentation only)
- [ ] Ready to merge

---

**Reviewers:** @borealBytes

---

_This PR follows the everything-as-code principle. See ADR-003 for rationale._
