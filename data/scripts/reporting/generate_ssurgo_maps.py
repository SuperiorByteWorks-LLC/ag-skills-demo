#!/usr/bin/env python3
"""Generate SSURGO soil map overlays with basemap, soil polygons, and field boundaries.

Downloads SSURGO polygons from USDA API if not cached locally.
"""

from __future__ import annotations

import sys
from pathlib import Path

import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from shapely import wkt

matplotlib.use("Agg")

_REPO = Path(__file__).resolve().parents[3]
_OUTPUT_DIR = _REPO / "data" / "EDA" / "soil_maps"
_CACHE_DIR = _REPO / "data" / "soil" / "cache"

SDA_URL = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest"


def download_ssurgo_polygons_for_field(
    field_gdf: gpd.GeoDataFrame, field_id: str
) -> gpd.GeoDataFrame:
    """Download SSURGO polygons from USDA API for a field boundary."""
    if field_gdf.empty:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")

    field_wgs84 = field_gdf.to_crs(epsg=4326)
    field_geom = field_wgs84.geometry.iloc[0]
    field_wkt = field_geom.wkt

    mukey_sql = f"""
    SELECT DISTINCT m.mukey
    FROM mupolygon m
    WHERE m.mupolygonkey IN (
        SELECT * FROM SDA_Get_Mupolygonkey_from_intersection_with_WktWgs84('{field_wkt}')
    )
    """

    try:
        resp = requests.post(SDA_URL, data={"query": mukey_sql, "format": "JSON"}, timeout=60)
        resp.raise_for_status()
        mukey_rows = resp.json().get("Table", [])
        mukeys = [str(row[0]) for row in mukey_rows]
    except Exception as e:
        print(f"    Error querying MUKEYs: {e}")
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")

    if not mukeys:
        print(f"    No SSURGO polygons found for field")
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")

    print(f"    Found {len(mukeys)} map units")

    mukey_list = ", ".join(f"'{m}'" for m in mukeys)
    poly_sql = f"""
    SELECT m.mukey, m.mupolygonkey, m.mupolygongeo.STAsText() AS wkt
    FROM mupolygon m
    WHERE m.mukey IN ({mukey_list})
      AND m.mupolygonkey IN (
        SELECT * FROM SDA_Get_Mupolygonkey_from_intersection_with_WktWgs84('{field_wkt}')
      )
    """

    try:
        resp = requests.post(SDA_URL, data={"query": poly_sql, "format": "JSON"}, timeout=120)
        resp.raise_for_status()
        rows = resp.json().get("Table", [])
    except Exception as e:
        print(f"    Error querying polygons: {e}")
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")

    records = []
    for row in rows:
        try:
            records.append(
                {
                    "mukey": str(row[0]),
                    "mupolygonkey": str(row[1]),
                    "geometry": wkt.loads(row[2]),
                    "field_id": field_id,
                }
            )
        except Exception:
            continue

    if not records:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")

    return gpd.GeoDataFrame(records, crs="EPSG:4326")


