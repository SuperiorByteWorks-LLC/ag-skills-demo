from __future__ import annotations

from pathlib import Path
from typing import Iterable

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter
from shapely import wkt

try:
    from .ssurgo_soil import download_soil
except ImportError:
    from ssurgo_soil import download_soil


SDA_URL = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest"

NUMERIC_SOIL_PROPS = [
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
]

TEXT_SOIL_PROPS = ["mukey", "muname", "compname", "drainagecl"]


def query_mupolygons_for_field(field_wkt: str, mukey_list: Iterable[str]) -> gpd.GeoDataFrame:
    mukeys = [str(m) for m in mukey_list]
    if not mukeys:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    sql = f"""
    SELECT m.mukey, m.mupolygonkey, m.mupolygongeo.STAsText() AS wkt
    FROM mupolygon m
    WHERE m.mukey IN ({", ".join(mukeys)})
      AND m.mupolygonkey IN (
        SELECT * FROM SDA_Get_Mupolygonkey_from_intersection_with_WktWgs84('{field_wkt}')
      )
    """
    try:
        resp = requests.post(SDA_URL, data={"query": sql, "format": "JSON"}, timeout=120)
        resp.raise_for_status()
        rows = resp.json().get("Table", [])
    except Exception:
        rows = []

    records = []
    for row in rows:
        try:
            records.append(
                {
                    "mukey": str(row[0]),
                    "mupolygonkey": str(row[1]),
                    "geometry": wkt.loads(row[2]),
                }
            )
        except Exception:
            continue
    if not records:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    return gpd.GeoDataFrame(records, crs="EPSG:4326")


def load_fallback_mukey_polygons(path: str | Path) -> gpd.GeoDataFrame:
    p = Path(path)
    if not p.exists():
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    gdf = gpd.read_file(p)
    if gdf.empty:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    gdf["mukey"] = gdf["mukey"].astype(str)
    cols = [c for c in ["mukey", "mupolygonkey", "geometry"] if c in gdf.columns]
    return gdf[cols].copy()


def weighted_mean(values: pd.Series, weights: pd.Series) -> float:
    valid = values.notna() & weights.notna()
    if not valid.any():
        return np.nan
    vals = values[valid].astype(float)
    wts = weights[valid].astype(float)
    denom = float(wts.sum())
    if denom <= 0:
        return float(vals.mean())
    return float((vals * wts).sum() / denom)


def most_common(values: pd.Series):
    non_null = values.dropna()
    if non_null.empty:
        return np.nan
    return non_null.mode().iloc[0]


def aggregate_soil_rows_by_mukey(soil_rows: pd.DataFrame) -> pd.DataFrame:
    groups = []
    for mukey, grp in soil_rows.groupby("mukey"):
        out = {"mukey": str(mukey)}
        weights = pd.to_numeric(grp["comppct_r"], errors="coerce").fillna(1.0)
        for col in NUMERIC_SOIL_PROPS:
            vals = pd.to_numeric(grp[col], errors="coerce")
            out[col] = float(vals.max()) if col == "comppct_r" else weighted_mean(vals, weights)
        for col in ["muname", "compname", "drainagecl"]:
            out[col] = most_common(grp[col])
        groups.append(out)
    return pd.DataFrame(groups)


def aggregate_surface_by_mukey(soil_rows: pd.DataFrame) -> pd.DataFrame:
    """Aggregate soil data to surface horizon only, one row per mukey.
    
    Filters to surface horizon (hzdept_r = 0 or min per component),
    then aggregates by mukey with weighted mean for numeric values
    and mode for text values.
    """
    if soil_rows.empty:
        return pd.DataFrame()
    
    soil = soil_rows.copy()
    soil["hzdept_r"] = pd.to_numeric(soil["hzdept_r"], errors="coerce")
    soil["comppct_r"] = pd.to_numeric(soil["comppct_r"], errors="coerce").fillna(1.0)
    
    surface_rows = []
    for mukey, grp in soil.groupby("mukey"):
        grp_sorted = grp.sort_values("hzdept_r", na_position="last")
        surface_horizon = grp_sorted[grp_sorted["hzdept_r"] == 0]
        if surface_horizon.empty:
            surface_horizon = grp_sorted.head(1)
        
        out = {"mukey": str(mukey)}
        weights = surface_horizon["comppct_r"]
        
        for col in ["om_r", "ph1to1h2o_r", "claytotal_r", "cec7_r", "awc_r", "dbthirdbar_r"]:
            if col in surface_horizon.columns:
                vals = pd.to_numeric(surface_horizon[col], errors="coerce")
                out[col] = weighted_mean(vals, weights)
            else:
                out[col] = np.nan
        
        for col in ["muname", "compname", "drainagecl"]:
            if col in surface_horizon.columns:
                out[col] = most_common(surface_horizon[col])
            else:
                out[col] = np.nan
        
        surface_rows.append(out)
    
    return pd.DataFrame(surface_rows)


