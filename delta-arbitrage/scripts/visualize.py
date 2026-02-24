#!/usr/bin/env python3
"""
Generate visualizations from Delta arbitrage data.

Supports multiple output formats:
- D3: Interactive HTML force-directed graph
- Static: PNG/SVG images using matplotlib/networkx
- Mermaid: Markdown diagram syntax
- JSON: Raw graph data for custom visualization
"""

import argparse
import json
import os
import subprocess
import sys
import webbrowser
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


def generate_d3_html(
    data: dict,
    width: int = 1200,
    height: int = 800,
    theme: str = "dark",
    title: str = "Delta Arbitrage Graph",
    cluster_focus: int | None = None,
    min_disparity: float = 0.0,
) -> str:
    """Generate interactive D3.js HTML visualization."""

    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    clusters = data.get("clusters", [])

    # Build event to cluster mapping
    event_to_cluster: dict[str, int] = {}
    for cluster in clusters:
        for eid in cluster.get("event_ids", []):
            event_to_cluster[eid] = cluster.get("id", -1)

    # Theme colors
    if theme == "dark":
        bg_color = "#0d1117"
        text_color = "#c8d4e0"
        kalshi_color = "#38bdf8"
        poly_color = "#a78bfa"
        edge_color = "#ef4444"
        grid_color = "#1e2733"
        tooltip_bg = "#161b22"
    else:
        bg_color = "#ffffff"
        text_color = "#1f2937"
        kalshi_color = "#2563eb"
        poly_color = "#7c3aed"
        edge_color = "#dc2626"
        grid_color = "#e5e7eb"
        tooltip_bg = "#f9fafb"

    # Filter edges by disparity
    if min_disparity > 0:
        edges = [e for e in edges if e.get("price_disparity", 0) >= min_disparity]

    # If focusing on a cluster, filter nodes and edges
    if cluster_focus is not None:
        cluster = next((c for c in clusters if c.get("id") == cluster_focus), None)
        if cluster:
            cluster_event_ids = set(cluster.get("event_ids", []))
            nodes = [n for n in nodes if n.get("id") in cluster_event_ids]
            edges = [
                e
                for e in edges
                if e.get("source_id") in cluster_event_ids
                and e.get("target_id") in cluster_event_ids
            ]

    # Build D3 data
    d3_nodes = []
    for node in nodes:
        d3_nodes.append(
            {
                "id": node.get("id"),
                "title": node.get("title", ""),
                "source": node.get("source"),
                "yes_price": node.get("yes_price", 0),
                "no_price": node.get("no_price", 0),
                "ticker": node.get("ticker", ""),
                "cluster": event_to_cluster.get(node.get("id", ""), -1),
                "market_url": node.get("market_url", ""),
            }
        )

    d3_edges = []
    for edge in edges:
        d3_edges.append(
            {
                "source": edge.get("source_id"),
                "target": edge.get("target_id"),
                "similarity": edge.get("similarity", 0),
                "disparity": edge.get("price_disparity", 0),
            }
        )

    # Generate clusters for L0 view
    cluster_data = []
    for cluster in clusters:
        c_nodes = [n for n in nodes if n.get("id") in cluster.get("event_ids", [])]
        kalshi_count = sum(1 for n in c_nodes if n.get("source") == "kalshi")
        poly_count = len(c_nodes) - kalshi_count
        cluster_data.append(
            {
                "id": cluster.get("id"),
                "label": cluster.get("label", f"Cluster {cluster.get('id')}"),
                "count": len(c_nodes),
                "kalshi": kalshi_count,
                "polymarket": poly_count,
            }
        )

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, monospace;
            background: {bg_color};
            color: {text_color};
            overflow: hidden;
        }}
        #container {{
            width: 100vw;
            height: 100vh;
            position: relative;
        }}
        #controls {{
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 100;
            background: {tooltip_bg};
            padding: 15px;
            border-radius: 8px;
            border: 1px solid {grid_color};
            font-size: 12px;
        }}
        #controls label {{
            display: block;
            margin-bottom: 5px;
            cursor: pointer;
        }}
        #controls input {{
            margin-right: 5px;
        }}
        #stats {{
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 100;
            background: {tooltip_bg};
            padding: 10px 15px;
            border-radius: 8px;
            border: 1px solid {grid_color};
            font-size: 11px;
        }}
        #tooltip {{
            position: absolute;
            padding: 10px;
            background: {tooltip_bg};
            border: 1px solid {grid_color};
            border-radius: 4px;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s;
            font-size: 11px;
            max-width: 300px;
            z-index: 200;
        }}
        .node circle {{
            cursor: pointer;
            stroke-width: 2px;
        }}
        .node text {{
            font-size: 10px;
            pointer-events: none;
        }}
        .link {{
            stroke-opacity: 0.6;
        }}
        .cluster-bubble {{
            cursor: pointer;
            stroke-width: 2px;
        }}
        .cluster-label {{
            font-size: 11px;
            font-weight: bold;
            pointer-events: none;
            text-anchor: middle;
        }}
        .legend {{
            position: absolute;
            bottom: 10px;
            left: 10px;
            z-index: 100;
            background: {tooltip_bg};
            padding: 10px 15px;
            border-radius: 8px;
            border: 1px solid {grid_color};
            font-size: 11px;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            margin: 5px 0;
        }}
        .legend-color {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }}
        #back-btn {{
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 100;
            background: {tooltip_bg};
            padding: 8px 16px;
            border-radius: 4px;
            border: 1px solid {grid_color};
            cursor: pointer;
            display: none;
            font-size: 12px;
        }}
        #back-btn:hover {{
            background: {grid_color};
        }}
    </style>
