# src/transform.py

"""
Description: This module transforms stock data for analysis.

Last update:
    Date: 12-16-2025
    Updated by: Cietto
    Changes made:
        - Graham Fair Price calculation
        - Upside calculation
        - Data validation and logging
"""

import pandas as pd
import numpy as np
import logging

def transform_prices(df: pd.DataFrame) -> pd.DataFrame:

    logging.info("Starting data transformation")

    df = df.copy()

    # Standardize tickers
    df["Stock"] = (
        df["Stock"]
        .str.upper()
        .str.replace(".SA", "", regex=False)
    )

    # Convert numeric columns
    numeric_cols = [
        "Price",
        "DailyChangePct",
        "Change5dPct",
        "EPS",
        "Book Value",
        "P/E",
        "Price-to-Book",
        "DividendYield",
        "ROE"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    
    # Graham Fair Price
    # Only valid when EPS > 0 and Book Value > 0
    valid_graham = (df["EPS"] > 0) & (df["Book Value"] > 0)

    df["GrahamFairPrice"] = np.where(
        valid_graham,
        np.sqrt(22.5 * df["EPS"] * df["Book Value"]),
        np.nan
    )

    # Upside / Downside vs Graham
    df["UpsideGrahamPct"] = np.where(
        df["GrahamFairPrice"].notna(),
        (df["GrahamFairPrice"] / df["Price"] - 1) * 100,
        np.nan
    )

    # Rounding
    round_cols = [
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
        "UpsideGrahamPct"
    ]

    for col in round_cols:
        df[col] = df[col].round(2)

    logging.info("Data transformation finished successfully")

    return df