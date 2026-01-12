# Design And Status
**Deterministic Weekly Trading**  
*DESIGN.md*  

---

## 1. Purpose

1.1 Provide a shared understanding of the current trading logic.  
1.2 Record known gaps and keep a short, ordered work list.  
1.3 Keep the repo intentionally minimal and beginner-friendly.  

## 2. Data / Inputs

2.1 Inputs include CSV-based weekly price history with `Price` (renamed to `Close`).  
2.2 EMA/MACD-H enrichment writes Excel outputs for weekly files.  
2.3 Summary snapshots are written to a separate Excel file per ETF.  

## 3. Core Logic

3.1 ETF health scoring (1-5) from EMA slopes and MACD-H signals.  
3.2 Worksheet logic references: `docs/atr_logic.md`, `docs/summary_logic.md`.  

## 4. Current Status

4.1 Implemented:  
4.1.1 `src/etf_health.py` with `etf_health_score`.  
4.1.2 `src/ema_macd.py` with EMA/MACD-H calculations (EMA-5/12/26).  
4.1.3 `src/ema_macd_excel.py` to enrich weekly Excel files.  
4.1.4 `src/atr.py` with TR/ATR calculations.  
4.1.5 `src/weekly_summary_excel.py` to generate latest-week summary Excel files.  
4.1.6 `docs/atr_logic.md` and `docs/summary_logic.md` with current worksheet logic.  
4.1.7 `examples/` with sample CSV/Excel outputs.  
4.1.8 Latest-week summary table includes ATR bands, EMA(5/12/26), PP (S1/S2/R1/R2), and HH(5).  

4.2 Not implemented:  
4.2.1 CLI or file parsing.  
4.2.2 Automated tests.  

## 5. Workboard

5.1 Planned:  
5.1.1 Add fill percentage stats to summary outputs (start with ATR; placeholders for others).  
5.1.2 Add Avg. Buy Price input (manual or frontend-provided) to summary output.  
5.1.3 (Nice to have) Improve summary formatting (column widths, spacing tweaks).  
5.1.4 (Nice to have) Improve Excel column auto-width to avoid ####.  
5.1.5 Add a CLI flag for custom data directory in weekly price summary.  
5.1.6 Implement CSV data handling for ETF health scoring.  
5.1.7 Add tests for etf_health_score.  
5.1.8 Add a minimal CLI when ready.  
5.1.9 (Optional / future) Explore JSON input support for CLI or integrations.

5.2 In Progress:  
5.2.1 None.  

5.3 Done:  
5.3.1 Core `etf_health_score` function.  
5.3.2 CSV to Excel EMA/MACD-H enrichment workflow.  
5.3.3 Excel formatting (layout, trends, conditional formatting).  
