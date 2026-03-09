#!/usr/bin/env python3
"""Download SSURGO soil data into canonical grower paths."""

import os
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_SCRIPTS_DIR))
sys.path.insert(0, str(_SCRIPTS_DIR / "lib"))

from paths import farm_boundary_path, farm_table_path, field_soil_full_path, field_soil_summary_path
from reporting_bootstrap import (
    ensure_canonical_data_tree,
    ensure_skill_path,
    field_slug_map_from_inventory,
)

ensure_skill_path("ssurgo-soil")

from ssurgo_soil import download_soil

SDA_URL = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest"


def _query_sda(sql: str, timeout: int = 120) -> list[list[object]]:
    response = requests.post(SDA_URL, data={"query": sql, "format": "JSON"}, timeout=timeout)
    response.raise_for_status()
    return response.json().get("Table", [])


def _fallback_field_soil(fields: gpd.GeoDataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    fields_wgs84 = fields.to_crs(epsg=4326)

    for _, field in fields_wgs84.iterrows():
        field_id = str(field["field_id"])
        field_wkt = field.geometry.wkt
        mukey_sql = f"""
        SELECT DISTINCT m.mukey
        FROM mupolygon m
        WHERE m.mupolygonkey IN (
            SELECT * FROM SDA_Get_Mupolygonkey_from_intersection_with_WktWgs84('{field_wkt}')
        )
        """
        try:
            mukey_rows = _query_sda(mukey_sql, timeout=60)
        except Exception:
            mukey_rows = []
        mukeys = [str(row[0]) for row in mukey_rows if row and row[0] is not None]
        if not mukeys:
            continue

        attr_sql = f"""
        SELECT c.mukey, c.compname, c.comppct_r, c.drainagecl,
               ch.hzdept_r, ch.hzdepb_r, ch.om_r, ch.ph1to1h2o_r,
               ch.awc_r, ch.claytotal_r, ch.sandtotal_r, ch.silttotal_r,
               ch.dbthirdbar_r, ch.cec7_r
        FROM component c
        LEFT JOIN chorizon ch ON c.cokey = ch.cokey
        WHERE c.mukey IN ({", ".join(repr(m) for m in mukeys)})
          AND c.majcompflag = 'Yes'
          AND (ch.hzdept_r < 30 OR ch.hzdept_r IS NULL)
        ORDER BY c.mukey, c.comppct_r DESC, ch.hzdept_r ASC
        """
        try:
            attr_rows = _query_sda(attr_sql)
        except Exception:
            attr_rows = []

        for row in attr_rows:
            if len(row) < 14:
                continue
            rows.append(
                {
                    "field_id": field_id,
                    "mukey": str(row[0]),
                    "compname": row[1],
                    "comppct_r": row[2],
                    "drainagecl": row[3],
                    "hzdept_r": row[4],
                    "hzdepb_r": row[5],
                    "om_r": row[6],
                    "ph1to1h2o_r": row[7],
                    "awc_r": row[8],
                    "claytotal_r": row[9],
                    "sandtotal_r": row[10],
                    "silttotal_r": row[11],
                    "dbthirdbar_r": row[12],
                    "cec7_r": row[13],
                }
            )

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    for col in [
        "comppct_r",
        "hzdept_r",
        "hzdepb_r",
        "om_r",
        "ph1to1h2o_r",
        "awc_r",
        "claytotal_r",
        "sandtotal_r",
        "silttotal_r",
        "dbthirdbar_r",
        "cec7_r",
    ]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _write_summary(soil_data: pd.DataFrame) -> None:
    if soil_data.empty:
        return
    grouped = (
        soil_data.groupby("field_id", as_index=False)
        .agg(
            n_mukeys=("mukey", "nunique"),
            n_components=("compname", "nunique"),
            n_horizons=("mukey", "count"),
            avg_om_pct=("om_r", "mean"),
            avg_ph=("ph1to1h2o_r", "mean"),
            total_aws_inches=("awc_r", "sum"),
            avg_cec=("cec7_r", "mean"),
            avg_clay_pct=("claytotal_r", "mean"),
            avg_sand_pct=("sandtotal_r", "mean"),
            dominant_soil=("compname", "first"),
            drainage_class=("drainagecl", "first"),
        )
        .assign(ph_constraint="none", erosion_risk="moderate")
    )
    raise RuntimeError("_write_summary requires an explicit output path")


def main():
    print("=" * 60)
    print("Step 2: Download SSURGO Soil Data")
    print("=" * 60)

    grower_slug = os.environ.get("AG_GROWER_SLUG", "iowa-demo-grower")
    farm_slug = os.environ.get("AG_FARM_SLUG", "iowa-demo-farm")
    inventory_path = Path(".sisyphus/evidence/task-3-field-inventory.csv")
    ensure_canonical_data_tree(
        grower_slug=grower_slug, farm_slug=farm_slug, inventory_path=inventory_path
    )
    field_slug_map = field_slug_map_from_inventory(
        inventory_path if inventory_path.exists() else None
    )

    boundaries_path = farm_boundary_path(grower_slug, farm_slug)
    fields = gpd.read_file(boundaries_path)
    print(f"Loaded {len(fields)} fields")

    farm_full_output = farm_table_path(grower_slug, farm_slug, "iowa_full_ssurgo.csv")
    farm_summary_output = farm_table_path(grower_slug, farm_slug, "iowa_ssurgo_summary.csv")
    farm_sample_output = farm_table_path(grower_slug, farm_slug, "iowa_10_fields_soil.csv")
    farm_sample_output.parent.mkdir(parents=True, exist_ok=True)
    force = os.environ.get("AG_FORCE") == "1"

    if (
        farm_full_output.exists()
        and farm_summary_output.exists()
        and farm_sample_output.exists()
        and not force
    ):
        soil_data = pd.read_csv(farm_sample_output)
        grouped = pd.read_csv(farm_summary_output)
        if field_slug_map:
            for field_id, field_slug in field_slug_map.items():
                field_rows = soil_data[soil_data["field_id"].astype(str) == str(field_id)].copy()
                if not field_rows.empty:
                    full_target = field_soil_full_path(grower_slug, farm_slug, field_slug)
                    full_target.parent.mkdir(parents=True, exist_ok=True)
                    field_rows.to_csv(full_target, index=False)
                summary_rows = grouped[grouped["field_id"].astype(str) == str(field_id)].copy()
                if not summary_rows.empty:
                    summary_target = field_soil_summary_path(grower_slug, farm_slug, field_slug)
                    summary_target.parent.mkdir(parents=True, exist_ok=True)
                    summary_rows.to_csv(summary_target, index=False)
        print(f"skip  SSURGO API fetch (cached): {farm_sample_output}")
        return soil_data

    soil_data = download_soil(
        fields,
        field_id_column="field_id",
        max_depth_cm=30,
        output_path=str(farm_sample_output),
    )

    if soil_data.empty:
        print("  Primary SSURGO download returned no rows; querying SDA fallback summaries...")
        soil_data = _fallback_field_soil(fields)
        if not soil_data.empty:
            soil_data.to_csv(farm_full_output, index=False)
            soil_data.to_csv(farm_sample_output, index=False)

    if not soil_data.empty:
        soil_data.to_csv(farm_full_output, index=False)
        soil_data.to_csv(farm_sample_output, index=False)
        grouped = (
            soil_data.groupby("field_id", as_index=False)
            .agg(
                n_mukeys=("mukey", "nunique"),
                n_components=("compname", "nunique"),
                n_horizons=("mukey", "count"),
                avg_om_pct=("om_r", "mean"),
                avg_ph=("ph1to1h2o_r", "mean"),
                total_aws_inches=("awc_r", "sum"),
                avg_cec=("cec7_r", "mean"),
                avg_clay_pct=("claytotal_r", "mean"),
                avg_sand_pct=("sandtotal_r", "mean"),
                dominant_soil=("compname", "first"),
                drainage_class=("drainagecl", "first"),
            )
            .assign(ph_constraint="none", erosion_risk="moderate")
        )
        grouped.to_csv(farm_summary_output, index=False)

        if field_slug_map:
            for field_id, field_slug in field_slug_map.items():
                field_rows = soil_data[soil_data["field_id"].astype(str) == str(field_id)].copy()
                if not field_rows.empty:
                    full_target = field_soil_full_path(grower_slug, farm_slug, field_slug)
                    full_target.parent.mkdir(parents=True, exist_ok=True)
                    field_rows.to_csv(full_target, index=False)
                summary_rows = grouped[grouped["field_id"].astype(str) == str(field_id)].copy()
                if not summary_rows.empty:
                    summary_target = field_soil_summary_path(grower_slug, farm_slug, field_slug)
                    summary_target.parent.mkdir(parents=True, exist_ok=True)
                    summary_rows.to_csv(summary_target, index=False)

    print(
        f"\n✓ Downloaded {len(soil_data)} soil records for {soil_data['field_id'].nunique()} fields"
    )
    print(f"  Output: {farm_sample_output}")

    return soil_data


if __name__ == "__main__":
    main()
