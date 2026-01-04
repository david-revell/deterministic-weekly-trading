# ETF Performance Metrics Cheatsheet (v1)

## Purpose
Track **returns**, **volatility**, and **risk-adjusted performance** side-by-side — to see both how much the portfolio earns and how smoothly it earns it.

---

## 1️⃣ Core Return Metrics

| Metric | Formula | Meaning | When It’s Useful |
|---------|----------|----------|------------------|
| **Profit (£)** | =D–C | Raw money gained/lost. | Always — intuitive check. |
| **Total Return (%)** | =(D–C)/C | Growth since that row’s start value. | Snapshot of progress (not time-adjusted). |
| **CAGR (%)** | =(D/C)^(1/YEARFRAC(DATE(2024,8,29),A))-1 | Annualised rate of return since 29 Aug 2024. | The “speed” of growth once ≥6 months elapsed. |

### Interpretation
- **Total Return** shows “how much richer”.  
- **CAGR** shows “how fast it’s compounding”.  
- Ignore CAGR before ~6 months of data — it’s mathematically unstable when the year fraction is tiny.  
- After Aug 2025 (≥1 yr), CAGR becomes your clean efficiency headline.

---

## 2️⃣ Risk & Volatility Metrics

| Metric | Formula (row 2 example) | Meaning | Typical Range |
|---------|--------------------------|----------|----------------|
| **Weekly % Change** | =(D2/D1)-1 | Week-to-week movement driver. | ±0.5–1 % (low-vol ETFs) / ±2–3 % (EQQQ). |
| **Volatility (12 w)** | =IF(ROW()<13,"",STDEV.S(INDEX($G:$G,ROW()-11):INDEX($G:$G,ROW()))) | Rolling 12-week standard deviation of weekly % change. | 0.5–3 %. Higher = bumpier ride. |
| **Max Drawdown (%)** | =(D2-MAX($D$2:D2))/MAX($D$2:D2) | Distance from the historical peak. | 0 % (new high) → –10 % typical pullback. |

### Interpretation
- **Volatility** rises sharply when adding higher-vol ETFs (e.g. EQQQ).  
- **Max Drawdown** tells you the deepest hole you’ve sat through.  
- Use these to judge *stability*, not success — a rough ride can still be profitable.

---

## 3️⃣ Sharpe-Type Ratio (Simple)

| Formula | Meaning | Typical Readings |
|----------|----------|------------------|
| =IF(OR(H2=0,H2=""),"",E2/H2) | Total Return % ÷ Volatility % | 1 = OK,  2 = very good,  3 = exceptional |

It measures **return per unit of risk**.  
Higher Sharpe = efficient growth; falling Sharpe = more turbulence for same gain.

---

## 4️⃣ How to Read Them Together

| If you see… | What it means | Action |
|--------------|---------------|--------|
| **Rising CAGR, flat Vol** | You’re compounding efficiently. | Stay steady. |
| **Rising CAGR + Rising Vol** | Higher reward *and* higher risk (EQQQ effect). | Decide if swings are acceptable. |
| **Falling CAGR, high Vol** | Risk rising faster than return. | Review ladder structure or ETF mix. |
| **Stable Total Return + Falling Drawdown** | Portfolio recovering strongly. | Positive signal. |

---

## 5️⃣ Practical Takeaway

- **CAGR = Efficiency** (long-term yardstick)  
- **Total Return = Progress** (cash reality)  
- **Volatility = Noise Level**  
- **Drawdown = Pain Level**  
- **Sharpe = Skill / Consistency**

You don’t need to watch all weekly — use the risk columns to explain *why* CAGR shifts when market noise rises.

---

*Cheatsheet version 1 — summarises ETF performance tracking logic after transition from ISF→VUSA→EQQQ (Oct 2025).*
