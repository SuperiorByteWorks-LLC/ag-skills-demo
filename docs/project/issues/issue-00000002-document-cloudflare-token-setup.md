# Issue-00000002: Document Cloudflare API Token Setup for Students

| Field              | Value            |
| ------------------ | ---------------- |
| **Issue**          | #2               |
| **Type**           | 📝 Documentation |
| **Priority**       | P1               |
| **Requester**      | Clayton Young    |
| **Assignee**       | Clay (AI Agent)  |
| **Date requested** | 2026-02-16       |
| **Status**         | In progress      |
| **Target release** | Spring 2026      |

---

## Summary

### Problem statement

Students need clear, step-by-step instructions for creating Cloudflare API tokens with the exact permissions required for GitHub Actions deployment. The current documentation has partial information but lacks exact step-by-step directions.

### Proposed solution

Update documentation with precise instructions including:

- Exact permissions needed (Account:Cloudflare Pages:Edit, Zone:DNS:Edit, Zone:Zone:Read)
- Step-by-step token creation workflow
- How to verify the token works
- Where to find Account ID
- How to add secrets to GitHub

---

## Acceptance Criteria

The following criteria define when this issue is complete:

- [ ] Cloudflare token documentation updated with exact permissions
- [ ] Step-by-step instructions for creating the token
- [ ] Instructions for getting Account ID
- [ ] Assignment 1 references the new documentation
- [ ] Class 2 materials reference the new documentation

---

## Changes

### Files Updated

1. `docs/preview-deployment-custom-domain.md`
   - Added exact permission requirements table
   - Added step-by-step token creation instructions
   - Added how to verify token works
   - Added how to get Account ID

2. `docs/classes/assignments/01-project-setup-data-acquisition.md`
   - References Cloudflare token setup
   - Lists all required secrets (CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID, OPENROUTER_API_KEY)

3. `docs/classes/02-Gearing-Up-Building-Your-Smart-Farm-Workspace.md`
   - Added Cloudflare deployment section
   - Added Google OAuth setup section

---

## Notes

- Token requires Account-level permissions for Cloudflare Pages
- Zone-level permissions needed for DNS management
- Must use custom token (not global API key)
- Token should be added to GitHub Secrets, not committed to repo

---

## References

- [Cloudflare API Token Documentation](https://developers.cloudflare.com/api/tokens/)
- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)

---

_Last updated: 2026-02-16_
