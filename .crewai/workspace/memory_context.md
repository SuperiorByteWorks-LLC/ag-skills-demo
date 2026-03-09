## Learned Patterns About This Codebase
- Do not flag placeholder secrets in .env.example files when values are clearly fake examples and no real credentials are present. (confidence: 1.0)

## Active Review Suppressions
Do NOT flag these patterns, the team has marked them acceptable:
- hardcoded URL in example file (files: agentic/mermaid_diagrams/*.md) - These are intentional documentation examples, not production code
- placeholder api keys and tokens (files: *.env.example) - Placeholder credentials in .env.example templates are acceptable when they are clearly fake and no real secrets are committed.
