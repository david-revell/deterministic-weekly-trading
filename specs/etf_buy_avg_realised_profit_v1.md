# Cheatsheet: Running Trade Calculations in Excel

| Col | Header                | Purpose                                | Example formula (row 2) |
|-----|-----------------------|----------------------------------------|--------------------------|
| A   | OID                   | Trade ID / order sequence              | (raw data)              |
| B   | Date                  | Trade date                             | (raw data)              |
| C   | TYPE                  | Order type (Buy/Sell)                  | (raw data)              |
| D   | QUANTITY              | Filled quantity                        | (raw data)              |
| E   | FILL PRICE            | Executed price (GBX)                   | (raw data)              |
| F   | Side                  | Encodes Buy as `1`, Sell as `-1`       | =IF(ISNUMBER(SEARCH("Buy",C2)),1,-1) |
| G   | Quantity (signed)     | Positive for Buy, negative for Sell     | =D2*F2                  |
| H   | Trade value (GBX)     | Quantity × Fill Price                  | =D2*E2                  |
| I   | Running qty           | Position size after this trade          | =IF(ROW()=2, G2, I1+G2) |
| J   | Running cost (GBX)    | Total book cost of position             | =IF(ROW()=2, H2, J1 + IF(F2=1, H2, -K1*D2)) |
| K   | Avg buy Price (GBX)   | Average cost of current holding         | =IF(I2=0,0, J2/I2)      |
| L   | Realised P&L (£)      | Profit/loss realised on this sell       | =IF($F2=-1, ($E2 - K1) * $D2, 0)/100 |
| M   | Cum Realised P&L (£)  | Running realised profit in £            | =IF(ROW(M2)=2,L2,M1 + L2) |

# Notes
- All prices entered in GBX, final realised P&L columns convert to £ by dividing by 100.
- Avg Buy Price (K) only reflects the cost of shares still held.
- Realised P&L (L) is calculated using the **average cost before** the trade.
- Cum Realised P&L (M) accumulates realised profit across all sells.
- Keep trades sorted by OID/date ascending so the running logic works.
