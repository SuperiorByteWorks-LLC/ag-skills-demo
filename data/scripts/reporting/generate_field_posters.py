#!/usr/bin/env python3
"""Generate large-format composable field posters."""

from __future__ import annotations

import sys
from pathlib import Path

import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.use("Agg")

_REPO = Path(__file__).resolve().parents[3]
_SKILLS = _REPO / ".opencode" / "skills"

sys.path.insert(0, str(_SKILLS / "farm-intelligence-reporting" / "src"))
sys.path.insert(0, str(_SKILLS / "headlands-ring" / "src"))
sys.path.insert(0, str(_SKILLS / "ssurgo-soil" / "src"))
sys.path.insert(0, str(_SKILLS / "cdl-cropland" / "src"))
sys.path.insert(0, str(_SKILLS / "nasa-power-weather" / "src"))

from headlands_ring import split_headlands_and_interior, summarize_headlands
from pipeline import (
    STEP_FIELD_POSTER_RENDER,
    FieldReportingConfig,
    build_step_manifest,
    load_manifest,
    step_is_stale,
)
from reporting import (
    build_field_reporting_dataset,
    compute_management_implications,
    compute_farm_relative_rankings,
)
from cdl_reporting import plot_crop_mix_stacked_100, summarize_crop_history
from weather_reporting import (
    summarize_weather_variability,
    plot_gdd_doy_overlay,
    plot_precip_boxplot,
    plot_temperature_doy_overlay,
)
from ssurgo_workflows import (
    plot_headlands_om_overlay,
    plot_soil_profile_depth,
    plot_ssurgo_component_map,
    plot_ssurgo_property_choropleth,
    render_soil_horizon_table,
)

_SCRIPT = Path(__file__)
_UTM_WEST = "EPSG:32615"
_UTM_EAST = "EPSG:32616"

PROP_MAPS = [
    ("om_r", "Organic matter (%)"),
    ("ph1to1h2o_r", "Soil pH"),
    ("awc_r", "Plant-available water (cm/cm)"),
    ("claytotal_r", "Clay (%)"),
]


def _utm(field_row) -> str:
    return _UTM_WEST if field_row.geometry.centroid.x < -90 else _UTM_EAST


def _field_identity_card(ax, field_row, hl_summary, crop_summary, wx_row):
    ax.axis("off")
    fid = str(field_row["field_id"])
    acres = float(field_row.get("area_acres", 0))
    cx = float(field_row.geometry.centroid.x)
    cy = float(field_row.geometry.centroid.y)
    hp = float(hl_summary.get("headlands_pct", 0))
    ha = float(hl_summary.get("headlands_area_acres", 0))
    lines = [
        f"Field:    {fid}",
        f"Area:     {acres:.1f} acres",
        f"Location: {cy:.4f} N  {abs(cx):.4f} W",
        f"Headlands:{ha:.2f} ac  ({hp:.1f}% of field)",
    ]
    if crop_summary is not None and not crop_summary.empty:
        r = crop_summary.iloc[0]
        lines += [
            f"Rotation: {r.get('rotation_sequence', 'N/A')}",
            f"Diversity:{r.get('crop_diversity', '?')} type(s)  "
            f"Corn {r.get('corn_years', 0)} yr  Soy {r.get('soybean_years', 0)} yr",
        ]
    if wx_row:
        lines += [
            f"Avg temp: {wx_row.get('avg_temp_c', float('nan')):.1f} C",
            f"Avg precip:{wx_row.get('annual_precip_mm', float('nan')):.0f} mm/yr",
        ]
    ax.text(
        0.05,
        0.95,
        "\n".join(lines),
        va="top",
        fontsize=9.5,
        transform=ax.transAxes,
        fontfamily="monospace",
        bbox=dict(
            boxstyle="round,pad=0.5", facecolor="#f0f9ff", edgecolor="#2563eb", linewidth=1.2
        ),
    )
    ax.set_title("Field identity and operations", fontsize=11, fontweight="bold", loc="left")


def _management_card(ax, row_dict, field_reporting_df, field_id):
    ax.axis("off")
    merged = dict(row_dict)
    if field_reporting_df is not None and not field_reporting_df.empty:
        match = field_reporting_df[field_reporting_df["field_id"] == field_id]
        if not match.empty:
            merged.update({k: v for k, v in match.iloc[0].to_dict().items() if v is not None})
    bullets = compute_management_implications(merged)
    text = "\n".join(f"• {b}" for b in bullets)
    ax.text(
        0.03,
        0.96,
        text,
        va="top",
        ha="left",
        fontsize=8.5,
        transform=ax.transAxes,
        bbox=dict(
            boxstyle="round,pad=0.5", facecolor="#fefce8", edgecolor="#ca8a04", linewidth=1.0
        ),
    )
    ax.set_title("Management implications", fontsize=11, fontweight="bold", loc="left")


