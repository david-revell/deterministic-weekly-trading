# ATR Logic

This document captures the logic currently implemented in the `ATR` worksheet
of `Weekly EQQQ (v8.0).xlsx`. It is a deterministic specification intended to
be portable to Python.

## Inputs

Source columns are pulled from the `Data` sheet (which in turn pulls from
`Raw`):

- `Date`
- `High`
- `Low`
- `Close`

## True Range (TR)

For each row (starting at row 3 in the spreadsheet), calculate:

```
TR = max(
    High - Low,
    abs(High - PriorClose),
    abs(Low - PriorClose)
)
```

Rows before this are blank for TR.

## ATR (14-week SMA)

ATR is a 14-week simple moving average of TR:

```
ATR_t = average(TR_{t-13} ... TR_t)
```

This produces the first ATR value at the 16th data row in the worksheet (i.e.,
the first 14 TR values are from rows 3–16).

## ATR Bands (Below)

Band levels below the close are computed from the current week’s close and ATR:

- `Summary!F2 x ATR (Below)`:
  ```
  BandBelowDynamic_t = Close_t - (Summary!F2 * ATR_t)
  ```
- `0.5x ATR (Below)`:
  ```
  BandBelow0_5_t = Close_t - (0.5 * ATR_t)
  ```
- `1x ATR (Below)`:
  ```
  BandBelow1_0_t = Close_t - (1.0 * ATR_t)
  ```

## ATR Bands (Above)

Band levels above the close are computed similarly:

- `Summary!F5 x ATR (Above)`:
  ```
  BandAboveDynamic_t = Close_t + (Summary!F5 * ATR_t)
  ```
- `1.5x ATR (Above)`:
  ```
  BandAbove1_5_t = Close_t + (1.5 * ATR_t)
  ```
- `2x ATR (Above)`:
  ```
  BandAbove2_0_t = Close_t + (2.0 * ATR_t)
  ```

## Filled (Boolean)

Each band has a `Filled` column. A band is considered filled in the current
week if the **prior week’s band level** falls within the **current week’s**
low/high range:

```
Filled_t = 1 if (Band_{t-1} >= Low_t and Band_{t-1} <= High_t) else 0
```

This is applied separately for each band (below/above).

## Fill Percentage

The fill percentage is computed as the ratio of filled values over the count of
filled entries in the range (in the spreadsheet this is rows 16–150):

```
FillPct = 100 * sum(Filled) / count(Filled)
```

## Notes

- ATR-related columns are blank until there are at least 14 TR values.
- The spreadsheet uses weekly data (one row per week).
- The `MA(10)` columns appear in the worksheet but are empty in the current
  file and are not defined here.
