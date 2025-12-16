# src/extract.py
import yfinance as yf
import pandas as pd

def extract_prices(tickers):
    data = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")

        data.append({
            "ticker": ticker,
            "price": hist["Close"].iloc[-1],
            "date": hist.index[-1].date()
        })

    return pd.DataFrame(data)