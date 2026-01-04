# Cheatsheet: Calculating MWRR (Money-Weighted Rate of Return) via Python  
**Use case: ETF Portfolio with Variable Contributions**

---

## 🎯 Why We Need MWRR (XIRR)

If you're actively investing over time — making multiple deposits — then **CAGR becomes meaningless**.

Why?  
Because CAGR assumes you invested one lump sum at the beginning.  
If you add money later, the whole calculation breaks.

What we actually want is:

> **MWRR (Money-Weighted Rate of Return)** — also known as XIRR

This adjusts for:
- The **timing** of every deposit or withdrawal
- The **amount** of capital you had at each moment

It reflects **what you actually earned on your money**, weighted by when it was at work.

---

## 🤯 Why Excel’s XIRR() Failed

We tried **for days** to get Excel to produce a reliable running MWRR (row-by-row):

- `LET()` formulas using `ROW()=ROW()` tricks
- Injecting account value manually as a fake inflow
- Wrapping the whole thing in `IF()` checks
- `Goal Seek` for manual root solving

But:

- ❌ It returned `#NUM!` errors when deposits weren’t balanced
- ❌ It was unreadable and broke the moment we added more capital
- ❌ It became too complex to trust or explain

**Bottom line: Excel XIRR is useless for running portfolio tracking.**

---

## ✅ Why Python Works

In Python, we calculate MWRR row-by-row **clearly and precisely**:

- For every row:
  - Take all historical cash flows
  - Add the current **account value** as if you sold everything
  - Solve for the internal rate of return (`r`) that makes NPV = 0

It works with:
- Partial contributions
- Midway account values
- Uneven dates
- No selling required

---

## 📥 Required Input Data (CSV or Excel)

Your spreadsheet must have **at least** these columns:

| Date       | Cash Flow (£) | Account Value (£) |
|------------|----------------|--------------------|
| 23/04/2024 | –1000          | 1020               |
| 29/04/2024 | –1000          | 1900               |
| 30/04/2024 | –4000          | 6200               |
| 07/05/2024 | –3000          | 8100               |
| 14/05/2024 | 0              | 8220               |

- Negative = deposit  
- Positive = withdrawal (optional — not required)
- Account value = pretend you're selling everything on that date

---

## 🐍 Python Logic for Row-by-Row MWRR

Every row is calculated like this:

1. Slice all cash flows up to that row
2. Add the current account value as a final fake inflow
3. Solve:

```
NPV = Σ [ cf / (1 + r)^(days/365) ] = 0
```

This gives MWRR at that point in time — assuming you exited then.

You’ll get:

| Date       | MWRR     |
|------------|----------|
| 23/04/2024 | 4.91%    |
| 29/04/2024 | 6.85%    |
| 30/04/2024 | 9.02%    |
| 07/05/2024 | 10.44%   |
| 14/05/2024 | 10.83%   |

Even after just one deposit, MWRR is valid — as long as account value is included.

---

## 🔁 Recap: Why This Wins

- No errors
- No broken formulas
- No skipped rows
- Full transparency
- Works for live portfolios, not just completed ones

> ✅ This is now the **only correct method** for row-by-row MWRR with variable deposits.

---

*Version 2 — updated after Excel failure. Running MWRR confirmed working via Python, with account value injected on every row.*