#!/usr/bin/env python3
"""
Find arbitrage opportunities between Kalshi and Polymarket prediction markets.

Detects semantically similar events with price disparities that indicate
potential arbitrage opportunities. Calculates profit potential and confidence scores.
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


@dataclass
class ArbitrageOpportunity:
    """Represents a potential arbitrage opportunity."""

    event_a: dict
    event_b: dict
    similarity: float
    price_disparity: float
    profit_potential: float
    time_urgency: int
    confidence: float


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


def calculate_time_urgency(event_a: dict, event_b: dict) -> int:
    """Calculate days to earliest expiration."""
    now = datetime.now()
    min_days = None

    for event in [event_a, event_b]:
        expires = event.get("expires_at", "")
        if expires:
            try:
                expiry = datetime.fromisoformat(expires.replace("Z", "+00:00"))
                days = (expiry - now).days
                if days >= 0 and (min_days is None or days < min_days):
                    min_days = days
            except (ValueError, TypeError):
                pass

    return min_days if min_days is not None else 30


def calculate_profit_potential(
    price_a: float,
    price_b: float,
    volume_a: float,
    volume_b: float,
    fees: float = 0.02,  # 2% per platform typical
) -> float:
    """Calculate potential profit after fees.

    Strategy: Buy YES on lower price, NO on higher price (or vice versa)
    for risk-free arbitrage.
    """
    disparity = abs(price_a - price_b)
    if disparity <= fees * 2:
        return 0.0

    # Effective profit after round-trip fees
    # Assume 2% fee each way on each platform
    total_fees = fees * 4
    profit = disparity - total_fees

    # Scale by liquidity (lower volume = harder to execute)
    min_volume = min(volume_a, volume_b)
    liquidity_factor = min(1.0, min_volume / 10000)  # Normalize to $10K

    return max(0, profit * liquidity_factor)


def calculate_confidence(
    similarity: float,
    disparity: float,
    urgency: int,
    has_ticker: bool,
) -> float:
    """Calculate overall confidence score (0-1).

    Factors:
    - Similarity: Higher = more confident events are truly matched
    - Disparity: Higher = more obvious opportunity
    - Urgency: More time = more confident (can wait for better execution)
    - Ticker: Having ticker symbols adds confidence
    """
    # Similarity score (heavily weighted)
    sim_score = min(1.0, similarity / 0.85)  # 0.85+ similarity = max score

    # Disparity score
    disp_score = min(1.0, disparity / 0.15)  # 15%+ disparity = max score

    # Urgency score (more time is better)
    urgency_score = min(1.0, urgency / 7) if urgency > 0 else 0.0

    # Ticker bonus
    ticker_bonus = 0.1 if has_ticker else 0.0

    # Weighted combination
    confidence = sim_score * 0.4 + disp_score * 0.3 + urgency_score * 0.2 + ticker_bonus

    return min(1.0, confidence)


def find_arbitrage_opportunities(
    data: dict,
    min_disparity: float = 0.05,
    min_similarity: float = 0.70,
    max_results: int = 20,
    source_filter: str = "both",
    expires_within: int = 30,
    min_confidence: float = 0.0,
    sort_by: str = "disparity",
) -> list[ArbitrageOpportunity]:
    """Find arbitrage opportunities from graph data."""
    nodes = {n["id"]: n for n in data.get("nodes", [])}
    edges = data.get("edges", [])
    opportunities = []

    now = datetime.now()

    for edge in edges:
        source_id = edge.get("source_id", "")
        target_id = edge.get("target_id", "")
        similarity = edge.get("similarity", 0)
        disparity = edge.get("price_disparity", 0)

        # Skip if below thresholds
        if similarity < min_similarity:
            continue
        if disparity < min_disparity:
            continue

        event_a = nodes.get(source_id, {})
        event_b = nodes.get(target_id, {})

        if not event_a or not event_b:
            continue

        # Source filter
        if source_filter == "kalshi":
            if event_a.get("source") != "kalshi" or event_b.get("source") != "kalshi":
                continue
        elif source_filter == "polymarket":
            if event_a.get("source") != "polymarket" or event_b.get("source") != "polymarket":
                continue
        elif source_filter == "both":
            # Require cross-platform
            if event_a.get("source") == event_b.get("source"):
                continue

        # Expiration filter
        if expires_within > 0:
            for event in [event_a, event_b]:
                expires = event.get("expires_at", "")
                if expires:
                    try:
                        expiry = datetime.fromisoformat(expires.replace("Z", "+00:00"))
                        days = (expiry - now).days
                        if days > expires_within or days < 0:
                            continue
                    except (ValueError, TypeError):
                        pass

        # Calculate derived metrics
        time_urgency = calculate_time_urgency(event_a, event_b)
        profit = calculate_profit_potential(
            event_a.get("yes_price", 0),
            event_b.get("yes_price", 0),
            event_a.get("volume_24h", 0),
            event_b.get("volume_24h", 0),
        )

        has_ticker = bool(event_a.get("ticker")) and bool(event_b.get("ticker"))
        confidence = calculate_confidence(similarity, disparity, time_urgency, has_ticker)

        # Confidence filter
        if confidence < min_confidence:
            continue

        opp = ArbitrageOpportunity(
            event_a=event_a,
            event_b=event_b,
            similarity=similarity,
            price_disparity=disparity,
            profit_potential=profit,
            time_urgency=time_urgency,
            confidence=confidence,
        )
        opportunities.append(opp)

    # Sort
    if sort_by == "disparity":
        opportunities.sort(key=lambda x: x.price_disparity, reverse=True)
    elif sort_by == "profit":
        opportunities.sort(key=lambda x: x.profit_potential, reverse=True)
    elif sort_by == "urgency":
        opportunities.sort(key=lambda x: x.time_urgency)
    elif sort_by == "confidence":
        opportunities.sort(key=lambda x: x.confidence, reverse=True)

    return opportunities[:max_results]


def format_opportunity_table(
    opportunities: list[ArbitrageOpportunity],
    max_width: int = 120,
    include_analysis: bool = False,
) -> str:
    """Format opportunities as a readable table."""
    if not opportunities:
        return "No arbitrage opportunities found matching criteria."

    lines = []
    lines.append(f"Found {len(opportunities)} arbitrage opportunities\n")

    for i, opp in enumerate(opportunities, 1):
        a = opp.event_a
        b = opp.event_b

        lines.append(f"{'=' * max_width}")
        lines.append(f"Opportunity #{i} | Confidence: {opp.confidence * 100:.0f}%")
        lines.append(f"{'=' * max_width}")

        # Header
        lines.append(f"\n{'Metric':<20} {'Event A':<40} {'Event B':<40}")
        lines.append(f"{'-' * 20} {'-' * 40} {'-' * 40}")

        # Platform
        lines.append(f"{'Platform':<20} {a.get('source', 'N/A'):<40} {b.get('source', 'N/A'):<40}")

        # Ticker
        lines.append(f"{'Ticker':<20} {a.get('ticker', 'N/A'):<40} {b.get('ticker', 'N/A'):<40}")

        # Prices
        lines.append(
            f"{'YES Price':<20} {a.get('yes_price', 0) * 100:.1f}¢{'':<37} {b.get('yes_price', 0) * 100:.1f}¢"
        )
        lines.append(
            f"{'NO Price':<20} {a.get('no_price', 0) * 100:.1f}¢{'':<37} {b.get('no_price', 0) * 100:.1f}¢"
        )

        # Volume
        vol_a = a.get("volume_24h", 0)
        vol_b = b.get("volume_24h", 0)
        lines.append(f"{'24h Volume':<20} ${vol_a / 1000:.1f}K{'':<35} ${vol_b / 1000:.1f}K")

        # URLs
        lines.append(
            f"{'URL':<20} {a.get('market_url', 'N/A')[:40]:<40} {b.get('market_url', 'N/A')[:40]:<40}"
        )

        # Match details
        lines.append(f"\n{'Match Analysis':<20}")
        lines.append(f"{'-' * 20}")
        lines.append(f"  Similarity: {opp.similarity * 100:.1f}%")
        lines.append(f"  Price Disparity: {opp.price_disparity * 100:.2f}%")
        lines.append(f"  Time to Expiry: {opp.time_urgency} days")

        if include_analysis:
            lines.append(f"\n{'Profit Analysis':<20}")
            lines.append(f"{'-' * 20}")
            lines.append(f"  Est. Profit: {opp.profit_potential * 100:.2f}%")

            if opp.profit_potential > 0.05:
                lines.append(f"  Status: HIGH POTENTIAL")
            elif opp.profit_potential > 0.02:
                lines.append(f"  Status: MODERATE POTENTIAL")
            else:
                lines.append(f"  Status: LOW POTENTIAL (fees may exceed profit)")

            # Strategy suggestion
            price_a = a.get("yes_price", 0)
            price_b = b.get("yes_price", 0)
            if price_a < price_b:
                lines.append(f"\n  Strategy:")
                lines.append(
                    f"    • Buy YES on {a.get('source', 'A')} (lower price: {price_a * 100:.1f}¢)"
                )
                lines.append(
                    f"    • Buy NO on {b.get('source', 'B')} (higher YES implies lower NO)"
                )
            else:
                lines.append(f"\n  Strategy:")
                lines.append(
                    f"    • Buy YES on {b.get('source', 'B')} (lower price: {price_b * 100:.1f}¢)"
                )
                lines.append(
                    f"    • Buy NO on {a.get('source', 'A')} (higher YES implies lower NO)"
                )

        # Titles
        lines.append(f"\n{'Event Titles':<20}")
        lines.append(f"{'-' * 20}")
        lines.append(f"  A: {a.get('title', 'N/A')[:80]}")
        lines.append(f"  B: {b.get('title', 'N/A')[:80]}")
        lines.append("")

    return "\n".join(lines)


def format_opportunity_json(opportunities: list[ArbitrageOpportunity]) -> str:
    """Format opportunities as JSON."""
    data = []
    for opp in opportunities:
        data.append(
            {
                "event_a": {
                    "id": opp.event_a.get("id"),
                    "source": opp.event_a.get("source"),
                    "title": opp.event_a.get("title"),
                    "ticker": opp.event_a.get("ticker"),
                    "yes_price": opp.event_a.get("yes_price"),
                    "no_price": opp.event_a.get("no_price"),
                    "volume_24h": opp.event_a.get("volume_24h"),
                    "expires_at": opp.event_a.get("expires_at"),
                    "market_url": opp.event_a.get("market_url"),
                },
                "event_b": {
                    "id": opp.event_b.get("id"),
                    "source": opp.event_b.get("source"),
                    "title": opp.event_b.get("title"),
                    "ticker": opp.event_b.get("ticker"),
                    "yes_price": opp.event_b.get("yes_price"),
                    "no_price": opp.event_b.get("no_price"),
                    "volume_24h": opp.event_b.get("volume_24h"),
                    "expires_at": opp.event_b.get("expires_at"),
                    "market_url": opp.event_b.get("market_url"),
                },
                "similarity": opp.similarity,
                "price_disparity": opp.price_disparity,
                "profit_potential": opp.profit_potential,
                "time_urgency": opp.time_urgency,
                "confidence": opp.confidence,
            }
        )
    return json.dumps(data, indent=2)


def format_opportunity_csv(opportunities: list[ArbitrageOpportunity]) -> str:
    """Format opportunities as CSV."""
    if not opportunities:
        return "source_a,source_b,ticker_a,ticker_b,yes_price_a,yes_price_b,disparity,similarity,profit_potential,urgency_days,confidence"

    lines = [
        "source_a,source_b,ticker_a,ticker_b,yes_price_a,yes_price_b,disparity,similarity,profit_potential,urgency_days,confidence,url_a,url_b"
    ]
    for opp in opportunities:
        a = opp.event_a
        b = opp.event_b
        lines.append(
            f"{a.get('source', '')},"
            f"{b.get('source', '')},"
            f'"{a.get("ticker", "")}",'
            f'"{b.get("ticker", "")}",'
            f"{a.get('yes_price', 0)},"
            f"{b.get('yes_price', 0)},"
            f"{opp.price_disparity},"
            f"{opp.similarity},"
            f"{opp.profit_potential},"
            f"{opp.time_urgency},"
            f"{opp.confidence},"
            f'"{a.get("market_url", "")}",'
            f'"{b.get("market_url", "")}"'
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Find arbitrage opportunities between Kalshi and Polymarket",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --max-results 10 --sort-by profit
  %(prog)s --min-disparity 0.10 --include-analysis
  %(prog)s --expires-within 7 --output json
        """,
    )

    parser.add_argument(
        "--min-disparity",
        type=float,
        default=0.05,
        help="Minimum price disparity (default: 0.05 = 5%%)",
    )
    parser.add_argument(
        "--min-similarity",
        type=float,
        default=0.70,
        help="Minimum semantic similarity (default: 0.70 = 70%%)",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=20,
        help="Maximum opportunities to return (default: 20)",
    )
    parser.add_argument(
        "--source",
        choices=["kalshi", "polymarket", "both"],
        default="both",
        help="Source filter: kalshi, polymarket, or cross-platform (default: both)",
    )
    parser.add_argument(
        "--expires-within",
        type=int,
        default=30,
        help="Max days to expiration (default: 30)",
    )
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.0,
        help="Minimum confidence score 0-1 (default: 0)",
    )
    parser.add_argument(
        "--sort-by",
        choices=["disparity", "profit", "urgency", "confidence"],
        default="disparity",
        help="Sort order (default: disparity)",
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
        "--include-analysis",
        action="store_true",
        help="Include profit analysis and strategy suggestions",
    )
    parser.add_argument(
        "--graph-path",
        type=str,
        help="Path to graph.json",
    )

    args = parser.parse_args()

    # Load data
    data = load_graph_data(args.graph_path)

    # Find opportunities
    opportunities = find_arbitrage_opportunities(
        data,
        min_disparity=args.min_disparity,
        min_similarity=args.min_similarity,
        max_results=args.max_results,
        source_filter=args.source,
        expires_within=args.expires_within,
        min_confidence=args.min_confidence,
        sort_by=args.sort_by,
    )

    # Format output
    if args.output == "json":
        output = format_opportunity_json(opportunities)
    elif args.output == "csv":
        output = format_opportunity_csv(opportunities)
    else:
        output = format_opportunity_table(opportunities, include_analysis=args.include_analysis)

    # Output
    if args.output_file:
        with open(args.output_file, "w") as f:
            f.write(output)
        print(f"Wrote {len(opportunities)} opportunities to {args.output_file}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