</head>
<body>
    <div id="container">
        <div id="controls">
            <label><strong>View Mode</strong></label>
            <label><input type="radio" name="view" value="clusters" checked> Clusters</label>
            <label><input type="radio" name="view" value="events"> Events</label>
            <label style="margin-top: 10px;"><strong>Filters</strong></label>
            <label><input type="checkbox" id="filter-arb" checked> Show arbitrages only</label>
            <label style="margin-top: 10px;"><strong>Search</strong></label>
            <input type="text" id="search" placeholder="Filter events..." style="width: 100%; padding: 4px; margin-top: 5px;">
        </div>
        <div id="stats">
            Nodes: {len(nodes)} | Edges: {len(edges)} | Clusters: {len(clusters)}
        </div>
        <button id="back-btn">← Back to Clusters</button>
        <div id="tooltip"></div>
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color" style="background: {kalshi_color};"></div>
                <span>Kalshi</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: {poly_color};"></div>
                <span>Polymarket</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: {edge_color};"></div>
                <span>Arbitrage Edge</span>
            </div>
        </div>
    </div>

    <script>
        const width = {width};
        const height = {height};
        const kalshiColor = "{kalshi_color}";
        const polyColor = "{poly_color}";
        const edgeColor = "{edge_color}";
        const bgColor = "{bg_color}";
        const textColor = "{text_color}";

        const nodes = {json.dumps(d3_nodes)};
        const links = {json.dumps(d3_edges)};
        const clusters = {json.dumps(cluster_data)};

        let currentView = 'clusters';
        let expandedCluster = null;
        let simulation = null;

        const svg = d3.select("#container")
            .append("svg")
            .attr("width", "100%")
            .attr("height", "100%")
            .attr("viewBox", [0, 0, width, height]);

        // Add grid pattern
        const defs = svg.append("defs");
        const pattern = defs.append("pattern")
            .attr("id", "grid")
            .attr("width", 40)
            .attr("height", 40)
            .attr("patternUnits", "userSpaceOnUse");

        pattern.append("path")
            .attr("d", "M 40 0 L 0 0 0 40")
            .attr("fill", "none")
            .attr("stroke", "{grid_color}")
            .attr("stroke-width", 0.5);

        svg.append("rect")
            .attr("width", width)
            .attr("height", height)
            .attr("fill", "url(#grid)");

        const g = svg.append("g");

        // Zoom
        const zoom = d3.zoom()
            .scaleExtent([0.1, 5])
            .on("zoom", (e) => g.attr("transform", e.transform));

        svg.call(zoom);

        // Tooltip
        const tooltip = d3.select("#tooltip");

        function showTooltip(event, html) {{
            tooltip.html(html)
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 10) + "px")
                .style("opacity", 1);
        }}

        function hideTooltip() {{
            tooltip.style("opacity", 0);
        }}

        // Color scale for nodes
        function getNodeColor(d) {{
            return d.source === 'kalshi' ? kalshiColor : polyColor;
        }}

        // Cluster view (L0)
        function drawClusters() {{
            g.selectAll("*").remove();

            // Build cluster nodes
            const clusterNodes = clusters.map(c => ({{
                ...c,
                radius: Math.max(30, Math.min(80, 10 + Math.sqrt(c.count) * 3))
            }}));

            // Aggregate edges between clusters
            const clusterEdges = [];
            const edgeMap = new Map();

            links.forEach(link => {{
                const sourceCluster = nodes.find(n => n.id === link.source)?.cluster;
                const targetCluster = nodes.find(n => n.id === link.target)?.cluster;

                if (sourceCluster && targetCluster && sourceCluster !== targetCluster) {{
                    const key = [Math.min(sourceCluster, targetCluster), Math.max(sourceCluster, targetCluster)].join("-");
                    if (!edgeMap.has(key)) {{
                        edgeMap.set(key, {{ source: sourceCluster, target: targetCluster, count: 0, maxSim: 0, maxDisp: 0 }});
                    }}
                    const edge = edgeMap.get(key);
                    edge.count++;
                    edge.maxSim = Math.max(edge.maxSim, link.similarity);
                    edge.maxDisp = Math.max(edge.maxDisp, link.disparity);
                }}
            }});

            edgeMap.forEach(v => clusterEdges.push(v));

            // Simulation
            simulation = d3.forceSimulation(clusterNodes)
                .force("link", d3.forceLink(clusterEdges).id(d => d.id).distance(200))
                .force("charge", d3.forceManyBody().strength(-500))
                .force("center", d3.forceCenter(width/2, height/2))
                .force("collision", d3.forceCollide().radius(d => d.radius + 10));

            // Links
            const link = g.append("g")
                .selectAll("line")
                .data(clusterEdges)
                .join("line")
                .attr("class", "link")
                .attr("stroke", edgeColor)
                .attr("stroke-width", d => Math.min(1 + d.count * 2, 8))
                .attr("stroke-opacity", 0.6);

            // Link labels
            const linkLabel = g.append("g")
                .selectAll("text")
                .data(clusterEdges)
                .join("text")
                .attr("fill", edgeColor)
                .attr("font-size", "9px")
                .attr("text-anchor", "middle")
                .text(d => `${{d.count}} arb · ${{Math.round(d.maxSim*100)}}% sim · ${{Math.round(d.maxDisp*100)}}% disp`);

            // Nodes
            const node = g.append("g")
                .selectAll("g")
                .data(clusterNodes)
                .join("g")
                .attr("class", "cluster-bubble")
                .style("cursor", "pointer")
                .call(d3.drag()
                    .on("start", (e, d) => {{
                        if (!e.active) simulation.alphaTarget(0.3).restart();
                        d.fx = d.x; d.fy = d.y;
                    }})
                    .on("drag", (e, d) => {{
                        d.fx = e.x; d.fy = e.y;
                    }})
                    .on("end", (e, d) => {{
                        if (!e.active) simulation.alphaTarget(0);
                        d.fx = null; d.fy = null;
                    }}));

            // Circles
            node.append("circle")
                .attr("r", d => d.radius)
                .attr("fill", d => d3.interpolateRgb(polyColor, kalshiColor)(d.kalshi / d.count))
                .attr("fill-opacity", 0.15)
                .attr("stroke", d => d3.interpolateRgb(polyColor, kalshiColor)(d.kalshi / d.count))
                .attr("stroke-width", 2);

            // Labels
            node.append("text")
                .attr("class", "cluster-label")
                .attr("dy", -5)
                .attr("fill", textColor)
                .text(d => d.label.length > 20 ? d.label.slice(0, 18) + '...' : d.label);

            node.append("text")
                .attr("dy", 10)
                .attr("fill", textColor)
                .attr("opacity", 0.7)
                .attr("text-anchor", "middle")
                .attr("font-size", "9px")
                .text(d => `${{d.count}} contracts`);

            // Click to expand
            node.on("click", (e, d) => {{
                expandedCluster = d.id;
                drawEvents();
                d3.select("#back-btn").style("display", "block");
            }});

            // Tick
            simulation.on("tick", () => {{
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                linkLabel
                    .attr("x", d => (d.source.x + d.target.x) / 2)
                    .attr("y", d => (d.source.y + d.target.y) / 2);

                node.attr("transform", d => `translate(${{d.x}},${{d.y}})`);
            }});
        }}

        // Event view (L1)
        function drawEvents() {{
            g.selectAll("*").remove();

            let filteredNodes = nodes;
            let filteredLinks = links;

            // Filter by cluster if expanded
            if (expandedCluster !== null) {{
                const clusterEvents = nodes.filter(n => n.cluster === expandedCluster);
                const clusterIds = new Set(clusterEvents.map(n => n.id));
                filteredNodes = clusterEvents;
                filteredLinks = links.filter(l =>
                    clusterIds.has(l.source) && clusterIds.has(l.target)
                );
            }}

            // Apply arbitrage filter
            if (d3.select("#filter-arb").property("checked")) {{
                const linkedIds = new Set();
                filteredLinks.forEach(l => {{
                    linkedIds.add(typeof l.source === 'string' ? l.source : l.source.id);
                    linkedIds.add(typeof l.target === 'string' ? l.target : l.target.id);
                }});
                filteredNodes = filteredNodes.filter(n => linkedIds.has(n.id));
            }}

            // Apply search filter
            const searchTerm = d3.select("#search").property("value").toLowerCase();
            if (searchTerm) {{
                filteredNodes = filteredNodes.filter(n =>
                    n.title.toLowerCase().includes(searchTerm) ||
                    n.ticker.toLowerCase().includes(searchTerm)
                );
                const filteredIds = new Set(filteredNodes.map(n => n.id));
                filteredLinks = filteredLinks.filter(l => {{
                    const sid = typeof l.source === 'string' ? l.source : l.source.id;
                    const tid = typeof l.target === 'string' ? l.target : l.target.id;
                    return filteredIds.has(sid) && filteredIds.has(tid);
                }});
            }}

            if (filteredNodes.length === 0) {{
                g.append("text")
                    .attr("x", width/2)
                    .attr("y", height/2)
                    .attr("text-anchor", "middle")
                    .attr("fill", textColor)
                    .attr("opacity", 0.5)
                    .text("No events match current filters");
                return;
            }}

            simulation = d3.forceSimulation(filteredNodes)
                .force("link", d3.forceLink(filteredLinks).id(d => d.id).distance(100))
                .force("charge", d3.forceManyBody().strength(-50))
                .force("center", d3.forceCenter(width/2, height/2))
                .force("collision", d3.forceCollide().radius(8));

            // Links
            const link = g.append("g")
                .selectAll("line")
                .data(filteredLinks)
                .join("line")
                .attr("class", "link")
                .attr("stroke", edgeColor)
                .attr("stroke-width", d => 1 + d.disparity * 5)
                .attr("stroke-opacity", 0.7);

            // Link labels
            const linkLabel = g.append("g")
                .selectAll("text")
                .data(filteredLinks)
                .join("text")
                .attr("fill", edgeColor)
                .attr("font-size", "8px")
                .attr("text-anchor", "middle")
                .text(d => `${{Math.round(d.similarity*100)}}% sim · ${{Math.round(d.disparity*100,1)}}% disp`);

            // Nodes
            const node = g.append("g")
                .selectAll("g")
                .data(filteredNodes)
                .join("g")
                .attr("class", "node")
                .style("cursor", "pointer")
                .call(d3.drag()
                    .on("start", (e, d) => {{
                        if (!e.active) simulation.alphaTarget(0.3).restart();
                        d.fx = d.x; d.fy = d.y;
                    }})
                    .on("drag", (e, d) => {{
                        d.fx = e.x; d.fy = e.y;
                    }})
                    .on("end", (e, d) => {{
                        if (!e.active) simulation.alphaTarget(0);
                        d.fx = null; d.fy = null;
                    }}));

            node.append("circle")
                .attr("r", 6)
                .attr("fill", getNodeColor)
                .attr("fill-opacity", 0.8);

            // Hover effects
            node.on("mouseenter", (e, d) => {{
                const html = `
                    <strong>${{d.title.slice(0, 50)}}${{d.title.length > 50 ? '...' : ''}}</strong><br>
                    ${{d.source}} · YES ${{Math.round(d.yes_price*100)}}¢ / NO ${{Math.round(d.no_price*100)}}¢<br>
                    <a href="${{d.market_url}}" target="_blank" style="color: ${{getNodeColor(d)}};">Open Market →</a>
                `;
                showTooltip(e, html);
            }}).on("mouseleave", hideTooltip);

            // Click to open
            node.on("click", (e, d) => {{
                if (d.market_url) window.open(d.market_url, '_blank');
            }});

            // Tick
            simulation.on("tick", () => {{
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                linkLabel
                    .attr("x", d => (d.source.x + d.target.x) / 2)
                    .attr("y", d => (d.source.y + d.target.y) / 2);

                node.attr("transform", d => `translate(${{d.x}},${{d.y}})`);
            }});
        }}

        // View controls
        d3.selectAll("input[name='view']").on("change", function() {{
            currentView = this.value;
            if (currentView === 'clusters') {{
                drawClusters();
            }} else {{
                drawEvents();
            }}
        }});

        d3.select("#filter-arb").on("change", () => {{
            if (currentView === 'events') drawEvents();
        }});

        d3.select("#search").on("input", () => {{
            if (currentView === 'events') drawEvents();
        }});

        d3.select("#back-btn").on("click", () => {{
            expandedCluster = null;
            drawClusters();
            d3.select("#back-btn").style("display", "none");
        }});

        // Initial draw
        drawClusters();
    </script>
