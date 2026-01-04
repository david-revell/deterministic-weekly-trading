# ETF Performance Comparison Cheatsheet (v2)

| Column | Formula | Plain English explanation |
|---------|----------|---------------------------|
| **Baseline P/L (L)** | =IF(D2="","", I$2 × (D2/100) − SUMIF(Orders!B:B, MIN(Orders!B:B), Orders!I:I)) | Value of a single buy-and-hold position purchased at the baseline start price (GBX → £). |
| **Actual P/L (M)** | =IF(C2="","", (I2 × (D2/100) − I2 × (C2/100)) + J2) | Unrealised gain/loss on current holdings plus realised P/L from past trades. |
| **Edge (N)** | =IF(OR(C2="", D2=""), "", M2 − L2) | Outperformance vs buy-and-hold. |
| **Edge + Dividend (O)** | =IF(H2="","", H2 + N2) | Adds dividends back in for fair ETF-to-ETF comparison. |

---

## 0️⃣ Definitions

**Entry Price**  
The **Open** of the entry period (normally the Monday open for weekly trading, or the day’s open if day trading).  
If a **market order** is used, the **actual fill price** replaces the Open.

**Exit Price**  
The **Open** of the exit period (for weekly trading, the Monday morning of the exit week).  
If a **market order** is used for the exit, the **actual fill price** overrides the Open.

---
## 1️⃣ Defining the Baseline Start

**Purpose** – Anchor every ETF’s buy-and-hold comparator at a consistent, rule-based point.

**Baseline Start Rule**  
- Use the **first week a meaningful position exists** — ignore token or exploratory trades.  
- The **baseline price** is the **Monday Open** of that same week.  
- This ensures the benchmark is independent of ladder execution or fill timing.  

**Applies to all ETFs** — ISF, VUSA, SGLN, SMGB, EQQQ, etc.  
Each ETF’s start week will differ, but the rule is identical.

**Use Case (SMGB, May 2024)**  
- Early micro-fills before 13 May 2024 were pre-system noise.  
- Proper position formed week of 13 May 2024.  
- Baseline for that cycle = Monday Open (13 May 2024).  

This illustrates the principle: *the clock starts when exposure becomes real, priced at that Monday Open.*

---

## 2️⃣ Ongoing vs Final Edge

| Term | Definition | When Used |
|------|-------------|-----------|
| **Ongoing Edge** | Rolling metric while trades remain open. | Weekly tracking / diagnostic. |
| **Final Edge** | Full-cycle outcome after complete exit. | Used once final sell ladder closes. |

**Final Edge Formula**  
```
Final Edge (£) = (Total Exit Proceeds + Cum Dividends) − (Baseline Shares × Final Price_at_Exit)
```
Compares your entire structured cycle with a passive buy-and-hold investor who bought at that ETF’s baseline Monday Open and exited on the same week you did.

---

## 3️⃣ Interpretation Framework

| Observation | Meaning | Comment |
|--------------|----------|----------|
| **Edge > 0** | Structured trading beat buy-and-hold. | Positive edge. |
| **Edge ≈ 0** | Roughly equal performance. | Neutral cycle. |
| **Edge < 0** | Buy-and-hold outperformed. | Review ladder depth, entry timing, or rotation rules. |

---

## 4️⃣ Summary

- **Baseline week:** first meaningful position  
- **Baseline price:** Monday Open of that week  
- **Applies to:** all ETF cycles (ISF, VUSA, SGLN, SMGB, EQQQ …)  
- **Ongoing edge:** live weekly diagnostic  
- **Final edge:** definitive performance verdict after full exit  

---

*Version 2 — adds universal baseline-start rule, clarifies ongoing vs final edge, and includes SMGB (May 2024) as example use case.*
