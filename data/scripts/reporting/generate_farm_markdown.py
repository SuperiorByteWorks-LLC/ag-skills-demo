#!/usr/bin/env python3
# pyright: reportMissingImports=false, reportAttributeAccessIssue=false, reportGeneralTypeIssues=false
"""Generate markdown farm intelligence report."""

from __future__ import annotations

import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd

_REPO = Path(__file__).resolve().parents[3]
_SKILLS = _REPO / ".opencode" / "skills"
_LIB = _REPO / "data" / "scripts" / "lib"

sys.path.insert(0, str(_SKILLS / "farm-intelligence-reporting" / "src"))
sys.path.insert(0, str(_SKILLS / "headlands-ring" / "src"))
sys.path.insert(0, str(_SKILLS / "cdl-cropland" / "src"))
sys.path.insert(0, str(_SKILLS / "nasa-power-weather" / "src"))
sys.path.insert(0, str(_LIB))

from cdl_reporting import summarize_crop_history
from headlands_ring import split_headlands_and_interior, summarize_headlands
from paths import (
    farm_boundary_path,
    farm_manifest_dir,
    farm_report_path,
    farm_table_path,
    shared_cdl_preferred_full_composition_path,
)
from pipeline import (
    STEP_FARM_MARKDOWN,
    FieldReportingConfig,
    build_step_manifest,
    load_manifest,
    step_is_stale,
)
from reporting import (
    build_farm_reporting_dataset,
    build_field_reporting_dataset,
    compute_management_implications,
)
from weather_reporting import summarize_weather_variability

_SCRIPT = Path(__file__)
_DEFAULT_GROWER = "iowa-demo-grower"
_DEFAULT_FARM = "iowa-demo-farm"
_FIELD_INVENTORY = _REPO / ".sisyphus" / "evidence" / "task-3-field-inventory.csv"
_CDL_PRIMARY = shared_cdl_preferred_full_composition_path()
_CDL_FALLBACK = shared_cdl_preferred_full_composition_path()


def _utm(frow) -> str:
    return "EPSG:32615" if frow.geometry.centroid.x < -90 else "EPSG:32616"


def _safe(val) -> str:
    if val is None or (not isinstance(val, str) and pd.isna(val)):
        return "—"
    if isinstance(val, float):
        return f"{val:.2f}"
    return str(val)


def _as_float(val, default: float = 0.0) -> float:
    try:
        if val is None or pd.isna(val):
            return default
        return float(val)
    except (TypeError, ValueError):
        return default


def _field_slug_lookup(inventory_path: Path = _FIELD_INVENTORY) -> dict[str, str]:
    if not inventory_path.exists():
        return {}
    inventory = pd.read_csv(inventory_path)
    if not {"field_id", "field_slug"}.issubset(inventory.columns):
        return {}
    return {
        str(row["field_id"]): str(row["field_slug"])
        for _, row in inventory[["field_id", "field_slug"]].dropna().iterrows()
    }


def _ndvi_asset_links(field_slug: str | None) -> list[str]:
    if not field_slug:
        return []
    feature_dir = (
        _REPO
        / "data"
        / "growers"
        / _DEFAULT_GROWER
        / "farms"
        / _DEFAULT_FARM
        / "fields"
        / field_slug
        / "derived"
        / "features"
    )
    links = []
    for filename, label in [
        ("ndvi_corn.png", "Corn average NDVI"),
        ("ndvi_corn_peak_95.png", "Corn 95th %ile peak NDVI"),
        ("ndvi_soybean.png", "Soybean average NDVI"),
        ("ndvi_soybean_peak_95.png", "Soybean 95th %ile peak NDVI"),
        ("ndvi_current_season_cumulative.png", "Cumulative NDVI by crop and year"),
    ]:
        path = feature_dir / filename
        if path.exists():
            links.append(f"[{label}](../../fields/{field_slug}/derived/features/{filename})")
    return links


def _cdl_csv_path() -> Path:
    return _CDL_PRIMARY if _CDL_PRIMARY.exists() else _CDL_FALLBACK


