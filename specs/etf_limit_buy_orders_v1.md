# ETF Buy Order Strategy Cheatsheet (Bell-Shaped Model, Revised)

This cheatsheet outlines the strategy used for placing ETF **limit buy orders** using a bell-shaped allocation model. It is based on weekly pullback probabilities, current momentum, and price-level KPIs. This system is unique and has been built from first principles using empirical logic and structured judgment.

---

## ETF Allocation Comes First

* Each week, we set a **short-term target allocation** between ETFs (e.g. ISF : VUSA = 55:45)
* This allocation determines **how much cash** is assigned to each ETF
* Some weeks, an ETF may receive **0% of new cash** — that's expected
* Buy orders only apply to the ETF(s) allocated cash

---

## Why Use a Bell-Shaped Distribution?

We model the probability of pullbacks as a **rough bell curve**, centred around the *median weekly pullback*. This allows us to:

* Weight orders toward **likely pullback zones**
* Reduce wasteful orders in rarely reached extremes
* Maintain exposure without overtrading

---

## Pullback Zones (from Python analysis)

| Zone            | Pullback | Probability | Interpretation                  |
|-----------------|----------|-------------|---------------------------------|
| Very Likely     | –0.40%   | ~75%        | Seen in most weeks              |
| Typical (Median)| –0.90%   | ~50%        | Standard pullback               |
| Ambitious       | –1.85%   | ~25%        | Happens ~1 in 4 weeks           |
| Extreme         | –8.32%   | ~<1%        | Historical worst — ignore by default |

---

## Bell Curve Allocation Rule-of-Thumb

* Place the **highest allocations** near the *typical pullback* (~–0.9%)
* Taper allocations **above and below** this zone
* Adjust the **centre point** depending on momentum:
  * **Shift centre shallower** if momentum is strong (closer to current price)
  * **Shift centre deeper** if momentum is weakening (further from current price)
* Adjust the **spread width** depending on volatility (see next)

---

## Volatility Adjustment (via ATR)

* No separate volatility measure is needed
* Volatility is already **baked in** via the use of ATR multiples
* Wider ATR → include deeper levels (e.g. 1.5x, 2x ATR)
* Narrow ATR → compress the order zone closer to current price

---

## Approximate Allocation and Fill Probability

| Zone            | Allocation % | Fill Chance | Expected Fill % |
|-----------------|---------------|-------------|-----------------|
| Very Likely     | 10–15         | ~75%        | ~11–15          |
| Typical         | 40–50         | ~50%        | ~20–25          |
| Ambitious       | 25–30         | ~25%        | ~6–8            |
| Deep            | 5–10          | ~10%        | ~0.5–1          |
| Extreme         | 0–1           | <1%         | ~0              |

*Total expected fill (per ETF allocation): ~35–45%*

---

## Summary of the Buy Strategy

1. Allocate cash based on ETF target weighting (e.g. 55:45)
2. Use bell-shaped limit order ladder:
   * Centre around ~–0.9% pullback
   * Shift centre shallower or deeper depending on momentum
   * Scale width based on ATR levels
3. Expect ~40% of orders to fill in a typical week
4. Remaining orders simply expire — no action needed

---

## Key Benefits

* Matches actual market pullback probabilities
* Avoids chasing price
* Keeps capital active without full exposure
* Enables structured, repeatable decision-making

---

## Open Questions / Future Refinement

* Would a **shifted normal** or **Poisson-style** model better fit the actual pullback histogram?
* Should we include a **volatility bucket system** (e.g. Low / Medium / High) for wider/narrower ladders?
* Should we revisit **order count vs cash per order** logic in low-cash weeks?
* Is there value in auto-adjusting ladder spacing based on ATR percentile?

---

## Momentum Adjustment Rule

The buy ladder adapts depending on the weekly momentum/reversal score (1 = Strong Reversal, 5 = Strong Momentum):

| Score | Market Read         | Buy Order Centre Point |
|-------|---------------------|-------------------------|
| **5** | Strong Momentum     | Shift centre shallower, narrower spread |
| **4** | Momentum Up         | Centre near typical, slightly shallower |
| **3** | Neutral / Mixed     | Centre near typical, symmetric spread |
| **2** | Reversal Starting   | Shift centre deeper, wider spread |
| **1** | Strong Reversal     | Shift centre deeper, much wider spread |

---

*Last reviewed: Week of 05.09.2025*

