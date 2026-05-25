import pandas as pd 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



def load_sales():
    path = BASE_DIR / "data" / "sales.xlsx"
    df = pd.read_excel(path)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df
    


def load_expenses(): 
    path = BASE_DIR / "data" / "expenses.xlsx"
    df = pd.read_excel(path)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df


def load_ads(): 
    path = BASE_DIR / "data" / "ads.xlsx"
    df = pd.read_excel(path)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df
