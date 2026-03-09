#!/usr/bin/env python3
"""Aggregate field weather into canonical county/FIPS weather tables."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
_REPO_ROOT = _SCRIPTS_DIR.parents[1]
sys.path.insert(0, str(_SCRIPTS_DIR))
sys.path.insert(0, str(_SCRIPTS_DIR / "lib"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grower-slug", default="iowa-demo-grower")
    parser.add_argument("--farm-slug", default="iowa-demo-farm")
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--weather-source", default="nasa-power")
    parser.add_argument(
        "--weather-csv",
        type=Path,
        default=None,
        help="Optional farm-level weather CSV override",
    )
    parser.add_argument(
        "--field-fips-path",
        type=Path,
        default=None,
        help="Optional field-to-FIPS mapping parquet override",
    )
    return parser.parse_args()


def _repo_relative(path: Path) -> str:
    return str(path.resolve().relative_to(_REPO_ROOT))


def main() -> int:
    from paths import (
        farm_table_path,
        shared_geoadmin_counties_dir,
        shared_weather_county_table_path,
    )
    from reporting_bootstrap import ensure_canonical_data_tree, ensure_skill_path

    args = parse_args()
    ensure_canonical_data_tree(grower_slug=args.grower_slug, farm_slug=args.farm_slug)
    ensure_skill_path("maturity-by-fips")

    from maturity_by_fips import (
        aggregate_weather_to_counties,
        build_county_weather_coverage_summary,
    )

    weather_csv = args.weather_csv or farm_table_path(
        args.grower_slug, args.farm_slug, "iowa_weather_2021_2025.csv"
    )
    field_fips_path = args.field_fips_path or farm_table_path(
        args.grower_slug, args.farm_slug, "field_fips_mapping.parquet"
    )

    weather = pd.read_csv(weather_csv, parse_dates=["date"])
    mapping = pd.read_parquet(field_fips_path)
    county_lookup = pd.read_parquet(shared_geoadmin_counties_dir() / "fips_lookup.parquet")

    county_weather = aggregate_weather_to_counties(weather, mapping)
    county_weather = county_weather[county_weather["year"] == args.year].copy()
    coverage_summary = build_county_weather_coverage_summary(
        county_weather,
        county_lookup,
        weather_source=args.weather_source,
        year=args.year,
    )

    table_path = shared_weather_county_table_path(
        args.weather_source, args.year, "daily_weather_by_fips.parquet"
    )
    summary_path = shared_weather_county_table_path(
        args.weather_source, args.year, "county_weather_coverage_summary.json"
    )
    table_path.parent.mkdir(parents=True, exist_ok=True)
    county_weather.to_parquet(table_path, index=False)
    summary_path.write_text(json.dumps(coverage_summary, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "year": args.year,
                "weather_source": args.weather_source,
                "county_weather_path": _repo_relative(table_path),
                "coverage_summary_path": _repo_relative(summary_path),
                "row_count": int(len(county_weather)),
                "county_count_covered": int(coverage_summary["county_count_covered"]),
                "county_count_uncovered": int(coverage_summary["county_count_uncovered"]),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
