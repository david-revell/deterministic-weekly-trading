# ETF Get-Out Strategy & Higher-Volatility Rotation Cheatsheet

## 1. Exit Strategy for Higher-Volatility ETFs (Open Question)

For **higher-volatility ETFs** (e.g. EQQQ, SGLN), the best exit structure is still being explored.

Limit orders are likely still appropriate, because:

- You don’t midweek trade, so you’re never reacting to price.
- That means: your **limit ladder is your logic**.
- **Market orders = surrender. You want edge.**
- Higher-volatility ETFs = more spikes = more chance your limit orders get hit.

However, it’s unclear whether a 3-week structure is still appropriate. It may be too slow for ETFs that regularly swing 2–3% in a week.

### Possibilities:
- Compress exits into a **1-week** (or at most 2-week) ladder
- Use **wider spacing** to match bigger daily/weekly moves
- Still **front-load heavily**, but cover more ground in one shot

**Status:** This is an open design space. You're entering new territory — fast-moving, higher-volatility trades that still benefit from structure, but may require new rules.

---

## 2. High-Volatility ETF Rotation

### Anchor → Rotator Transition
- **Previous pairing (low-volatility)**: ISF (FTSE 100) + VUSA (S&P 500).  
- **New pairing (higher-volatility)**: EQQQ (Nasdaq-100) + SGLN (Gold).  

### Rationale
- ISF + VUSA = low-volatility anchors, limited weekly edge.  
- EQQQ + SGLN = higher-volatility instruments with broader ranges, offering:  
  - Larger pullbacks and rallies.  
  - Greater trading edge for weekly ladder systems.  
  - Complementary dynamics (tech vs gold often move differently).  

### Other Candidates
- **Tech/AI variants**: QQQ3 (leveraged, not recommended for long holding), ARKK, sector ETFs.  
- **Other commodities**: SLVR (Silver), PHAU (Physical Gold alternative).  
- **Rule**: Must be liquid, large AUM, and provide volatility edge vs ISF/VUSA.

---

## 3. Summary

- **Exit Strategy**: 3-week model may not apply for higher-volatility ETFs. Structure still being explored.  
- **Rotation Strategy**: Shift core holdings from low-volatility (ISF, VUSA) → higher-volatility (EQQQ, SGLN).  
- **Objective**: Exploit larger weekly ranges while keeping structure and discipline.