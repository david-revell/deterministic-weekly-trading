"""ETF health scoring based on EMA slopes and MACD-H signals."""

from __future__ import annotations


_ALLOWED_SLOPES = {"rising", "falling"}
_ALLOWED_SIGNS = {"positive", "negative"}
_ALLOWED_DIRECTIONS = {"rising", "falling"}


def etf_health_score(
    ema26_slope: str,
    ema12_slope: str,
    macd_h_sign: str,
    macd_h_direction: str,
) -> int:
    """Return the ETF health score (1-5).

    Inputs are strings with values:
    - ema26_slope: "rising" or "falling"
    - ema12_slope: "rising" or "falling"
    - macd_h_sign: "positive" or "negative"
    - macd_h_direction: "rising" or "falling"
    """
    if ema26_slope not in _ALLOWED_SLOPES:
        raise ValueError(f"Invalid ema26_slope: {ema26_slope}")
    if ema12_slope not in _ALLOWED_SLOPES:
        raise ValueError(f"Invalid ema12_slope: {ema12_slope}")
    if macd_h_sign not in _ALLOWED_SIGNS:
        raise ValueError(f"Invalid macd_h_sign: {macd_h_sign}")
    if macd_h_direction not in _ALLOWED_DIRECTIONS:
        raise ValueError(f"Invalid macd_h_direction: {macd_h_direction}")

    # Decision tree from etf_health_1_to_5_v1.md
    if ema26_slope == "falling":
        return 1 if macd_h_sign == "negative" else 2

    if macd_h_sign == "positive":
        if ema12_slope == "rising":
            return 5 if macd_h_direction == "rising" else 4
        return 3

    return 2 if ema12_slope == "falling" else 3


__all__ = ["etf_health_score"]
