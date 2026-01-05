"""Summarize weekly pullback/rally ranges from ETF historical price CSVs."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
import pytz


def _clean_numeric(series: pd.Series) -> pd.Series:
    return series.astype(str).str.replace(",", "", regex=False).astype(float)


def summarize_file(file_path: Path) -> None:
    print(f"\nProcessing file: {file_path}\n")

    df = pd.read_csv(file_path)

    # Normalize numeric columns (exports sometimes include commas).
    df["Price"] = _clean_numeric(df["Price"])
    df["Low"] = _clean_numeric(df["Low"])
    df["High"] = _clean_numeric(df["High"])

    # Reverse so oldest week first (most files are newest-first).
    df = df.iloc[::-1].reset_index(drop=True)

    df["Close (last week)"] = df["Price"].shift(1)
    df["change_to_low"] = (df["Low"] - df["Close (last week)"]) / df[
        "Close (last week)"
    ] * 100
    df["change_to_high"] = (df["High"] - df["Close (last week)"]) / df[
        "Close (last week)"
    ] * 100

    df = df.dropna()

    low_percentiles = ["75%", "50%", "25%", "min"]
    high_percentiles = ["max", "75%", "50%", "25%"]

    low_desc = df[["change_to_low"]].describe().round(2).map(lambda x: f"{x:.2f}%")
    low_trimmed = low_desc.loc[low_percentiles]
    low_trimmed.index = [
        "Very likely pullback (75% of weeks were better)",
        "Typical pullback (median week)",
        "Ambitious pullback (only 25% of weeks were worse)",
        "Extreme pullback (worst recorded week)",
    ]

    print("Estimated % Pullback Ranges (from last week's close to this week's low):")
    print(low_trimmed)
    print("\n" + "-" * 40 + "\n")

    high_desc = (
        df[["change_to_high"]].describe().round(2).map(lambda x: f"{x:.2f}%")
    )
    high_trimmed = high_desc.loc[high_percentiles]
    high_trimmed.index = [
        "Extreme rally (best recorded week)",
        "Ambitious rally (top 25% of weeks)",
        "Typical rally (median week)",
        "Very likely rally (seen in 75% of weeks)",
    ]

    print("Estimated % Rally Ranges (from last week's close to this week's high):")
    print(high_trimmed)
    print("\n" + "=" * 80 + "\n")


def main() -> None:
    uk_time = datetime.now(pytz.timezone("Europe/London"))
    timestamp_str = uk_time.strftime("%a %d/%m/%Y %H:%M")
    print("Script last run on:", timestamp_str)

    data_dir = Path("data")
    file_list = sorted(data_dir.glob("* Stock Price History.csv"))
    if not file_list:
        raise FileNotFoundError(
            "No matching '* Stock Price History.csv' files found in data/."
        )

    for file_path in file_list:
        summarize_file(file_path)


if __name__ == "__main__":
    main()
