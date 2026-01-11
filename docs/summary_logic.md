# Summary Logic

This document captures the current logic in the `Summary` worksheet (columns
`B:E`) of `Weekly EQQQ (v8.0).xlsx`. The table is a "latest row" dashboard that
pulls the most recent values from other sheets to decide limit order levels.

## Column Meaning

- **Order** (col B): Buy/Sell/Current/Avg Price label for the row.
- **KPI** (col C): Name of the indicator or derived label.
- **Value** (col D): The latest indicator value used for decision-making.
- **Chng** (col E): Percent change vs current close (see below).

## Current Close Reference

The "Current Close Price" row uses:

```
CurrentClose = Data!F150
```

All percent change cells reference the current close:

```
Chng = (Value - CurrentClose) / CurrentClose
```

## ATR Rows (Buy)

Rows 10–12 use the latest ATR band values from the `ATR` sheet:

- `ATR!G150` = dynamic **x ATR (Below)** (multiplier from `Summary!F2`)
- `ATR!J150` = **0.5x ATR (Below)**
- `ATR!M150` = **1x ATR (Below)**

## ATR Rows (Sell)

Rows 21–23 use the latest ATR band values from the `ATR` sheet:

- `ATR!P150` = dynamic **x ATR (Above)** (multiplier from `Summary!F5`)
- `ATR!S150` = **1.5x ATR (Above)**
- `ATR!V150` = **2x ATR (Above)**

## Pivot Point Rows (Buy/Sell)

Pivot Point values are pulled from the `PP` sheet:

- Buy: `PP!F150`, `PP!G150` (S1, S2)
- Sell: `PP!H150`, `PP!I150` (R1, R2)

## EMA Rows (Buy)

EMA values are pulled from the `EMA` sheet:

- `EMA!F150`, `EMA!G150`

The labels are built dynamically:

```
"EMA(" & F17 & ")"
"EMA(" & F18 & ")"
```

## HH/LL Rows (Sell)

Highest-High / Lowest-Low values are pulled from the `LLHH` sheet:

- `LLHH!F150`

The label is built dynamically:

```
"HH(" & F26 & ")"
```

## Notes

- The sheet is anchored to the latest data row (row 150 in this file).
- Most values are direct cell references from indicator sheets.
- Rows 2–7 are ATR fill percentage stats and are not part of order decisions.
