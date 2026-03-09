from __future__ import annotations

import argparse
import json

from reporting_bootstrap import ensure_canonical_data_tree, ensure_skill_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare repo-native annual maturity-by-FIPS pipeline scaffolding"
    )
    parser.add_argument("--year", type=int, required=True, help="Annual maturity output year")
    parser.add_argument(
        "--weather-source",
        default="nasa-power",
        help="Canonical shared weather source slug for annual maturity outputs",
    )
    parser.add_argument(
        "--list-steps",
        action="store_true",
        help="Print the planned annual maturity output roots and exit",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ensure_canonical_data_tree()
    ensure_skill_path("maturity-by-fips")

    from maturity_by_fips import AnnualMaturityConfig, build_year_output_index

    config = AnnualMaturityConfig(year=args.year, weather_source=args.weather_source)
    output_index = build_year_output_index(config)
    if args.list_steps:
        print(json.dumps(output_index, indent=2, sort_keys=True))
        return 0
    print(
        "Annual maturity scaffolding is ready. Use --list-steps to inspect canonical output targets "
        "while the full pipeline stages are implemented."
    )
    print(json.dumps(output_index, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