def _ranking_card(ax, field_reporting_df, field_id):
    ax.axis("off")
    if field_reporting_df is None or field_reporting_df.empty:
        ax.text(0.5, 0.5, "Farm rankings unavailable", ha="center", va="center")
        return
    row = field_reporting_df[field_reporting_df["field_id"] == field_id]
    if row.empty:
        return
    r = row.iloc[0]
    rank_cols = [c for c in r.index if c.endswith("_pct_rank")][:8]
    if not rank_cols:
        ax.text(0.5, 0.5, "No ranking data", ha="center", va="center")
        return
    labels = [c.replace("_pct_rank", "").replace("_", " ") for c in rank_cols]
    values = [float(r[c]) if pd.notna(r[c]) else 50.0 for c in rank_cols]
    y_pos = np.arange(len(labels))
    colors = ["#22c55e" if v >= 66 else "#f59e0b" if v >= 33 else "#ef4444" for v in values]
    ax_real = ax.inset_axes([0.05, 0.05, 0.90, 0.85])
    ax_real.barh(y_pos, values, color=colors, edgecolor="white", height=0.6)
    ax_real.set_yticks(y_pos)
    ax_real.set_yticklabels(labels, fontsize=8)
    ax_real.set_xlim(0, 100)
    ax_real.set_xlabel("Farm percentile", fontsize=8)
    ax_real.axvline(50, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
    ax_real.grid(True, axis="x", alpha=0.25)
    ax.set_title("Farm-relative standing", fontsize=11, fontweight="bold", loc="left")


def _render_field_poster(
    field_id, field_gdf, ssurgo_wgs84, detail_df, weather, cdl, field_reporting_df, output_path
):
    field_row = field_gdf.iloc[0]
    field_wgs84 = field_gdf.to_crs("EPSG:4326")
    field_utm = field_gdf.to_crs(_utm(field_row))
    ring_utm, _ = split_headlands_and_interior(field_utm, width_m=9.0)
    hl = summarize_headlands(field_utm, ring_utm).iloc[0].to_dict()

    fw = weather[weather["field_id"] == field_id].copy()
    fw["date"] = pd.to_datetime(fw["date"])
    fc = cdl[cdl["field_id"] == field_id].copy()
    crop_sum = summarize_crop_history(fc)
    wx_row = None
    if not fw.empty:
        ws = summarize_weather_variability(fw)
        if not ws.empty:
            wx_row = ws.iloc[0].to_dict()

    merged_row = field_row.to_dict()
    if field_reporting_df is not None and not field_reporting_df.empty:
        match = field_reporting_df[field_reporting_df["field_id"] == field_id]
        if not match.empty:
            merged_row.update(match.iloc[0].to_dict())

    fig = plt.figure(figsize=(28, 36))
    fig.patch.set_facecolor("#fafaf9")
    fig.suptitle(
        f"Field Intelligence Report — {field_id[-8:]}  ·  {float(field_row.get('area_acres', 0)):.1f} ac  ·  Iowa Corn Belt",
        fontsize=16,
        fontweight="bold",
        y=0.993,
        color="#1e293b",
        fontfamily="serif",
    )
    gs = fig.add_gridspec(
        6, 4, hspace=0.42, wspace=0.28, left=0.04, right=0.97, top=0.975, bottom=0.015
    )

    _field_identity_card(fig.add_subplot(gs[0, 0]), field_row, hl, crop_sum, wx_row)
    plot_ssurgo_component_map(
        fig.add_subplot(gs[0, 1]), field_wgs84, ssurgo_wgs84, "Soil components (SSURGO)"
    )
    plot_headlands_om_overlay(fig.add_subplot(gs[0, 2:]), field_utm, ring_utm, ssurgo_wgs84)

    for i, (prop, label) in enumerate(PROP_MAPS):
        plot_ssurgo_property_choropleth(
            fig.add_subplot(gs[1, i]), field_wgs84, ssurgo_wgs84, prop, label
        )

    plot_soil_profile_depth(fig.add_subplot(gs[2, 0]), detail_df, field_id)
    render_soil_horizon_table(fig.add_subplot(gs[2, 1:]), detail_df)

    plot_temperature_doy_overlay(fig.add_subplot(gs[3, 0]), fw)
    plot_gdd_doy_overlay(fig.add_subplot(gs[3, 1]), fw)
    plot_precip_boxplot(fig.add_subplot(gs[3, 2:]), fw)

    plot_crop_mix_stacked_100(fig.add_subplot(gs[4, 0:2]), fc, title="CDL crop composition by year")

    for _i, sensor in enumerate(["Sentinel-2 NDVI", "Landsat NDVI"]):
        ax_rs = fig.add_subplot(gs[4, 2 + _i])
        ax_rs.axis("off")
        ax_rs.set_title(sensor, fontsize=11, fontweight="bold", loc="left")
        ax_rs.text(
            0.5,
            0.5,
            "Run imagery download step\nto populate this panel",
            ha="center",
            va="center",
            fontsize=8.5,
            color="#9ca3af",
            transform=ax_rs.transAxes,
        )

    _management_card(fig.add_subplot(gs[5, 0:2]), merged_row, field_reporting_df, field_id)
    _ranking_card(fig.add_subplot(gs[5, 2:]), field_reporting_df, field_id)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main() -> None:
    print("=" * 60)
    print("Field posters — large-format composable")
    print("=" * 60)

    config = FieldReportingConfig(
        farm_name="Iowa Demo Farm",
        field_boundary_path="data/field-boundaries/iowa_10_fields.geojson",
    )
    manifest_dir = Path(config.reporting_dir) / "manifests"
    output_dir = Path("data/EDA/field_cards")
    output_dir.mkdir(parents=True, exist_ok=True)

    fields = gpd.read_file(config.field_boundary_path)
    soil_full = pd.read_csv("data/soil/iowa_full_ssurgo.csv")
    soil_summary = pd.read_csv("data/soil/iowa_ssurgo_summary.csv")
    weather = pd.read_csv("data/weather/iowa_weather_2021_2025.csv", parse_dates=["date"])
    cdl_path = "data/cdl/iowa_cdl_2021_2024.csv"
    cdl = pd.read_csv(cdl_path)

    hl_rows = []
    for idx, frow in fields.iterrows():
        fgdf = fields.iloc[[idx]].to_crs(_utm(frow))
        ring, _ = split_headlands_and_interior(fgdf, width_m=9.0)
        s = summarize_headlands(fgdf, ring).iloc[0].to_dict()
        s["field_id"] = frow["field_id"]
        hl_rows.append(s)
    headlands_df = pd.DataFrame(hl_rows)

    wx_summary = summarize_weather_variability(weather)
    crop_sum = summarize_crop_history(cdl)

    field_reporting_df = build_field_reporting_dataset(
        fields,
        headlands_summary=headlands_df,
        soil_summary=soil_summary,
        weather_summary=wx_summary,
        cdl_summary=crop_sum,
    )

    for idx, frow in fields.iterrows():
        field_id = frow["field_id"]
        output_path = output_dir / f"iowa_field_report_{idx + 1:02d}.png"
        prior = load_manifest(manifest_dir / f"{STEP_FIELD_POSTER_RENDER}_{field_id}.json")

        # Check for cached SSURGO polygons
        cache_path = _REPO / "data" / "soil" / "cache" / f"{field_id}_polygons.geojson"
        input_paths = [
            config.field_boundary_path,
            "data/soil/iowa_full_ssurgo.csv",
            "data/weather/iowa_weather_2021_2025.csv",
            cdl_path,
        ]
        if cache_path.exists():
            input_paths.append(str(cache_path))

        manifest = build_step_manifest(
            step_name=f"{STEP_FIELD_POSTER_RENDER}_{field_id}",
            input_paths=input_paths,
            output_paths=[output_path],
            code_paths=[_SCRIPT],
            config=config,
        )
        if not step_is_stale(manifest, prior):
            print(f"skip  {field_id}")
            continue
        print(f"run   {field_id}")
        field_gdf = fields.iloc[[idx]].copy()
        detail_df = (
            soil_full[soil_full["field_id"] == field_id].copy()
            if "field_id" in soil_full.columns
            else pd.DataFrame()
        )

        # Load SSURGO polygons if available
        ssurgo_gdf = gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
        if cache_path.exists():
            try:
                ssurgo_gdf = gpd.read_file(cache_path)
                # Merge with soil data for component names
                if not detail_df.empty and "mukey" in detail_df.columns:
                    soil_agg = (
                        detail_df.groupby("mukey")
                        .agg(
                            {
                                "compname": "first",
                                "comppct_r": "first",
                                "drainagecl": "first",
                            }
                        )
                        .reset_index()
                    )
                    soil_agg["mukey"] = soil_agg["mukey"].astype(str)
                    ssurgo_gdf["mukey"] = ssurgo_gdf["mukey"].astype(str)
                    ssurgo_gdf = ssurgo_gdf.merge(soil_agg, on="mukey", how="left")
                print(f"    Loaded {len(ssurgo_gdf)} SSURGO polygons")
            except Exception as e:
                print(f"    Warning: Could not load SSURGO polygons: {e}")

        _render_field_poster(
            field_id=field_id,
            field_gdf=field_gdf,
            ssurgo_wgs84=ssurgo_gdf,
            detail_df=detail_df,
            weather=weather,
            cdl=cdl,
            field_reporting_df=field_reporting_df,
            output_path=output_path,
        )
        manifest.status = "complete"
        manifest.write(manifest_dir / f"{STEP_FIELD_POSTER_RENDER}_{field_id}.json")
        print(f"   saved {output_path}")

    print(f"\n✓ Field posters complete → {output_dir}")


if __name__ == "__main__":
    main()
