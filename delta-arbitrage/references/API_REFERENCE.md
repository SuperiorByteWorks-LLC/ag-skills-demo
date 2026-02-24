# Delta Arbitrage API Reference

## Python API

### Importing Modules

```python
# Direct script imports
from scripts.query_events import filter_events, sort_events
from scripts.find_arbitrage import find_arbitrage_opportunities, ArbitrageOpportunity
from scripts.visualize import generate_d3_html, generate_static_image
from scripts.export_data import calculate_statistics
```

## Script APIs

### query_events.py

#### `load_graph_data(graph_path: str | None = None) -> dict`

Load graph data from Delta pipeline output.

**Parameters:**

- `graph_path`: Path to graph.json. Uses `GRAPH_PATH` env var or standard location if not provided.

**Returns:** Dictionary with `nodes`, `edges`, `clusters`.

**Raises:**

- `FileNotFoundError`: If graph file not found
- `JSONDecodeError`: If file contains invalid JSON

**Example:**

```python
data = load_graph_data("/path/to/graph.json")
nodes = data["nodes"]
edges = data["edges"]
```

---

#### `filter_events(

    events: list[dict],
    source: str | None = None,
    search: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    min_volume: float | None = None,
    expires_within: int | None = None,
    cluster_id: int | None = None,
    status: str = "active",
    clusters: list[dict] | None = None,

) -> list[dict]`

Filter events by multiple criteria.

**Parameters:**

| Parameter        | Type  | Description                                    |
| ---------------- | ----- | ---------------------------------------------- |
| `events`         | list  | List of event dictionaries                     |
| `source`         | str   | Filter by platform: `"kalshi"`, `"polymarket"` |
| `search`         | str   | Case-insensitive search in title/description   |
| `min_price`      | float | Minimum YES price (0-1)                        |
| `max_price`      | float | Maximum YES price (0-1)                        |
| `min_volume`     | float | Minimum 24h volume                             |
| `expires_within` | int   | Expires within N days                          |
| `cluster_id`     | int   | Filter by cluster membership                   |
| `status`         | str   | `"active"`, `"closed"`, or `"all"`             |
| `clusters`       | list  | Cluster data for cluster filtering             |

**Returns:** Filtered list of event dictionaries.

**Example:**

```python
high_volume = filter_events(
    events,
    min_volume=100000,
    source="kalshi",
    expires_within=7
)
```

---

#### `sort_events(

    events: list[dict],
    sort_by: str,
    edges: list[dict] | None = None,

) -> list[dict]`

Sort events by specified field.

**Parameters:**

- `events`: List of event dictionaries
- `sort_by`: `"price"`, `"volume"`, `"expiry"`, or `"similarity"`
- `edges`: Required for similarity sorting

**Returns:** Sorted list of events.

---

### find_arbitrage.py

#### `find_arbitrage_opportunities(

    data: dict,
    min_disparity: float = 0.05,
    min_similarity: float = 0.70,
    max_results: int = 20,
    source_filter: str = "both",
    expires_within: int = 30,
    min_confidence: float = 0.0,
    sort_by: str = "disparity",

) -> list[ArbitrageOpportunity]`

Find arbitrage opportunities from graph data.

**Parameters:**

| Parameter        | Type  | Default     | Description                                            |
| ---------------- | ----- | ----------- | ------------------------------------------------------ |
| `data`           | dict  | -           | Graph data with nodes, edges, clusters                 |
| `min_disparity`  | float | 0.05        | Minimum price disparity (0-1)                          |
| `min_similarity` | float | 0.70        | Minimum semantic similarity (0-1)                      |
| `max_results`    | int   | 20          | Maximum opportunities to return                        |
| `source_filter`  | str   | "both"      | `"kalshi"`, `"polymarket"`, or `"both"`                |
| `expires_within` | int   | 30          | Maximum days to expiration                             |
| `min_confidence` | float | 0.0         | Minimum confidence score (0-1)                         |
| `sort_by`        | str   | "disparity" | `"disparity"`, `"profit"`, `"urgency"`, `"confidence"` |

**Returns:** List of `ArbitrageOpportunity` objects.

---

#### `ArbitrageOpportunity`

Dataclass representing a potential arbitrage.

**Attributes:**

| Attribute          | Type  | Description                       |
| ------------------ | ----- | --------------------------------- |
| `event_a`          | dict  | First event details               |
| `event_b`          | dict  | Second event details              |
| `similarity`       | float | Semantic similarity score (0-1)   |
| `price_disparity`  | float | Absolute price difference (0-1)   |
| `profit_potential` | float | Estimated profit after fees (0-1) |
| `time_urgency`     | int   | Days to earliest expiration       |
| `confidence`       | float | Overall confidence score (0-1)    |

**Example:**

```python
for opp in opportunities:
    print(f"{opp.event_a['title']} vs {opp.event_b['title']}")
    print(f"  Disparity: {opp.price_disparity * 100:.1f}%")
    print(f"  Confidence: {opp.confidence * 100:.0f}%")
