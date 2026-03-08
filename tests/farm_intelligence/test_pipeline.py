from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_SRC = REPO_ROOT / ".opencode" / "skills" / "farm-intelligence-reporting" / "src"
if str(SKILL_SRC) not in sys.path:
    sys.path.insert(0, str(SKILL_SRC))

import pipeline as pl
import reporting as rp


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
    first = pl.build_step_manifest("s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg, status="complete")
    second = pl.build_step_manifest("s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg)
    assert pl.step_is_stale(second, first) is False


def test_step_stale_when_output_missing(tmp_path):
    inp = tmp_path / "input.txt"
    out = tmp_path / "output.txt"
    inp.write_text("hello")
    out.write_text("done")
    cfg = pl.FieldReportingConfig(farm_name="T", field_boundary_path="f.geojson")
    first = pl.build_step_manifest("s", [inp], [out], [SKILL_SRC / "pipeline.py"], cfg, status="complete")
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
    m = pl.build_step_manifest("roundtrip", [inp], [], [SKILL_SRC / "pipeline.py"], cfg, status="complete")
    path = m.write(tmp_path / "roundtrip.json")
    loaded = pl.load_manifest(path)
    assert loaded is not None
    assert loaded.step_name == "roundtrip"
    assert loaded.status == "complete"


def test_compute_management_implications_returns_list():
    row = {
        "avg_ph": 5.5, "avg_om_pct": 1.0, "total_aws_inches": 3.0,
        "drainage_class": "Poorly drained", "headlands_pct": 22.0,
        "avg_clay_pct": 40.0, "crop_diversity": 1, "erosion_risk": "high",
    }
    result = rp.compute_management_implications(row)
    assert isinstance(result, list)
    assert len(result) >= 3


def test_compute_management_implications_optimal():
    row = {"avg_ph": 6.5, "avg_om_pct": 2.5, "total_aws_inches": 6.0}
    result = rp.compute_management_implications(row)
    assert any(w in " ".join(result).lower() for w in ("optimal", "good", "strong", "high", "within", "provides"))


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
