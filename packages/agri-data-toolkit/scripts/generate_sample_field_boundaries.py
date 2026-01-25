#!/usr/bin/env python3
"""Generate sample field boundaries data for testing.

This script generates synthetic field boundaries and saves them as a local
Parquet file for use in unit tests.
"""

import argparse
from pathlib import Path

import geopandas as gpd

from agri_toolkit.core.config import Config
from agri_toolkit.downloaders.field_boundaries import FieldBoundaryDownloader


def generate_sample_data(output_path: Path, count: int = 10) -> None:
    """Generate sample field boundaries data by downloading real data.

    Args:
        output_path: Path to save the sample Parquet file.
        count: Number of fields to sample (default: 10).
    """
    print(f"Downloading real sample data ({count} fields) from Source Cooperative...")
    print("Applying filters: Region=corn_belt, Area=40-300 acres")

    # Use the downloader to fetch real data
    # We use the default URL (Source Cooperative)
    config = Config()
    downloader = FieldBoundaryDownloader(config=config)

    # Download a larger sample to allow for filtering
    # We use 'corn_belt' region (e.g., Iowa/Illinois)
    try:
        # Request more fields to ensure we have enough after filtering
        raw_count = count * 5
        gdf = downloader.download(
            count=raw_count,
            regions=["corn_belt"],
            crops=["corn", "soybeans"],
            output_format="geojson",  # Format doesn't matter here as we get a GDF
        )

        # Filter by acreage (40-300 acres)
        initial_len = len(gdf)
        gdf = gdf[(gdf["area_acres"] >= 40) & (gdf["area_acres"] <= 300)]
        print(f"Filtered {initial_len} fields down to {len(gdf)} fields based on acreage (40-300)")

        if len(gdf) < count:
            print(f"Warning: Only found {len(gdf)} fields matching criteria (requested {count})")
        else:
            gdf = gdf.iloc[:count]

    except Exception as e:
        print(f"Error downloading data: {e}")
        print("Falling back to synthetic data generation not implemented.")
        raise

    # The downloader returns data in EPSG:4326 with 'area_acres' calculated.
    # However, for the sample file to be a valid *source* for the downloader (in tests),
    # it needs to match the format of the Source Cooperative parquet file.
    # The Source Cooperative file is in EPSG:5070 (Albers) and has specific column names.

    # Reproject to EPSG:5070 (Albers Equal Area)
    gdf = gdf.to_crs("EPSG:5070")

    # Rename columns to match Source Cooperative schema (fiboa)
    # The downloader output has friendly names, we need to map them back to source names
    # field_id -> id
    # crop_code -> crop:code
    # crop_name -> crop:name
    # crop_code_list -> crop:code_list
    # region/state_fips -> (derived from id, so we don't strictly need them but good to keep)
    # administrative_area_level_2 -> (not in downloader output, but in source)

    # Note: The downloader output already has 'field_id', 'crop_code', etc.
    # We need to rename them to what the downloader *expects* to read from the parquet file.

    rename_map = {
        "field_id": "id",
        "crop_code": "crop:code",
        "crop_name": "crop:name",
        "crop_code_list": "crop:code_list",
    }
    gdf = gdf.rename(columns=rename_map)

    # Add missing columns that might be expected
    if "administrative_area_level_2" not in gdf.columns:
        gdf["administrative_area_level_2"] = "Unknown County"

    # Ensure we have the required columns for the downloader to read it back
    # The downloader query selects: id, crop:code, crop:name, crop:code_list, geometry

    # Save as Parquet
    gdf.to_parquet(output_path, index=False)
    print(f"Sample data saved to: {output_path}")

    # Verify the file
    verify_sample_data(output_path)


def verify_sample_data(parquet_path: Path) -> None:
    """Verify the generated sample data has correct schema."""
    print(f"Verifying sample data at {parquet_path}...")

    # Read back the data
    df = gpd.read_parquet(parquet_path)

    print(f"Sample data contains {len(df)} fields")
    print(f"Columns: {list(df.columns)}")
    print(f"CRS: {df.crs}")
    print(f"Sample crop codes: {df['crop:code'].unique()}")
    print(f"Sample areas (acres): {df['area_acres'].tolist()}")
    print("First 5 rows:")
    print(df.head(5))

    # Verify required columns
    required_columns = [
        "id",
        "crop:code",
        "crop:name",
        "crop:code_list",
        "administrative_area_level_2",
        "geometry",
        "area_acres",
    ]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    print("Sample data verification passed!")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate sample field boundaries data")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/data/sample_field_boundaries.parquet"),
        help="Output path for sample Parquet file",
    )
    parser.add_argument("--count", type=int, default=10, help="Number of fields to sample")

    args = parser.parse_args()

    # Create output directory
    args.output.parent.mkdir(parents=True, exist_ok=True)

    # Generate sample data
    generate_sample_data(args.output, args.count)


if __name__ == "__main__":
    main()
