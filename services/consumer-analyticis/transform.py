import pandas as pd

class TransformDataframe:   
    @staticmethod
    def sales_by_rep(df: pd.DataFrame) -> pd.DataFrame:
        return (
            df.groupby('sales_rep', as_index=False)
            .agg(total_sales=('total_price', 'sum'))
            .sort_values('total_sales',ascending=False)
        )
