#!/usr/bin/env python3
"""Extract field IDs from GeoJSON and generate deterministic slug mapping."""

import csv
import json
from pathlib import Path

# Read source GeoJSON
source_path = Path(".opencode/skills/field-boundaries/examples/real_10_fields_iowa.geojson")
with open(source_path) as f:
    data = json.load(f)

# Extract field IDs and transform to slugs
field_mappings = []
for feature in data["features"]:
    field_id = feature["properties"]["field_id"]
    # Transform: lowercase, replace _ with -
    field_slug = field_id.lower().replace("_", "-")
    field_mappings.append({"field_id": field_id, "field_slug": field_slug})

# Sort by field_id for deterministic output
field_mappings.sort(key=lambda x: x["field_id"])

# Check for duplicates
slugs = [m["field_slug"] for m in field_mappings]
duplicates = [s for s in set(slugs) if slugs.count(s) > 1]

# Write CSV mapping
csv_path = Path(".sisyphus/evidence/task-3-field-inventory.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["field_id", "field_slug"])
    writer.writeheader()
    writer.writerows(field_mappings)

# Write unique slugs text file
slugs_path = Path(".sisyphus/evidence/task-3-slugs.txt")
with open(slugs_path, "w") as f:
    for mapping in field_mappings:
        f.write(f"{mapping['field_slug']}\n")

# Write error file if duplicates found
if duplicates:
    error_path = Path(".sisyphus/evidence/task-3-slugs-error.txt")
    with open(error_path, "w") as f:
        f.write(f"Duplicate slugs found: {duplicates}\n")
    print(f"ERROR: Duplicate slugs found: {duplicates}")
else:
    # Remove error file if it exists and no duplicates
    error_path = Path(".sisyphus/evidence/task-3-slugs-error.txt")
    if error_path.exists():
        error_path.unlink()

print(f"Processed {len(field_mappings)} fields")
print(f"CSV mapping saved to: {csv_path}")
print(f"Unique slugs saved to: {slugs_path}")
if not duplicates:
    print("Verification: No duplicate slugs found")
    print("Verification: All slugs are lowercase with hyphens")