def main() -> None:
    print("=" * 60)
    print("Farm Markdown Report")
    print("=" * 60)

    config = FieldReportingConfig(
        farm_name="Iowa Demo Farm",
        field_boundary_path=str(farm_boundary_path(_DEFAULT_GROWER, _DEFAULT_FARM)),
        grower_slug=_DEFAULT_GROWER,
        farm_slug=_DEFAULT_FARM,
    )
    manifest_dir = farm_manifest_dir(_DEFAULT_GROWER, _DEFAULT_FARM)
    output_path = farm_report_path(_DEFAULT_GROWER, _DEFAULT_FARM, "iowa_farm_report.md")
    field_slug_lookup = _field_slug_lookup()
    ndvi_input_paths = []
    for field_slug in field_slug_lookup.values():
        feature_dir = (
            _REPO
            / "data"
            / "growers"
            / _DEFAULT_GROWER
            / "farms"
            / _DEFAULT_FARM
            / "fields"
            / field_slug
            / "derived"
            / "features"
        )
        for filename in (
            "ndvi_corn.png",
            "ndvi_corn_peak_95.png",
            "ndvi_soybean.png",
            "ndvi_soybean_peak_95.png",
            "ndvi_current_season_cumulative.png",
        ):
            path = feature_dir / filename
            if path.exists():
                ndvi_input_paths.append(str(path.relative_to(_REPO)))

    prior = load_manifest(manifest_dir / f"{STEP_FARM_MARKDOWN}.json")
    manifest = build_step_manifest(
        step_name=STEP_FARM_MARKDOWN,
        input_paths=[
            config.field_boundary_path,
            str(farm_table_path(_DEFAULT_GROWER, _DEFAULT_FARM, "iowa_ssurgo_summary.csv")),
            str(farm_table_path(_DEFAULT_GROWER, _DEFAULT_FARM, "iowa_weather_2021_2025.csv")),
            str(_cdl_csv_path().relative_to(_REPO)),
            *ndvi_input_paths,
        ],
        output_paths=[output_path],
        code_paths=[_SCRIPT],
        config=config,
    )
    if not step_is_stale(manifest, prior):
        print("skip  Markdown (current)")
        return

    fields = gpd.read_file(_REPO / config.field_boundary_path)
    soil_summary = pd.read_csv(
        farm_table_path(_DEFAULT_GROWER, _DEFAULT_FARM, "iowa_ssurgo_summary.csv")
    )
    weather = pd.read_csv(
        farm_table_path(_DEFAULT_GROWER, _DEFAULT_FARM, "iowa_weather_2021_2025.csv"),
        parse_dates=["date"],
    )
    cdl = pd.read_csv(_cdl_csv_path())
    hl_rows = []
    for idx, frow in fields.iterrows():
        fgdf = fields.iloc[[idx]].to_crs(_utm(frow))
        ring, _ = split_headlands_and_interior(fgdf, width_m=9.0)
        s = summarize_headlands(fgdf, ring).iloc[0].to_dict()
        s["field_id"] = frow["field_id"]
        hl_rows.append(s)
    headlands_df = pd.DataFrame(hl_rows)

    wx_summary = summarize_weather_variability(weather)
    crop_sum = summarize_crop_history(cdl, window_years=5)

    field_df = build_field_reporting_dataset(
        fields,
        headlands_summary=headlands_df,
        soil_summary=soil_summary,
        weather_summary=wx_summary,
        cdl_summary=crop_sum,
    )
    farm_df = build_farm_reporting_dataset(field_df)

    total_ac = float(farm_df.iloc[0].get("total_acres", 0))
    n_fields = int(farm_df.iloc[0].get("field_count", len(fields)))

    md_lines = []
    md_lines.append("# Iowa Farm Intelligence Report")
    md_lines.append("")
    md_lines.append("**Farm:** Iowa Demo Farm")
    md_lines.append(f"**Fields:** {n_fields}")
    md_lines.append(f"**Total Area:** {total_ac:.1f} acres")
    md_lines.append("**Analysis Period:** 2021-2025")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Farm Overview")
    md_lines.append("")
    md_lines.append("| Metric | Value |")
    md_lines.append("|--------|-------|")
    md_lines.append(f"| Total Fields | {n_fields} |")
    md_lines.append(f"| Total Area | {total_ac:.1f} acres |")
    md_lines.append(f"| Avg Field Size | {total_ac / max(n_fields, 1):.1f} acres |")

    for col, label in [
        ("avg_avg_om_pct", "Avg Organic Matter"),
        ("avg_avg_ph", "Avg pH"),
        ("avg_total_aws_inches", "Avg Water Storage"),
    ]:
        if col in farm_df.columns and pd.notna(farm_df.iloc[0].get(col)):
            md_lines.append(f"| {label} | {float(farm_df.iloc[0][col]):.2f} |")

    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Field Summary Table")
    md_lines.append("")

    cols = [
        "field_id",
        "area_acres",
        "headlands_pct",
        "dominant_soil",
        "avg_om_pct",
        "avg_ph",
        "total_aws_inches",
        "drainage_class",
        "crop_diversity",
        "corn_years",
        "soybean_years",
    ]
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

    for idx_num, (_, frow) in enumerate(fields.iterrows()):
        fid = str(frow["field_id"])
        field_slug = field_slug_lookup.get(str(fid), "")
        acres = _as_float(frow.get("area_acres", 0), 0.0)
        row_match = field_df[field_df["field_id"] == fid]
        row_dict = row_match.iloc[0].to_dict() if not row_match.empty else {}

        md_lines.append(f"### Field {fid[-8:]} ({acres:.1f} acres)")
        md_lines.append("")
        md_lines.append(
            f"**Poster:** [field_report.png](../../fields/{field_slug}/derived/reports/field_report.png)"
        )
        md_lines.append("")

        soil_cards_exist = False
        soil_card_links = []
        for card_type, label in [
            ("properties", "Soil Properties"),
            ("texture", "Texture RGB"),
        ]:
            card_link = f"../../fields/{field_slug}/derived/summaries/soil_{card_type}.png"
            card_path = output_path.parent / card_link
            if card_path.exists():
                soil_cards_exist = True
                soil_card_links.append(f"[{label}]({card_link})")

        if soil_cards_exist:
            md_lines.append(f"**Soil Profile Cards:** {' | '.join(soil_card_links)}")
            md_lines.append("")

        ndvi_links = _ndvi_asset_links(field_slug_lookup.get(str(fid)))
        if ndvi_links:
            md_lines.append(f"**NDVI Cards:** {' | '.join(ndvi_links)}")
            md_lines.append("")

        if row_dict.get("rotation_sequence"):
            md_lines.append(
                f"**Crop Rotation History:** {_safe(row_dict.get('rotation_sequence'))}"
            )
            md_lines.append("")
        if row_dict.get("rotation_outlook"):
            md_lines.append(
                f"**Heuristic Crop Outlook:** {_safe(row_dict.get('rotation_outlook'))}"
            )
            md_lines.append("")

        implications = compute_management_implications(row_dict)
        md_lines.append("**Management Implications:**")
        for imp in implications:
            md_lines.append(f"- {imp}")
        md_lines.append("")

        md_lines.append("| Property | Value |")
        md_lines.append("|----------|-------|")
        for col, label in [
            ("area_acres", "Area"),
            ("headlands_pct", "Headlands %"),
            ("total_aws_inches", "Total AWS"),
            ("avg_om_pct", "Avg OM %"),
            ("avg_ph", "Avg pH"),
            ("drainage_class", "Drainage"),
            ("dominant_soil", "Dominant Soil"),
        ]:
            if col in row_dict:
                md_lines.append(f"| {label} | {_safe(row_dict.get(col))} |")
        md_lines.append("")

        rank_cols = [c for c in row_dict if c.endswith("_pct_rank")]
        if rank_cols:
            md_lines.append("**Farm-Relative Rankings:**")
            for rc in rank_cols[:6]:
                base = rc.replace("_pct_rank", "").replace("_", " ")
                val = row_dict.get(rc)
                pct = (
                    float(val)
                    if val is not None and not (isinstance(val, float) and pd.isna(val))
                    else 50.0
                )
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
