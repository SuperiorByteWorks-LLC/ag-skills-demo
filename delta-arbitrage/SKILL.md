---
name: delta-arbitrage
description: Query prediction market arbitrage opportunities across Kalshi and Polymarket. Detect price disparities, semantic matches, and generate D3.js visualizations. Use when analyzing prediction market data, finding arbitrage opportunities, visualizing market clusters, or exporting trading insights.
license: MIT
compatibility: Requires Python 3.10+, ZeroMQ, sentence-transformers, numpy, scikit-learn, pydantic. Optional: Node.js 18+ for D3 visualizations.
metadata:
  author: borealBytes
  version: "1.0.0"
  category: finance
  tags: arbitrage, prediction-markets, kalshi, polymarket, d3, visualization
---

# Delta Arbitrage Skill

Query and analyze arbitrage opportunities across Kalshi and Polymarket prediction markets. This skill provides programmatic access to the Delta arbitrage detection system with support for semantic matching, price disparity analysis, clustering, and D3.js visualizations.

## When to Use

- Finding arbitrage opportunities between prediction markets
- Querying events by similarity, price disparity, or platform
- Generating visualizations of market clusters and arbitrage edges
- Exporting trading data for analysis
- Monitoring price movements across platforms

## Quick Start

```bash
# Query top arbitrage opportunities
python scripts/find_arbitrage.py --min-disparity 0.05 --limit 10

# Query events by keyword
python scripts/query_events.py --search "election" --source kalshi

# Generate D3 visualization
python scripts/visualize.py --output-format d3 --output-dir ./viz

# Export data for analysis
python scripts/export_data.py --format json --include-matches
```

## Core Capabilities

### 1. Event Querying

Query events from the Delta graph store with filters:

| Filter             | Description          | Example                       |
| ------------------ | -------------------- | ----------------------------- |
| `--source`         | Platform filter      | `kalshi`, `polymarket`, `all` |
| `--search`         | Title keyword search | `"election"`, `"bitcoin"`     |
| `--min-price`      | Minimum YES price    | `0.30`                        |
| `--max-price`      | Maximum YES price    | `0.70`                        |
| `--expires-within` | Expiration window    | `7d`, `30d`                   |
| `--cluster`        | Cluster ID filter    | `5`                           |

### 2. Arbitrage Detection

Find cross-platform arbitrage opportunities using semantic matching:

| Metric      | Description                        | Threshold   |
| ----------- | ---------------------------------- | ----------- |
| Similarity  | Cosine similarity of embeddings    | ≥ 0.70      |
| Disparity   | Price difference between platforms | ≥ 0.05 (5%) |
| Time Window | Event expiration proximity         | 30 days     |

### 3. Clustering Analysis

Events are automatically clustered using k-means on sentence embeddings:

- **L0 View**: Cluster bubbles with arbitrage counts
- **L1 View**: Individual contracts within clusters
- **Cluster Labels**: Auto-generated from most frequent keywords

### 4. Visualization Generation

Generate multiple visualization formats:

| Format    | Output            | Use Case         |
| --------- | ----------------- | ---------------- |
| `d3`      | Interactive HTML  | Web dashboards   |
| `static`  | PNG/SVG images    | Reports, sharing |
| `mermaid` | Markdown diagrams | Documentation    |
| `json`    | Raw graph data    | API consumption  |

## Scripts Reference

### query_events.py

Query and filter events from the Delta store.

**Usage:**

```bash
python scripts/query_events.py [OPTIONS]

Options:
  --source {kalshi,polymarket,all}  Platform filter (default: all)
  --search TEXT                     Search in title/description
  --min-price FLOAT                 Minimum YES price (0-1)
  --max-price FLOAT                 Maximum YES price (0-1)
  --min-volume FLOAT                Minimum 24h volume
  --expires-within DAYS             Expires within N days
  --cluster INT                     Filter by cluster ID
  --status {active,closed,all}      Status filter (default: active)
  --output {json,csv,table}         Output format (default: table)
  --output-file PATH                Save to file
  --limit INT                       Max results (default: 50)
  --sort {price,volume,expiry,similarity}  Sort field
```

**Examples:**

```bash
# Find high-volume events
python scripts/query_events.py --min-volume 100000 --sort volume

# Search for crypto markets on Polymarket
python scripts/query_events.py --source polymarket --search "bitcoin"

# Export all active Kalshi markets to CSV
python scripts/query_events.py --source kalshi --status active --output csv --output-file kalshi.csv
```

### find_arbitrage.py

Detect arbitrage opportunities between platforms.

**Usage:**

```bash
python scripts/find_arbitrage.py [OPTIONS]

Options:
  --min-disparity FLOAT     Minimum price disparity (default: 0.05)
  --min-similarity FLOAT    Minimum semantic similarity (default: 0.70)
  --max-results INT         Max opportunities (default: 20)
  --source {kalshi,polymarket,both}  Cross-platform pairs (default: both)
  --expires-within DAYS     Max days to expiration (default: 30)
  --min-confidence FLOAT    Minimum confidence score
  --output {json,csv,table} Output format (default: table)
  --output-file PATH        Save to file
  --include-analysis        Include profit analysis
  --sort-by {disparity,profit,urgency}  Sort order (default: disparity)
```

**Examples:**

```bash
# Find top 10 arbitrage opportunities
python scripts/find_arbitrage.py --max-results 10 --sort-by profit

# Find opportunities with >10% price difference
python scripts/find_arbitrage.py --min-disparity 0.10 --include-analysis

# Export all opportunities to JSON
python scripts/find_arbitrage.py --output json --output-file arb.json
```

**Output Fields:**

