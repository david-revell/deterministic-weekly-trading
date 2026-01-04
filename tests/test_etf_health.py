import pytest

from etf_health import etf_health_score


@pytest.mark.parametrize(
    "ema26, ema12, macd_sign, macd_dir, expected",
    [
        ("rising", "rising", "positive", "rising", 5),
        ("rising", "rising", "positive", "falling", 4),
        ("rising", "rising", "negative", "rising", 3),
        ("rising", "rising", "negative", "falling", 3),
        ("rising", "falling", "positive", "rising", 3),
        ("rising", "falling", "positive", "falling", 3),
        ("rising", "falling", "negative", "rising", 2),
        ("rising", "falling", "negative", "falling", 2),
        ("falling", "rising", "positive", "rising", 2),
        ("falling", "rising", "positive", "falling", 2),
        ("falling", "rising", "negative", "rising", 1),
        ("falling", "rising", "negative", "falling", 1),
        ("falling", "falling", "positive", "rising", 2),
        ("falling", "falling", "positive", "falling", 2),
        ("falling", "falling", "negative", "rising", 1),
        ("falling", "falling", "negative", "falling", 1),
    ],
)
def test_etf_health_score_matrix(ema26, ema12, macd_sign, macd_dir, expected):
    assert etf_health_score(ema26, ema12, macd_sign, macd_dir) == expected


def test_etf_health_score_rejects_invalid_inputs():
    with pytest.raises(ValueError):
        etf_health_score("up", "rising", "positive", "rising")