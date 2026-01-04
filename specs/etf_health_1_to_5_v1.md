# ETF Health (scale 1 to 5)

This system is based on **Elder-style regime detection**, stripped back to **trend + momentum only**.  
**Price vs EMA is intentionally excluded** from scoring.

---

## Inputs (only these are used)

- 26-EMA slope: rising / falling  
- 12-EMA slope: rising / falling  
- MACD-H sign: positive / negative  
- MACD-H direction: rising / falling  

---

## 1. State Definitions (authoritative meaning)

### 5 – Strong Momentum
- 26-EMA rising  
- 12-EMA rising  
- MACD-H positive and rising  

Trend and momentum fully aligned.

---

### 4 – Momentum Up (cooling)
- 26-EMA rising  
- 12-EMA rising  
- MACD-H positive but falling  

Trend intact, momentum easing.

---

### 3 – Neutral / Mixed
- 26-EMA rising  
- MACD-H not aligned with EMA structure  

Typical digestion / chop. No action state.

---

### 2 – Weakness (two valid cases)

Pullback in uptrend:
- 26-EMA rising  
- 12-EMA falling  
- MACD-H negative  

Counter-rally in downtrend:
- 26-EMA falling  
- MACD-H positive  

Weakness, but **not** a confirmed reversal.

---

### 1 – Reversal (sell state)
- 26-EMA falling  
- MACD-H negative  
- Direction irrelevant  

Trend damage confirmed.

---

## 2. Full Matrix (all 16 states)

Order: Score | 26-EMA | 12-EMA | MACD-H sign | MACD-H direction

| Score | 26-EMA | 12-EMA | MACD-H sign | MACD-H direction |
|------:|--------|--------|-------------|------------------|
| 5 | rising | rising | positive | rising |
| 4 | rising | rising | positive | falling |
| 3 | rising | rising | negative | rising |
| 3 | rising | rising | negative | falling |
| 3 | rising | falling | positive | rising |
| 3 | rising | falling | positive | falling |
| 2 | rising | falling | negative | rising |
| 2 | rising | falling | negative | falling |
| 2 | falling | rising | positive | rising |
| 2 | falling | rising | positive | falling |
| 1 | falling | rising | negative | rising |
| 1 | falling | rising | negative | falling |
| 2 | falling | falling | positive | rising |
| 2 | falling | falling | positive | falling |
| 1 | falling | falling | negative | rising |
| 1 | falling | falling | negative | falling |

---

## 3. Decision Tree (how to think / code it)

1. Is 26-EMA falling?  
   - Yes →  
     - MACD-H negative → 1  
     - MACD-H positive → 2  
   - No → go to 2  

2. Is MACD-H positive?  
   - Yes →  
     - 12-EMA rising →  
       - MACD-H rising → 5  
       - MACD-H falling → 4  
     - 12-EMA falling → 3  
   - No →  
     - 12-EMA falling → 2  
     - 12-EMA rising → 3  

---

## 4. Allocation Rules (relative, unchanged)

Let K and L be the two ETF scores.

K − L =  0  → 50 / 50  
K − L = +1  → 55 / 45  
K − L ≥ +2  → 65 / 35  
K − L = −1  → 45 / 55  
K − L ≤ −2  → 35 / 65  

Notes:
- Allocation is relative, never absolute  
- Score 2 does NOT trigger selling  
- Only score 1 represents a regime that justifies exits  
- Most weeks will be 3 vs 4 or 2 vs 4 — this is normal  

---

This version is **coherent, robust, and allocation-safe**.
