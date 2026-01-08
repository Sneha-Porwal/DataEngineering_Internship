import os
import pandas as pd

def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    if path.endswith(".csv"):
        try:
            return pd.read_csv(path, encoding="utf-8")
        except UnicodeDecodeError:
            return pd.read_csv(path, encoding="latin1")

    elif path.endswith(".xlsx") or path.endswith(".xls"):
        return pd.read_excel(path)

    else:
        raise ValueError("Unsupported file format")
