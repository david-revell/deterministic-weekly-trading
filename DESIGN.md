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

## 3. Core Logic

3.1 ETF health scoring (1-5) from EMA slopes and MACD-H signals.  

## 4. Current Status

4.1 Implemented:  
4.1.1 `src/etf_health.py` with `etf_health_score`.  
4.1.2 `src/ema_macd.py` with EMA/MACD-H calculations.  
4.1.3 `src/ema_macd_excel.py` to enrich weekly Excel files.  

4.2 Not implemented:  
4.2.1 CLI or file parsing.  
4.2.2 Automated tests.  

## 5. Workboard

5.1 Planned:  
5.1.1 Reorder and expand EMA/MACD output columns.  
5.1.2 Add a CLI flag for custom data directory in weekly price summary.  
5.1.3 Implement CSV data handling for ETF health scoring.  
5.1.4 Add tests for etf_health_score.  
5.1.5 Add a minimal CLI when ready.  
5.1.6 (Optional / future) Explore JSON input support for CLI or integrations.

5.2 In Progress:  
5.2.1 None.  

5.3 Done:  
5.3.1 Core `etf_health_score` function.  
5.3.2 CSV to Excel EMA/MACD-H enrichment workflow.  
