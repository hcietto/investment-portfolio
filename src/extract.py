# src/extract.py

#Description: This module extracts stock prices and financial indicators using yfinance.

#Last update:
    #Date: 12-16-2025
    #Updated by: Cietto
    #Changes made: Included Graham, "DailyChangePct" and "Change5dPct" columns.

import yfinance as yf
import pandas as pd

def extract_prices_and_indicators(tickers):
    data = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)

        hist = stock.history(period="5d")
        info = stock.info

        if hist.empty or len(hist) < 2:
            continue

        last_close = hist["Close"].iloc[-1]
        prev_close = hist["Close"].iloc[-2]
        close_5d_ago = hist["Close"].iloc[0]

        daily_change_pct = (last_close / prev_close - 1) * 100
        change_5d_pct = (last_close / close_5d_ago - 1) * 100

        data.append({
            "Stock": ticker,
            "Market": "BR" if ticker.endswith(".SA") else "US",
            "Price": last_close,

            "DailyChangePct": daily_change_pct,
            "Change5dPct": change_5d_pct,

            # Some Brazilian stocks may not have the main EPS data available
            "EPS": (
                info.get("earningsPerShare")
                or info.get("epsTrailingTwelveMonths")
                or info.get("trailingEps")
            ),

            "Book Value": info.get("bookValue"),
            "P/E": info.get("trailingPE"),
            "Price-to-Book": info.get("priceToBook"),
            "DividendYield": info.get("dividendYield"),
            "ROE": info.get("returnOnEquity")
        })

    return pd.DataFrame(data)