from __future__ import annotations

import importlib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_SRC = REPO_ROOT / ".opencode" / "skills" / "farm-intelligence-reporting" / "src"
CDL_SRC = REPO_ROOT / ".opencode" / "skills" / "cdl-cropland" / "src"
SCRIPT_LIB = REPO_ROOT / "data" / "scripts" / "lib"
INGEST_SRC = REPO_ROOT / "data" / "scripts" / "ingest"
REPORTING_SRC = REPO_ROOT / "data" / "scripts" / "reporting"
if str(SKILL_SRC) not in sys.path:
    sys.path.insert(0, str(SKILL_SRC))
if str(CDL_SRC) not in sys.path:
    sys.path.insert(0, str(CDL_SRC))
if str(SCRIPT_LIB) not in sys.path:
    sys.path.insert(0, str(SCRIPT_LIB))
if str(INGEST_SRC) not in sys.path:
    sys.path.insert(0, str(INGEST_SRC))
if str(REPORTING_SRC) not in sys.path:
    sys.path.insert(0, str(REPORTING_SRC))

cdl = importlib.import_module("cdl_reporting")
pl = importlib.import_module("pipeline")
rp = importlib.import_module("reporting")
si = importlib.import_module("satellite_imagery")
paths = importlib.import_module("paths")
dsi = importlib.import_module("download_satellite_imagery")
dnc = importlib.import_module("generate_ndvi_composites")
gnc = importlib.import_module("generate_ndvi_cards")


