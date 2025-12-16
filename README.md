Investment Portfolio Data Pipeline

This project is a simple data engineering ETL pipeline designed to collect, transform, and load
stock market data from Brazilian and U.S. markets into an Excel file.

The goal is to demonstrate practical skills in data ingestion, data cleaning, and data delivery,
using real-world financial data.

--------------------------------------------------

DATA SOURCE
- Yahoo Finance, accessed via the yfinance Python library.

--------------------------------------------------

PIPELINE OVERVIEW

1. Extract
- Fetches the latest closing price for each stock.
- Collects fundamental indicators when available:
  - EPS (LPA)
  - Book Value (VPA)
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

MARKETS COVERED
- Brazilian stocks (B3)
- U.S. stocks (NYSE / NASDAQ)

Note:
Fundamental data coverage for Brazilian stocks may be incomplete due to limitations of the data source.

--------------------------------------------------

PROJECT STRUCTURE

investment-portfolio/
|
|-- src/
|   |-- __init__.py
|   |-- main.py
|   |-- config.py
|   |-- extract.py
|   |-- transform.py
|   |-- load.py
|
|-- output/
|   |-- portfolio.xlsx
|
|-- README.txt

--------------------------------------------------

HOW TO RUN

From the project root directory, run:

python -m src.main

The output file will be generated at:

output/portfolio.xlsx

--------------------------------------------------

REQUIREMENTS

- Python 3.10 or higher
- pandas
- yfinance
- openpyxl

To install dependencies:

pip install pandas yfinance openpyxl

--------------------------------------------------

PURPOSE

This project was built to:
- Showcase data engineering fundamentals
- Practice ETL design with real external data
- Demonstrate handling of missing and inconsistent data
- Serve as a portfolio project for GitHub

--------------------------------------------------

POSSIBLE IMPROVEMENTS

- Add historical time-series data
- Convert U.S. stock prices to BRL using FX rates
- Store data in a database such as PostgreSQL or DuckDB
- Add automated tests
- Containerize the pipeline using Docker

--------------------------------------------------

DISCLAIMER

This project is for educational purposes only and should not be considered financial advice.
