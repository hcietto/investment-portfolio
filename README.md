# Investment Portfolio Data Pipeline

This project is a simple data engineering ETL pipeline designed to collect, transform, and load
stock market data from Brazilian and U.S. markets into an Excel file.

The goal is to demonstrate practical skills in data ingestion, data cleaning, and data delivery,
using real-world financial data.

--------------------------------------------------

## DATA SOURCE
- Yahoo Finance, accessed via the yfinance Python library.

--------------------------------------------------

## PIPELINE OVERVIEW

1. Extract
- Fetches the latest closing price for each stock.
- Collects fundamental indicators when available:
  - EPS
  - Book Value
  - P/E Ratio
  - Price-to-Book
  - Dividend Yield
  - Return on Equity (ROE)

2. Transform
- Standardizes ticker symbols.
- Removes the ".SA" suffix from Brazilian stocks.
- Converts data types and handles missing values.
- Rounds numeric values for better readability.
- Converts Dividend Yield and ROE to percentages.

3. Load
- Exports the processed dataset to an Excel file.

--------------------------------------------------

## MARKETS COVERED
- Brazilian stocks
- U.S. stocks

Note:
Fundamental data coverage for Brazilian stocks may be incomplete due to limitations of the data source.

--------------------------------------------------

## HOW TO RUN

From the project root directory, run:

python -m src.main

The output file will be generated at:

output/portfolio.xlsx

--------------------------------------------------

## REQUIREMENTS

- Python 3.10 or higher
- pandas
- yfinance
- openpyxl

To install dependencies:

pip install pandas yfinance openpyxl

--------------------------------------------------

## PURPOSE

This project was built to:
- Showcase data engineering fundamentals
- Practice ETL design with real external data
- Demonstrate handling of missing and inconsistent data
- Serve as a portfolio project for GitHub

--------------------------------------------------

## DISCLAIMER

This project is for educational purposes only and should not be considered financial advice.
