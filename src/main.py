from src.extract import extract_prices
from src.transform import transform_prices
from src.load import load_to_excel

TICKERS = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
OUTPUT_FILE = "data/portfolio.xlsx"

def run_pipeline():
    raw_data = extract_prices(TICKERS)
    clean_data = transform_prices(raw_data)
    load_to_excel(clean_data, OUTPUT_FILE)

if __name__ == "__main__":
    run_pipeline()
