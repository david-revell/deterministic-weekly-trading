# ETF Lean Ladder Move

This cheatsheet documents the decision to **remove weaker levels** (EMA(5), LL(5), pivots, etc.) and commit to a **lean ladder structure** built only from strong weekly anchors. It combines rationale, a worked scenario, and the psychology behind the change.

---

## 1. Rationale: Why remove weaker levels?

- **Weekly relevance**: EMA(5) and LL(5) are daily constructs. On weekly charts, they are noisy and lack institutional weight.
- **Dilution risk**: When clustered between stronger levels (e.g. S1 and 0.5x ATR), they pull the average entry shallower, reducing edge.
- **Clarity**: A lean ladder (4–5 levels) is easier to track, remember, and deploy consistently week after week.
- **Professional standard**: Institutional and quant desks concentrate size at robust anchors (ATR multiples, EMA(12/26), S1/S2). They do not scatter across weaker levels for comfort.

**Conclusion:** The expanded ladder guarantees more fills, but the lean ladder delivers higher-quality entries and a cleaner framework.

---

## 2. Worked Example (VUSA, September 2025)

**Setup:**
- Previous close = 90.76
- Next week’s low assumed = 89.85 (so both S1 and 0.5x ATR trigger)

**Expanded vs Lean Ladders:**

| KPI                  | Value   | % change | Expanded Allocation % | Lean Allocation % |
|----------------------|---------|----------|------------------------|-------------------|
| Current Close Price  | 90.76   | 0.00%    | 0                      | 0                 |
| 0.25x ATR (Below)    | 90.33   | -0.47%   | 15                     | 15                |
| EMA(5)               | 90.31   | -0.50%   | 15                     | 0                 |
| Average (buy) Price  | 90.16   | -0.66%   | 0                      | 0                 |
| S1                   | 90.12   | -0.71%   | 20                     | 25                |
| 0.5x ATR (Below)     | 89.91   | -0.94%   | 30                     | 35                |
| S2                   | 89.48   | -1.41%   | 10                     | 15                |
| LL(5)                | 89.31   | -1.60%   | 5                      | 0                 |
| 1x ATR (Below)       | 89.06   | -1.88%   | 5                      | 10                |

**Result in this scenario:**
- Expanded ladder fills EMA(5), S1, 0.5x ATR → larger portion spread across clustered levels → **average entry ≈ 90.11**
- Lean ladder fills only S1, 0.5x ATR → concentration in stronger zones → **average entry ≈ 90.00**

**Outcome:** Both ladders fill, but the expanded ladder is diluted upwards; the lean ladder delivers a deeper, stronger entry.

---

## 3. Psychology: Why this feels hard

- **Fill bias:** More orders = more fills. This feels good psychologically, even if it weakens the edge.
- **Pride in old strategies:** Hard to abandon constructs originally adapted from daily trading (EMA5, LL5), even when the evidence says they don’t add value.
- **Fear of missing out:** Removing levels feels like leaving money on the table, even though backtests show the real profit lies in better average entries, not raw fill count.

---

## 4. Summary

- **Expanded ladder:** more fills, shallower entries, psychological comfort.
- **Lean ladder:** fewer fills, deeper entries, professional alignment.
- **Decision:** Commit to lean ladder. Trust the data, respect the edge, resist comfort fills.

*Note: This refinement currently applies only to **buy ladders**. Sell ladders remain monotonic, where additional levels act as insurance rather than dilution. Trimming sell levels is not considered useful at this stage, but this can be reviewed in future.*

*Last reviewed: Week of 06.09.2025*


---

## 5. RNF vs RNC Clarification

- **RNF (Round Number Floor):** Removed. It is arbitrary, scale-dependent, and overlaps with stronger anchors like ATR multiples and S1/S2. Including it risks diluting average entries, which contradicts the lean ladder principle.  
- **RNC (Round Number Ceiling):** Retained. On the sell side, round-number ceilings remain useful for opportunistic spikes and align with the monotonic sell ladder logic.  

**Decision:** RNF is cut permanently from buy ladders; RNC continues as part of sell ladders where appropriate.
