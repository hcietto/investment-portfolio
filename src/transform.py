# src/transform.py

#Description: This module transforms stock data for analysis

#Last update:
    #Date: 12-16-2025
    #Updated by: Cietto
    #Changes made: Inluded Graham Fair Price and Upside calculations.

import pandas as pd
import numpy as np

def transform_prices(df):
    # Removes '.SA' from Brazilian tickers and standardizes to uppercase
    df["Stock"] = df["Stock"].str.upper()
    df["Stock"] = df["Stock"].str.replace(".SA", "", regex=False)

    # Convert columns to numeric types and handle missing values (coerce errors)
    numeric_cols = [
        "Price", "DailyChangePct", "Change5dPct",
        "EPS", "Book Value", "P/E", "Price-to-Book", "DividendYield", "ROE"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Graham Fair Price calculation
    df["GrahamFairPrice"] = np.sqrt(22.5 * df["EPS"] * df["Book Value"])

    df["UpsideGrahamPct"] = (df["GrahamFairPrice"] / df["Price"] - 1) * 100

    # Round numerical columns for better readability
    df["Price"] = df["Price"].round(2)
    df["DailyChangePct"] = df["DailyChangePct"].round(2)
    df["Change5dPct"] = df["Change5dPct"].round(2)
    df["EPS"] = df["EPS"].round(2)
    df["Book Value"] = df["Book Value"].round(2)
    df["P/E"] = df["P/E"].round(2)
    df["Price-to-Book"] = df["Price-to-Book"].round(2)
    df["DividendYield"] = (df["DividendYield"]).round(2)
    df["ROE"] = (df["ROE"] * 100).round(2)
    df["GrahamFairPrice"] = df["GrahamFairPrice"].round(2)
    df["UpsideGrahamPct"] = df["UpsideGrahamPct"].round(2)

    return df
