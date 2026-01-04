# Design Notes

## Scope
This repo codifies deterministic portions of the ETF workflow. The first target is
ETF health scoring (1-5) based on EMA slopes and MACD-H state.

## Package layout
- Source code lives under `src/` to support clean imports and tooling.
- The library surface is `etf_health.etf_health_score`.
- The CLI entry point is `src/etf_health/cli.py` and a thin shim exists at
  `etf_health_cli.py` for convenience.

## Determinism
The scoring function is pure and accepts only categorical inputs:
- EMA slopes: `rising` or `falling`
- MACD-H sign: `positive` or `negative`
- MACD-H direction: `rising` or `falling`

No I/O or price data is required. All 16 input states map to a score 1-5.

## Testing
Matrix coverage is complete in `tests/test_etf_health.py` and asserts all 16
state combinations, plus input validation.