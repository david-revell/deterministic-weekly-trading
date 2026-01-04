# ETF Tracker Cheatsheet (II + Barclays)

## Purpose
Track ETFs that appear in the **interactive investor (II)** and **Barclays** Top 10 lists.  
- **II** → monthly rank (based on buy orders), with 6 months of history available.  
- **Barclays** → weekly rank snapshot (based on % allocation), logged once per month.  

## Structure
- **Two separate tables:**  
  - One for II (with full 6 months backfill).  
  - One for Barclays (starting July 25, no backfill).  
- After 6 months, you can trim the II table back to July 25 and merge into a single unified table if you prefer.  

## Columns
- **Ticker** → ETF ticker symbol (e.g. SGLN, VUSA).  
- **Month columns (07/25, 08/25, …)** → record the rank that month. Leave blank if not in Top 10.  

## How to Use
1. Once a month, collect both II and Barclays Top 10 lists.  
2. For each ETF:  
   - Add/locate its row in the relevant table.  
   - Enter the rank in the current month column.  
   - If ETF is missing, leave blank.  
3. Keep II and Barclays separate until you’ve logged 6 months of Barclays data.  
4. At that point, you can either:  
   - Continue with two tables, or  
   - Delete the extra 6 months from II and combine both into one tracker.  

## Interpretation
- **II table** → best for spotting **rotations** (up/down movements).  
- **Barclays table** → shows **anchor allocations** but occasionally highlights niche thematics (e.g. ARCI).  
- **Together** → II = **flow signals**, Barclays = **base positioning context**.  

## Notes
- Don’t record returns (%) — only ranks.  
- Focus on **rank changes** across months.  
- Combine with TA (EMA, MACD-H) for confirmation before trading.  