</body>
</html>
"""
    return html


def generate_static_image(
    data: dict,
    output_path: str,
    width: int = 1200,
    height: int = 800,
    theme: str = "dark",
    title: str = "Delta Arbitrage Graph",
    cluster_focus: int | None = None,
    min_disparity: float = 0.0,
) -> str:
    """Generate static PNG/SVG visualization using matplotlib/networkx."""
    try:
        import matplotlib.pyplot as plt
        import networkx as nx
    except ImportError:
        print("Error: matplotlib and networkx required for static images.", file=sys.stderr)
        print("Install: pip install matplotlib networkx", file=sys.stderr)
        sys.exit(1)

    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    clusters = data.get("clusters", [])

    # Filter by disparity
    if min_disparity > 0:
        edges = [e for e in edges if e.get("price_disparity", 0) >= min_disparity]

    # Build event to cluster mapping
    event_to_cluster: dict[str, int] = {}
    for cluster in clusters:
        for eid in cluster.get("event_ids", []):
            event_to_cluster[eid] = cluster.get("id", -1)

    # Filter by cluster focus
    if cluster_focus is not None:
        cluster = next((c for c in clusters if c.get("id") == cluster_focus), None)
        if cluster:
            cluster_event_ids = set(cluster.get("event_ids", []))
            nodes = [n for n in nodes if n.get("id") in cluster_event_ids]
            node_ids = {n.get("id") for n in nodes}
            edges = [
                e
                for e in edges
                if e.get("source_id") in node_ids and e.get("target_id") in node_ids
            ]

    # Theme colors
    if theme == "dark":
        bg_color = "#0d1117"
        text_color = "#c8d4e0"
        kalshi_color = "#38bdf8"
        poly_color = "#a78bfa"
        edge_color = "#ef4444"
    else:
        bg_color = "#ffffff"
        text_color = "#1f2937"
        kalshi_color = "#2563eb"
        poly_color = "#7c3aed"
        edge_color = "#dc2626"

    # Create figure
    fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    # Build network
    G = nx.Graph()

    # Add nodes
    for node in nodes:
        G.add_node(
            node.get("id"),
            source=node.get("source"),
            title=node.get("title", "")[:30],
            color=kalshi_color if node.get("source") == "kalshi" else poly_color,
        )

    # Add edges
    for edge in edges:
        G.add_edge(
            edge.get("source_id"),
            edge.get("target_id"),
            weight=edge.get("similarity", 0.5),
        )

    # Layout
    pos = nx.spring_layout(G, k=2, iterations=50)

    # Draw
    node_colors = [G.nodes[n].get("color", "#888888") for n in G.nodes()]
    edge_widths = [G[u][v].get("weight", 0.5) * 3 for u, v in G.edges()]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=100, alpha=0.8, ax=ax)
    nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_color, alpha=0.5, ax=ax)

    ax.set_title(title, color=text_color, fontsize=14, pad=20)
    ax.axis("off")

    # Legend
    from matplotlib.patches import Patch

    legend_elements = [
        Patch(facecolor=kalshi_color, label="Kalshi"),
        Patch(facecolor=poly_color, label="Polymarket"),
        Patch(facecolor=edge_color, label="Arbitrage Edge"),
    ]
    ax.legend(
        handles=legend_elements,
        loc="upper right",
        facecolor=bg_color,
        edgecolor=text_color,
        labelcolor=text_color,
    )

    plt.tight_layout()

    # Save
    ext = Path(output_path).suffix.lower()
    if ext == ".svg":
        plt.savefig(output_path, format="svg", facecolor=bg_color, edgecolor="none")
    else:
        plt.savefig(output_path, format="png", facecolor=bg_color, edgecolor="none")

    plt.close()
    return output_path


def generate_mermaid(data: dict, min_disparity: float = 0.05) -> str:
    """Generate Mermaid diagram syntax."""
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    clusters = data.get("clusters", [])

    # Filter edges
    if min_disparity > 0:
        edges = [e for e in edges if e.get("price_disparity", 0) >= min_disparity]

    lines = ["```mermaid", "graph LR"]

    # Add cluster subgraphs
    for cluster in clusters[:10]:  # Limit to first 10 clusters
        cluster_id = cluster.get("id", 0)
        label = cluster.get("label", f"Cluster {cluster_id}")
        event_ids = cluster.get("event_ids", [])[:5]  # Limit to 5 events per cluster

        lines.append(f"    subgraph cluster_{cluster_id} [{label}]")
        for eid in event_ids:
            node = next((n for n in nodes if n.get("id") == eid), None)
            if node:
                short_id = eid[:8]
                title = node.get("title", "")[:20]
                lines.append(f"        {short_id}[{title}...]")
        lines.append("    end")

    # Add arbitrage edges
    for edge in edges[:20]:  # Limit to 20 edges
        source_id = edge.get("source_id", "")[:8]
        target_id = edge.get("target_id", "")[:8]
        disparity = edge.get("price_disparity", 0) * 100
        lines.append(f'    {source_id} -->|"{disparity:.1f}%"| {target_id}')

    lines.append("```")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate visualizations from Delta arbitrage data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --output-format d3 --output-dir ./dashboard
  %(prog)s --output-format static --width 1920 --height 1080
  %(prog)s --output-format mermaid > diagram.md
        """,
    )

    parser.add_argument(
        "--output-format",
        choices=["d3", "static", "mermaid", "json"],
        default="d3",
        help="Visualization type (default: d3)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./viz",
        help="Output directory (default: ./viz)",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        help="Output file path (overrides --output-dir naming)",
    )
    parser.add_argument(
        "--cluster-focus",
        type=int,
        help="Focus on specific cluster ID",
    )
    parser.add_argument(
        "--min-disparity",
        type=float,
        default=0.0,
        help="Minimum disparity for edges (default: 0)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1200,
        help="Canvas width (default: 1200)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=800,
        help="Canvas height (default: 800)",
    )
    parser.add_argument(
        "--theme",
        choices=["dark", "light"],
        default="dark",
        help="Color theme (default: dark)",
    )
    parser.add_argument(
        "--title",
        type=str,
        default="Delta Arbitrage Graph",
        help="Chart title",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Don't auto-open browser (for D3)",
    )
    parser.add_argument(
        "--graph-path",
        type=str,
        help="Path to graph.json",
    )

    args = parser.parse_args()

    # Load data
    data = load_graph_data(args.graph_path)

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate visualization
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if args.output_format == "d3":
        output_path = args.output_file or output_dir / f"delta_viz_{timestamp}.html"
        html = generate_d3_html(
            data,
            width=args.width,
            height=args.height,
            theme=args.theme,
            title=args.title,
            cluster_focus=args.cluster_focus,
            min_disparity=args.min_disparity,
        )
        with open(output_path, "w") as f:
            f.write(html)
        print(f"Generated D3 visualization: {output_path}")

        if not args.no_browser:
            webbrowser.open(f"file://{Path(output_path).absolute()}")

    elif args.output_format == "static":
        output_path = args.output_file or output_dir / f"delta_viz_{timestamp}.png"
        generate_static_image(
            data,
            str(output_path),
            width=args.width,
            height=args.height,
            theme=args.theme,
            title=args.title,
            cluster_focus=args.cluster_focus,
            min_disparity=args.min_disparity,
        )
        print(f"Generated static image: {output_path}")

    elif args.output_format == "mermaid":
        mermaid = generate_mermaid(data, min_disparity=args.min_disparity)
        if args.output_file:
            with open(args.output_file, "w") as f:
                f.write(mermaid)
            print(f"Generated Mermaid diagram: {args.output_file}")
        else:
            print(mermaid)

    elif args.output_format == "json":
        output_path = args.output_file or output_dir / f"delta_data_{timestamp}.json"
        with open(output_path, "w") as f:
            json.dump(data, indent=2, fp=f)
        print(f"Exported JSON data: {output_path}")


if __name__ == "__main__":
    main()