```

---

#### `calculate_profit_potential(

    price_a: float,
    price_b: float,
    volume_a: float,
    volume_b: float,
    fees: float = 0.02,

) -> float`

Calculate estimated profit potential after fees.

**Strategy:** Buy YES on lower price platform, NO on higher price platform.

**Parameters:**

- `price_a`, `price_b`: YES prices on each platform (0-1)
- `volume_a`, `volume_b`: 24h trading volumes
- `fees`: Platform fee percentage (default: 2%)

**Returns:** Estimated profit percentage (0-1).

---

### visualize.py

#### `generate_d3_html(

    data: dict,
    width: int = 1200,
    height: int = 800,
    theme: str = "dark",
    title: str = "Delta Arbitrage Graph",
    cluster_focus: int | None = None,
    min_disparity: float = 0.0,

) -> str`

Generate interactive D3.js HTML visualization.

**Parameters:**

| Parameter       | Type  | Default                 | Description                  |
| --------------- | ----- | ----------------------- | ---------------------------- |
| `data`          | dict  | -                       | Graph data                   |
| `width`         | int   | 1200                    | Canvas width in pixels       |
| `height`        | int   | 800                     | Canvas height in pixels      |
| `theme`         | str   | "dark"                  | `"dark"` or `"light"`        |
| `title`         | str   | "Delta Arbitrage Graph" | Page title                   |
| `cluster_focus` | int   | None                    | Focus on specific cluster ID |
| `min_disparity` | float | 0.0                     | Minimum disparity for edges  |

**Returns:** Complete HTML string with embedded D3.js.

**Features:**

- Interactive force-directed graph
- Zoom and pan support
- Hover tooltips with event details
- Click clusters to expand
- Drag nodes to rearrange
- Color-coded by platform
- Arbitrage edges highlighted in red

**Example:**

```python
html = generate_d3_html(
    data,
    width=1920,
    height=1080,
    theme="dark",
    title="Arbitrage Opportunities"
)
with open("viz.html", "w") as f:
    f.write(html)
```

---

#### `generate_static_image(

    data: dict,
    output_path: str,
    width: int = 1200,
    height: int = 800,
    theme: str = "dark",
    title: str = "Delta Arbitrage Graph",
    cluster_focus: int | None = None,
    min_disparity: float = 0.0,

) -> str`

Generate static PNG/SVG visualization.

**Dependencies:** matplotlib, networkx

**Parameters:** Same as `generate_d3_html` plus:

- `output_path`: Path to save image (.png or .svg)

**Returns:** Output file path.

---

#### `generate_mermaid(data: dict, min_disparity: float = 0.05) -> str`

Generate Mermaid diagram syntax for documentation.

**Returns:** Mermaid markdown syntax.

**Example Output:**

```mermaid
graph LR
    subgraph cluster_5 [Bitcoin Crypto]
        id1[Bitcoin above 100k...]
        id2[BTC Price Feb 28...]
    end
    id1 --> "8.5%" --> id2
