"""CLI wrapper for ETF health scoring.

Reads JSON from stdin (or a file path arg) and prints the integer score.
"""

from __future__ import annotations

import json
import sys

from etf_health import etf_health_score


def _load_json_input() -> dict:
    if len(sys.argv) > 2:
        raise SystemExit("Usage: python etf_health_cli.py [input.json]")

    if len(sys.argv) == 2:
        with open(sys.argv[1], "r", encoding="utf-8") as handle:
            return json.load(handle)

    return json.load(sys.stdin)


def main() -> int:
    try:
        data = _load_json_input()
        score = etf_health_score(
            data["ema26_slope"],
            data["ema12_slope"],
            data["macd_h_sign"],
            data["macd_h_direction"],
        )
    except (KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2

    print(score)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
