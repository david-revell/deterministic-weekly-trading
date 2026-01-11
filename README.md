# Deterministic Weekly Trading

**Status:** In progress (active)  
**Scope:** Deterministic rule-based analysis only. No execution, no live trading, no optimisation.

Minimal repo for implementing **explicit, inspectable weekly trading rules** over ETF price data.

## What works now
- CSV-based ingestion of historical ETF price data
- Weekly price change summaries
- Deterministic indicator logic (EMA/MACD-H calculations in `src/ema_macd.py`)
- Excel export with ordered columns, trend labels, and rich formatting
- Reproducible, rule-driven outputs (no learning, no tuning)

## Highlights
- End-to-end CSV → Excel pipeline with ordered OHLC + indicator columns
- Deterministic MACD/EMA outputs with trend flags (Up/Down)
- Excel polish: header styling, freeze panes, filters, number formats, no borders
- Conditional formatting for key signals (Change, Direction, Trend columns)

## Not implemented (by design / pending)
- Order execution or broker integration
- Backtesting engine
- Parameter optimisation
- Signal performance evaluation

## Layout
- `specs/` – formal specifications of trading rules and logic
- `src/` – Python implementations of deterministic logic
- `docs/` – design notes and rationale
- `data/` – local CSV inputs and generated Excel outputs (not versioned)
- `examples/` – small sample inputs/outputs for reference

## Example usage
1. Place ETF CSVs in `data/` matching `* Stock Price History.csv`
2. Ensure required columns exist: `Price`, `Low`, `High`
3. Run:
   ```bash
   python src/weekly_price_change_summary.py
   ```

## EMA/MACD-H Excel usage
1. Place `* Stock Price History.csv` files in `data/` with a `Price` column.
2. Run:
   ```bash
   python src/ema_macd_excel.py
   ```
3. Outputs `Weekly_<ETF>.xlsx` files in `data/` with EMA/MACD-H columns added and overwrites them on each run.
4. MACD formulas: `fast_line = EMA12 - EMA26`, `slow_line = EMA9(fast_line)`, `macd_h = fast_line - slow_line`.

## Examples
- `examples/` contains a trimmed CSV and its generated Excel output so you can see the expected format.
