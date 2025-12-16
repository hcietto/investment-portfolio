import pandas as pd
from pathlib import Path

def load_to_excel(df, file_path):
    file_path = Path(file_path)

    if file_path.exists() and file_path.stat().st_size > 0:
        try:
            existing = pd.read_excel(file_path)
            df = pd.concat([existing, df], ignore_index=True)
        except Exception:
            pass

    df.to_excel(file_path, index=False)