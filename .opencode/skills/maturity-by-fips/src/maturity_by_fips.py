from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[4]
DATA_SCRIPTS_ROOT = REPO_ROOT / "data" / "scripts"
if str(DATA_SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(DATA_SCRIPTS_ROOT))


def _paths_module() -> Any:
    return importlib.import_module("paths")


@dataclass(slots=True)
class AnnualMaturityConfig:
    year: int
    weather_source: str = "nasa-power"

    @property
    def geoadmin_root(self) -> Path:
        return _paths_module().shared_geoadmin_dir()

    @property
    def corn_gdd_path(self) -> Path:
        return _paths_module().shared_corn_gdd_table_path(self.year)

    @property
    def county_weather_path(self) -> Path:
        return _paths_module().shared_weather_county_table_path(
            self.weather_source, self.year, "daily_weather_by_fips.parquet"
        )

    @property
    def county_weather_summary_path(self) -> Path:
        return _paths_module().shared_weather_county_table_path(
            self.weather_source, self.year, "county_weather_coverage_summary.json"
        )

    @property
    def corn_rm_path(self) -> Path:
        return _paths_module().shared_corn_rm_table_path(self.year)

    @property
    def soybean_mg_path(self) -> Path:
        return _paths_module().shared_soybean_mg_table_path(self.year)


def build_year_output_index(config: AnnualMaturityConfig) -> dict[str, str]:
    return {
        "geoadmin_root": str(config.geoadmin_root),
        "county_weather": str(config.county_weather_path),
        "county_weather_summary": str(config.county_weather_summary_path),
        "corn_gdd": str(config.corn_gdd_path),
        "corn_rm": str(config.corn_rm_path),
        "soybean_mg": str(config.soybean_mg_path),
    }


def aggregate_weather_to_counties(
    weather: pd.DataFrame,
    field_fips_mapping: pd.DataFrame,
) -> pd.DataFrame:
    mapping = cast(pd.DataFrame, field_fips_mapping.copy())
    mapping["field_id"] = mapping["field_id"].astype(str)
    mapping["fips"] = mapping["fips"].astype(str)
    mapping = cast(pd.DataFrame, mapping[mapping["fips"].str.len() > 0].copy())

    weather_frame = cast(pd.DataFrame, weather.copy())
    weather_frame["field_id"] = weather_frame["field_id"].astype(str)
    weather_frame["date"] = pd.to_datetime(weather_frame["date"])
    weather_frame["year"] = weather_frame["date"].dt.year.astype(int)

    mapping_fields = cast(
        pd.DataFrame,
        mapping[
            [
                "field_id",
                "field_slug",
                "fips",
                "state_fips",
                "county_fips",
                "county_name",
                "county_name_full",
            ]
        ].copy(),
    )

    joined = cast(pd.DataFrame, weather_frame.merge(mapping_fields, on="field_id", how="inner"))
    if joined.empty:
        return pd.DataFrame(
            {
                column: pd.Series(dtype="object")
                for column in [
                    "date",
                    "year",
                    "fips",
                    "state_fips",
                    "county_fips",
                    "county_name",
                    "county_name_full",
                    "field_count",
                    "source_field_ids",
                    "source_field_slugs",
                    "T2M",
                    "T2M_MAX",
                    "T2M_MIN",
                    "PRECTOTCORR",
                    "ALLSKY_SFC_SW_DWN",
                    "RH2M",
                    "WS10M",
                ]
            }
        )

    aggregated = (
        joined.groupby(
            [
                "date",
                "year",
                "fips",
                "state_fips",
                "county_fips",
                "county_name",
                "county_name_full",
            ],
            dropna=False,
        )
        .agg(
            field_count=("field_id", "nunique"),
            source_field_ids=("field_id", lambda values: sorted({str(value) for value in values})),
            source_field_slugs=(
                "field_slug",
                lambda values: sorted({str(value) for value in values if str(value)}),
            ),
            T2M=("T2M", "mean"),
            T2M_MAX=("T2M_MAX", "mean"),
            T2M_MIN=("T2M_MIN", "mean"),
            PRECTOTCORR=("PRECTOTCORR", "mean"),
            ALLSKY_SFC_SW_DWN=("ALLSKY_SFC_SW_DWN", "mean"),
            RH2M=("RH2M", "mean"),
            WS10M=("WS10M", "mean"),
        )
        .reset_index()
        .sort_values(["date", "fips"])
        .reset_index(drop=True)
    )
    return aggregated


def build_county_weather_coverage_summary(
    county_weather: pd.DataFrame,
    county_lookup: pd.DataFrame,
    *,
    weather_source: str,
    year: int,
) -> dict[str, object]:
    lookup = cast(pd.DataFrame, county_lookup.copy())
    lookup["fips"] = lookup["fips"].astype(str)
    county_weather_frame = cast(pd.DataFrame, county_weather.copy())
    county_weather_frame["fips"] = county_weather_frame.get(
        "fips", pd.Series(dtype="object")
    ).astype(str)

    covered = set(county_weather_frame["fips"].unique())
    all_counties = set(lookup["fips"].unique())
    uncovered = sorted(all_counties - covered)

    return {
        "weather_source": weather_source,
        "year": int(year),
        "county_count_total": int(len(all_counties)),
        "county_count_covered": int(len(covered)),
        "county_count_uncovered": int(len(uncovered)),
        "coverage_policy": "Counties without mapped field weather remain absent from the daily county weather table.",
        "uncovered_fips_sample": uncovered[:25],
    }
