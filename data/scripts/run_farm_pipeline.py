#!/usr/bin/env python3
"""
run_farm_pipeline.py — Master pipeline entrypoint.

Usage:
    python data/scripts/run_farm_pipeline.py \\
        --boundaries data/field-boundaries/iowa_10_fields.geojson \\
        [--farm-name "Iowa Demo Farm"] \\
        [--force]

Runs the full farm intelligence reporting pipeline from a single field
boundaries GeoJSON file.  Each step is idempotent and will be skipped if
inputs, code, and config are unchanged since the last run.

Outputs:
    data/EDA/field_cards/iowa_field_report_NN.png   — one per field
    data/EDA/iowa_farm_report.png                   — farm portfolio poster
    data/EDA/iowa_farm_report.html                  — self-contained HTML report
    data/reporting/manifests/                       — per-step manifests
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
_SCRIPTS = Path(__file__).parent


def _run(script: str, extra_env: dict | None = None) -> bool:
    cmd = [sys.executable, str(_SCRIPTS / script)]
    t0 = time.monotonic()
    result = subprocess.run(cmd, cwd=str(_REPO), capture_output=False)
    elapsed = time.monotonic() - t0
    status = "ok" if result.returncode == 0 else "FAILED"
    print(f"  {status}  ({elapsed:.1f}s)  {script}")
    return result.returncode == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Farm intelligence reporting pipeline")
    parser.add_argument("--boundaries", default="data/field-boundaries/iowa_10_fields.geojson",
                        help="Path to field boundaries GeoJSON")
    parser.add_argument("--farm-name", default="Iowa Demo Farm")
    parser.add_argument("--force", action="store_true", help="Force rerun all steps")
    args = parser.parse_args()

    boundaries = Path(args.boundaries)
    if not boundaries.exists():
        print(f"ERROR: field boundaries not found: {boundaries}")
        sys.exit(1)

    print()
    print("=" * 60)
    print(f"  Farm Intelligence Reporting Pipeline")
    print(f"  Farm: {args.farm_name}")
    print(f"  Boundaries: {boundaries}")
    print("=" * 60)

    steps = [
        ("11_generate_field_posters.py", "Field posters"),
        ("12_generate_aggregate_poster.py", "Farm portfolio poster"),
        ("13_generate_farm_html.py", "Self-contained HTML report"),
    ]

    all_ok = True
    for script, label in steps:
        print(f"\n[{label}]")
        ok = _run(script)
        if not ok:
            all_ok = False
            print(f"  Pipeline halted at: {script}")
            print("  Fix the error above and rerun.")
            sys.exit(1)

    print()
    print("=" * 60)
    if all_ok:
        print("  Pipeline complete.")
        print()
        print("  Outputs:")
        output_dir = _REPO / "data" / "EDA"
        for f in sorted(output_dir.glob("iowa_farm_report.*")):
            print(f"    {f.relative_to(_REPO)}")
        card_dir = output_dir / "field_cards"
        if card_dir.exists():
            cards = sorted(card_dir.glob("*.png"))
            print(f"    {card_dir.relative_to(_REPO)}/  ({len(cards)} field posters)")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
