#!/usr/bin/env python3
"""
Export Delta arbitrage data in various formats.

Supports JSON, CSV, Parquet, and Excel formats for external analysis.
Can export events, matches, clusters, and summary statistics.
"""

import argparse
import json
import os
import sys
from datetime import datetime
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
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in graph file: {e}", file=sys.stderr)
        sys.exit(1)


def calculate_statistics(data: dict) -> dict:
    """Calculate summary statistics from graph data."""
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    clusters = data.get("clusters", [])

    # Platform breakdown
    kalshi_count = sum(1 for n in nodes if n.get("source") == "kalshi")
    poly_count = len(nodes) - kalshi_count

    # Price stats
    prices = [n.get("yes_price", 0) for n in nodes]
    avg_price = sum(prices) / len(prices) if prices else 0

    # Volume stats
    volumes = [n.get("volume_24h", 0) for n in nodes]
    total_volume = sum(volumes)
    avg_volume = total_volume / len(volumes) if volumes else 0

    # Disparity stats
    disparities = [e.get("price_disparity", 0) for e in edges]
    avg_disparity = sum(disparities) / len(disparities) if disparities else 0
    max_disparity = max(disparities) if disparities else 0

    # Similarity stats
    similarities = [e.get("similarity", 0) for e in edges]
    avg_similarity = sum(similarities) / len(similarities) if similarities else 0

    # Time stats
    now = datetime.now()
    expiring_soon = 0
    for node in nodes:
        expires = node.get("expires_at", "")
        if expires:
            try:
                expiry = datetime.fromisoformat(expires.replace("Z", "+00:00"))
                days = (expiry - now).days
                if 0 <= days <= 7:
                    expiring_soon += 1
            except (ValueError, TypeError):
                pass

    return {
        "total_events": len(nodes),
        "total_matches": len(edges),
        "total_clusters": len(clusters),
        "kalshi_events": kalshi_count,
        "polymarket_events": poly_count,
        "avg_yes_price": round(avg_price, 4),
        "total_volume_24h": round(total_volume, 2),
        "avg_volume_24h": round(avg_volume, 2),
        "avg_price_disparity": round(avg_disparity, 4),
        "max_price_disparity": round(max_disparity, 4),
        "avg_similarity": round(avg_similarity, 4),
        "expiring_within_7d": expiring_soon,
        "generated_at": datetime.now().isoformat(),
    }


def export_json(data: dict, output_path: str, include_stats: bool = False) -> None:
    """Export data as JSON."""
    export = {
        "nodes": data.get("nodes", []),
        "edges": data.get("edges", []),
        "clusters": data.get("clusters", []),
    }
    if include_stats:
        export["statistics"] = calculate_statistics(data)

    with open(output_path, "w") as f:
        json.dump(export, indent=2, fp=f)


def export_csv(
    data: dict,
    output_path: str,
    include_events: bool = True,
    include_matches: bool = False,
    include_clusters: bool = False,
) -> None:
    """Export data as CSV."""
    lines = []

    if include_events:
        lines.append("\n# EVENTS")
        lines.append(
            "id,source,title,ticker,yes_price,no_price,volume_24h,expires_at,market_url,status"
        )
        for node in data.get("nodes", []):
            title = node.get("title", "").replace('"', '""')
            lines.append(
                f'"{node.get("id", "")}",'
                f'"{node.get("source", "")}",'
                f'"{title}",'
                f'"{node.get("ticker", "")}",'
                f"{node.get('yes_price', 0)},"
                f"{node.get('no_price', 0)},"
                f"{node.get('volume_24h', 0)},"
                f'"{node.get("expires_at", "")}",'
                f'"{node.get("market_url", "")}",'
                f'"{node.get("status", "active")}"'
            )

    if include_matches:
        lines.append("\n# MATCHES")
        lines.append("source_id,target_id,similarity,price_disparity,matched_at")
        for edge in data.get("edges", []):
            lines.append(
                f'"{edge.get("source_id", "")}",'
                f'"{edge.get("target_id", "")}",'
                f"{edge.get('similarity', 0)},"
                f"{edge.get('price_disparity', 0)},"
                f'"{edge.get("matched_at", "")}"'
            )

    if include_clusters:
        lines.append("\n# CLUSTERS")
        lines.append("id,label,count,event_ids")
        for cluster in data.get("clusters", []):
            event_ids = "|".join(cluster.get("event_ids", []))
            lines.append(
                f"{cluster.get('id', 0)},"
                f'"{cluster.get("label", "")}",'
                f"{cluster.get('count', 0)},"
                f'"{event_ids}"'
            )

    with open(output_path, "w") as f:
        f.write("\n".join(lines))