def classify_quantiles(values: pd.Series, n_classes: int = 5) -> tuple[np.ndarray, list[str]]:
    """Classify values into n quantile-based bins."""
    arr = pd.to_numeric(values, errors="coerce").dropna().to_numpy(dtype=float)
    if arr.size == 0:
        return np.array([], dtype=int), []
    if arr.size < n_classes:
        n_classes = arr.size
    try:
        quantiles = np.percentile(arr, np.linspace(0, 100, n_classes + 1))
        quantiles = np.unique(quantiles)
        if len(quantiles) < 2:
            return np.zeros(arr.size, dtype=int), [f"{arr[0]:.2f}"]
    except Exception:
        return np.zeros(arr.size, dtype=int), [f"{arr.mean():.2f}"]
    
    class_ids = np.digitize(arr, quantiles[1:-1])
    class_ids = np.clip(class_ids, 0, n_classes - 1)
    
    labels = []
    for i in range(len(quantiles) - 1):
        labels.append(f"{quantiles[i]:.2f} - {quantiles[i+1]:.2f}")
    
    return class_ids, labels


def prepare_ssurgo_field_package(
    field_wgs84: gpd.GeoDataFrame,
    field_id_column: str = "field_id",
    max_depth_cm: int = 30,
    fallback_mukey_geojson: str | Path | None = None,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame, pd.DataFrame]:
    soil = download_soil(field_wgs84, field_id_column=field_id_column, max_depth_cm=max_depth_cm)
    if soil.empty:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326"), pd.DataFrame(), pd.DataFrame()

    fid = field_wgs84.iloc[0][field_id_column]
    field_soil = soil[soil[field_id_column] == fid].copy()
    if field_soil.empty:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326"), pd.DataFrame(), pd.DataFrame()

    field_soil["mukey"] = field_soil["mukey"].astype(str)
    fallback = (
        load_fallback_mukey_polygons(fallback_mukey_geojson)
        if fallback_mukey_geojson is not None
        else gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    )

    mukeys = set(field_soil["mukey"].tolist())
    if not fallback.empty:
        mukeys.update(fallback["mukey"].astype(str).tolist())

    sda = query_mupolygons_for_field(field_wgs84.iloc[0].geometry.wkt, sorted(mukeys))
    if sda.empty and not fallback.empty:
        polygons = fallback
    elif (
        not sda.empty
        and not fallback.empty
        and fallback["mukey"].nunique() > sda["mukey"].nunique()
    ):
        polygons = fallback
    else:
        polygons = sda

    if polygons.empty:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326"), pd.DataFrame(), pd.DataFrame()

    clipped = gpd.overlay(polygons, field_wgs84, how="intersection")
    if clipped.empty:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326"), pd.DataFrame(), pd.DataFrame()

    dissolved = clipped.dissolve(by="mukey", as_index=False)
    dissolved["mukey"] = dissolved["mukey"].astype(str)
    agg = aggregate_soil_rows_by_mukey(field_soil)
    dissolved = dissolved.merge(agg, on="mukey", how="left")

    utm = dissolved.to_crs(
        "EPSG:32615" if field_wgs84.geometry.iloc[0].centroid.x < -90 else "EPSG:32616"
    )
    dissolved["area_acres"] = utm.geometry.area * 0.000247105

    detail = field_soil.copy()
    detail = detail.merge(dissolved[["mukey", "area_acres"]], on="mukey", how="left")
    detail = detail.sort_values(["mukey", "hzdept_r", "comppct_r"], ascending=[True, True, False])
    return dissolved, detail, agg


