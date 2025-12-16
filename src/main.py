# src/main.py

"""
Description: Main script to run the ETL pipeline for stock data.

Last update:
    Date: 12-16-2025
    Updated by: Cietto
    Changes made:
        - Added logging
        - Added global error handling
        - Added basic data validation
"""

import logging
from src.logging_utils import rotate_logs, setup_logging
from src.extract import extract_prices_and_indicators
from src.transform import transform_prices
from src.load import load_to_excel
from src.config import ALL_TICKERS

# Defines the output Excel file path
OUTPUT_FILE = "output/portfolio.xlsx"

def run_pipeline():

    rotate_logs()
    setup_logging()

    logging.info("ETL pipeline execution started")

    try:

        # Extract
        raw_data = extract_prices_and_indicators(ALL_TICKERS)

        if raw_data.empty:
            logging.warning("No data extracted. Pipeline aborted.")
            return

        # Transform
        clean_data = transform_prices(raw_data)

        # Load
        load_to_excel(clean_data, OUTPUT_FILE)

        logging.info("ETL pipeline executed successfully")

    except Exception as e:
        logging.exception(f"Pipeline failed: {str(e)}")
        raise # Reraise the exception after logging

if __name__ == "__main__":
    run_pipeline()