```

---

### export_data.py

#### `calculate_statistics(data: dict) -> dict`

Calculate summary statistics from graph data.

**Returns:** Dictionary with:

| Key                   | Type  | Description                      |
| --------------------- | ----- | -------------------------------- |
| `total_events`        | int   | Total number of events           |
| `total_matches`       | int   | Total arbitrage matches          |
| `total_clusters`      | int   | Number of clusters               |
| `kalshi_events`       | int   | Kalshi event count               |
| `polymarket_events`   | int   | Polymarket event count           |
| `avg_yes_price`       | float | Average YES price                |
| `total_volume_24h`    | float | Total 24h volume                 |
| `avg_volume_24h`      | float | Average volume per event         |
| `avg_price_disparity` | float | Average disparity across matches |
| `max_price_disparity` | float | Maximum disparity found          |
| `avg_similarity`      | float | Average semantic similarity      |
| `expiring_within_7d`  | int   | Events expiring within 7 days    |
| `generated_at`        | str   | ISO8601 timestamp                |

---

## Command Line APIs

### query_events.py CLI

```bash
python scripts/query_events.py [OPTIONS]
```

**Exit Codes:**

- `0`: Success
- `1`: Graph file not found or invalid

**Environment Variables:**

- `GRAPH_PATH`: Default path to graph.json

---

### find_arbitrage.py CLI

```bash
python scripts/find_arbitrage.py [OPTIONS]
```

**Output Formats:**

**Table** (default):

```
Opportunity #1 | Confidence: 85%
============================================================
Metric               Event A                              Event B
------------------------------------------------------------
Platform             kalshi                               polymarket
Ticker               XBTC-250228                          BTC-FEB28
YES Price            65.0¢                                72.5¢
...
```

**JSON:**

```json
[{
  "event_a": {...},
  "event_b": {...},
  "similarity": 0.85,
  "price_disparity": 0.075,
  "profit_potential": 0.035,
  "time_urgency": 12,
  "confidence": 0.85
}]
```

**CSV:**

```csv
source_a,source_b,ticker_a,ticker_b,yes_price_a,yes_price_b,disparity,similarity,...
```

---

### visualize.py CLI

```bash
python scripts/visualize.py [OPTIONS]
```

**Output Formats:**

- `d3`: Interactive HTML file
- `static`: PNG/SVG image
- `mermaid`: Markdown syntax (stdout or file)
- `json`: Raw graph data export

**Browser Integration:**
D3 format automatically opens in default browser unless `--no-browser` is set.

---

### export_data.py CLI

```bash
python scripts/export_data.py [OPTIONS]
```

**Format Support:**

| Format  | Events | Matches | Clusters | Stats | Multi-sheet    |
| ------- | ------ | ------- | -------- | ----- | -------------- |
| JSON    | Yes    | Yes     | Yes      | Yes   | No             |
| CSV     | Yes    | Yes     | Yes      | Yes   | No             |
| Parquet | Yes    | Yes     | Yes      | No    | Separate files |
| Excel   | Yes    | Yes     | Yes      | Yes   | Yes            |

**Parquet Export:**
Creates separate files:

- `{name}_events.parquet`
- `{name}_matches.parquet`
- `{name}_clusters.parquet`

**Excel Export:**
Creates single file with multiple sheets:

- Sheet: "Events"
- Sheet: "Matches"
- Sheet: "Clusters"
- Sheet: "Statistics"

---

## Data Access Patterns

### Pattern 1: Find High-Confidence Arbitrage

```python
from scripts.find_arbitrage import find_arbitrage_opportunities
from scripts.query_events import load_graph_data

data = load_graph_data()
opportunities = find_arbitrage_opportunities(
    data,
    min_disparity=0.05,
    min_similarity=0.80,
    min_confidence=0.75,
    sort_by="profit",
    max_results=10
)

for opp in opportunities:
    if opp.profit_potential > 0.03:
        print(f"High profit: {opp.event_a['title']}")
```

### Pattern 2: Export for Analysis

```python
from scripts.export_data import calculate_statistics, export_json

data = load_graph_data()
stats = calculate_statistics(data)
print(f"Total arbitrage edges: {stats['total_matches']}")

export_json(data, "export.json", include_stats=True)
```

### Pattern 3: Cluster Analysis

```python
# Get events in a specific cluster
cluster_id = 5
data = load_graph_data()
cluster = next(c for c in data["clusters"] if c["id"] == cluster_id)
event_ids = set(cluster["event_ids"])
events = [n for n in data["nodes"] if n["id"] in event_ids]

# Find arbitrages within cluster
matches = [e for e in data["edges"]
           if e["source_id"] in event_ids and e["target_id"] in event_ids]

print(f"Cluster {cluster_id}: {len(events)} events, {len(matches)} arbitrages")
```

---

## Error Handling

All scripts follow consistent error handling:

| Error                | Exit Code | Message                               |
| -------------------- | --------- | ------------------------------------- |
| Graph file not found | 1         | "Graph file not found at {path}"      |
| Invalid JSON         | 1         | "Invalid JSON in graph file: {error}" |
| Missing dependencies | 1         | "{package} required for {feature}"    |

---

## Performance Considerations

| Operation      | Time Complexity | Notes               |
| -------------- | --------------- | ------------------- |
| Load graph     | O(n + e + c)    | Linear in data size |
| Filter events  | O(n)            | Single pass         |
| Sort events    | O(n log n)      | Python timsort      |
| Find arbitrage | O(e)            | Pre-computed edges  |
| Generate D3    | O(n + e)        | HTML generation     |
| Export data    | O(n + e + c)    | Linear              |

**Memory Usage:**

- Graph data: ~500 bytes per event
- 10,000 events: ~5 MB
- 50,000 events: ~25 MB

---

## Version Compatibility

| Script Version | Delta Version | Python Version |
| -------------- | ------------- | -------------- |
| 1.0.0          | 1.0+          | 3.10+          |
