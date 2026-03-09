from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _SCRIPTS_DIR.parents[1]
sys.path.insert(0, str(_SCRIPTS_DIR))
sys.path.insert(0, str(_SCRIPTS_DIR / "lib"))


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
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild all annual maturity outputs even when target files already exist",
    )
    return parser.parse_args()


def _run_step(command: list[str]) -> None:
    result = subprocess.run(command, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def _iso_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def _repo_relative(path: Path) -> str:
    return str(path.resolve().relative_to(_REPO_ROOT))


def main() -> int:
    from reporting_bootstrap import ensure_canonical_data_tree, ensure_skill_path

    args = parse_args()
    ensure_canonical_data_tree()
    ensure_skill_path("maturity-by-fips")

    from manifest import read_json, write_json
    from maturity_by_fips import AnnualMaturityConfig, build_year_output_index
    from paths import shared_manifest_dir

    config = AnnualMaturityConfig(year=args.year, weather_source=args.weather_source)
    output_index = build_year_output_index(config)
    if args.list_steps:
        print(json.dumps(output_index, indent=2, sort_keys=True))
        return 0

    geoadmin_output = Path(output_index["geoadmin_root"]) / "l2_counties" / "metadata.json"
    field_fips_output = Path(output_index["field_fips_summary"])
    manifest_path = shared_manifest_dir() / f"maturity_by_fips_{args.year}.json"
    manifest = read_json(manifest_path, default={}) or {}
    manifest.update(
        {
            "year": args.year,
            "weather_source": args.weather_source,
            "updated_at": _iso_now(),
            "steps": manifest.get("steps", {}),
        }
    )

    steps: list[tuple[str, list[Path], list[str]]] = [
        (
            "geoadmin",
            [geoadmin_output],
            [
                sys.executable,
                "data/scripts/ingest/download_geoadmin.py",
                "--levels",
                "l0_countries",
                "l1_states",
                "l2_counties",
            ],
        ),
        (
            "field-fips",
            [field_fips_output],
            [sys.executable, "data/scripts/ingest/assign_field_fips.py"],
        ),
        (
            "county-weather",
            [
                Path(output_index["county_weather"]),
                Path(output_index["county_weather_summary"]),
            ],
            [
                sys.executable,
                "data/scripts/ingest/aggregate_weather_by_fips.py",
                "--year",
                str(args.year),
                "--weather-source",
                args.weather_source,
            ],
        ),
        (
            "county-gdd",
            [
                Path(output_index["corn_gdd"]),
                _REPO_ROOT / f"data/shared/corn_maturity/metadata/gdd_by_fips_{args.year}.json",
            ],
            [
                sys.executable,
                "data/scripts/ingest/calculate_gdd_by_fips.py",
                "--year",
                str(args.year),
                "--weather-source",
                args.weather_source,
            ],
        ),
        (
            "corn-rm",
            [
                Path(output_index["corn_rm"]),
                Path(output_index["corn_rm_csv"]),
                _REPO_ROOT / f"data/shared/corn_maturity/metadata/rm_by_fips_{args.year}.json",
            ],
            [
                sys.executable,
                "data/scripts/ingest/calculate_corn_rm_by_fips.py",
                "--year",
                str(args.year),
            ],
        ),
        (
            "soybean-mg",
            [
                Path(output_index["soybean_mg"]),
                Path(output_index["soybean_mg_csv"]),
                _REPO_ROOT / f"data/shared/soybean_maturity/metadata/mg_by_fips_{args.year}.json",
            ],
            [
                sys.executable,
                "data/scripts/ingest/calculate_soybean_mg_by_fips.py",
                "--year",
                str(args.year),
            ],
        ),
        (
            "maps",
            [
                Path(output_index["corn_map"]),
                Path(output_index["soybean_map"]),
            ],
            [
                sys.executable,
                "data/scripts/reporting/generate_maturity_maps.py",
                "--year",
                str(args.year),
            ],
        ),
    ]

    for step_name, output_paths, command in steps:
        step_record = dict(manifest["steps"].get(step_name, {}))
        primary_output = output_paths[0] if output_paths else None
        outputs_exist = bool(output_paths) and all(path.exists() for path in output_paths)
        if outputs_exist and not args.force:
            print(f"skip {step_name}: {primary_output}")
            step_record.update(
                {
                    "status": "skipped",
                    "output_path": _repo_relative(primary_output)
                    if primary_output is not None
                    else None,
                    "output_paths": [_repo_relative(path) for path in output_paths],
                    "updated_at": _iso_now(),
                }
            )
            manifest["steps"][step_name] = step_record
            continue
        print(f"run  {step_name}: {' '.join(command)}")
        _run_step(command)
        step_record.update(
            {
                "status": "complete",
                "output_path": _repo_relative(primary_output)
                if primary_output is not None
                else None,
                "output_paths": [_repo_relative(path) for path in output_paths],
                "updated_at": _iso_now(),
            }
        )
        manifest["steps"][step_name] = step_record

    write_json(manifest_path, manifest)

    print(json.dumps(output_index, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