def test_step_is_stale_when_no_previous(tmp_path):
    inp = tmp_path / "input.txt"
    inp.write_text("hello")
    out = tmp_path / "output.txt"
    cfg = pl.FieldReportingConfig(farm_name="T", field_boundary_path="f.geojson")
    m = pl.build_step_manifest("s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg)
    assert pl.step_is_stale(m, None) is True


def test_step_not_stale_when_fingerprints_match(tmp_path):
    inp = tmp_path / "input.txt"
    out = tmp_path / "output.txt"
    inp.write_text("hello")
    out.write_text("done")
    cfg = pl.FieldReportingConfig(farm_name="T", field_boundary_path="f.geojson")
    first = pl.build_step_manifest(
        "s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg, status="complete"
    )
    second = pl.build_step_manifest("s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg)
    assert pl.step_is_stale(second, first) is False


def test_step_stale_when_output_missing(tmp_path):
    inp = tmp_path / "input.txt"
    out = tmp_path / "output.txt"
    inp.write_text("hello")
    out.write_text("done")
    cfg = pl.FieldReportingConfig(farm_name="T", field_boundary_path="f.geojson")
    first = pl.build_step_manifest(
        "s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg, status="complete"
    )
    out.unlink()
    second = pl.build_step_manifest("s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg)
    assert pl.step_is_stale(second, first) is True


def test_load_manifest_returns_none_when_missing(tmp_path):
    result = pl.load_manifest(tmp_path / "nonexistent.json")
    assert result is None


def test_load_manifest_roundtrip(tmp_path):
    inp = tmp_path / "input.txt"
    inp.write_text("data")
    cfg = pl.FieldReportingConfig(farm_name="T", field_boundary_path="f.geojson")
    m = pl.build_step_manifest(
        "roundtrip", [inp], [], [SKILL_SRC / "pipeline.py"], cfg, status="complete"
    )
    path = m.write(tmp_path / "roundtrip.json")
    loaded = pl.load_manifest(path)
    assert loaded is not None
    assert loaded.step_name == "roundtrip"
    assert loaded.status == "complete"


def test_compute_management_implications_returns_list():
    row = {
        "avg_ph": 5.5,
        "avg_om_pct": 1.0,
        "total_aws_inches": 3.0,
        "drainage_class": "Poorly drained",
        "headlands_pct": 22.0,
        "avg_clay_pct": 40.0,
        "crop_diversity": 1,
        "erosion_risk": "high",
    }
    result = rp.compute_management_implications(row)
    assert isinstance(result, list)
    assert len(result) >= 3


def test_compute_management_implications_optimal():
    row = {"avg_ph": 6.5, "avg_om_pct": 2.5, "total_aws_inches": 6.0}
    result = rp.compute_management_implications(row)
    assert any(
        w in " ".join(result).lower()
        for w in ("optimal", "good", "strong", "high", "within", "provides")
    )


def test_build_field_reporting_dataset_columns():
    import pandas as pd

    try:
        import geopandas as gpd
        from shapely.geometry import Point
    except ImportError:
        return
    fields = gpd.GeoDataFrame(
        {"field_id": ["F1", "F2"], "area_acres": [80.0, 120.0]},
        geometry=[Point(-93, 41), Point(-92, 42)],
        crs="EPSG:4326",
    )
    soil = pd.DataFrame({"field_id": ["F1", "F2"], "avg_om_pct": [2.1, 1.8], "avg_ph": [6.5, 6.2]})
    result = rp.build_field_reporting_dataset(fields, soil_summary=soil)
    assert "field_id" in result.columns
    assert "area_acres" in result.columns
    assert "avg_om_pct" in result.columns


def test_compute_farm_relative_rankings_adds_cols():
    import pandas as pd

    df = pd.DataFrame({"field_id": ["A", "B", "C"], "area_acres": [80.0, 120.0, 60.0]})
    result = rp.compute_farm_relative_rankings(df)
    assert "area_acres_pct_rank" in result.columns


def test_field_reporting_config_targets_five_year_windows():
    cfg = pl.FieldReportingConfig(farm_name="T", field_boundary_path="f.geojson")
    assert cfg.weather_years == (2021, 2022, 2023, 2024, 2025)
    assert cfg.cdl_years == (2021, 2022, 2023, 2024, 2025)
    assert cfg.imagery_years == (2021, 2022, 2023, 2024, 2025)


def test_field_reporting_config_uses_canonical_manifest_dirs():
    cfg = pl.FieldReportingConfig(
        farm_name="T",
        field_boundary_path="f.geojson",
        grower_slug="grower-a",
        farm_slug="farm-b",
    )
    assert cfg.farm_manifest_dir == Path("data/growers/grower-a/farms/farm-b/manifests")
    assert cfg.field_manifest_dir("field-c") == Path(
        "data/growers/grower-a/farms/farm-b/fields/field-c/manifests"
    )


def test_paths_module_exposes_canonical_contract_locations():
    assert paths.grower_manifest_path("grower-a") == (
        paths.DATA_ROOT / "growers/grower-a/manifests/pipeline_schedule.json"
    )
    assert paths.farm_logs_path("grower-a", "farm-b") == (
        paths.DATA_ROOT / "growers/grower-a/farms/farm-b/logs/pipeline_runs.jsonl"
    )
    assert paths.field_feature_path("grower-a", "farm-b", "field-c", "ndvi_corn.png") == (
        paths.DATA_ROOT
        / "growers/grower-a/farms/farm-b/fields/field-c/derived/features/ndvi_corn.png"
    )
    assert paths.shared_cdl_raster_dir() == paths.DATA_ROOT / "shared/cdl/rasters"
    assert paths.shared_cdl_tables_dir() == paths.DATA_ROOT / "shared/cdl/derived/tables"
    assert paths.shared_cdl_full_composition_path(2021, 2025) == (
        paths.DATA_ROOT / "shared/cdl/derived/tables/iowa_cdl_2021_2025_full_composition.csv"
    )


def test_ndvi_card_outputs_include_peak_assets():
    outputs = gnc._card_outputs("field-c")
    assert outputs["corn_peak_95"] == (
        paths.DATA_ROOT
        / "growers/iowa-demo-grower/farms/iowa-demo-farm/fields/field-c/derived/features/ndvi_corn_peak_95.png"
    )
    assert outputs["soybean_peak_95_tif"] == (
        paths.DATA_ROOT
        / "growers/iowa-demo-grower/farms/iowa-demo-farm/fields/field-c/derived/features/ndvi_soybean_peak_95.tif"
    )


def test_select_monthly_scene_rows_keeps_best_scene_per_year_month():
    import pandas as pd

    rows = [
        {
            "sensor": "landsat",
            "scene_date": pd.Timestamp("2024-07-10"),
            "cloud_cover": 12.0,
            "mean_ndvi": 0.71,
            "ndvi_path": REPO_ROOT / "a.tif",
            "month": 7,
            "year": 2024,
        },
        {
            "sensor": "sentinel",
            "scene_date": pd.Timestamp("2024-07-12"),
            "cloud_cover": 12.0,
            "mean_ndvi": 0.74,
            "ndvi_path": REPO_ROOT / "b.tif",
            "month": 7,
            "year": 2024,
        },
        {
            "sensor": "sentinel",
            "scene_date": pd.Timestamp("2023-07-08"),
            "cloud_cover": 4.0,
            "mean_ndvi": 0.69,
            "ndvi_path": REPO_ROOT / "c.tif",
            "month": 7,
            "year": 2023,
        },
    ]

    selected = gnc._select_monthly_scene_rows(rows)
    assert len(selected) == 2
    assert [int(row["year"]) for row in selected] == [2023, 2024]
    assert str(selected[1]["sensor"]) == "sentinel"


def test_summarize_year_coverage_flags_missing_years():
    coverage = rp.summarize_year_coverage([2021, 2023, 2025], (2021, 2022, 2023, 2024, 2025))
    assert coverage["observed_years"] == [2021, 2023, 2025]
    assert coverage["missing_years"] == [2022, 2024]
    assert coverage["has_full_coverage"] is False


def test_choose_primary_ndvi_source_prefers_sentinel_on_tie():
    import pandas as pd

    sentinel = pd.DataFrame(
        [{"beginposition": "2025-07-01", "cloudcoverpercentage": 10.0, "scene_id": "s2-1"}]
    )
    landsat = pd.DataFrame(
        [{"acquisition_date": "2025-07-01", "cloud_cover": 10.0, "scene_id": "ls-1"}]
    )

    result = rp.choose_primary_ndvi_source(sentinel, landsat, target_date="2025-07-01")
    assert result["source"] == "sentinel"


def test_summarize_crop_history_uses_recent_five_year_window():
    import pandas as pd

    crop_mix = pd.DataFrame(
        {
            "field_id": ["F1"] * 6,
            "year": [2019, 2020, 2021, 2022, 2023, 2024],
            "crop_name": ["Corn", "Soybeans", "Corn", "Soybeans", "Corn", "Soybeans"],
            "pct": [90.0, 92.0, 91.0, 93.0, 94.0, 95.0],
        }
    )

    result = cdl.summarize_crop_history(crop_mix, window_years=5)
    row = result.iloc[0]
    assert row["history_start_year"] == 2020
    assert row["history_end_year"] == 2024
    assert row["history_years"] == 5
    assert row["rotation_sequence"] == "Soybeans -> Corn -> Soybeans -> Corn -> Soybeans"


def test_summarize_crop_history_adds_rotation_outlook():
    import pandas as pd

    crop_mix = pd.DataFrame(
        {
            "field_id": ["F1"] * 5,
            "year": [2020, 2021, 2022, 2023, 2024],
            "crop_name": ["Corn", "Soybeans", "Corn", "Soybeans", "Corn"],
            "pct": [95.0, 95.0, 95.0, 95.0, 95.0],
        }
    )

    result = cdl.summarize_crop_history(crop_mix)
    row = result.iloc[0]
    assert row["predicted_next_crop"] == "Soybeans"
    assert row["predicted_following_crop"] == "Corn"
    assert row["rotation_confidence"] in {"medium", "high"}
    assert "Heuristic outlook" in row["rotation_outlook"]


def test_growing_season_range_uses_expected_window():
    assert si.growing_season_range(2024) == "2024-03-01T00:00:00Z/2024-11-30T23:59:59Z"


def test_feature_datetime_and_cloud_cover_helpers():
    feature = {
        "properties": {
            "datetime": "2025-07-10T16:15:00Z",
            "eo:cloud_cover": 12.5,
        }
    }
    assert si.feature_datetime(feature).date().isoformat() == "2025-07-10"
    assert si.feature_cloud_cover(feature) == 12.5


def test_sentinel_asset_keys_accept_named_and_band_assets():
    named = {"assets": {"red": {}, "nir": {}, "scl": {}}}
    fallback = {"assets": {"B04": {}, "B08": {}, "SCL": {}}}
    assert si.sentinel_asset_keys(named) == {"red": "red", "nir": "nir", "scl": "scl"}
    assert si.sentinel_asset_keys(fallback) == {"red": "B04", "nir": "B08", "scl": "SCL"}


def test_landsat_asset_keys_match_planetary_computer_assets():
    feature = {"assets": {"red": {}, "nir08": {}, "qa_pixel": {}}}
    assert si.landsat_asset_keys(feature) == {"red": "red", "nir": "nir08", "qa": "qa_pixel"}


def test_normalize_year_entry_migrates_legacy_single_scene_shape():
    legacy = {
        "year": 2024,
        "scene_id": "scene-1",
        "scene_date": "2024-07-10",
        "cloud_cover": 4.2,
        "status": "complete",
        "raw_tiffs": {"red": "red.tif"},
        "ndvi_tif": "ndvi.tif",
    }
    normalized = dsi._normalize_year_entry(legacy)
    assert normalized["scene_count"] == 1
    assert len(normalized["scenes"]) == 1
    assert normalized["scenes"][0]["scene_id"] == "scene-1"


def test_select_scene_inventory_prefers_best_scene_per_month():
    features = [
        {"id": "a", "properties": {"datetime": "2024-06-10T00:00:00Z", "eo:cloud_cover": 10.0}},
        {"id": "b", "properties": {"datetime": "2024-06-20T00:00:00Z", "eo:cloud_cover": 5.0}},
        {"id": "c", "properties": {"datetime": "2024-07-05T00:00:00Z", "eo:cloud_cover": 7.0}},
    ]
    selected = dsi._select_scene_inventory(features, max_scenes_per_year=9)
    assert [feature["id"] for feature in selected] == ["b", "c"]


def test_preferred_cdl_full_composition_path_uses_available_canonical_file():
    preferred = paths.shared_cdl_preferred_full_composition_path()
    assert preferred.parent == paths.shared_cdl_tables_dir()


def test_dominant_crop_lookup_uses_highest_pct_by_year(tmp_path):
    crop_csv = tmp_path / "crop.csv"
    crop_csv.write_text(
        "field_id,year,crop_name,pct\nF1,2024,Corn,40\nF1,2024,Soybeans,60\nF1,2023,Corn,70\n",
        encoding="utf-8",
    )
    result = dnc._dominant_crop_lookup(crop_csv)
    assert result[("F1", 2024)] == "Soybeans"
    assert result[("F1", 2023)] == "Corn"


def test_crop_years_returns_sorted_matches():
    import pandas as pd

    join_df = pd.DataFrame(
        {
            "crop_name": ["Soybeans", "Corn", "Corn", "Unknown"],
            "year": [2023, 2024, 2022, 2025],
        }
    )
    assert gnc._crop_years(join_df, "Corn") == [2022, 2024]
    assert gnc._crop_years(join_df, "Soybeans") == [2023]


def test_select_current_season_scenes_prefers_sentinel_then_lower_cloud():
    import pandas as pd

    rows = [
        {
            "sensor": "landsat",
            "scene_date": pd.Timestamp("2025-06-12"),
            "cloud_cover": 1.0,
            "month": 6,
        },
        {
            "sensor": "sentinel",
            "scene_date": pd.Timestamp("2025-06-08"),
            "cloud_cover": 12.0,
            "month": 6,
        },
        {
            "sensor": "sentinel",
            "scene_date": pd.Timestamp("2025-07-03"),
            "cloud_cover": 8.0,
            "month": 7,
        },
        {
            "sensor": "sentinel",
            "scene_date": pd.Timestamp("2025-07-20"),
            "cloud_cover": 2.0,
            "month": 7,
        },
    ]
    selected = gnc._select_current_season_scenes(rows)
    assert [(row["sensor"], row["month"], row["cloud_cover"]) for row in selected] == [
        ("sentinel", 6, 12.0),
        ("sentinel", 7, 2.0),
    ]
