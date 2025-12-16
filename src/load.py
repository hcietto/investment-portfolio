# src/load.py

#Description: This module loads data to an Excel file.

#Last update:
    #Date: 12-16-2025
    #Updated by: Cietto
    #Changes made: Included Graham, "DailyChangePct" and "Change5dPct" to Analysis tab.

import pandas as pd
from pathlib import Path


def load_to_excel(df, file_path):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:

        # Define main tab
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

        # Define analysis tab
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
            "UpsideGrahamPct"
        ]

        df[analysis_cols].to_excel(
            writer,
            sheet_name="Analysis",
            index=False
        )