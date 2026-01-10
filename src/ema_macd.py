"""EMA and MACD-H calculations for weekly ETF price data."""

from __future__ import annotations

from typing import Iterable

import pandas as pd


def manual_ema(prices: pd.Series, span: int) -> pd.Series:
    """Calculate EMA manually to match spreadsheet-style logic."""
    if span <= 0:
        raise ValueError("span must be a positive integer")
    if prices.empty:
        return pd.Series([], index=prices.index, dtype="float64")
    if len(prices) < span:
        return pd.Series([float("nan")] * len(prices), index=prices.index)

    alpha = 2 / (span + 1)
    values = prices.tolist()
    ema_values = [float("nan")] * len(values)
    prev_ema = None
    seeded = False

    for i in range(len(values)):
        window_start = i - span + 1
        if not seeded:
            if window_start >= 0:
                window = values[window_start : i + 1]
                if all(pd.notna(v) for v in window):
                    prev_ema = sum(window) / span
                    ema_values[i] = prev_ema
                    seeded = True
            continue

        if pd.isna(values[i]):
            prev_ema = None
            seeded = False
            continue

        prev_ema = values[i] * alpha + prev_ema * (1 - alpha)
        ema_values[i] = prev_ema

    return pd.Series(ema_values, index=prices.index)


def add_ema_macd_features(
    df: pd.DataFrame,
    close_column: str = "close",
    spans: Iterable[int] = (12, 26),
    signal_span: int = 9,
) -> pd.DataFrame:
    """Add EMA (12, 26) and MACD histogram columns to a DataFrame."""
    spans_list = list(spans)
    if len(spans_list) < 2:
        raise ValueError("spans must contain at least two EMA periods")

    df = df.copy()
    for span in spans_list:
        df[f"ema_{span}"] = manual_ema(df[close_column], span)

    fast_span, slow_span = spans_list[0], spans_list[1]
    df["fast_line"] = df[f"ema_{fast_span}"] - df[f"ema_{slow_span}"]
    df["slow_line"] = manual_ema(df["fast_line"], signal_span)
    df["macd_h"] = (df["fast_line"] - df["slow_line"]).round(4)

    columns_to_round = [
        *(f"ema_{span}" for span in spans_list),
        "fast_line",
        "slow_line",
        "macd_h",
    ]
    df[columns_to_round] = df[columns_to_round].round(4)
    return df


__all__ = ["manual_ema", "add_ema_macd_features"]
