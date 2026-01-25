# ADR-002: Monorepo Structure and Organization

**Status**: Accepted  
**Date**: 2026-01-12  
**Decision Maker**: Agri Data Toolkit Maintainers

---

## Problem Statement

The repository needs to support:

- A deployable startup blueprint app
- A public website
- An installable Python package (`agri-data-toolkit`)

Without a clear monorepo structure, we risk unclear ownership, inconsistent CI behavior, and duplicated setup across projects.

---

## Constraints

1. **Mixed tech stack**
   - JavaScript workspaces (pnpm + Turbo)
   - Python package management (Poetry)

2. **Independent delivery**
   - Website and app deploy independently
   - Python package releases independently

3. **CI compatibility**
   - CI should run only relevant checks per workspace
   - Python tests must run inside `packages/agri-data-toolkit`

---

## Decision

Use a monorepo layout that separates deployable apps from the Python package:

```
agri-data-toolkit/
├── apps/                          # Deployable applications
│   └── startup-blueprint/         # Startup blueprint app
├── packages/                      # Packages and libraries
│   └── agri-data-toolkit/          # Python package (Poetry)
├── website/                       # Public site
├── docs/                          # Startup blueprint docs
├── scripts/                       # Root-level automation
├── docs/agentic/                  # Agentic workflow docs
├── .github/                       # GitHub configuration
├── turbo.json                     # Turborepo orchestration
├── pnpm-workspace.yaml            # Workspace definition
├── package.json                   # Root dependencies & scripts
├── .gitignore                     # Git ignore rules
└── README.md                      # Project overview
```

Workflow conventions:

- JavaScript workspaces run via `pnpm` from the repo root.
- Python workflows run inside `packages/agri-data-toolkit` using Poetry.

---

## Consequences

### Positive

- Clear ownership boundaries between app, website, and package
- CI can run targeted checks per workspace
- Python package remains installable and isolated

### Trade-offs

- Requires explicit docs for workspace context switching
- Mixed tooling (pnpm + Poetry) increases setup complexity
