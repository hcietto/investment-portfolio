# src/extract.py

"""
Description: This module extracts stock prices and financial indicators using yfinance.

Last update:
    Date: 12-16-2025
    Updated by: Cietto
    Changes made:
        - Added logging
        - Added fault tolerance per ticker
        - Normalized indicators
"""

import yfinance as yf
import pandas as pd
import logging

def extract_prices_and_indicators(tickers: list[str]) -> pd.DataFrame:

    data = []

    for ticker in tickers:
        try:
            logging.info(f"Extracting data for {ticker}")

            stock = yf.Ticker(ticker)
            hist = stock.history(period="5d")
            info = stock.info or {}

            if hist.empty or len(hist) < 2:
                logging.warning(f"Not enough historical data for {ticker}")
                continue

            last_close = hist["Close"].iloc[-1]
            prev_close = hist["Close"].iloc[-2]
            close_5d_ago = hist["Close"].iloc[0]

            daily_change_pct = (last_close / prev_close - 1) * 100
            change_5d_pct = (last_close / close_5d_ago - 1) * 100

            eps = (
                info.get("earningsPerShare")
                or info.get("epsTrailingTwelveMonths")
                or info.get("trailingEps")
            )

            book_value = info.get("bookValue")
            pe_ratio = info.get("trailingPE")
            pb_ratio = info.get("priceToBook")

            dividend_yield = info.get("dividendYield")
            roe = info.get("returnOnEquity")

            data.append({
                "Stock": ticker.replace(".SA", ""),
                "Market": "BR" if ticker.endswith(".SA") else "US",
                "Price": round(last_close, 2),
                "DailyChangePct": round(daily_change_pct, 2),
                "Change5dPct": round(change_5d_pct, 2),
                "EPS": round(eps, 2) if eps else None,
                "Book Value": round(book_value, 2) if book_value else None,
                "P/E": round(pe_ratio, 2) if pe_ratio else None,
                "Price-to-Book": round(pb_ratio, 2) if pb_ratio else None,
                "DividendYield": round(dividend_yield, 2) if dividend_yield else None,
                "ROE": round(roe * 100, 2) if roe else None
            })

            logging.info(f"Successfully extracted {ticker}")

        except Exception as e:
            logging.exception(f"Error extracting data for {ticker}: {str(e)}")

    return pd.DataFrame(data)