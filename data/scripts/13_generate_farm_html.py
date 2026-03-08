#!/usr/bin/env python3
"""Generate self-contained single-page HTML farm intelligence report with embedded posters."""

from __future__ import annotations

import base64
import io
import json
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use("Agg")

_REPO = Path(__file__).resolve().parents[2]
_SKILLS = _REPO / ".opencode" / "skills"

sys.path.insert(0, str(_SKILLS / "farm-intelligence-reporting" / "src"))
sys.path.insert(0, str(_SKILLS / "headlands-ring" / "src"))
sys.path.insert(0, str(_SKILLS / "cdl-cropland" / "src"))
sys.path.insert(0, str(_SKILLS / "nasa-power-weather" / "src"))

from headlands_ring import split_headlands_and_interior, summarize_headlands
from pipeline import STEP_FARM_HTML_RENDER, FieldReportingConfig, build_step_manifest, load_manifest, step_is_stale
from reporting import (
    build_field_reporting_dataset,
    build_farm_reporting_dataset,
    compute_management_implications,
    PANEL_REGISTRY,
)
from cdl_reporting import plot_crop_mix_stacked_100, summarize_crop_history
from weather_reporting import summarize_weather_variability, plot_gdd_doy_overlay, plot_precip_boxplot, plot_temperature_doy_overlay

_SCRIPT = Path(__file__)


def _utm(frow) -> str:
    return "EPSG:32615" if frow.geometry.centroid.x < -90 else "EPSG:32616"


