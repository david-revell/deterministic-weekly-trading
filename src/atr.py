"""ATR calculations for weekly ETF price data."""

from __future__ import annotations

import pandas as pd


def add_atr_features(
    df: pd.DataFrame,
    high_column: str,
    low_column: str,
    close_column: str,
    window: int = 14,
) -> pd.DataFrame:
    """Add True Range and ATR (SMA) columns to the DataFrame."""
    if window <= 0:
        raise ValueError("window must be a positive integer")

    df = df.copy()
    high = df[high_column]
    low = df[low_column]
    close = df[close_column]
    prev_close = close.shift(1)

    tr_components = pd.concat(
        [
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    )
    true_range = tr_components.max(axis=1)
    true_range = true_range.where(prev_close.notna(), pd.NA)
    atr = true_range.rolling(window=window, min_periods=window).mean()

    df["true_range"] = true_range
    df["atr"] = atr
    return df


__all__ = ["add_atr_features"]
