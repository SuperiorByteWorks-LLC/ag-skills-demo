from __future__ import annotations

from collections import Counter
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
from rasterstats import zonal_stats


CDL_CODES = {
    0: "No Data",
    1: "Corn",
    5: "Soybeans",
    24: "Winter Wheat",
    28: "Alfalfa",
    36: "Forest",
    38: "Grassland",
    43: "Open Water",
    61: "Fallow/Idle",
    63: "Other",
    176: "Grass/Pasture",
}


def extract_crop_composition(fields: gpd.GeoDataFrame, cdl_path: str | Path, year: int) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    with rasterio.open(cdl_path) as src:
        fields_proj = fields.to_crs(src.crs)
        for _, field in fields_proj.iterrows():
            stats = zonal_stats(field.geometry, cdl_path, categorical=True)
            counts = stats[0] if stats else {}
            total = int(sum(counts.values()))
            if total <= 0:
                rows.append(
                    {
                        "field_id": field["field_id"],
                        "year": year,
                        "crop_code": 0,
                        "crop_name": "No Data",
                        "pixel_count": 0,
                        "pct": 0.0,
                    }
                )
                continue
            for crop_code, pixel_count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
                rows.append(
                    {
                        "field_id": field["field_id"],
                        "year": year,
                        "crop_code": int(crop_code),
                        "crop_name": CDL_CODES.get(int(crop_code), f"Code_{crop_code}"),
                        "pixel_count": int(pixel_count),
                        "pct": round(float(pixel_count) / total * 100.0, 2),
                    }
                )
    return pd.DataFrame(rows)


def _pct_col(df: pd.DataFrame) -> str:
    if "pct" in df.columns:
        return "pct"
    if "dominant_pct" in df.columns:
        return "dominant_pct"
    return "pct"


def summarize_crop_history(crop_mix: pd.DataFrame) -> pd.DataFrame:
    if crop_mix.empty:
        return pd.DataFrame()
    pct = _pct_col(crop_mix)
    dominant = crop_mix.sort_values(["field_id", "year", pct], ascending=[True, True, False])
    dominant = dominant.groupby(["field_id", "year"], as_index=False).first()
    sequences = []
    for field_id, group in dominant.groupby("field_id"):
        ordered = group.sort_values("year")
        crop_names = ordered["crop_name"].tolist()
        transitions = [f"{crop_names[i]} → {crop_names[i + 1]}" for i in range(len(crop_names) - 1)]
        sequences.append(
            {
                "field_id": field_id,
                "rotation_sequence": " -> ".join(crop_names),
                "rotation_count": len(transitions),
                "rotation_patterns": "; ".join(sorted(set(transitions))),
                "crop_diversity": int(ordered["crop_name"].nunique()),
                "corn_years": int((ordered["crop_name"] == "Corn").sum()),
                "soybean_years": int((ordered["crop_name"] == "Soybeans").sum()),
            }
        )
    return pd.DataFrame(sequences)


def plot_crop_mix_stacked_100(ax, crop_mix: pd.DataFrame, title: str = "Crop composition by year"):
    if crop_mix.empty:
        ax.text(0.5, 0.5, "No CDL data", ha="center", va="center")
        ax.set_axis_off()
        return ax
    pct = _pct_col(crop_mix)
    pivot = crop_mix.pivot_table(index="year", columns="crop_name", values=pct, aggfunc="sum").fillna(0)
    colors = plt.cm.tab20(np.linspace(0, 1, max(1, len(pivot.columns))))
    bottom = np.zeros(len(pivot))
    for idx, crop_name in enumerate(pivot.columns):
        values = pivot[crop_name].to_numpy(dtype=float)
        ax.bar(pivot.index.astype(str), values, bottom=bottom, label=crop_name, color=colors[idx])
        bottom += values
    ax.set_ylim(0, 100)
    ax.set_ylabel("Percent of field")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.legend(loc="upper left", fontsize=7)
    return ax