def export_parquet(
    data: dict,
    output_path: str,
    include_events: bool = True,
    include_matches: bool = False,
    include_clusters: bool = False,
) -> None:
    """Export data as Parquet."""
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas and pyarrow required for Parquet export.", file=sys.stderr)
        print("Install: pip install pandas pyarrow", file=sys.stderr)
        sys.exit(1)

    # Create multiple files for different data types
    base_path = Path(output_path).parent
    base_name = Path(output_path).stem

    if include_events:
        events_df = pd.DataFrame(data.get("nodes", []))
        events_path = base_path / f"{base_name}_events.parquet"
        events_df.to_parquet(events_path, index=False)
        print(f"Exported events to {events_path}")

    if include_matches:
        matches_df = pd.DataFrame(data.get("edges", []))
        matches_path = base_path / f"{base_name}_matches.parquet"
        matches_df.to_parquet(matches_path, index=False)
        print(f"Exported matches to {matches_path}")

    if include_clusters:
        # Flatten event_ids for cluster export
        clusters = []
        for cluster in data.get("clusters", []):
            cluster_copy = cluster.copy()
            cluster_copy["event_ids"] = "|".join(cluster_copy.get("event_ids", []))
            clusters.append(cluster_copy)
        clusters_df = pd.DataFrame(clusters)
        clusters_path = base_path / f"{base_name}_clusters.parquet"
        clusters_df.to_parquet(clusters_path, index=False)
        print(f"Exported clusters to {clusters_path}")


def export_excel(
    data: dict,
    output_path: str,
    include_events: bool = True,
    include_matches: bool = False,
    include_clusters: bool = False,
) -> None:
    """Export data as Excel with multiple sheets."""
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas and openpyxl required for Excel export.", file=sys.stderr)
        print("Install: pip install pandas openpyxl", file=sys.stderr)
        sys.exit(1)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        if include_events:
            events_df = pd.DataFrame(data.get("nodes", []))
            events_df.to_excel(writer, sheet_name="Events", index=False)

        if include_matches:
            matches_df = pd.DataFrame(data.get("edges", []))
            matches_df.to_excel(writer, sheet_name="Matches", index=False)

        if include_clusters:
            clusters_df = pd.DataFrame(data.get("clusters", []))
            clusters_df.to_excel(writer, sheet_name="Clusters", index=False)

        # Stats sheet
        stats_df = pd.DataFrame([calculate_statistics(data)])
        stats_df.to_excel(writer, sheet_name="Statistics", index=False)


