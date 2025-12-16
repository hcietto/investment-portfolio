# src/config.py

#Description: This module defines lists of stock tickers for Brazilian and US markets

#Last update:
    #Date: 12-16-2025
    #Updated by: Cietto
    #Changes made: Included US stock tickers

#Note: Brazilian stock tickers end with '.SA' to denote São Paulo Stock Exchange listings
BRAZIL_TICKERS = [
    "PETR4.SA",
    "VALE3.SA",
    "ITUB4.SA",
    "BPAC11.SA",
    "BBAS3.SA"
]

US_TICKERS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN"
]

ALL_TICKERS = BRAZIL_TICKERS + US_TICKERS