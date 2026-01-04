# ETF Weekly Pack Cheatsheet (Automation Plan with Streamlit Dashboard)

## Purpose
Automate weekly ETF reporting — replacing most manual spreadsheet steps — by generating a full **weekly pack** (numbers, orders, and charts) from Python with one command.

---

## Inputs
- **Historical CSVs:** Weekly OHLCV for each ETF (e.g. ISF, VUSA).
- **Ladder CSVs:** One per ETF  
  Columns → KPI | Price | %Change | Side (buy/sell) | Allocation% | Approx Fill%.
- **Cash_now:** Current portfolio cash.
- **Target allocations:** e.g. ISF 55 : VUSA 45.

---

## Core Calculations
- EMAs (5, 12, 26), MACD-H (sign + direction), ATR.
- 3-year pullback / rally bands: Very Likely | Typical | Ambitious | Extreme.
- Per-row **expected fill = Allocation × Fill %**.
- **Expected £ Buys / Sells** = Σ (Allocation × Fill × ETF £ allocation).
- **Cash projection:**  
  `Cash_next = Cash_now − E(Buys) + E(Sells)`
- **Post-trade allocation check** vs target.

---

## Outputs
- **weekly_summary.json** → All numeric results, machine-readable core.
- **orders_markdown.md** → Buy / sell tables + totals.
- **charts/** →  
  Price + EMAs, MACD-H bars, ATR trend, Ladder bar visuals.

---

## Run Example
```bash
python weekly_pack.py --cash 2936.82 --isf_ladder isf_ladder.csv --vusa_ladder vusa_ladder.csv --out ./wk_2025_09_01
```

---

## MVP (Minimum Viable Product)
Inputs: `isf_ladder.csv`, `vusa_ladder.csv`, `cash_now`.  
Outputs: Console summary lines for each ETF and combined cash projection.  
Goal: Validate JSON + markdown generation before adding charting.

---

## Streamlit Dashboard (Next Phase)

### Purpose
Add an interactive **dashboard** layer to visualise the weekly outputs. Streamlit hosts the web UI; Plotly generates the charts.

### Installation
```bash
pip install streamlit plotly pandas
```

### dashboard.py (example)
```python
import streamlit as st
import pandas as pd, json
import plotly.express as px

# Load JSON summary
with open("weekly_summary.json") as f:
    data = json.load(f)

st.title("ETF Weekly Pack Dashboard")

# Summary table
st.subheader("Portfolio Summary")
summary = {
    "Week start": data["week_start"],
    "Cash start (£)": data["cash_start"],
    "Cash expected end (£)": data["cash_expected_end"]
}
st.table(pd.DataFrame(summary, index=[0]))

# ETF breakdown
etf_df = pd.DataFrame([
    {
        "ETF": k,
        "Close": v["close"],
        "ATR": v["atr"],
        "MACD-H": v["macd_h"]["value"],
        "Direction": v["macd_h"]["direction"],
        "E(Buys £)": sum(x["exp_cash"] for x in v.get("ladder_expectation", []))
    }
    for k, v in data["etfs"].items()
])

st.subheader("ETF Details")
st.dataframe(etf_df)

# Visuals
st.subheader("ATR vs Close")
fig = px.scatter(etf_df, x="ATR", y="Close", color="ETF", size="E(Buys £)", hover_name="ETF")
st.plotly_chart(fig)
```

### Run the Dashboard
```bash
streamlit run dashboard.py
```
Opens a free local web dashboard at [http://localhost:8501](http://localhost:8501).

---

## Future Extensions
- Auto-detect ETF list (e.g. EQQQ, SGLN).
- Add historical price + EMA line plots.
- Add buy/sell ladder visualisations.
- Optional Excel export via `openpyxl`.
- Integrate into `etf_weekly_pack_plan_v1.md` master cheatsheet.

---

*Cheatsheet version 2 — updated 05 Oct 2025 to include Streamlit dashboard phase.*