def headlands_ring(field_utm: gpd.GeoDataFrame, combine_width_m: float = 9.0) -> gpd.GeoDataFrame:
    rings = []
    for geom in field_utm.geometry:
        inner = geom.buffer(-combine_width_m)
        rings.append(geom if inner.is_empty else geom.difference(inner))
    valid = [g for g in rings if not g.is_empty]
    return (
        gpd.GeoDataFrame(geometry=valid, crs=field_utm.crs)
        if valid
        else gpd.GeoDataFrame(geometry=[], crs=field_utm.crs)
    )


def classify_natural_breaks(values: pd.Series, n_classes: int = 3) -> tuple[np.ndarray, list[str]]:
    arr = pd.to_numeric(values, errors="coerce").dropna().to_numpy(dtype=float)
    if arr.size == 0:
        return np.array([], dtype=int), []
    unique = np.sort(np.unique(arr))
    class_count = max(1, min(n_classes, unique.size))
    if class_count == 1:
        return np.zeros(arr.size, dtype=int), [f"{unique[0]:.2f}"]
    if unique.size <= class_count:
        edges = np.linspace(arr.min(), arr.max(), class_count + 1)
    else:
        gaps = np.diff(unique)
        split_idx = np.sort(np.argsort(gaps)[-(class_count - 1) :])
        mids = [(unique[i] + unique[i + 1]) / 2.0 for i in split_idx]
        edges = np.array([arr.min(), *mids, arr.max()], dtype=float)
    edges = np.unique(edges)
    if edges.size < 2:
        return np.zeros(arr.size, dtype=int), [f"{arr[0]:.2f}"]
    class_ids = pd.cut(arr, bins=edges, labels=False, include_lowest=True)
    class_ids = pd.Series(class_ids).fillna(0).astype(int).to_numpy()
    labels = [f"{edges[i]:.2f} to {edges[i + 1]:.2f}" for i in range(edges.size - 1)]
    class_ids = np.clip(class_ids, 0, max(0, len(labels) - 1))
    return class_ids, labels


def _add_basemap(
    ax, gdf_wgs84: gpd.GeoDataFrame, alpha: float = 0.5, attribution_size: int = 5
) -> gpd.GeoDataFrame:
    try:
        import contextily as ctx
    except ImportError:
        return gdf_wgs84
    gdf_wm = gdf_wgs84.to_crs(epsg=3857)
    bounds = gdf_wm.total_bounds
    xb = (bounds[2] - bounds[0]) * 0.25
    yb = (bounds[3] - bounds[1]) * 0.25
    ax.set_xlim(bounds[0] - xb, bounds[2] + xb)
    ax.set_ylim(bounds[1] - yb, bounds[3] + yb)
    ctx.add_basemap(
        ax, source=ctx.providers.Esri.WorldImagery, alpha=alpha, attribution_size=attribution_size
    )
    return gdf_wm


def render_ssurgo_property_map(
    field_wgs84: gpd.GeoDataFrame,
    ssurgo_wgs84: gpd.GeoDataFrame,
    property_col: str,
    output_path: str | Path,
    title: str | None = None,
    show_axis_labels: bool = False,
    basemap_alpha: float = 0.5,
) -> None:
    fig, ax = plt.subplots(figsize=(8, 8))
    field_plot = _add_basemap(ax, field_wgs84, alpha=basemap_alpha)
    if not ssurgo_wgs84.empty and property_col in ssurgo_wgs84.columns:
        ssurgo_plot = (
            ssurgo_wgs84.to_crs(epsg=3857) if str(field_plot.crs).endswith("3857") else ssurgo_wgs84
        )
        data = ssurgo_plot.dropna(subset=[property_col]).copy()
        if not data.empty:
            class_ids, labels = classify_natural_breaks(data[property_col])
            if labels:
                data["class_id"] = class_ids
                colors = plt.cm.YlGn(np.linspace(0.35, 0.85, len(labels)))
                handles = []
                for i, label in enumerate(labels):
                    part = data[data["class_id"] == i]
                    if part.empty:
                        continue
                    part.plot(
                        ax=ax, color=colors[i], alpha=0.45, edgecolor="darkgreen", linewidth=1.0
                    )
                    handles.append(
                        Patch(facecolor=colors[i], edgecolor="darkgreen", alpha=0.45, label=label)
                    )
                if handles:
                    ax.legend(
                        handles=handles,
                        loc="lower right",
                        fontsize=7,
                        title=f"{property_col} ranges",
                    )
    field_plot.plot(ax=ax, color="none", edgecolor="darkgreen", linewidth=2.2)
    ax.set_title(title or f"{property_col} (Natural Breaks)")
    if show_axis_labels:
        ax.set_xlabel("Longitude (degrees)")
        ax.set_ylabel("Latitude (degrees)")
    else:
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_xticks([])
        ax.set_yticks([])
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


