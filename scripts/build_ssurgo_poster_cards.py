#!/usr/bin/env python3
"""
build_ssurgo_poster_cards.py — Generate poster-ready SSURGO soil profile cards.

This script generates four types of poster cards from SSURGO SQLite data:
- Single profile visualization
- Multi-profile comparison
- Texture RGB coloring (sand=red, silt=green, clay=blue)
- Clustered profiles by similarity

Inputs:
- SQLite database with SSURGO schema (mapunit, component, chorizon tables)
- Optional MUKEY filters
- Optional dominant-component-only flag

Outputs:
- card_01_single_profile.{svg,pdf,png}
- card_02_compare_profiles.{svg,pdf,png}
- card_03_texture_profiles.{svg,pdf,png}
- card_04_clustered_profiles.{svg,pdf,png}
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def load_ssurgo_data(
    db_path: str,
    mukeys: list[str] | None = None,
    dominant_only: bool = False,
) -> pd.DataFrame:
    """
    Load and join SSURGO data from SQLite.

    Returns DataFrame with horizons joined to components and mapunits.
    """
    conn = sqlite3.connect(db_path)

    query = """
    SELECT 
        m.mukey,
        m.muname,
        c.cokey,
        c.compname,
        c.comppct_r,
        ch.chkey,
        ch.hzname,
        ch.hzdept_r,
        ch.hzdepb_r,
        ch.sandtotal_r,
        ch.silttotal_r,
        ch.claytotal_r,
        ch.om_r,
        ch.awc_r,
        ch.ph1to1h2o_r,
        ch.ksat_r,
        ch.dbthirdbar_r
    FROM mapunit m
    JOIN component c ON m.mukey = c.mukey
    JOIN chorizon ch ON c.cokey = ch.cokey
    WHERE ch.hzdept_r IS NOT NULL
      AND ch.hzdepb_r IS NOT NULL
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    if mukeys:
        df = df[df["mukey"].isin(mukeys)]

    if dominant_only:
        # Keep only the dominant component per map unit
        df = df.loc[df.groupby("mukey")["comppct_r"].idxmax()]

    # Create profile identifier
    df["profile_id"] = (
        df["mukey"].astype(str) + " | " + df["compname"] + " (" + df["comppct_r"].astype(str) + "%)"
    )

    return df


