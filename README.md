
# Deterministic Weekly Trading

Minimal repo for implementing deterministic trading rules.

## Layout
- `specs/`: source specifications (trading rules and logic)
- `src/`: Python code for processing and logic
- `docs/`: project documentation and reference materials

## Example usage
1. Define your inputs (EMA slopes, MACD-H signals) in a CSV or JSON.
2. Run the core function to calculate the ETF health score:
   python src/etf_health.py --input your_input_file.json

## Requirements
- Python 3.x
- pandas (for CSV/JSON handling)
- any other dependencies listed in `requirements.txt`