def render_complete_workflow_figure(
    field_wgs84: gpd.GeoDataFrame,
    ssurgo_wgs84: gpd.GeoDataFrame,
    detail_table: pd.DataFrame,
    output_path: str | Path,
    combine_width_m: float = 9.0,
) -> None:
    utm_crs = "EPSG:32615" if field_wgs84.geometry.iloc[0].centroid.x < -90 else "EPSG:32616"
    field_utm = field_wgs84.to_crs(utm_crs)
    ring_utm = headlands_ring(field_utm, combine_width_m=combine_width_m)

    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    base1 = _add_basemap(axes[0, 0], field_wgs84)
    base1.plot(ax=axes[0, 0], color="none", edgecolor="darkgreen", linewidth=2.5)
    axes[0, 0].set_title("Field Boundary (WGS84)")
    axes[0, 0].set_xlabel("Longitude (degrees)")
    axes[0, 0].set_ylabel("Latitude (degrees)")

    base2 = _add_basemap(axes[0, 1], field_wgs84)
    if not ssurgo_wgs84.empty and "compname" in ssurgo_wgs84.columns:
        ssurgo2 = (
            ssurgo_wgs84.to_crs(epsg=3857) if str(base2.crs).endswith("3857") else ssurgo_wgs84
        )
        colors = plt.cm.Set3(np.linspace(0, 1, max(1, len(ssurgo2))))
        handles = []
        for i, row in ssurgo2.iterrows():
            c = colors[i % len(colors)]
            gpd.GeoSeries([row.geometry], crs=ssurgo2.crs).plot(
                ax=axes[0, 1], color=c, alpha=0.5, edgecolor="darkgreen"
            )
            comp = row.get("compname", "Unknown")
            comp = comp if isinstance(comp, str) else "Unknown"
            handles.append(Patch(facecolor=c, edgecolor="darkgreen", alpha=0.5, label=comp))
        if handles:
            axes[0, 1].legend(handles=handles, loc="lower right", fontsize=7, title="compname")
    base2.plot(ax=axes[0, 1], color="none", edgecolor="darkgreen", linewidth=2.5)
    axes[0, 1].set_title("Field + SSURGO (WGS84)")
    axes[0, 1].set_xlabel("")
    axes[0, 1].set_ylabel("")
    axes[0, 1].set_xticks([])
    axes[0, 1].set_yticks([])

    base3 = _add_basemap(axes[1, 0], field_utm.to_crs(epsg=4326))
    field3 = field_utm.to_crs(epsg=3857) if str(base3.crs).endswith("3857") else field_utm
    ring3 = (
        ring_utm.to_crs(epsg=3857)
        if not ring_utm.empty and str(base3.crs).endswith("3857")
        else ring_utm
    )
    ssurgo3 = (
        ssurgo_wgs84.to_crs(epsg=3857)
        if not ssurgo_wgs84.empty and str(base3.crs).endswith("3857")
        else ssurgo_wgs84
    )
    if not ssurgo3.empty and "om_r" in ssurgo3.columns:
        ssurgo3.dropna(subset=["om_r"]).plot(
            ax=axes[1, 0],
            column="om_r",
            cmap="YlGn",
            alpha=0.35,
            edgecolor="darkgreen",
            legend=False,
        )
    if not ring3.empty:
        ring3.plot(ax=axes[1, 0], color="orange", alpha=0.35, edgecolor="darkorange", linewidth=1.5)
    field3.plot(ax=axes[1, 0], color="none", edgecolor="darkgreen", linewidth=2.5)
    axes[1, 0].set_title("Headlands Ring + OM Overlay (UTM)")
    axes[1, 0].set_xlabel("X (meters)")
    axes[1, 0].set_ylabel("Y (meters)")
    axes[1, 0].xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(round(x)):,}"))
    axes[1, 0].yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{int(round(y)):,}"))

    axes[1, 1].axis("off")
    cols = [
        "mukey",
        "compname",
        "comppct_r",
        "hzdept_r",
        "hzdepb_r",
        "drainagecl",
        "om_r",
        "ph1to1h2o_r",
        "awc_r",
        "claytotal_r",
        "sandtotal_r",
        "silttotal_r",
        "dbthirdbar_r",
        "cec7_r",
        "area_acres",
    ]
    if not detail_table.empty:
        table_df = detail_table[cols].copy().head(18)
        table_df["drainagecl"] = table_df["drainagecl"].apply(
            lambda s: "".join(w[0].upper() for w in str(s).split()) if pd.notna(s) else ""
        )
        table_df = table_df.rename(
            columns={
                "comppct_r": "comppct",
                "hzdept_r": "hzdept",
                "hzdepb_r": "hzdepb",
                "om_r": "om",
                "ph1to1h2o_r": "ph1to1h2o",
                "awc_r": "awc",
                "claytotal_r": "claytotal",
                "sandtotal_r": "sandtotal",
                "silttotal_r": "silttotal",
                "dbthirdbar_r": "dbthirdbar",
                "cec7_r": "cec7",
            }
        )
        table_df = table_df.replace([np.nan, "nan", "NaN", "None"], "")
        table = axes[1, 1].table(
            cellText=table_df.values, colLabels=table_df.columns, loc="center", cellLoc="center"
        )
        table.auto_set_font_size(False)
        table.set_fontsize(7)
        table.scale(1.0, 1.2)
        mukey_idx = table_df.columns.get_loc("mukey")
        palette = ["#f8f4d8", "#e6f4ea", "#e6eef8", "#f8e8ef", "#eef8f8", "#f3e8ff"]
        mukeys = list(table_df["mukey"].astype(str).unique())
        color_map = {m: palette[i % len(palette)] for i, m in enumerate(mukeys)}
        for c in range(len(table_df.columns)):
            h = table[(0, c)]
            h.set_text_props(weight="bold", color="black")
            h.set_facecolor("#f1f3f5")
            h.set_edgecolor("#9aa1a9")
            h.set_linewidth(0.35)
        for r in range(1, len(table_df) + 1):
            m = str(table_df.iloc[r - 1, mukey_idx])
            row_color = color_map.get(m, "#ffffff")
            for c in range(len(table_df.columns)):
                cell = table[(r, c)]
                cell.set_facecolor(row_color)
                cell.set_edgecolor("#aeb6bf")
                cell.set_linewidth(0.35)
                cell.set_text_props(color="black")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