def plot_single_profile(df: pd.DataFrame, output_dir: Path) -> None:
    """Generate single profile visualization card."""
    fig, ax = plt.subplots(figsize=(10, 12))

    # Get first profile
    profile_id = df["profile_id"].unique()[0]
    profile = df[df["profile_id"] == profile_id]

    colors = plt.cm.Set3(np.linspace(0, 1, len(profile)))

    for idx, (_, row) in enumerate(profile.iterrows()):
        top = row["hzdept_r"]
        bottom = row["hzdepb_r"]
        height = bottom - top

        ax.barh(
            top + height / 2,
            1,
            height=height,
            color=colors[idx],
            edgecolor="black",
            linewidth=1.5,
        )

        # Add horizon label
        ax.text(
            0.5,
            top + height / 2,
            row["hzname"],
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_ylim(profile["hzdepb_r"].max() + 5, -5)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylabel("Depth (cm)", fontsize=12)
    ax.set_title(f"Soil Profile: {profile_id}", fontsize=14, fontweight="bold")
    ax.set_xticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    plt.tight_layout()

    # Save in multiple formats
    base_path = output_dir / "card_01_single_profile"
    fig.savefig(f"{base_path}.svg", format="svg", bbox_inches="tight")
    fig.savefig(f"{base_path}.pdf", format="pdf", bbox_inches="tight")
    fig.savefig(f"{base_path}.png", format="png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print("  Saved: card_01_single_profile.{svg,pdf,png}")


def plot_compare_profiles(df: pd.DataFrame, output_dir: Path, max_profiles: int = 6) -> None:
    """Generate multi-profile comparison card."""
    profile_ids = df["profile_id"].unique()[:max_profiles]
    n_profiles = len(profile_ids)

    fig, axes = plt.subplots(1, n_profiles, figsize=(3 * n_profiles, 12))
    if n_profiles == 1:
        axes = [axes]

    colors = plt.cm.tab10(np.linspace(0, 1, 10))

    for idx, (ax, profile_id) in enumerate(zip(axes, profile_ids)):
        profile = df[df["profile_id"] == profile_id]

        for hidx, (_, row) in enumerate(profile.iterrows()):
            top = row["hzdept_r"]
            bottom = row["hzdepb_r"]
            height = bottom - top

            ax.barh(
                top + height / 2,
                1,
                height=height,
                color=colors[hidx % 10],
                edgecolor="black",
                linewidth=1,
            )

            ax.text(
                0.5,
                top + height / 2,
                row["hzname"],
                ha="center",
                va="center",
                fontsize=8,
            )

        ax.set_ylim(profile["hzdepb_r"].max() + 5, -5)
        ax.set_xlim(-0.1, 1.1)
        ax.set_title(profile_id[:30] + "...", fontsize=9, rotation=45, ha="right")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    fig.suptitle("Profile Comparison", fontsize=14, fontweight="bold", y=0.98)
    plt.tight_layout()

    base_path = output_dir / "card_02_compare_profiles"
    fig.savefig(f"{base_path}.svg", format="svg", bbox_inches="tight")
    fig.savefig(f"{base_path}.pdf", format="pdf", bbox_inches="tight")
    fig.savefig(f"{base_path}.png", format="png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print("  Saved: card_02_compare_profiles.{svg,pdf,png}")


def plot_texture_profiles(df: pd.DataFrame, output_dir: Path, max_profiles: int = 6) -> None:
    """Generate texture RGB visualization (sand=red, silt=green, clay=blue)."""
    profile_ids = df["profile_id"].unique()[:max_profiles]
    n_profiles = len(profile_ids)

    fig, axes = plt.subplots(1, n_profiles, figsize=(3 * n_profiles, 12))
    if n_profiles == 1:
        axes = [axes]

    for idx, (ax, profile_id) in enumerate(zip(axes, profile_ids)):
        profile = df[df["profile_id"] == profile_id].copy()

        # Normalize texture components to 0-1 for RGB
        profile["sand_norm"] = profile["sandtotal_r"].fillna(0) / 100
        profile["silt_norm"] = profile["silttotal_r"].fillna(0) / 100
        profile["clay_norm"] = profile["claytotal_r"].fillna(0) / 100

        for _, row in profile.iterrows():
            top = row["hzdept_r"]
            bottom = row["hzdepb_r"]
            height = bottom - top

            # RGB color: sand=red, silt=green, clay=blue
            color = (
                row["sand_norm"],
                row["silt_norm"],
                row["clay_norm"],
            )

            ax.barh(
                top + height / 2,
                1,
                height=height,
                color=color,
                edgecolor="black",
                linewidth=1,
            )

        max_depth = profile["hzdepb_r"].max()
        ax.set_ylim(max_depth + 5, -5)
        ax.set_xlim(-0.1, 1.1)
        ax.set_title(profile_id[:30] + "...", fontsize=9, rotation=45, ha="right")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    fig.suptitle(
        "Texture RGB Profiles (Sand=Red, Silt=Green, Clay=Blue)",
        fontsize=14,
        fontweight="bold",
        y=0.98,
    )
    plt.tight_layout()

    base_path = output_dir / "card_03_texture_profiles"
    fig.savefig(f"{base_path}.svg", format="svg", bbox_inches="tight")
    fig.savefig(f"{base_path}.pdf", format="pdf", bbox_inches="tight")
    fig.savefig(f"{base_path}.png", format="png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print("  Saved: card_03_texture_profiles.{svg,pdf,png}")


def plot_clustered_profiles(df: pd.DataFrame, output_dir: Path, max_profiles: int = 6) -> None:
    """Generate clustered profiles visualization."""
    profile_ids = df["profile_id"].unique()[:max_profiles]

    # Prepare clustering data
    cluster_data = []
    profile_keys = []

    for profile_id in profile_ids:
        profile = df[df["profile_id"] == profile_id]

        # Aggregate profile features
        features = {
            "avg_sand": profile["sandtotal_r"].mean(),
            "avg_silt": profile["silttotal_r"].mean(),
            "avg_clay": profile["claytotal_r"].mean(),
            "avg_om": profile["om_r"].mean(),
            "avg_ph": profile["ph1to1h2o_r"].mean(),
            "depth": profile["hzdepb_r"].max(),
            "n_horizons": len(profile),
        }

        cluster_data.append(list(features.values()))
        profile_keys.append(profile_id)

    # Convert to DataFrame and handle missing values
    cluster_df = pd.DataFrame(cluster_data)
    cluster_df = cluster_df.fillna(cluster_df.mean())

    if len(cluster_df) < 2:
        print("  Skipping clustering: need at least 2 profiles")
        return

    # Standardize and cluster
    scaler = StandardScaler()
    scaled = scaler.fit_transform(cluster_df)

    n_clusters = min(3, len(cluster_df))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled)

    # Plot clustered profiles
    fig, axes = plt.subplots(1, len(profile_ids), figsize=(3 * len(profile_ids), 12))
    if len(profile_ids) == 1:
        axes = [axes]

    cluster_colors = plt.cm.Set2(np.linspace(0, 1, n_clusters))

    for idx, (ax, profile_id) in enumerate(zip(axes, profile_ids)):
        profile = df[df["profile_id"] == profile_id]
        cluster_id = cluster_labels[idx]

        for _, row in profile.iterrows():
            top = row["hzdept_r"]
            bottom = row["hzdepb_r"]
            height = bottom - top

            ax.barh(
                top + height / 2,
                1,
                height=height,
                color=cluster_colors[cluster_id],
                edgecolor="black",
                linewidth=1,
                alpha=0.8,
            )

        max_depth = profile["hzdepb_r"].max()
        ax.set_ylim(max_depth + 5, -5)
        ax.set_xlim(-0.1, 1.1)
        ax.set_title(
            f"{profile_id[:25]}...\n(Cluster {cluster_id + 1})",
            fontsize=8,
            rotation=45,
            ha="right",
        )
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    fig.suptitle(
        f"Clustered Profiles (k={n_clusters})",
        fontsize=14,
        fontweight="bold",
        y=0.98,
    )
    plt.tight_layout()

    base_path = output_dir / "card_04_clustered_profiles"
    fig.savefig(f"{base_path}.svg", format="svg", bbox_inches="tight")
    fig.savefig(f"{base_path}.pdf", format="pdf", bbox_inches="tight")
    fig.savefig(f"{base_path}.png", format="png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print("  Saved: card_04_clustered_profiles.{svg,pdf,png}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build SSURGO poster cards from SQLite database",
    )
    parser.add_argument(
        "--db",
        required=True,
        help="Path to SSURGO SQLite database",
    )
    parser.add_argument(
        "--out",
        default="outputs/cards",
        help="Output directory (default: outputs/cards)",
    )
    parser.add_argument(
        "--dominant-only",
        action="store_true",
        help="Keep only dominant component per map unit",
    )
    parser.add_argument(
        "--max-profiles",
        type=int,
        default=6,
        help="Maximum number of profiles to visualize (default: 6)",
    )
    parser.add_argument(
        "--mukeys",
        nargs="+",
        help="Optional list of MUKEYs to filter",
    )

    args = parser.parse_args()

    # Validate database exists
    db_path = Path(args.db)
    if not db_path.exists():
        print(f"Error: Database not found: {db_path}")
        sys.exit(1)

    # Create output directory
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading SSURGO data from: {db_path}")
    df = load_ssurgo_data(
        str(db_path),
        mukeys=args.mukeys,
        dominant_only=args.dominant_only,
    )

    if len(df) == 0:
        print("Error: No data found matching criteria")
        sys.exit(1)

    n_profiles = df["profile_id"].nunique()
    print(f"Loaded {len(df)} horizons from {n_profiles} profiles")

    if args.dominant_only:
        print("  Filtered to dominant components only")

    if args.mukeys:
        print(f"  Filtered to MUKEYs: {args.mukeys}")

    print(f"\nGenerating poster cards in: {output_dir}")

    # Generate all four card types
    plot_single_profile(df, output_dir)
    plot_compare_profiles(df, output_dir, max_profiles=args.max_profiles)
    plot_texture_profiles(df, output_dir, max_profiles=args.max_profiles)
    plot_clustered_profiles(df, output_dir, max_profiles=args.max_profiles)

    print(f"\nDone! Generated 4 card types in {output_dir}/")
    print("  - card_01_single_profile.{svg,pdf,png}")
    print("  - card_02_compare_profiles.{svg,pdf,png}")
    print("  - card_03_texture_profiles.{svg,pdf,png}")
    print("  - card_04_clustered_profiles.{svg,pdf,png}")


if __name__ == "__main__":
    main()
