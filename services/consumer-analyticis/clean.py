import pandas as pd

class CleanDataframe:

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna().copy()
        df["purchase_date"] = pd.to_datetime(df["purchase_date"])
        df["total_price"] = df["quantity"] * df["unit_price"]
        return df