def render_3x4_dashboard(
    field_wgs84: gpd.GeoDataFrame,
    ssurgo_wgs84: gpd.GeoDataFrame,
    detail_table: pd.DataFrame,
    output_path: str | Path,
    combine_width_m: float = 9.0,
) -> None:
    """Render a 3x4 dashboard of SSURGO soil properties.
    
    Layout:
    Row 1: OM | pH | Clay | CEC
    Row 2: Mukey/compname | Drainage | Bulk density | (blank)
    Row 3: Field boundary | Field + buffer | TABLE (spans 2 cols)
    
    Numeric properties use 5-quantile classification.
    Categorical properties use unique colors per category.
    Table shows aggregated surface values per mukey.
    """
    utm_crs = "EPSG:32615" if field_wgs84.geometry.iloc[0].centroid.x < -90 else "EPSG:32616"
    field_utm = field_wgs84.to_crs(utm_crs)
    ring_utm = headlands_ring(field_utm, combine_width_m=combine_width_m)
    
    agg = aggregate_surface_by_mukey(detail_table)
    if agg.empty:
        agg = aggregate_soil_rows_by_mukey(detail_table)
    
    ssurgo_with_agg = ssurgo_wgs84.merge(agg, on="mukey", how="left", suffixes=("", "_agg"))
    for col in ["om_r", "ph1to1h2o_r", "claytotal_r", "cec7_r", "dbthirdbar_r"]:
        if f"{col}_agg" in ssurgo_with_agg.columns:
            ssurgo_with_agg[col] = ssurgo_with_agg[f"{col}_agg"]
    
    cmap_numeric = "Greens"
    cmap_ph = "RdYlGn_r"
    
    fig, axes = plt.subplots(3, 4, figsize=(20, 15))
    fig.suptitle(f"SSURGO Soil Dashboard - {field_wgs84.iloc[0].get('field_id', 'Field')}", fontsize=14, fontweight="bold")
    
    def setup_axis(ax, show_labels=False):
        ax.set_xlabel("")
        ax.set_ylabel("")
        if not show_labels:
            ax.set_xticks([])
            ax.set_yticks([])
    
    def plot_choropleth(ax, data, column, cmap, title, show_legend=True):
        data_plot = data.dropna(subset=[column]).copy()
        if data_plot.empty:
            ax.text(0.5, 0.5, f"No {column} data", ha="center", va="center", transform=ax.transAxes)
            ax.set_title(title, fontsize=9)
            return
        
        try:
            class_ids, labels = classify_quantiles(data_plot[column], n_classes=5)
            data_plot = data_plot.copy()
            data_plot["class_id"] = class_ids
            colors = plt.cm.get_cmap(cmap)(np.linspace(0.3, 0.95, len(labels)))
            handles = []
            for i, label in enumerate(labels):
                part = data_plot[data_plot["class_id"] == i]
                if part.empty:
                    continue
                part.plot(ax=ax, color=colors[i], alpha=0.6, edgecolor="black", linewidth=0.5)
                handles.append(Patch(facecolor=colors[i], edgecolor="black", alpha=0.6, label=label))
            
            if handles and show_legend:
                ax.legend(handles=handles, loc="lower right", fontsize=5, title=column, framealpha=0.9)
        except Exception:
            data_plot.plot(ax=ax, column=column, cmap=cmap, alpha=0.6, edgecolor="black", linewidth=0.5, legend=True)
        
        ax.set_title(title, fontsize=9)
    
    def plot_categorical(ax, data, column, title, show_legend=True):
        data_plot = data.dropna(subset=[column]).copy()
        if data_plot.empty:
            ax.text(0.5, 0.5, f"No {column} data", ha="center", va="center", transform=ax.transAxes)
            ax.set_title(title, fontsize=9)
            return
        
        unique_vals = data_plot[column].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(unique_vals)))
        color_map = {v: colors[i] for i, v in enumerate(unique_vals)}
        
        handles = []
        for val in unique_vals:
            part = data_plot[data_plot[column] == val]
            if part.empty:
                continue
            label = str(val)[:20] if val else "Unknown"
            part.plot(ax=ax, color=color_map[val], alpha=0.6, edgecolor="black", linewidth=0.5)
            handles.append(Patch(facecolor=color_map[val], edgecolor="black", alpha=0.6, label=label))
        
        if handles and show_legend:
            ax.legend(handles=handles, loc="lower right", fontsize=5, title=column, framealpha=0.9)
        
        ax.set_title(title, fontsize=9)
    
    ssurgo_plot = ssurgo_with_agg.to_crs(epsg=3857)
    field_plot = field_wgs84.to_crs(epsg=3857)
    ring_plot = ring_utm.to_crs(epsg=3857) if not ring_utm.empty else None
    
    plot_choropleth(axes[0, 0], ssurgo_plot, "om_r", cmap_numeric, "Organic Matter (%)", show_legend=True)
    plot_choropleth(axes[0, 1], ssurgo_plot, "ph1to1h2o_r", cmap_ph, "pH", show_legend=True)
    plot_choropleth(axes[0, 2], ssurgo_plot, "claytotal_r", cmap_numeric, "Clay Content (%)", show_legend=True)
    plot_choropleth(axes[0, 3], ssurgo_plot, "cec7_r", cmap_numeric, "CEC (meq/100g)", show_legend=True)
    
    plot_categorical(axes[1, 0], ssurgo_plot, "compname", "Soil Name (mode)", show_legend=True)
    plot_categorical(axes[1, 1], ssurgo_plot, "drainagecl", "Drainage Class", show_legend=True)
    plot_choropleth(axes[1, 2], ssurgo_plot, "dbthirdbar_r", cmap_numeric, "Bulk Density (g/cm³)", show_legend=True)
    axes[1, 3].axis("off")
    
    axes[2, 0].set_title("Field Boundary", fontsize=9)
    _add_basemap(axes[2, 0], field_wgs84, alpha=0.5)
    field_wgs84.plot(ax=axes[2, 0], color="none", edgecolor="blue", linewidth=2)
    setup_axis(axes[2, 0])
    
    axes[2, 1].set_title("Field + Headlands Buffer", fontsize=9)
    _add_basemap(axes[2, 1], field_utm.to_crs(epsg=4326), alpha=0.5)
    if ring_plot is not None:
        ring_plot.plot(ax=axes[2, 1], color="orange", alpha=0.4, edgecolor="darkorange", linewidth=1.5)
    field_utm.to_crs(epsg=3857).plot(ax=axes[2, 1], color="none", edgecolor="blue", linewidth=2)
    setup_axis(axes[2, 1])
    
    axes[2, 2].axis("off")
    axes[2, 3].axis("off")
    
    table_ax = fig.add_subplot(2, 2, 3)
    table_ax.axis("off")
    table_ax.set_position([0.52, 0.02, 0.46, 0.28])
    
    table_cols = [
        "mukey", "compname", "comppct_r", "hzdept_r", "hzdepb_r",
        "drainagecl", "om_r", "ph1to1h2o_r", "claytotal_r", 
        "dbthirdbar_r", "cec7_r", "area_acres"
    ]
    table_data = detail_table[table_cols].copy().head(18) if not detail_table.empty else pd.DataFrame(columns=table_cols)
    
    table_data = table_data.rename(columns={
        "comppct_r": "comppct",
        "hzdept_r": "hzdept",
        "hzdepb_r": "hzdepb",
        "om_r": "OM",
        "ph1to1h2o_r": "pH",
        "claytotal_r": "Clay",
        "cec7_r": "CEC",
        "dbthirdbar_r": "BD",
        "drainagecl": "Drainage",
        "compname": "Soil"
    })
    
    if not table_data.empty:
        table_data["OM"] = table_data["OM"].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "")
        table_data["pH"] = table_data["pH"].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "")
        table_data["Clay"] = table_data["Clay"].apply(lambda x: f"{x:.1f}" if pd.notna(x) else "")
        table_data["CEC"] = table_data["CEC"].apply(lambda x: f"{x:.1f}" if pd.notna(x) else "")
        table_data["BD"] = table_data["BD"].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "")
        table_data["Drainage"] = table_data["Drainage"].apply(lambda x: "".join(w[0].upper() for w in str(x).split()) if pd.notna(x) else "")
        table_data["Soil"] = table_data["Soil"].apply(lambda x: str(x)[:15] if pd.notna(x) else "")
        table_data["comppct"] = table_data["comppct"].apply(lambda x: f"{x:.0f}" if pd.notna(x) else "")
        table_data["hzdept"] = table_data["hzdept"].apply(lambda x: f"{x:.0f}" if pd.notna(x) else "")
        table_data["hzdepb"] = table_data["hzdepb"].apply(lambda x: f"{x:.0f}" if pd.notna(x) else "")
        table_data["area_acres"] = table_data["area_acres"].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "")
    
    table_data = table_data.replace([np.nan, "nan", "NaN", "None"], "")
    
    table = table_ax.table(
        cellText=table_data.values,
        colLabels=table_data.columns,
        loc="center",
        cellLoc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(6)
    table.scale(1.0, 1.1)
    
    mukey_idx = table_data.columns.get_loc("mukey")
    palette = ["#f8f4d8", "#e6f4ea", "#e6eef8", "#f8e8ef", "#eef8f8", "#f3e8ff"]
    mukeys = list(table_data["mukey"].astype(str).unique())
    color_map = {m: palette[i % len(palette)] for i, m in enumerate(mukeys)}
    
    for c in range(len(table_data.columns)):
        h = table[(0, c)]
        h.set_text_props(weight="bold", color="black")
        h.set_facecolor("#e8f4ea")
        h.set_edgecolor("#9aa1a9")
    
    for r in range(1, len(table_data) + 1):
        m = str(table_data.iloc[r - 1, mukey_idx])
        row_color = color_map.get(m, "#ffffff")
        for c in range(len(table_data.columns)):
            cell = table[(r, c)]
            cell.set_facecolor(row_color)
            cell.set_edgecolor("#d0d0d0")
            cell.set_text_props(color="black")
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
