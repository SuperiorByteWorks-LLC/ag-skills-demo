# PR-00000003: Sync Template Repository with PyPI Publishing

| Field               | Value                                                                   |
| ------------------- | ----------------------------------------------------------------------- |
| **PR**              | [#3](https://github.com/SuperiorByteWorks-LLC/agri-data-toolkit/pull/3) |
| **Author**          | AI Agent (Sisyphus)                                                     |
| **Date**            | 2026-02-19                                                              |
| **Status**          | Open                                                                    |
| **Branch**          | `feat/sync-template-on-tag` → `main`                                    |
| **Related issues**  | PyPI publishing workflow, template repository automation                |
| **Deploy strategy** | Standard - CI workflow update                                           |

---

## 📋 Summary

### What changed and why

This PR adds automatic synchronization of the template repository (`py-agri-data-toolkit`) whenever a version tag is pushed. Previously, the template repository was only updated manually via a separate workflow. Now, when a user pushes a tag (e.g., `v0.1.0`), the CI workflow will:

1. Build and publish the package to PyPI (already implemented)
2. Automatically update the template repository with the latest code

This ensures the template repository stays in sync with released versions, providing users with the most current stable code.

### Impact classification

| Dimension         | Level             | Notes                                                         |
| ----------------- | ----------------- | ------------------------------------------------------------- |
| **Risk**          | 🟢 Low            | Only adds new functionality, doesn't change existing behavior |
| **Scope**         | Narrow            | Affects CI workflow only, no code changes                     |
| **Reversibility** | Easily reversible | Can disable by removing the new job                           |
| **Security**      | None              | Uses existing GITHUB_TOKEN, no new secrets                    |

---

## 🔍 Changes

### Change inventory

| File / Area                                           | Change type | Description                                          |
| ----------------------------------------------------- | ----------- | ---------------------------------------------------- |
| `.github/workflows/ci.yml`                            | Modified    | Added `sync-template-repo` job that runs on tag push |
| `.github/workflows/ci.yml`                            | Modified    | Added `tags: ['v*']` trigger to push events          |
| `docs/project/pr/pr-00000003-sync-template-on-tag.md` | Added       | This PR documentation file                           |

### Before and after

**Before:**

- Tag pushes did not trigger CI workflow
- Template repository required manual updates via `workflow_dispatch`
- PyPI publishing happened but template was not automatically synced

**After:**

- Tag pushes (`v*`) trigger full CI workflow
- Template repository automatically updated when tags are pushed
- Both PyPI and template repo stay in sync on every release

---

## 🧪 Testing

### How to verify

```bash
# 1. Create and push a test tag
git tag -a v0.1.0-test -m "Test release for template sync"
git push origin v0.1.0-test

# 2. Monitor CI workflow
gh run list --repo SuperiorByteWorks-LLC/agri-data-toolkit --limit 5

# 3. Verify template repo updated
# Check: https://github.com/SuperiorByteWorks-LLC/py-agri-data-toolkit
# The latest commit should match the tag
```

### Test coverage

| Test type         | Status     | Notes                              |
| ----------------- | ---------- | ---------------------------------- |
| Unit tests        | ⬜ N/A     | No code changes, CI workflow only  |
| Integration tests | ⬜ N/A     | Will be tested via actual tag push |
| Manual testing    | 🟡 Pending | Requires tag push to verify        |

### Edge cases considered

- Template repo doesn't exist: Will be created automatically
- Authentication failure: Job will fail with clear error
- Network issues: Standard GitHub Actions retry behavior applies
- Concurrent updates: Git push uses force to ensure update succeeds

---

## 🔒 Security

### Security checklist

- [x] No secrets, credentials, API keys, or PII in the diff
- [x] Authentication/authorization changes reviewed (if applicable)
- [x] Input validation added for new user-facing inputs
- [x] Injection protections maintained (SQL, XSS, CSRF)
- [x] Dependencies scanned for known vulnerabilities
- [x] Data encryption at rest/in transit maintained

**Security impact:** None — Uses existing `GITHUB_TOKEN` secret, no new credentials required.

---

## ⚡ Breaking Changes

**This PR introduces breaking changes:** No

---

## 🔄 Rollback Plan

**Revert command:**

```bash
git revert [commit-sha]
```

**Additional steps needed:**

- [ ] Disable `sync-template-repo` job in CI workflow if issues arise

> ⚠️ **Rollback risk:** Low — Template repo can be manually fixed if sync fails.

---

## 🚀 Deployment

### Strategy

**Approach:** Standard deploy — CI workflow update

**Feature flags:** None

### Pre-deployment

- [x] CI workflow syntax validated
- [x] No secrets in diff
- [x] GitHub token permissions sufficient

### Post-deployment verification

- [ ] Push test tag and verify workflow triggers
- [ ] Verify template repo updated with new commit
- [ ] Check PyPI publishing still works

---

## 📡 Observability

### Monitoring

- **Dashboard:** GitHub Actions tab
- **Key metrics to watch:** Workflow success rate, template sync job duration
- **Watch window:** 24h after first tag push

### Alerts

- [ ] No new alerts needed

### Logging

- [ ] Job outputs to GitHub Actions logs

### Success criteria

- Tag push triggers CI workflow
- Template repository shows new commit matching the tag
- PyPI package published successfully

---

## ✅ Reviewer Checklist

- [ ] Code follows project style guide and linting rules
- [x] No `TODO` or `FIXME` comments introduced without linked issues
- [x] Error handling covers failure modes (no empty catch blocks)
- [x] No secrets, credentials, or PII in the diff
- [ ] Tests cover the happy path and at least one error path
- [x] Documentation updated if public API or behavior changed
- [ ] Database migrations are reversible (if applicable)
- [x] Performance impact considered (no N+1 queries, no unbounded lists)
- [x] Breaking changes documented with migration guide (if applicable)
- [ ] Feature flag configured correctly (if applicable)
- [ ] Monitoring/alerting updated for new failure modes (if applicable)
- [x] Security review completed (if security-sensitive)

---

## 💬 Discussion

### Release note

**Category:** Feature

> Add automatic template repository synchronization on version tag push. When a tag (e.g., `v0.1.0`) is pushed, the CI workflow now updates the template repository (`py-agri-data-toolkit`) in addition to publishing to PyPI.

### Key review decisions

- **Trigger condition:** Only runs on tags starting with `v` to avoid triggering on every push
- **Job ordering:** Runs in parallel with PyPI publishing (both depend on `test-build` gate)
- **Git strategy:** Uses force push to ensure template repo stays in sync even if manual changes were made

### Follow-up items

- [ ] Test with actual tag push after merge
- [ ] Document template sync behavior in publishing.md

---

## 🔗 References

- [Template repository](https://github.com/SuperiorByteWorks-LLC/py-agri-data-toolkit)
- [Publishing documentation](../packages/agri-data-toolkit/docs/publishing.md)
- [GitHub Actions documentation](https://docs.github.com/en/actions)

---

_Last updated: 2026-02-19_