def _fig_to_b64(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=110, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


def _img_to_b64(img_path: Path) -> str:
    """Convert image file to base64 string."""
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def _weather_b64(field_weather: pd.DataFrame) -> str:
    fig, axes = plt.subplots(1, 3, figsize=(18, 4))
    fig.patch.set_facecolor("#fafaf9")
    plot_temperature_doy_overlay(axes[0], field_weather)
    plot_gdd_doy_overlay(axes[1], field_weather)
    plot_precip_boxplot(axes[2], field_weather)
    plt.tight_layout()
    return _fig_to_b64(fig)


def _cdl_b64(field_cdl: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor("#fafaf9")
    plot_crop_mix_stacked_100(ax, field_cdl)
    plt.tight_layout()
    return _fig_to_b64(fig)


def _farm_map_b64(fields: gpd.GeoDataFrame) -> str:
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("#fafaf9")
    fields.boundary.plot(ax=ax, color="#166534", linewidth=1.5)
    centroids = fields.geometry.centroid
    sz = fields["area_acres"].fillna(30).astype(float) * 5 if "area_acres" in fields.columns else 60
    ax.scatter(centroids.x, centroids.y, s=sz, color="#2563eb", alpha=0.75, zorder=5)
    for _, r in fields.iterrows():
        c = r.geometry.centroid
        ax.annotate(str(r["field_id"])[-5:], (c.x, c.y), fontsize=7, ha="center",
                    color="white", fontweight="bold", zorder=6)
    ax.set_title("Farm field map", fontsize=12, fontweight="bold")
    ax.set_axis_off()
    plt.tight_layout()
    return _fig_to_b64(fig)


def _safe(v) -> str:
    if v is None or (not isinstance(v, str) and pd.isna(v)):
        return "—"
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


def _field_card(frow, df_row, field_weather, field_cdl, poster_b64: str, idx: int) -> str:
    fid = str(frow["field_id"])
    acres = float(frow.get("area_acres", 0))
    row_dict = df_row.to_dict() if hasattr(df_row, "to_dict") else dict(df_row)
    implications = compute_management_implications(row_dict)
    bullets_html = "".join(f"<li>{b}</li>" for b in implications)

    soil_rows = ""
    for col, label in [("avg_om_pct", "Avg OM (%)"), ("avg_ph", "Avg pH"),
                        ("total_aws_inches", "Total AWS (in)"), ("avg_cec", "Avg CEC"),
                        ("drainage_class", "Drainage class"), ("dominant_soil", "Dominant soil"),
                        ("n_components", "Soil components"), ("n_horizons", "Horizons sampled"),
                        ("headlands_pct", "Headlands (%)"), ("headlands_area_acres", "Headlands (ac)")]:
        soil_rows += f"<tr><td><b>{label}</b></td><td>{_safe(row_dict.get(col))}</td></tr>"

    wx_b64 = _weather_b64(field_weather) if not field_weather.empty else ""
    cdl_b64 = _cdl_b64(field_cdl) if not field_cdl.empty else ""
    wx_img = f'<img src="data:image/png;base64,{wx_b64}" style="width:100%" alt="Weather">' if wx_b64 else "<p>No weather data</p>"
    cdl_img = f'<img src="data:image/png;base64,{cdl_b64}" style="width:100%" alt="CDL">' if cdl_b64 else "<p>No CDL data</p>"

    rank_html = ""
    rank_cols = sorted([k for k in row_dict if k.endswith("_pct_rank")])
    if rank_cols:
        rank_html = "<table class='data-table'><tbody>"
        for k in rank_cols[:8]:
            base = k.replace("_pct_rank", "").replace("_", " ")
            v = row_dict.get(k)
            pct = float(v) if v is not None and not (isinstance(v, float) and pd.isna(v)) else 50.0
            color = "#22c55e" if pct >= 66 else "#f59e0b" if pct >= 33 else "#ef4444"
            bar = f'<span style="display:inline-block;width:{pct:.0f}%;height:10px;background:{color};border-radius:3px"></span>'
            rank_html += f"<tr><td><b>{base}</b></td><td>{bar} {pct:.0f}th pctile</td></tr>"
        rank_html += "</tbody></table>"

    clean_dict = {k: _safe(v) for k, v in row_dict.items() if not k.endswith("_pct_rank")}

    return f"""
<section class="field-card" id="field-{fid[-6:]}">
  <h2>Field {fid[-8:]} <span class="badge">{acres:.1f} ac</span></h2>
  
  <div class="poster-preview">
    <h3>Field Poster</h3>
    <a href="#poster-modal-{idx}" class="poster-thumb">
      <img src="data:image/png;base64,{poster_b64}" style="max-width:300px;border:2px solid #2563eb;border-radius:8px;cursor:pointer;" alt="Field poster thumbnail">
      <p style="font-size:0.85rem;color:#2563eb;margin-top:0.5rem;">Click to view full poster</p>
    </a>
  </div>
  
  <div class="grid-2">
    <div>
      <h3>Soil and operations summary</h3>
      <table class="data-table"><tbody>{soil_rows}</tbody></table>
    </div>
    <div>
      <h3>Management implications</h3>
      <ul class="implications">{bullets_html}</ul>
    </div>
  </div>
  <details open><summary><strong>Weather context (temperature, GDD, precipitation)</strong></summary>
    {wx_img}
  </details><hr>
  <details open><summary><strong>Crop history (CDL composition by year)</strong></summary>
    {cdl_img}
  </details><hr>
  <details><summary><strong>Farm-relative standing</strong></summary>
    {rank_html if rank_html else "<p>No ranking data available</p>"}
  </details><hr>
  <details><summary><strong>Remote sensing NDVI</strong></summary>
    <p class="note">Run imagery download steps (Sentinel-2, Landsat) to populate NDVI panels.</p>
  </details><hr>
  <details><summary><strong>Full field metrics</strong></summary>
    <pre class="raw-data">{json.dumps(clean_dict, indent=2)}</pre>
  </details>
</section>

<div id="poster-modal-{idx}" class="modal">
  <div class="modal-content">
    <a href="#" class="modal-close">&times; Close</a>
    <h2>Field {fid[-8:]} Poster</h2>
    <img src="data:image/png;base64,{poster_b64}" style="width:100%;max-width:1200px;" alt="Full field poster">
  </div>
</div>
"""


def main() -> None:
    print("=" * 60)
    print("Farm HTML report — self-contained with embedded posters")
    print("=" * 60)

    config = FieldReportingConfig(
        farm_name="Iowa Demo Farm",
        field_boundary_path="data/field-boundaries/iowa_10_fields.geojson",
    )
    manifest_dir = Path(config.reporting_dir) / "manifests"
    output_path = Path("data/EDA/iowa_farm_report.html")

    prior = load_manifest(manifest_dir / f"{STEP_FARM_HTML_RENDER}.json")
    manifest = build_step_manifest(
        step_name=STEP_FARM_HTML_RENDER,
        input_paths=[config.field_boundary_path, "data/soil/iowa_ssurgo_summary.csv",
                     "data/weather/iowa_weather_2021_2025.csv", "data/cdl/iowa_cdl_2021_2024.csv"],
        output_paths=[output_path],
        code_paths=[_SCRIPT],
        config=config,
    )
    if not step_is_stale(manifest, prior):
        print("skip  HTML (current)")
        return

    fields = gpd.read_file(config.field_boundary_path)
    soil_summary = pd.read_csv("data/soil/iowa_ssurgo_summary.csv")
    weather = pd.read_csv("data/weather/iowa_weather_2021_2025.csv", parse_dates=["date"])
    cdl = pd.read_csv("data/cdl/iowa_cdl_2021_2024.csv")

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

    field_df = build_field_reporting_dataset(
        fields, headlands_summary=headlands_df,
        soil_summary=soil_summary, weather_summary=wx_summary, cdl_summary=crop_sum,
    )
    farm_df = build_farm_reporting_dataset(field_df)

    total_ac = float(farm_df.iloc[0].get("total_acres", 0))
    n_fields = int(farm_df.iloc[0].get("field_count", len(fields)))

    print("  Rendering farm map and crop portfolio charts...")
    farm_map_b64 = _farm_map_b64(fields)
    farm_crop_b64 = _cdl_b64(cdl)

    print("  Loading and embedding field posters...")
    field_cards = []
    for idx, frow in fields.iterrows():
        fid = frow["field_id"]
        print(f"    Loading poster for field {fid[-6:]}...")
        poster_path = Path("data/EDA/field_cards") / f"iowa_field_poster_{idx+1:02d}.png"
        poster_b64 = _img_to_b64(poster_path) if poster_path.exists() else ""
        
        fw = weather[weather["field_id"] == fid].copy()
        fw["date"] = pd.to_datetime(fw["date"])
        fc = cdl[cdl["field_id"] == fid].copy()
        df_row_matches = field_df[field_df["field_id"] == fid]
        df_row = df_row_matches.iloc[0] if not df_row_matches.empty else pd.Series(frow)
        field_cards.append(_field_card(frow, df_row, fw, fc, poster_b64, idx))

    nav = " | ".join(f'<a href="#field-{str(r["field_id"])[-6:]}">{str(r["field_id"])[-6:]}</a>' for _, r in fields.iterrows())

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Iowa Farm Intelligence Report</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{ font-family: Georgia, serif; margin: 0; background: #f8f7f1; color: #1e293b; line-height: 1.6; }}
    header {{ padding: 2rem 2.5rem; background: linear-gradient(135deg, #e0f2fe, #fef3c7); border-bottom: 2px solid #bfdbfe; }}
    header h1 {{ margin: 0 0 0.25rem; font-size: 1.75rem; color: #1e3a5f; }}
    header p {{ margin: 0; color: #475569; }}
    .farm-overview {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; padding: 1.5rem 2.5rem; background: white; border-bottom: 1px solid #e2e8f0; }}
    .farm-overview h2 {{ grid-column: 1/-1; margin: 0 0 0.5rem; font-size: 1.3rem; color: #1e3a5f; }}
    .farm-overview img {{ width: 100%; border-radius: 8px; border: 1px solid #e2e8f0; }}
    nav.field-nav {{ padding: 0.75rem 2.5rem; background: #1e3a5f; color: white; font-size: 0.85rem; }}
    nav.field-nav a {{ color: #93c5fd; text-decoration: none; margin: 0 0.25rem; }}
    nav.field-nav a:hover {{ color: white; }}
    main {{ padding: 1.5rem 2.5rem; }}
    .field-card {{ background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; box-shadow: 0 4px 16px rgba(15,23,42,0.07); }}
    .field-card h2 {{ margin: 0 0 1rem; font-size: 1.3rem; color: #1e3a5f; border-bottom: 2px solid #bfdbfe; padding-bottom: 0.5rem; }}
    .field-card h3 {{ font-size: 1rem; margin: 0.75rem 0 0.4rem; color: #374151; }}
    .badge {{ background: #dbeafe; color: #1e40af; font-size: 0.8rem; padding: 0.15rem 0.5rem; border-radius: 999px; font-family: sans-serif; font-weight: 600; }}
    .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1rem; }}
    .data-table {{ width: 100%; border-collapse: collapse; font-size: 0.88rem; }}
    .data-table td {{ padding: 0.28rem 0.5rem; border-bottom: 1px solid #f1f5f9; }}
    .data-table tr:last-child td {{ border: none; }}
    .implications {{ margin: 0; padding-left: 1.2rem; font-size: 0.88rem; }}
    .implications li {{ margin-bottom: 0.35rem; }}
    details {{ margin: 0.75rem 0; }}
    details summary {{ cursor: pointer; font-weight: 600; padding: 0.5rem 0; color: #374151; font-family: sans-serif; font-size: 0.95rem; }}
    details summary:hover {{ color: #2563eb; }}
    details img {{ margin-top: 0.5rem; }}
    .note {{ color: #6b7280; font-style: italic; font-size: 0.88rem; }}
    .raw-data {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; font-size: 0.72rem; overflow-x: auto; max-height: 280px; overflow-y: scroll; }}
    hr {{ border: none; border-top: 1px solid #e2e8f0; margin: 0; }}
    footer {{ padding: 1.5rem 2.5rem; text-align: center; font-size: 0.8rem; color: #94a3b8; font-family: sans-serif; border-top: 1px solid #e2e8f0; }}
    
    .poster-preview {{ margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 8px; text-align: center; }}
    .poster-thumb {{ text-decoration: none; display: inline-block; }}
    .poster-thumb:hover img {{ box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }}
    
    .modal {{ display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); overflow: auto; }}
    .modal:target {{ display: block; }}
    .modal-content {{ background: white; margin: 2% auto; padding: 2rem; width: 95%; max-width: 1400px; border-radius: 12px; position: relative; }}
    .modal-close {{ position: absolute; top: 1rem; right: 1rem; font-size: 1.5rem; color: #64748b; text-decoration: none; background: #f1f5f9; padding: 0.5rem 1rem; border-radius: 6px; }}
    .modal-close:hover {{ color: #1e293b; background: #e2e8f0; }}
    
    @media (max-width: 768px) {{ .grid-2, .farm-overview {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <header>
    <h1>Iowa Farm Intelligence Report</h1>
    <p>{n_fields} fields &middot; {total_ac:.0f} total acres &middot; Data years 2021–2025 &middot; Soil, weather, crop history, headlands</p>
  </header>
  <div class="farm-overview">
    <h2>Farm overview</h2>
    <div>
      <img src="data:image/png;base64,{farm_map_b64}" alt="Farm field map">
    </div>
    <div>
      <h3>Farm crop portfolio</h3>
      <img src="data:image/png;base64,{farm_crop_b64}" alt="Farm CDL crop composition">
    </div>
  </div>
  <nav class="field-nav">Jump to field: {nav}</nav>
  <main>{''.join(field_cards)}</main>
  <footer>Generated by farm-intelligence-reporting &mdash; self-contained, no external dependencies required at runtime.</footer>
</body>
</html>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")

    manifest.status = "complete"
    manifest.write(manifest_dir / f"{STEP_FARM_HTML_RENDER}.json")
    print(f"✓ HTML report saved → {output_path}")
    print(f"  Size: {output_path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
