# Delta Arbitrage Skill

An AgentSkills.io compliant skill for querying and analyzing arbitrage opportunities across Kalshi and Polymarket prediction markets.

## Overview

This skill provides programmatic access to the [Delta](https://github.com/borealBytes/Delta) arbitrage detection system, enabling AI agents to:

- Query prediction market events with powerful filters
- Detect cross-platform arbitrage opportunities
- Generate D3.js and static visualizations
- Export data for external analysis
- Calculate profit potential and confidence scores

## Quick Start

```bash
# Find top arbitrage opportunities
python scripts/find_arbitrage.py --max-results 10 --sort-by profit

# Query events by keyword
python scripts/query_events.py --search "election" --source kalshi

# Generate D3 visualization
python scripts/visualize.py --output-format d3 --output-dir ./viz

# Export data for analysis
python scripts/export_data.py --format json --include-all
```

## Directory Structure

```
delta-arbitrage/
├── SKILL.md                 # Main skill definition (required)
├── README.md               # This file
├── scripts/                # Executable scripts
│   ├── query_events.py     # Event querying and filtering
│   ├── find_arbitrage.py   # Arbitrage detection
│   ├── visualize.py        # D3/static visualization generation
│   └── export_data.py      # Data export utilities
└── references/             # Reference documentation
    ├── DATA_MODEL.md       # Data schema reference
    ├── API_REFERENCE.md    # API documentation
    └── QUICK_START.md      # Quick start guide
```

## Requirements

- Python 3.10+
- Delta pipeline running (generates graph.json)
- Optional: matplotlib, networkx (for static images)
- Optional: pandas, pyarrow (for Parquet export)
- Optional: openpyxl (for Excel export)

## Installation

1. Clone and set up [Delta](https://github.com/borealBytes/Delta)
2. Start the Delta pipeline (ingestion + matching)
3. Place this skill directory anywhere in your skills path
4. Ensure `GRAPH_PATH` points to your `graph.json` (or use default location)

## Core Capabilities

### 1. Event Querying (`query_events.py`)

Filter events by source, price, volume, expiration, search terms, and cluster membership.

**Example:**

```bash
python scripts/query_events.py \
    --source kalshi \
    --search "bitcoin" \
    --min-volume 50000 \
    --expires-within 7 \
    --sort volume
```

### 2. Arbitrage Detection (`find_arbitrage.py`)

Find semantically similar events with price disparities across platforms.

**Example:**

```bash
python scripts/find_arbitrage.py \
    --min-disparity 0.10 \
    --min-confidence 0.80 \
    --sort-by profit \
    --include-analysis
```

**Output includes:**

- Event pair details
- Price disparity percentage
- Semantic similarity score
- Estimated profit potential
- Confidence score
- Trading strategy suggestion

### 3. Visualization (`visualize.py`)

Generate multiple visualization formats:

| Format  | Output           | Use Case                    |
| ------- | ---------------- | --------------------------- |
| D3      | Interactive HTML | Web dashboards, exploration |
| Static  | PNG/SVG          | Reports, presentations      |
| Mermaid | Markdown         | Documentation               |
| JSON    | Raw data         | API consumption             |

**Example:**

```bash
python scripts/visualize.py \
    --output-format d3 \
    --width 1920 \
    --height 1080 \
    --theme dark \
    --title "Arbitrage Opportunities"
```

**D3 Features:**

- Interactive force-directed graph
- Zoom and pan
- Hover tooltips
- Cluster expand/collapse
- Drag-to-rearrange
- Color-coded by platform

### 4. Data Export (`export_data.py`)

Export in multiple formats:

| Format  | Best For                  |
| ------- | ------------------------- |
| JSON    | API integration, web apps |
| CSV     | Spreadsheet analysis      |
| Parquet | Data science, ML          |
| Excel   | Business reporting        |

**Example:**

```bash
python scripts/export_data.py \
    --format parquet \
    --include-all \
    --split-by-cluster
```

## Integration with Agent Frameworks

This skill follows the [AgentSkills.io](https://agentskills.io) specification, making it compatible with:

- Claude Code
- OpenCode
- Roo Code
- Cursor
- GitHub Copilot
- And any AgentSkills-compliant tool

### Usage Pattern

When the skill is activated, agents receive:

1. **Metadata**: Name, description, triggers
2. **Instructions**: Full SKILL.md with capabilities and examples
3. **Scripts**: On-demand access to executable scripts

### Example Agent Interaction

**User:** "Find me arbitrage opportunities in Bitcoin markets"

**Agent (with skill activated):**

```bash
python scripts/find_arbitrage.py \
    --search "bitcoin" \
    --min-disparity 0.05 \
    --sort-by profit
```

**User:** "Show me a visualization"

**Agent:**

```bash
python scripts/visualize.py \
    --output-format d3 \
    --cluster-focus 5 \
    --output-file btc_arbitrage.html
```

## Data Model

Events follow a unified schema regardless of source platform:

| Field        | Type    | Description                  |
| ------------ | ------- | ---------------------------- |
| `id`         | string  | Unique identifier            |
| `source`     | string  | `"kalshi"` or `"polymarket"` |
| `title`      | string  | Market question              |
| `yes_price`  | float   | YES price (0-1)              |
| `no_price`   | float   | NO price (0-1)               |
| `volume_24h` | float   | 24h trading volume           |
| `expires_at` | ISO8601 | Expiration time              |
| `market_url` | URL     | Direct link                  |

See [DATA_MODEL.md](references/DATA_MODEL.md) for complete schema.

## Configuration

| Environment Variable | Description            | Default                    |
| -------------------- | ---------------------- | -------------------------- |
| `GRAPH_PATH`         | Path to graph.json     | `pipeline/data/graph.json` |
| `ZMQ_ADDRESS`        | Delta pipeline address | `tcp://127.0.0.1:5555`     |

## Performance

- Handles 50,000+ events efficiently
- Sub-second query times
- Incremental graph updates
- Minimal memory footprint (~25 MB for 50k events)

## Limitations

- Requires Delta pipeline to be running
- Kalshi API requires authentication
- Semantic matching uses CPU (no GPU required)
- Visualization limited by browser memory for large graphs

## Troubleshooting

See [QUICK_START.md](references/QUICK_START.md) for common issues and solutions.

## License

MIT - See Delta repository for full license terms.

## References

- **Delta Repository**: https://github.com/borealBytes/Delta
- **AgentSkills Specification**: https://agentskills.io/specification
- **Data Model**: [references/DATA_MODEL.md](references/DATA_MODEL.md)
- **API Reference**: [references/API_REFERENCE.md](references/API_REFERENCE.md)
- **Quick Start**: [references/QUICK_START.md](references/QUICK_START.md)
