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
from matplotlib.patches import Patch
from shapely import wkt

matplotlib.use("Agg")

_REPO = Path(__file__).resolve().parents[2]
_OUTPUT_DIR = _REPO / "data" / "EDA" / "soil_maps"
_CACHE_DIR = _REPO / "data" / "soil" / "cache"

SDA_URL = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest"


def download_ssurgo_polygons_for_field(field_gdf: gpd.GeoDataFrame, field_id: str) -> gpd.GeoDataFrame:
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
            records.append({
                "mukey": str(row[0]),
                "mupolygonkey": str(row[1]),
                "geometry": wkt.loads(row[2]),
                "field_id": field_id,
            })
        except Exception:
            continue
    
    if not records:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    
    return gpd.GeoDataFrame(records, crs="EPSG:4326")


def get_ssurgo_polygons_with_soil_data(field_gdf: gpd.GeoDataFrame, field_id: str) -> gpd.GeoDataFrame:
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
    
    soil_csv = _REPO / "data" / "soil" / "iowa_full_ssurgo.csv"
    if soil_csv.exists():
        soil_df = pd.read_csv(soil_csv)
        soil_agg = soil_df.groupby("mukey").agg({
            "compname": "first",
            "comppct_r": "first",
            "drainagecl": "first",
            "om_r": "mean",
            "ph1to1h2o_r": "mean",
        }).reset_index()
        soil_agg["mukey"] = soil_agg["mukey"].astype(str)
        
        polygons["mukey"] = polygons["mukey"].astype(str)
        polygons = polygons.merge(soil_agg, on="mukey", how="left")
    
    return polygons


def _add_basemap(ax, field_gdf: gpd.GeoDataFrame, zoom: int = 14):
    """Add contextily basemap to axes."""
    try:
        import contextily as ctx
        
        bounds = field_gdf.total_bounds
        margin_x = (bounds[2] - bounds[0]) * 0.1
        margin_y = (bounds[3] - bounds[1]) * 0.1
        
        ax.set_xlim(bounds[0] - margin_x, bounds[2] + margin_x)
        ax.set_ylim(bounds[1] - margin_y, bounds[3] + margin_y)
        
        ctx.add_basemap(
            ax,
            crs=field_gdf.crs,
            source=ctx.providers.CartoDB.Positron,
            alpha=0.5,
            zoom=zoom
        )
        return True
    except Exception as e:
        print(f"    Basemap error: {e}")
        return False


def render_ssurgo_field_map(
    field_gdf: gpd.GeoDataFrame,
    ssurgo_gdf: gpd.GeoDataFrame,
    output_path: Path,
    field_id: str = "",
) -> None:
    """Render layered map: basemap (50%) + SSURGO polygons (80%) + field boundary (100%)."""
    
    fig, ax = plt.subplots(figsize=(12, 10))
    fig.patch.set_facecolor("#fafaf9")
    
    if field_gdf.empty:
        ax.text(0.5, 0.5, "No field data", ha="center", va="center", transform=ax.transAxes)
        plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close(fig)
        return
    
    field_wm = field_gdf.to_crs(epsg=3857)
    
    _add_basemap(ax, field_wm, zoom=15)
    
    if not ssurgo_gdf.empty:
        ssurgo_wm = ssurgo_gdf.to_crs(epsg=3857)
        
        if "compname" in ssurgo_wm.columns:
            unique_comps = ssurgo_wm["compname"].dropna().unique()
            if len(unique_comps) > 0:
                colors = plt.cm.Set3(np.linspace(0, 1, len(unique_comps)))
                color_map = dict(zip(unique_comps, colors))
                
                for comp_name in unique_comps:
                    comp_data = ssurgo_wm[ssurgo_wm["compname"] == comp_name]
                    comp_data.plot(
                        ax=ax,
                        color=color_map[comp_name],
                        alpha=0.8,
                        edgecolor="darkgreen",
                        linewidth=0.5,
                    )
                
                handles = [Patch(facecolor=color_map[c], edgecolor="darkgreen", alpha=0.8, label=c[:25]) 
                          for c in unique_comps]
                ax.legend(handles=handles, loc="lower right", fontsize=8, title="Soil Components")
        else:
            ssurgo_wm.plot(
                ax=ax,
                color="#D2B48C",
                alpha=0.8,
                edgecolor="darkgreen",
                linewidth=0.5
            )
    
    field_wm.boundary.plot(ax=ax, color="red", linewidth=3, label="Field Boundary")
    
    centroid = field_wm.geometry.iloc[0].centroid
    ax.annotate(
        field_id[-8:] if field_id else "Field",
        (centroid.x, centroid.y),
        fontsize=12,
        fontweight="bold",
        color="red",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8, edgecolor="red")
    )
    
    ax.set_title(f"SSURGO Soil Map: {field_id[-8:] if field_id else 'Field'}", 
                 fontsize=14, fontweight="bold", pad=20)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks([])
    ax.set_yticks([])
    
    bounds = field_wm.total_bounds
    width_m = bounds[2] - bounds[0]
    scale_length_m = width_m / 5
    scale_x = bounds[0] + width_m * 0.05
    scale_y = bounds[1] + (bounds[3] - bounds[1]) * 0.05
    
    ax.plot([scale_x, scale_x + scale_length_m], [scale_y, scale_y], 
            'k-', linewidth=3, solid_capstyle='butt')
    ax.text(scale_x + scale_length_m/2, scale_y + scale_length_m*0.1, 
            f'{scale_length_m:.0f}m', ha='center', fontsize=9)
    
    arrow_x = bounds[2] - width_m * 0.08
    arrow_y = bounds[3] - (bounds[3] - bounds[1]) * 0.08
    ax.annotate('N', xy=(arrow_x, arrow_y), xytext=(arrow_x, arrow_y - width_m*0.05),
                arrowprops=dict(arrowstyle='->', color='black', lw=2),
                fontsize=14, fontweight='bold', ha='center')
    
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
    
    for idx, field_row in fields.iterrows():
        field_id = str(field_row.get("field_id", f"field_{idx}"))
        field_short = field_id[-8:] if len(field_id) > 8 else field_id
        
        print(f"\nProcessing field: {field_short}")
        
        field_single = fields.iloc[[idx]].copy()
        
        field_ssurgo = get_ssurgo_polygons_with_soil_data(field_single, field_id)
        
        output_path = _OUTPUT_DIR / f"field_{idx+1:02d}_map.png"
        render_ssurgo_field_map(field_single, field_ssurgo, output_path, field_id=field_short)
        print(f"  ✓ Map saved: {output_path.name}")
    
    print("\n" + "=" * 60)
    print(f"SSURGO soil maps complete → {_OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
