# src/transform.py
def transform_prices(df):
    df["price"] = df["price"].round(2)
    df["ticker"] = df["ticker"].str.upper()
    return df