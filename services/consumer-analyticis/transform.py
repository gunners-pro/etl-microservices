import pandas as pd

class TransformDataframe:   
    @staticmethod
    def sales_by_rep(df: pd.DataFrame) -> pd.DataFrame:
        df.dropna()
        df["purchase_date"] = pd.to_datetime(df["purchase_date"])
        df["total_price"] = df["quantity"] * df["unit_price"]

        total_sales_by_rep = (
            df.groupby('sales_rep', as_index=False)
            .agg(total_sales=('total_price', 'sum'))
            .sort_values('total_sales',ascending=False)
            )

        return total_sales_by_rep