- `event_a`, `event_b`: Matched event pair
- `price_a`, `price_b`: YES prices on each platform
- `disparity`: Absolute price difference
- `similarity`: Semantic match score
- `profit_potential`: Estimated profit after fees
- `time_urgency`: Days to expiration
- `confidence`: Overall confidence score

### visualize.py

Generate D3.js or static visualizations.

**Usage:**

```bash
python scripts/visualize.py [OPTIONS]

Options:
  --output-format {d3,static,mermaid,json}  Viz type (default: d3)
  --output-dir PATH                         Output directory (default: ./viz)
  --cluster-focus INT                       Focus on specific cluster
  --min-disparity FLOAT                     Min disparity for edges
  --width INT                               Canvas width (default: 1200)
  --height INT                              Canvas height (default: 800)
  --theme {dark,light}                      Color theme (default: dark)
  --title TEXT                              Chart title
  --no-browser                              Don't auto-open browser
```

**Examples:**

```bash
# Generate interactive D3 dashboard
python scripts/visualize.py --output-format d3 --output-dir ./dashboard

# Generate static PNG for reporting
python scripts/visualize.py --output-format static --width 1920 --height 1080

# Generate Mermaid diagram for documentation
python scripts/visualize.py --output-format mermaid > diagram.md
```

**D3 Output Features:**

- Interactive force-directed graph
- Zoom and pan support
- Hover tooltips with event details
- Click to expand clusters
- Drag nodes to rearrange
- Color-coded by platform
- Arbitrage edges highlighted

### export_data.py

Export data in various formats for external analysis.

**Usage:**

```bash
python scripts/export_data.py [OPTIONS]

Options:
  --format {json,csv,parquet,xlsx}  Output format (default: json)
  --output PATH                     Output file path
  --include-events                  Include all events
  --include-matches                 Include arbitrage matches
  --include-clusters                Include cluster assignments
  --include-stats                   Include summary statistics
  --since DATE                      Filter events since date (YYYY-MM-DD)
  --split-by-cluster                Export separate files per cluster
```

**Examples:**

```bash
# Full export for analysis
python scripts/export_data.py --format parquet --output delta.parquet --include-events --include-matches --include-clusters

# CSV for spreadsheet analysis
python scripts/export_data.py --format csv --output events.csv --include-events

# Separate files per cluster
python scripts/export_data.py --format json --split-by-cluster --output-dir ./clusters/
```

## Data Model

### Event

| Field         | Type                     | Description        |
| ------------- | ------------------------ | ------------------ |
| `id`          | string                   | Unique identifier  |
| `source`      | "kalshi" \| "polymarket" | Platform           |
| `title`       | string                   | Event title        |
| `description` | string                   | Full description   |
| `category`    | string                   | Market category    |
| `ticker`      | string                   | Trading symbol     |
| `yes_price`   | float                    | YES price (0-1)    |
| `no_price`    | float                    | NO price (0-1)     |
| `volume_24h`  | float                    | 24h trading volume |
| `expires_at`  | ISO8601                  | Expiration time    |
| `market_url`  | URL                      | Direct link        |
| `status`      | string                   | active/closed      |

### Arbitrage Match

| Field             | Type    | Description               |
| ----------------- | ------- | ------------------------- |
| `source_id`       | string  | Event A ID                |
| `target_id`       | string  | Event B ID                |
| `similarity`      | float   | Semantic similarity (0-1) |
| `price_disparity` | float   | Price difference (0-1)    |
| `matched_at`      | ISO8601 | Detection timestamp       |

### Cluster

| Field       | Type     | Description          |
| ----------- | -------- | -------------------- |
| `id`        | int      | Cluster number       |
| `label`     | string   | Auto-generated topic |
| `event_ids` | string[] | Member events        |
| `count`     | int      | Size                 |

## Configuration

Set via environment variables or `config.json`:

| Variable                  | Default              | Description            |
| ------------------------- | -------------------- | ---------------------- |
| `ZMQ_ADDRESS`             | tcp://127.0.0.1:5555 | Delta pipeline address |
| `GRAPH_PATH`              | ./data/graph.json    | Graph data location    |
| `KALSHI_API_KEY`          | -                    | For live data          |
| `KALSHI_PRIVATE_KEY_PATH` | -                    | RSA key path           |

## Integration Patterns

### With Trading Bots

```python
# Continuous arbitrage monitoring
from scripts.find_arbitrage import find_opportunities

while True:
    ops = find_opportunities(min_disparity=0.05)
    for op in ops:
        if op['confidence'] > 0.8:
            execute_trade(op)
    time.sleep(30)
```

### With Analytics Pipelines

```python
# Export for ML training
import subprocess

subprocess.run([
    "python", "scripts/export_data.py",
    "--format", "parquet",
    "--include-matches",
    "--include-stats"
])

# Load into pandas
df = pd.read_parquet("delta.parquet")
```

### With Dashboards

```python
# Generate D3 for web dashboard
subprocess.run([
    "python", "scripts/visualize.py",
    "--output-format", "d3",
    "--output-dir", "/var/www/dashboard",
    "--no-browser"
])
```

## Troubleshooting

| Issue                   | Cause                | Solution                          |
| ----------------------- | -------------------- | --------------------------------- |
| "No graph data found"   | Pipeline not running | Start Delta pipeline first        |
| "ZMQ connection failed" | Wrong address        | Check `ZMQ_ADDRESS` env var       |
| "Empty results"         | Filters too strict   | Relax min-price/min-disparity     |
| "Visualization blank"   | No clusters yet      | Wait for clustering (1000 events) |

## References

- [Data Model Reference](references/DATA_MODEL.md)
- [API Reference](references/API_REFERENCE.md)
- [Delta Repository](https://github.com/borealBytes/Delta)
