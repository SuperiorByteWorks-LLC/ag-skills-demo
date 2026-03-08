from __future__ import annotations

import calendar

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def prepare_weather_reporting(weather: pd.DataFrame, base_temp_c: float = 10.0) -> pd.DataFrame:
    df = weather.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["doy"] = df["date"].dt.dayofyear
    df["month"] = df["date"].dt.month
    t_avg = (df["T2M_MAX"] + df["T2M_MIN"]) / 2.0
    df["gdd"] = np.maximum(0.0, t_avg - base_temp_c)
    df["gdd_cumulative"] = df.sort_values("date").groupby(["field_id", "year"])["gdd"].cumsum()
    return df


def summarize_weather_variability(weather: pd.DataFrame) -> pd.DataFrame:
    df = prepare_weather_reporting(weather)
    grouped = df.groupby("field_id")
    return grouped.agg(
        avg_temp_c=("T2M", "mean"),
        avg_precip_mm=("PRECTOTCORR", "mean"),
        annual_precip_mm=("PRECTOTCORR", "sum"),
        avg_gdd=("gdd", "mean"),
        max_gdd_cumulative=("gdd_cumulative", "max"),
        years=("year", "nunique"),
    ).reset_index()


def plot_temperature_doy_overlay(ax, weather: pd.DataFrame, title: str = "Temperature by day-of-year"):
    df = prepare_weather_reporting(weather)
    for year, group in df.groupby("year"):
        ax.plot(group["doy"], group["T2M"], label=str(year), linewidth=1.3, alpha=0.85)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlabel("Day of year")
    ax.set_ylabel("Temperature (C)")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7, ncol=3)
    return ax


def plot_gdd_doy_overlay(ax, weather: pd.DataFrame, title: str = "Cumulative GDD by day-of-year"):
    df = prepare_weather_reporting(weather)
    for year, group in df.groupby("year"):
        ax.plot(group["doy"], group["gdd_cumulative"], label=str(year), linewidth=1.6, alpha=0.9)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlabel("Day of year")
    ax.set_ylabel("GDD base 10 C")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7, ncol=3)
    return ax


def plot_precip_boxplot(ax, weather: pd.DataFrame, title: str = "Monthly precipitation distribution"):
    df = prepare_weather_reporting(weather)
    monthly = df.groupby(["year", "month"])["PRECTOTCORR"].sum().reset_index()
    positions = sorted(monthly["month"].unique())
    data = [monthly.loc[monthly["month"] == month, "PRECTOTCORR"].tolist() for month in positions]
    ax.boxplot(data, positions=positions, widths=0.6)
    ax.set_xticks(positions)
    ax.set_xticklabels([calendar.month_abbr[m] for m in positions], rotation=45, fontsize=8)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_ylabel("Monthly total precipitation (mm)")
    ax.grid(True, axis="y", alpha=0.3)
    return ax
