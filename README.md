# Deterministic Weekly Trading

Deterministic trading rules and utilities derived from the specs in `specs/`.

## Layout
- `specs/`: source specifications and cheatsheets
- `src/etf_health/`: ETF health scoring library and CLI
- `tests/`: pytest coverage for codified rules
- `examples/etf_health_input.json`: sample CLI input

## Quickstart (PowerShell)
```powershell
C:\venvs\deterministic-weekly-trading\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

## CLI usage
```powershell
python etf_health_cli.py examples/etf_health_input.json
```

JSON schema for the CLI:
```json
{
  "ema26_slope": "rising",
  "ema12_slope": "rising",
  "macd_h_sign": "positive",
  "macd_h_direction": "rising"
}
```
