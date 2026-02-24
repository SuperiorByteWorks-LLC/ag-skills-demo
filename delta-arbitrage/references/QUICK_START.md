# Delta Arbitrage Quick Start Guide

## Installation

1. **Clone Delta repository** (if not already done):

```bash
git clone https://github.com/borealBytes/Delta.git
cd Delta
```

2. **Set up Delta pipeline**:

```bash
# C++ ingestion
make ingestion-configure
make ingestion-build

# Python pipeline
make pipeline-install

# Frontend (optional)
cd frontend && npm install && cd ..
```

3. **Configure API keys**:

```bash
cp config.example.json config.json
# Edit config.json with your Kalshi credentials
```

## Running the Pipeline

Start three terminals:

**Terminal 1 - Ingestion:**

```bash
make ingestion
```

**Terminal 2 - Pipeline:**

```bash
make pipeline
```

**Terminal 3 - Skill usage:**

```bash
# Wait for graph.json to be generated (~60s or 1000 events)
ls pipeline/data/graph.json
```

## Using the Skill

### Find Arbitrage Opportunities

```bash
# Top 10 opportunities
python scripts/find_arbitrage.py --max-results 10 --sort-by profit

# High-confidence opportunities with analysis
python scripts/find_arbitrage.py --min-confidence 0.8 --include-analysis

# Export to CSV for spreadsheet
python scripts/find_arbitrage.py --output csv --output-file opportunities.csv
```

### Query Events

```bash
# Search for crypto markets
python scripts/query_events.py --search "bitcoin" --source polymarket

# High-volume events expiring soon
python scripts/query_events.py --min-volume 100000 --expires-within 7 --sort volume

# Events in specific cluster
python scripts/query_events.py --cluster 5 --limit 20
```

### Generate Visualizations

```bash
# Interactive D3 dashboard
python scripts/visualize.py --output-format d3 --output-dir ./viz

# Static image for reports
python scripts/visualize.py --output-format static --width 1920 --height 1080

# Mermaid diagram for docs
python scripts/visualize.py --output-format mermaid > diagram.md
```

### Export Data

```bash
# Full export for analysis
python scripts/export_data.py --format parquet --include-all

# CSV for spreadsheet
python scripts/export_data.py --format csv --include-events --include-matches

# Separate files per cluster
python scripts/export_data.py --format json --split-by-cluster --output-dir ./clusters/
```

## Common Workflows

### Daily Arbitrage Scan

```bash
#!/bin/bash
# daily_scan.sh

echo "=== Daily Arbitrage Scan ==="
echo "Date: $(date)"

# Find top opportunities
python scripts/find_arbitrage.py \
    --min-disparity 0.05 \
    --min-confidence 0.75 \
    --sort-by profit \
    --output json \
    --output-file "arbitrage_$(date +%Y%m%d).json"

# Generate visualization
python scripts/visualize.py \
    --output-format d3 \
    --output-file "report_$(date +%Y%m%d).html"

echo "Scan complete. Results saved."
```

### Cluster Analysis

```bash
# Export cluster data
python scripts/export_data.py \
    --format csv \
    --split-by-cluster \
    --output-dir ./cluster_analysis/

# Query specific cluster
python scripts/query_events.py --cluster 3 --output csv > cluster_3.csv
```

### Integration with Trading

```python
# monitor.py
import time
import json
from scripts.find_arbitrage import find_arbitrage_opportunities, load_graph_data

def monitor():
    while True:
        data = load_graph_data()
        ops = find_arbitrage_opportunities(
            data,
            min_disparity=0.05,
            min_confidence=0.80,
            sort_by="profit"
        )

        for opp in ops[:5]:  # Top 5
            if opp.profit_potential > 0.03:
                alert(f"High profit: {opp.event_a['title']} vs {opp.event_b['title']}")

        time.sleep(60)  # Check every minute

def alert(message):
    print(f"[ALERT] {message}")
    # Add webhook, email, etc.

if __name__ == "__main__":
    monitor()
```

## Environment Variables

| Variable      | Description            | Default                    |
| ------------- | ---------------------- | -------------------------- |
| `GRAPH_PATH`  | Path to graph.json     | `pipeline/data/graph.json` |
| `ZMQ_ADDRESS` | Delta pipeline address | `tcp://127.0.0.1:5555`     |

## Troubleshooting

| Problem                  | Solution                                        |
| ------------------------ | ----------------------------------------------- |
| "Graph file not found"   | Start Delta pipeline first, wait for graph.json |
| "No opportunities found" | Relax filters (--min-disparity 0.03)            |
| "Empty visualization"    | Wait for clustering (1000 events)               |
| Slow queries             | Use --limit to cap results                      |

## Tips

1. **Start with broad filters**, then narrow down
2. **Check confidence scores** - aim for >0.75
3. **Consider time urgency** - expiring events may resolve soon
4. **Export regularly** - keep historical data
5. **Automate** - schedule daily scans with cron

## Getting Help

- **Data Model**: See [DATA_MODEL.md](DATA_MODEL.md)
- **API Reference**: See [API_REFERENCE.md](API_REFERENCE.md)
- **Delta Repo**: https://github.com/borealBytes/Delta
