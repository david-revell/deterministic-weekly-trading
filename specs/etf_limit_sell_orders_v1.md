# ETF Sell Order Strategy Cheatsheet (Monotonic Model)

This cheatsheet outlines the strategy used for placing ETF **limit sell orders**. Unlike buys (which follow a bell-shaped model around frequent pullbacks), sells are structured as a **monotonically increasing allocation with price**. The purpose is not to clip steady bull runs, but to always have orders in place to capture opportunistic rallies, even extreme ones.

---

## ETF Allocation Comes First

* Each week, we set a **short-term target allocation** between ETFs (e.g. ISF : VUSA = 55:45)
* This allocation determines **how much of the holding** is assigned to potential sells
* Some weeks, an ETF may receive **0% of sell allocation** — that is expected
* Sell orders only apply to the ETF(s) allocated for trimming or exit

---

## Why Use a Monotonic Distribution?

Weekly rallies are **asymmetric**:
* Small rallies are common but should not trigger large disposals (avoid selling in bull runs)
* Larger rallies are rarer but are exactly where we want more size waiting
* Allocations therefore **increase with distance from the current price**

---

## Rally Zones (from ISF analysis)

| Zone            | Rally        | Probability | Interpretation                  |
|-----------------|--------------|-------------|---------------------------------|
| Very Likely     | +0.54%       | ~75%        | Seen in most weeks — minimal size |
| Typical (Median)| +1.10%       | ~50%        | Standard rally — small allocation |
| Ambitious       | +1.77%       | ~25%        | Worth sizing into               |
| Extreme         | +5.08%       | ~<1%        | Historical best — major focus   |

---

## Monotonic Allocation Rule-of-Thumb

* Place the **smallest allocations** near very likely rallies (avoid bleeding in trends)
* Increase allocations **step by step** as rally distance grows
* Maintain **large weight at extreme levels** (to never miss a spike)
* Adjust **spread width** depending on volatility (ATR still governs rally ranges)

---

## Approximate Allocation and Fill Probability

| Zone            | Allocation % | Fill Chance | Expected Fill % |
|-----------------|--------------|-------------|-----------------|
| Very Likely     | 0–5          | ~75%        | ~0–4            |
| Typical         | 10–15        | ~50%        | ~5–7            |
| Ambitious       | 20–25        | ~25%        | ~5–6            |
| Extreme         | 50–60        | ~<1%        | ~0.5            |

*Total expected fill (per ETF allocation): ~5–8%*

---

## Summary of the Sell Strategy

1. Allocate target sell exposure based on ETF weighting
2. Use monotonically increasing limit order ladder:
   * Small at near-price rallies
   * Build up heavier allocations further out
   * Keep extreme levels as the largest allocation
3. Expect ~5–8% of allocated size to execute over time
4. Remaining orders expire — no action needed

---

## Key Benefits

* Avoids over-selling in normal bull weeks
* Keeps exposure to upside intact
* Provides insurance against rare, sharp rallies
* Ensures consistent, repeatable structure

---

## Open Questions / Future Refinement

* Should near-price zones be eliminated entirely (pure “extremes only” model)?
* How best to adjust allocations when long-term bull momentum is strong?
* Is there value in linking sell allocation to position age (e.g. longer holds sell more aggressively)?

---

## Momentum Adjustment Rule

The sell ladder adapts depending on the weekly momentum/reversal score (1 = Strong Reversal, 5 = Strong Momentum):

| Score | Market Read         | Sell Order Shape                        |
|-------|---------------------|-----------------------------------------|
| **5** | Strong Momentum     | Monotonic increasing, shallow slope stretched wide |
| **4** | Momentum Up         | Monotonic increasing, steeper slope (more weight closer) |
| **3** | Neutral / Mixed     | Shallow monotonic (almost flat, allocations spread evenly) |
| **2** | Reversal Starting   | Bell-shaped near price (take profits early) |
| **1** | Strong Reversal     | Bell-shaped, heaviest near current price (accelerated exit) |

---

*Last reviewed: Week of 18.08.2025*
