# src/load.py

# src/load.py

"""
Description: This module loads data to an Excel file.

Last update:
    Date: 12-16-2025
    Updated by: Cietto
    Changes made:
        - Included Graham valuation
        - Added DailyChangePct and Change5dPct
        - Added logging and failure handling
"""

import logging
import pandas as pd
from pathlib import Path

# Ensure logs directory exists
Path("logs").mkdir(parents=True, exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_execution_start():
    logging.info("Pipeline started")

def log_execution_end():
    logging.info("Pipeline finished")

def log_ticker_error(ticker, error_message):
    logging.error(f"Error processing {ticker}: {error_message}")

def load_to_excel(df: pd.DataFrame, file_path: str):

    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    log_execution_start()

    try:
        with pd.ExcelWriter(file_path, engine="openpyxl") as writer:

            # Main tab
            main_cols = [
                "Stock",
                "Market",
                "Price",
                "DailyChangePct"
            ]

            df[main_cols].to_excel(
                writer,
                sheet_name="Main",
                index=False
            )

            # Analysis tab
            analysis_cols = [
                "Stock",
                "Price",
                "DailyChangePct",
                "Change5dPct",
                "EPS",
                "Book Value",
                "P/E",
                "Price-to-Book",
                "DividendYield",
                "ROE",
                "GrahamFairPrice",
                "UpsideGrahamPct",
                "TargetPrice",
                "Recommendation",
                "AnalystOpinions"
            ]

            df[analysis_cols].to_excel(
                writer,
                sheet_name="Analysis",
                index=False
            )

        logging.info(f"Excel file successfully generated: {file_path}")

    except Exception as e:
        logging.exception(f"Error saving Excel file: {str(e)}")

    finally:
        log_execution_end()