#!/usr/bin/env python3
"""Generate markdown farm intelligence report."""

from __future__ import annotations

import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd

_REPO = Path(__file__).resolve().parents[2]
_SKILLS = _REPO / ".opencode" / "skills"

sys.path.insert(0, str(_SKILLS / "farm-intelligence-reporting" / "src"))
sys.path.insert(0, str(_SKILLS / "headlands-ring" / "src"))
sys.path.insert(0, str(_SKILLS / "cdl-cropland" / "src"))
sys.path.insert(0, str(_SKILLS / "nasa-power-weather" / "src"))

from headlands_ring import split_headlands_and_interior, summarize_headlands
from pipeline import STEP_FARM_MARKDOWN, FieldReportingConfig, build_step_manifest, load_manifest, step_is_stale
from reporting import build_field_reporting_dataset, build_farm_reporting_dataset, compute_management_implications
from cdl_reporting import summarize_crop_history
from weather_reporting import summarize_weather_variability

_SCRIPT = Path(__file__)


def _utm(frow) -> str:
    return "EPSG:32615" if frow.geometry.centroid.x < -90 else "EPSG:32616"


def _safe(val) -> str:
    if val is None or (not isinstance(val, str) and pd.isna(val)):
        return "—"
    if isinstance(val, float):
        return f"{val:.2f}"
    return str(val)


def main() -> None:
    print("=" * 60)
    print("Farm Markdown Report")
    print("=" * 60)

    config = FieldReportingConfig(
        farm_name="Iowa Demo Farm",
        field_boundary_path="data/field-boundaries/iowa_10_fields.geojson",
    )
    manifest_dir = Path(config.reporting_dir) / "manifests"
    output_path = Path("data/EDA/iowa_farm_report.md")

    prior = load_manifest(manifest_dir / f"{STEP_FARM_MARKDOWN}.json")
    manifest = build_step_manifest(
        step_name=STEP_FARM_MARKDOWN,
        input_paths=[config.field_boundary_path, "data/soil/iowa_ssurgo_summary.csv",
                     "data/weather/iowa_weather_2021_2025.csv", "data/cdl/iowa_cdl_2021_2024.csv"],
        output_paths=[output_path],
        code_paths=[_SCRIPT],
        config=config,
    )
    if not step_is_stale(manifest, prior):
        print("skip  Markdown (current)")
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

    md_lines = []
    md_lines.append("# Iowa Farm Intelligence Report")
    md_lines.append("")
    md_lines.append(f"**Farm:** Iowa Demo Farm")
    md_lines.append(f"**Fields:** {n_fields}")
    md_lines.append(f"**Total Area:** {total_ac:.1f} acres")
    md_lines.append(f"**Analysis Period:** 2021-2025")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Farm Overview")
    md_lines.append("")
    md_lines.append("| Metric | Value |")
    md_lines.append("|--------|-------|")
    md_lines.append(f"| Total Fields | {n_fields} |")
    md_lines.append(f"| Total Area | {total_ac:.1f} acres |")
    md_lines.append(f"| Avg Field Size | {total_ac/max(n_fields,1):.1f} acres |")
    
    for col, label in [("avg_avg_om_pct", "Avg Organic Matter"), 
                        ("avg_avg_ph", "Avg pH"),
                        ("avg_total_aws_inches", "Avg Water Storage")]:
        if col in farm_df.columns and pd.notna(farm_df.iloc[0].get(col)):
            md_lines.append(f"| {label} | {float(farm_df.iloc[0][col]):.2f} |")
    
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Field Summary Table")
    md_lines.append("")
    
    cols = ["field_id", "area_acres", "headlands_pct", "dominant_soil", 
            "avg_om_pct", "avg_ph", "total_aws_inches", "drainage_class",
            "crop_diversity", "corn_years", "soybean_years"]
    display_cols = [c for c in cols if c in field_df.columns]
    
    header = "| " + " | ".join(display_cols) + " |"
    md_lines.append(header)
    md_lines.append("|" + "|".join([" --- " for _ in display_cols]) + "|")
    
    for _, row in field_df.iterrows():
        vals = [_safe(row.get(c, "—")) for c in display_cols]
        md_lines.append("| " + " | ".join(vals) + " |")
    
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Individual Field Reports")
    md_lines.append("")
    
    for idx, frow in fields.iterrows():
        fid = frow["field_id"]
        acres = float(frow.get("area_acres", 0))
        row_match = field_df[field_df["field_id"] == fid]
        row_dict = row_match.iloc[0].to_dict() if not row_match.empty else {}
        
        md_lines.append(f"### Field {fid[-8:]} ({acres:.1f} acres)")
        md_lines.append("")
        md_lines.append(f"**Poster:** [iowa_field_poster_{idx+1:02d}.png](./field_cards/iowa_field_poster_{idx+1:02d}.png)")
        md_lines.append("")
        
        soil_cards_exist = False
        soil_card_links = []
        for card_type, label in [("single", "Soil Profile"), ("texture", "Texture RGB"), ("properties", "Properties")]:
            card_path = Path(f"data/EDA/soil_cards/field_{idx+1:02d}_{card_type}.png")
            if card_path.exists():
                soil_cards_exist = True
                soil_card_links.append(f"[{label}](./soil_cards/field_{idx+1:02d}_{card_type}.png)")
        
        if soil_cards_exist:
            md_lines.append(f"**Soil Profile Cards:** {' | '.join(soil_card_links)}")
            md_lines.append("")
        
        implications = compute_management_implications(row_dict)
        md_lines.append("**Management Implications:**")
        for imp in implications:
            md_lines.append(f"- {imp}")
        md_lines.append("")
        
        md_lines.append("| Property | Value |")
        md_lines.append("|----------|-------|")
        for col, label in [("area_acres", "Area"), ("headlands_pct", "Headlands %"),
                           ("total_aws_inches", "Total AWS"), ("avg_om_pct", "Avg OM %"),
                           ("avg_ph", "Avg pH"), ("drainage_class", "Drainage"),
                           ("dominant_soil", "Dominant Soil")]:
            if col in row_dict:
                md_lines.append(f"| {label} | {_safe(row_dict.get(col))} |")
        md_lines.append("")
        
        rank_cols = [c for c in row_dict if c.endswith("_pct_rank")]
        if rank_cols:
            md_lines.append("**Farm-Relative Rankings:**")
            for rc in rank_cols[:6]:
                base = rc.replace("_pct_rank", "").replace("_", " ")
                val = row_dict.get(rc)
                pct = float(val) if val is not None and not (isinstance(val, float) and pd.isna(val)) else 50.0
                md_lines.append(f"- {base}: {pct:.0f}th percentile")
            md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
    
    md_lines.append("")
    md_lines.append("## Outputs")
    md_lines.append("")
    md_lines.append("- Farm Poster: [iowa_farm_report.png](./iowa_farm_report.png)")
    md_lines.append("- HTML Report: [iowa_farm_report.html](./iowa_farm_report.html)")
    md_lines.append("- Field Posters: [field_cards/](./field_cards/)")
    md_lines.append("- Soil Profile Cards: [soil_cards/](./soil_cards/)")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("*Generated by farm-intelligence-reporting system*")
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(md_lines), encoding="utf-8")
    
    manifest.status = "complete"
    manifest.write(manifest_dir / f"{STEP_FARM_MARKDOWN}.json")
    print(f"✓ Markdown report saved → {output_path}")
    print(f"  Size: {output_path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