def get_ssurgo_polygons_with_soil_data(
    field_gdf: gpd.GeoDataFrame, field_id: str
) -> gpd.GeoDataFrame:
    """Get SSURGO polygons merged with soil properties."""
    cache_path = _CACHE_DIR / f"{field_id}_polygons.geojson"

    if cache_path.exists():
        print(f"    Loading cached polygons from {cache_path}")
        polygons = gpd.read_file(cache_path)
    else:
        print(f"    Downloading SSURGO polygons from USDA API...")
        polygons = download_ssurgo_polygons_for_field(field_gdf, field_id)

        if not polygons.empty:
            _CACHE_DIR.mkdir(parents=True, exist_ok=True)
            polygons.to_file(cache_path, driver="GeoJSON")
            print(f"    Cached polygons to {cache_path}")

    if polygons.empty:
        return polygons

    try:
        target_crs = polygons.crs or field_gdf.crs or "EPSG:4326"
        clip_target = field_gdf.to_crs(target_crs)
        polygons = gpd.clip(polygons, clip_target)
        polygons = polygons[~polygons.geometry.is_empty].copy()
    except Exception as e:
        print(f"    Warning: clipping failed, using uncut polygons: {e}")

    soil_csv = _REPO / "data" / "soil" / "iowa_full_ssurgo.csv"
    if soil_csv.exists():
        soil_df = pd.read_csv(soil_csv)
        soil_agg = (
            soil_df.groupby("mukey")
            .agg(
                {
                    "compname": "first",
                    "comppct_r": "first",
                    "drainagecl": "first",
                    "om_r": "mean",
                    "ph1to1h2o_r": "mean",
                }
            )
            .reset_index()
        )
        soil_agg["mukey"] = soil_agg["mukey"].astype(str)

        polygons["mukey"] = polygons["mukey"].astype(str)
        polygons = polygons.merge(soil_agg, on="mukey", how="left")

    return gpd.GeoDataFrame(polygons, geometry="geometry", crs=polygons.crs)


def _add_basemap(ax, field_gdf: gpd.GeoDataFrame, zoom: int = 14):
    """Add contextily basemap to axes."""
    try:
        import contextily as ctx

        bounds = field_gdf.total_bounds
        margin_x = (bounds[2] - bounds[0]) * 0.2
        margin_y = (bounds[3] - bounds[1]) * 0.2

        ax.set_xlim(bounds[0] - margin_x, bounds[2] + margin_x)
        ax.set_ylim(bounds[1] - margin_y, bounds[3] + margin_y)

        esri = getattr(ctx.providers, "Esri")
        imagery = getattr(esri, "WorldImagery")
        ctx.add_basemap(ax, crs=field_gdf.crs, source=imagery)
        return True
    except Exception as e:
        print(f"    Basemap error: {e}")
        return False


def _classify_natural_breaks(
    values: pd.Series, class_count: int = 3
) -> tuple[np.ndarray, list[str]]:
    arr = values.astype(float).to_numpy()
    unique_values = np.sort(np.unique(arr))
    bins = max(1, min(class_count, unique_values.size))

    if bins == 1:
        v = float(arr[0]) if arr.size else 0.0
        return np.zeros(arr.size, dtype=int), [f"{v:.1f}"]

    if unique_values.size <= bins:
        edges = np.linspace(arr.min(), arr.max(), bins + 1)
    else:
        gaps = np.diff(unique_values)
        split_idx = np.argsort(gaps)[-(bins - 1) :]
        split_idx = np.sort(split_idx)
        mids = [(unique_values[i] + unique_values[i + 1]) / 2.0 for i in split_idx]
        edges = np.array([arr.min(), *mids, arr.max()], dtype=float)

    edges = np.unique(edges)
    if edges.size < 2:
        v = float(arr[0]) if arr.size else 0.0
        return np.zeros(arr.size, dtype=int), [f"{v:.1f}"]

    class_ids = pd.cut(arr, bins=edges, labels=False, include_lowest=True)
    class_ids = pd.Series(class_ids).fillna(0).astype(int).to_numpy()
    labels = [f"{edges[i]:.1f} to {edges[i + 1]:.1f}" for i in range(edges.size - 1)]
    class_ids = np.clip(class_ids, 0, max(0, len(labels) - 1))
    return class_ids, labels


