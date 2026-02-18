# Agent Autonomy & Boundaries

> What AI agents can/cannot do when working on Agri Data Toolkit

**This is your operating manual. Read it before every task.**

---

## ✅ Agent CAN Autonomously Do

### Reading & Exploration

- ✅ Read any file in the repo
- ✅ Understand codebase structure
- ✅ Search for existing implementations
- ✅ Reference docs, ADRs, configuration

### Planning & Design

- ✅ Write design docs explaining approach
- ✅ Ask clarifying questions and wait for answers
- ✅ Propose alternative solutions
- ✅ Document reasoning in PR descriptions

### Implementation

- ✅ Write code following standards
- ✅ Create tests (unit, integration)
- ✅ Refactor existing code
- ✅ Update documentation
- ✅ Fix type errors and warnings

### Git & Version Control

- ✅ Create branches with proper naming (`feat/`, `fix/`, `docs/`, `chore/`)
- ✅ Make commits with Conventional Commits format
- ✅ Write clear commit messages
- ✅ Push to remote

### Pull Requests

- ✅ Create PRs immediately after starting work
- ✅ Write comprehensive PR descriptions
- ✅ Document what changed, why, and how tested
- ✅ Include links to related issues, ADRs, docs
- ✅ Keep PR description updated (living document)
- ✅ Mark PR as **Draft** initially for design review
- ✅ Update PR status as work progresses
- ✅ Move to **Ready for Review** ONLY after explicit human confirmation

### Responding to Feedback

- ✅ Read PR review comments
- ✅ Understand reviewer feedback
- ✅ Make requested changes
- ✅ Commit fixes with clear messages
- ✅ Respond to comments
- ✅ Iterate until human approves

### Quality Gates

- ✅ Run tests locally before pushing
- ✅ Fix lint/format errors
- ✅ Respond to GitHub Actions failures
- ✅ Verify build passes
- ✅ Follow project standards

---

## ⚠️ Agent MUST Escalate (Ask First)

For these decisions, **stop and ask for human confirmation**:

### Breaking Changes

- ⚠️ Changing public APIs or function signatures
- ⚠️ Modifying database schema in breaking ways
- ⚠️ Removing features or deprecating endpoints
- ❓ **Ask**: "Is this breaking change intentional? Should we add a deprecation period?"

### Security & Authentication

- ⚠️ Adding/modifying authentication logic
- ⚠️ Changing authorization/permission rules
- ⚠️ Handling secrets, keys, sensitive data
- ❓ **Ask**: "Should we review this security change? Any compliance concerns?"

### Major Architectural Decisions

- ⚠️ Choosing new library/framework for shared code
- ⚠️ Changing how multiple workspaces interact
- ⚠️ Proposing new patterns or conventions
- ❓ **Ask**: "Should we create an ADR for this? Any precedent to follow?"

### Multi-Workspace Changes

- ⚠️ Changes affecting 3+ workspaces
- ⚠️ Moving shared code between packages
- ❓ **Ask**: "Is this refactoring aligned with our monorepo strategy?"

### Versioning & Releases

- ⚠️ Bumping major/minor versions
- ⚠️ Publishing new releases or tags
- ❓ **Ask**: "What version bump is appropriate? Release notes needed?"

### Deployment & Infrastructure

- ⚠️ Modifying deployment configurations
- ⚠️ Changing CI/CD workflows
- ⚠️ Adding new environment variables or secrets
- ❓ **Ask**: "Should we test in staging first? Any rollback concerns?"

### Large Refactorings

- ⚠️ Rewriting significant portions of code
- ⚠️ Changing file/folder structure significantly
- ❓ **Ask**: "Should we break this into smaller increments?"

---

## 🚫 Agent NEVER Does

**Absolutely off-limits**:

### Merging & Deployment

- 🚫 **Never merge PRs** (only humans merge)
- 🚫 **Never merge to `main` branch** (protected)
- 🚫 **Never force-push** or rebase others' work
- 🚫 **Never delete branches/tags** without explicit request
- 🚫 **Never trigger production deployments**

### Secrets & Configuration

- 🚫 **Never read/write GitHub Secrets** (humans only)
- 🚫 **Never commit `.env.local` or secret files**
- 🚫 **Never hardcode credentials, API keys, tokens**
- 🚫 **Never set environment variables in CI/CD**

### Destructive Operations

- 🚫 **Never drop databases** or delete data
- 🚫 **Never rollback changes without approval**
- 🚫 **Never modify `.gitignore` to allow secrets**

### External Systems

- 🚫 **Never access external APIs** with real credentials
- 🚫 **Never modify cloud infrastructure** (AWS, Cloudflare, etc.)
- 🚫 **Never send emails, Slack, notifications** to users/team

### PR Status Management

- 🚫 **Never unilaterally mark PR "Ready for Review"** (see workflow step 10)
- 🚫 **Never force-change PR status** without human confirmation

---

## 🎯 Decision Boundaries

### Agent Decides

- ✅ Implementation details (libraries, patterns, code structure)
- ✅ Code organization (file placement, function splitting)
- ✅ Testing approach (which tests, what coverage)
- ✅ Commit messages (clear, descriptive)
- ✅ PR descriptions (document work clearly)

### Human Decides

- 🚫 Merging to main (approval required)
- 🚫 Release versioning (semantic version)
- 🚫 Production deployment (approval required)
- 🚫 Breaking changes (policy decision)
- 🚫 Architecture (new patterns, major refactors)
- 🚫 Security policies (auth, secrets, permissions)
- 🚫 Design approach (human confirms approach before implementation)
- 🚫 Code quality (human confirms implementation before "Ready")
- 🚫 PR status changes (human approves moving to "Ready for Review")

---

## 📝 Example Escalation Questions

When to **ask instead of deciding**:

```
⚠️ "I'm about to change the API response format. This breaks existing clients.
   Is this intentional, or should we add backwards compatibility?"

⚠️ "I found three ways to implement the cache layer:
   1. Redis (external dependency, fast)
   2. In-memory with TTL (simple, single process)
   3. Database-backed (slower, shared across servers)
   Which aligns with our architecture?"

⚠️ "I've drafted a design approach for this feature [link to doc].
   Does this direction look correct before I implement?"

⚠️ "Should I add a new environment variable for this feature?
   If yes, what should it be called and what are valid values?"

⚠️ "This refactor affects 4 workspaces. Should we:
   A) Handle in one PR, or
   B) Break into separate PRs per workspace?"
```

---

## 🔄 Quick Reference

| Scenario                | Your Action                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| **New feature request** | Ask clarifying questions → Design → Wait for approval → Code → PR        |
| **Bug fix**             | Reproduce → Root cause analysis → Fix → Tests → PR                       |
| **Refactor**            | Understand impact → Propose alternatives → Wait for approval → Implement |
| **Breaking change**     | **STOP** → Ask human → Wait for decision → Proceed                       |
| **Security concern**    | **STOP** → Ask human → Wait for security review → Proceed                |
| **PR review feedback**  | Read comments → Understand requests → Fix → Commit → Respond             |
| **Test failure**        | Investigate → Fix → Re-run → Verify → Commit                             |
| **Merge conflicts**     | See `agent_error_recovery.md`                                            |

---

## 📚 For More Information

- **Workflow details**: See `workflow_guide.md`
- **Error recovery**: See `agent_error_recovery.md`
- **Company-specific rules**: See `custom-instructions.md`
- **Code standards**: See `contribute_standards.md`

---

**Remember**: When in doubt, **ask**. Humans appreciate clear questions more than silent mistakes.
