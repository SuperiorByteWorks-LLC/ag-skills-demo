#!/usr/bin/env python3
"""
Query events from the Delta arbitrage detection system.

Provides filtering by source, price, volume, expiration, and search terms.
Supports multiple output formats including JSON, CSV, and formatted tables.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


def load_graph_data(graph_path: str | None = None) -> dict:
    """Load graph data from the Delta pipeline output."""
    if graph_path is None:
        graph_path = os.getenv(
            "GRAPH_PATH",
            str(Path(__file__).parent.parent.parent / "pipeline" / "data" / "graph.json"),
        )

    try:
        with open(graph_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Graph file not found at {graph_path}", file=sys.stderr)
        print("Ensure the Delta pipeline is running and has generated graph data.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in graph file: {e}", file=sys.stderr)
        sys.exit(1)


def filter_events(
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
) -> list[dict]:
    """Apply filters to event list."""
    filtered = events.copy()

    # Build cluster membership map if cluster filter requested
    event_to_cluster: dict[str, int] = {}
    if clusters:
        for cluster in clusters:
            for eid in cluster.get("event_ids", []):
                event_to_cluster[eid] = cluster.get("id", -1)

    result = []
    now = datetime.now()

    for event in filtered:
        # Source filter
        if source and source != "all":
            if event.get("source") != source:
                continue

        # Status filter
        if status != "all":
            if event.get("status", "active") != status:
                continue

        # Search filter (case-insensitive in title and description)
        if search:
            search_lower = search.lower()
            title = event.get("title", "").lower()
            desc = event.get("description", "").lower()
            if search_lower not in title and search_lower not in desc:
                continue

        # Price filters
        yes_price = event.get("yes_price", 0)
        if min_price is not None and yes_price < min_price:
            continue
        if max_price is not None and yes_price > max_price:
            continue

        # Volume filter
        volume = event.get("volume_24h", 0)
        if min_volume is not None and volume < min_volume:
            continue

        # Expiration filter
        if expires_within is not None:
            expires_at = event.get("expires_at", "")
            if expires_at:
                try:
                    expiry = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
                    days_until = (expiry - now).days
                    if days_until > expires_within or days_until < 0:
                        continue
                except (ValueError, TypeError):
                    continue
            else:
                continue

        # Cluster filter
        if cluster_id is not None:
            if event_to_cluster.get(event.get("id", "")) != cluster_id:
                continue

        result.append(event)

    return result


def sort_events(
    events: list[dict],
    sort_by: str,
    edges: list[dict] | None = None,
) -> list[dict]:
    """Sort events by specified field."""
    if sort_by == "price":
        return sorted(events, key=lambda e: e.get("yes_price", 0), reverse=True)
    elif sort_by == "volume":
        return sorted(events, key=lambda e: e.get("volume_24h", 0), reverse=True)
    elif sort_by == "expiry":

        def expiry_key(e):
            expires = e.get("expires_at", "")
            if expires:
                try:
                    return datetime.fromisoformat(expires.replace("Z", "+00:00"))
                except (ValueError, TypeError):
                    pass
            return datetime.max

        return sorted(events, key=expiry_key)
    elif sort_by == "similarity" and edges:
        # Sort by max similarity to other events
        event_max_sim: dict[str, float] = {}
        for edge in edges:
            sim = edge.get("similarity", 0)
            sid = edge.get("source_id", "")
            tid = edge.get("target_id", "")
            event_max_sim[sid] = max(event_max_sim.get(sid, 0), sim)
            event_max_sim[tid] = max(event_max_sim.get(tid, 0), sim)
        return sorted(events, key=lambda e: event_max_sim.get(e.get("id", ""), 0), reverse=True)
    return events


def format_table(events: list[dict], max_width: int = 120) -> str:
    """Format events as a readable table."""
    if not events:
        return "No events found matching criteria."

    # Column widths
    id_width = 20
    source_width = 10
    ticker_width = 12
    price_width = 8
    vol_width = 12
    expiry_width = 12
    title_width = max_width - (
        id_width + source_width + ticker_width + price_width + vol_width + expiry_width + 7
    )

    lines = []
    header = (
        f"{'ID':<{id_width}} "
        f"{'Source':<{source_width}} "
        f"{'Ticker':<{ticker_width}} "
        f"{'Price':>{price_width}} "
        f"{'Volume':>{vol_width}} "
        f"{'Expiry':<{expiry_width}} "
        f"{'Title':<{title_width}}"
    )
    lines.append(header)
    lines.append("-" * len(header))

    for event in events:
        event_id = event.get("id", "")[: id_width - 1]
        source = event.get("source", "")[: source_width - 1]
        ticker = event.get("ticker", "")[: ticker_width - 1]
        price = f"{event.get('yes_price', 0) * 100:.1f}¢"
        volume = event.get("volume_24h", 0)
        vol_str = f"${volume / 1000:.1f}K" if volume >= 1000 else f"${volume:.0f}"

        expires = event.get("expires_at", "")
        if expires:
            try:
                expiry_dt = datetime.fromisoformat(expires.replace("Z", "+00:00"))
                days = (expiry_dt - datetime.now()).days
                expiry_str = f"{days}d" if days >= 0 else "exp"
            except (ValueError, TypeError):
                expiry_str = "?"
        else:
            expiry_str = "N/A"

        title = event.get("title", "")
        if len(title) > title_width - 1:
            title = title[: title_width - 4] + "..."

        line = (
            f"{event_id:<{id_width}} "
            f"{source:<{source_width}} "
            f"{ticker:<{ticker_width}} "
            f"{price:>{price_width}} "
            f"{vol_str:>{vol_width}} "
            f"{expiry_str:<{expiry_width}} "
            f"{title:<{title_width}}"
        )
        lines.append(line)

    return "\n".join(lines)


def format_csv(events: list[dict]) -> str:
    """Format events as CSV."""
    if not events:
        return "id,source,title,ticker,yes_price,no_price,volume_24h,expires_at,market_url,status"

    lines = ["id,source,title,ticker,yes_price,no_price,volume_24h,expires_at,market_url,status"]
    for event in events:
        title = event.get("title", "").replace('"', '""')
        desc = event.get("description", "").replace('"', '""')
        lines.append(
            f'"{event.get("id", "")}",'
            f'"{event.get("source", "")}",'
            f'"{title}",'
            f'"{event.get("ticker", "")}",'
            f"{event.get('yes_price', 0)},"
            f"{event.get('no_price', 0)},"
            f"{event.get('volume_24h', 0)},"
            f'"{event.get("expires_at", "")}",'
            f'"{event.get("market_url", "")}",'
            f'"{event.get("status", "active")}"'
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query events from Delta arbitrage detection system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --source kalshi --search "election" --limit 10
  %(prog)s --min-price 0.30 --max-price 0.70 --sort volume
  %(prog)s --expires-within 7 --output csv --output-file urgent.csv
        """,
    )

    parser.add_argument(
        "--source",
        choices=["kalshi", "polymarket", "all"],
        default="all",
        help="Filter by platform (default: all)",
    )
    parser.add_argument(
        "--search",
        type=str,
        help="Search in title and description",
    )
    parser.add_argument(
        "--min-price",
        type=float,
        help="Minimum YES price (0-1)",
    )
    parser.add_argument(
        "--max-price",
        type=float,
        help="Maximum YES price (0-1)",
    )
    parser.add_argument(
        "--min-volume",
        type=float,
        help="Minimum 24h volume",
    )
    parser.add_argument(
        "--expires-within",
        type=int,
        metavar="DAYS",
        help="Filter events expiring within N days",
    )
    parser.add_argument(
        "--cluster",
        type=int,
        metavar="ID",
        help="Filter by cluster ID",
    )
    parser.add_argument(
        "--status",
        choices=["active", "closed", "all"],
        default="active",
        help="Status filter (default: active)",
    )
    parser.add_argument(
        "--sort",
        choices=["price", "volume", "expiry", "similarity"],
        default="price",
        help="Sort field (default: price)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum results (default: 50)",
    )
    parser.add_argument(
        "--output",
        choices=["json", "csv", "table"],
        default="table",
        help="Output format (default: table)",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        help="Save output to file instead of stdout",
    )
    parser.add_argument(
        "--graph-path",
        type=str,
        help="Path to graph.json (default: from GRAPH_PATH env or standard location)",
    )

    args = parser.parse_args()

    # Load data
    data = load_graph_data(args.graph_path)
    events = data.get("nodes", [])
    clusters = data.get("clusters", [])
    edges = data.get("edges", [])

    # Apply filters
    filtered = filter_events(
        events,
        source=args.source if args.source != "all" else None,
        search=args.search,
        min_price=args.min_price,
        max_price=args.max_price,
        min_volume=args.min_volume,
        expires_within=args.expires_within,
        cluster_id=args.cluster,
        status=args.status,
        clusters=clusters,
    )

    # Sort
    filtered = sort_events(filtered, args.sort, edges)

    # Limit
    filtered = filtered[: args.limit]

    # Format output
    if args.output == "json":
        output = json.dumps(filtered, indent=2)
    elif args.output == "csv":
        output = format_csv(filtered)
    else:
        output = format_table(filtered)

    # Output
    if args.output_file:
        with open(args.output_file, "w") as f:
            f.write(output)
        print(f"Wrote {len(filtered)} events to {args.output_file}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
