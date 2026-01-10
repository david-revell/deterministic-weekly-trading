"""Convert weekly CSVs to Excel and add EMA/MACD-H columns."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from ema_macd import add_ema_macd_features


def _find_close_column(columns: list[str]) -> str:
    for col in columns:
        if col.lower() == "close":
            return col
    raise ValueError("No 'close' column found in the Excel sheet.")


def _coerce_numeric(series: pd.Series) -> pd.Series:
    if series.dtype == object:
        return series.astype(str).str.replace(",", "", regex=False).astype(float)
    return series.astype(float)


def _extract_etf_name(file_path: Path) -> str:
    stem = file_path.stem
    suffix = " Stock Price History"
    if stem.endswith(suffix):
        stem = stem[: -len(suffix)]
    return stem.replace(" ", "_")


def process_csv(file_path: Path, output_dir: Path) -> None:
    df = pd.read_csv(file_path)
    if "Price" in df.columns and "Close" not in df.columns:
        df = df.rename(columns={"Price": "Close"})

    close_col = _find_close_column(list(df.columns))
    df[close_col] = _coerce_numeric(df[close_col])

    # Ensure oldest-first ordering before EMA calculations.
    df = df.iloc[::-1].reset_index(drop=True)
    df_with_features = add_ema_macd_features(df, close_column=close_col)

    etf_name = _extract_etf_name(file_path)
    output_path = output_dir / f"Weekly_{etf_name}.xlsx"
    with pd.ExcelWriter(output_path, engine="openpyxl", mode="w") as writer:
        df_with_features.to_excel(writer, sheet_name="Weekly", index=False)


def main() -> None:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    files = sorted(data_dir.glob("* Stock Price History.csv"))
    if not files:
        raise FileNotFoundError(
            "No '* Stock Price History.csv' files found in data/."
        )

    for file_path in files:
        print(f"Processing {file_path.name}...")
        process_csv(file_path, data_dir)
    print("Done.")


if __name__ == "__main__":
    main()