def render_ssurgo_field_map(
    field_gdf: gpd.GeoDataFrame,
    ssurgo_gdf: gpd.GeoDataFrame,
    output_path: Path,
    field_id: str = "",
) -> None:
    """Render per-field SSURGO natural-breaks choropleth over imagery basemap."""

    fig, ax = plt.subplots(figsize=(12, 10))
    fig.patch.set_facecolor("#fafaf9")

    if field_gdf.empty:
        ax.text(0.5, 0.5, "No field data", ha="center", va="center", transform=ax.transAxes)
        plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close(fig)
        return

    field_wm = field_gdf.to_crs(epsg=3857)
    use_basemap = _add_basemap(ax, field_wm, zoom=15)

    plot_source = ssurgo_gdf.copy()
    if "mukey" in plot_source.columns:
        plot_source["mukey"] = plot_source["mukey"].astype(str)
        plot_source = plot_source.dissolve(by="mukey", as_index=False)

    choropleth_col = "om_r" if "om_r" in plot_source.columns else "comppct_r"
    choropleth_label = "Organic Matter" if choropleth_col == "om_r" else "Component Percentage"
    units = "%"

    plot_source = plot_source.dropna(subset=[choropleth_col]).copy()
    if not plot_source.empty:
        class_ids, class_labels = _classify_natural_breaks(
            pd.Series(plot_source[choropleth_col]), class_count=3
        )
        plot_source["class_id"] = class_ids
        plot_target = plot_source.to_crs(epsg=3857) if use_basemap else plot_source

        colors = plt.get_cmap("YlGn")(np.linspace(0.35, 0.85, max(1, len(class_labels))))
        legend_elements: list[object] = [
            Line2D([0], [0], color="darkgreen", linewidth=3, label="Field Boundary")
        ]

        for class_id, label in enumerate(class_labels):
            class_slice = plot_target[plot_target["class_id"] == class_id]
            if class_slice.empty:
                continue
            class_slice.plot(
                ax=ax,
                color=colors[class_id],
                alpha=0.55,
                edgecolor="darkgreen",
                linewidth=1.3,
            )
            legend_elements.append(
                Patch(
                    facecolor=colors[class_id],
                    alpha=0.55,
                    edgecolor="darkgreen",
                    label=f"{choropleth_label} {label}",
                )
            )

        ax.legend(
            handles=legend_elements,
            loc="lower right",
            fontsize=8,
            framealpha=0.9,
            title=f"{choropleth_label} ({units}) Classes",
            title_fontsize=9,
        )
    else:
        ax.text(
            0.5, 0.5, "No soil property values", transform=ax.transAxes, ha="center", va="center"
        )

    boundary_target = field_wm if use_basemap else field_gdf
    boundary_target.plot(ax=ax, color="none", edgecolor="darkgreen", linewidth=3)

    field_short = field_id[-6:] if field_id else "Field"
    mukey_count = (
        int(plot_source["mukey"].nunique())
        if not plot_source.empty and "mukey" in plot_source.columns
        else 0
    )
    ax.set_title(
        f"Field {field_short} - SSURGO {choropleth_label} (Natural Breaks)\n({mukey_count} MUKEYs)",
        fontsize=13,
    )

    if not use_basemap:
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main() -> None:
    print("=" * 60)
    print("SSURGO Soil Map Generator")
    print("=" * 60)

    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)

    fields_path = _REPO / "data" / "field-boundaries" / "iowa_10_fields.geojson"
    if not fields_path.exists():
        print(f"ERROR: Fields file not found: {fields_path}")
        sys.exit(1)

    fields = gpd.read_file(fields_path)
    print(f"Loaded {len(fields)} fields")

    for idx, field_row in enumerate(fields.itertuples(index=False), start=1):
        field_id = str(getattr(field_row, "field_id", f"field_{idx}"))
        field_short = field_id[-8:] if len(field_id) > 8 else field_id

        print(f"\nProcessing field: {field_short}")

        field_single = fields.iloc[[idx - 1]].copy()

        field_ssurgo = get_ssurgo_polygons_with_soil_data(field_single, field_id)

        output_path = _OUTPUT_DIR / f"field_{idx:02d}_map.png"
        render_ssurgo_field_map(field_single, field_ssurgo, output_path, field_id=field_short)
        print(f"  ✓ Map saved: {output_path.name}")

    print("\n" + "=" * 60)
    print(f"SSURGO soil maps complete → {_OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
