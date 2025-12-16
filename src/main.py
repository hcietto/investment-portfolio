# src/main.py

#Description: Main script to run the ETL pipeline for stock data

#Last update:
    #Date: 12-16-2025
    #Updated by: Cietto
    #Changes made: Creation

from src.extract import extract_prices_and_indicators
from src.transform import transform_prices
from src.load import load_to_excel
from src.config import ALL_TICKERS

OUTPUT_FILE = "output/portfolio.xlsx"

def run_pipeline():
    raw_data = extract_prices_and_indicators(ALL_TICKERS)
    clean_data = transform_prices(raw_data)
    load_to_excel(clean_data, OUTPUT_FILE)
    print(clean_data)

if __name__ == "__main__":
    run_pipeline()