def export_by_cluster(
    data: dict,
    output_dir: str,
    format: str = "json",
) -> None:
    """Export separate files per cluster."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    nodes = {n.get("id"): n for n in data.get("nodes", [])}
    clusters = data.get("clusters", [])

    for cluster in clusters:
        cluster_id = cluster.get("id")
        event_ids = cluster.get("event_ids", [])

        cluster_data = {
            "cluster": cluster,
            "events": [nodes.get(eid) for eid in event_ids if eid in nodes],
        }

        # Filter edges for this cluster
        cluster_event_set = set(event_ids)
        cluster_data["matches"] = [
            e
            for e in data.get("edges", [])
            if e.get("source_id") in cluster_event_set and e.get("target_id") in cluster_event_set
        ]

        filename = (
            f"cluster_{cluster_id}_{cluster.get('label', 'unknown').replace(' ', '_')}.{format}"
        )
        file_path = output_path / filename

        if format == "json":
            with open(file_path, "w") as f:
                json.dump(cluster_data, indent=2, fp=f)
        elif format == "csv":
            lines = ["# EVENTS", "id,source,title,yes_price,market_url"]
            for event in cluster_data["events"]:
                title = event.get("title", "").replace('"', '""')[:50]
                lines.append(
                    f'"{event.get("id", "")}",'
                    f'"{event.get("source", "")}",'
                    f'"{title}",'
                    f"{event.get('yes_price', 0)},"
                    f'"{event.get("market_url", "")}"'
                )
            lines.extend(["", "# MATCHES", "source_id,target_id,similarity"])
            for match in cluster_data["matches"]:
                lines.append(
                    f'"{match.get("source_id", "")}",'
                    f'"{match.get("target_id", "")}",'
                    f"{match.get('similarity', 0)}"
                )
            with open(file_path, "w") as f:
                f.write("\n".join(lines))

        print(f"Exported {filename}")


def filter_by_date(data: dict, since_date: str) -> dict:
    """Filter data to only include events/matches since a specific date."""
    since = datetime.strptime(since_date, "%Y-%m-%d")

    # Filter nodes
    filtered_nodes = []
    for node in data.get("nodes", []):
        created = node.get("created_at", "")
        if created:
            try:
                node_date = datetime.fromisoformat(created.replace("Z", "+00:00"))
                if node_date >= since:
                    filtered_nodes.append(node)
            except (ValueError, TypeError):
                # Include if can't parse date
                filtered_nodes.append(node)
        else:
            filtered_nodes.append(node)

    # Get filtered node IDs
    filtered_ids = {n.get("id") for n in filtered_nodes}

    # Filter edges
    filtered_edges = [
        e
        for e in data.get("edges", [])
        if e.get("source_id") in filtered_ids and e.get("target_id") in filtered_ids
    ]

    # Filter clusters
    filtered_clusters = []
    for cluster in data.get("clusters", []):
        cluster_events = [eid for eid in cluster.get("event_ids", []) if eid in filtered_ids]
        if cluster_events:
            filtered_cluster = cluster.copy()
            filtered_cluster["event_ids"] = cluster_events
            filtered_cluster["count"] = len(cluster_events)
            filtered_clusters.append(filtered_cluster)

    return {
        "nodes": filtered_nodes,
        "edges": filtered_edges,
        "clusters": filtered_clusters,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Export Delta arbitrage data in various formats",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --format json --output data.json --include-matches
  %(prog)s --format parquet --output analysis.parquet --include-all
  %(prog)s --format csv --split-by-cluster --output-dir ./clusters/
        """,
    )

    parser.add_argument(
        "--format",
        choices=["json", "csv", "parquet", "xlsx"],
        default="json",
        help="Export format (default: json)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Output directory for split exports",
    )
    parser.add_argument(
        "--include-events",
        action="store_true",
        help="Include all events",
    )
    parser.add_argument(
        "--include-matches",
        action="store_true",
        help="Include arbitrage matches",
    )
    parser.add_argument(
        "--include-clusters",
        action="store_true",
        help="Include cluster assignments",
    )
    parser.add_argument(
        "--include-stats",
        action="store_true",
        help="Include summary statistics",
    )
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Include everything",
    )
    parser.add_argument(
        "--since",
        type=str,
        metavar="YYYY-MM-DD",
        help="Filter events since this date",
    )
    parser.add_argument(
        "--split-by-cluster",
        action="store_true",
        help="Export separate files per cluster",
    )
    parser.add_argument(
        "--graph-path",
        type=str,
        help="Path to graph.json",
    )

    args = parser.parse_args()

    # Load data
    data = load_graph_data(args.graph_path)

    # Apply date filter
    if args.since:
        data = filter_by_date(data, args.since)

    # Handle --include-all
    if args.include_all:
        args.include_events = True
        args.include_matches = True
        args.include_clusters = True
        args.include_stats = True

    # Set default includes
    if not any([args.include_events, args.include_matches, args.include_clusters]):
        args.include_events = True  # Default to events only

    # Split by cluster
    if args.split_by_cluster:
        if not args.output_dir:
            print("Error: --output-dir required with --split-by-cluster", file=sys.stderr)
            sys.exit(1)
        export_by_cluster(data, args.output_dir, args.format)
        return

    # Determine output path
    if not args.output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"delta_export_{timestamp}.{args.format}"

    # Export based on format
    if args.format == "json":
        export_json(data, args.output, include_stats=args.include_stats)
    elif args.format == "csv":
        export_csv(
            data,
            args.output,
            include_events=args.include_events,
            include_matches=args.include_matches,
            include_clusters=args.include_clusters,
        )
    elif args.format == "parquet":
        export_parquet(
            data,
            args.output,
            include_events=args.include_events,
            include_matches=args.include_matches,
            include_clusters=args.include_clusters,
        )
    elif args.format == "xlsx":
        export_excel(
            data,
            args.output,
            include_events=args.include_events,
            include_matches=args.include_matches,
            include_clusters=args.include_clusters,
        )

    print(f"Exported to: {args.output}")

    # Print statistics
    if args.include_stats:
        stats = calculate_statistics(data)
        print("\nSummary Statistics:")
        for key, value in stats.items():
            if key != "generated_at":
                print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
