import pandas as pd

class TransformDataframe:   
    @staticmethod
    def sales_by_rep(df: pd.DataFrame) -> pd.DataFrame:
        return (
            df.groupby('sales_rep', as_index=False)
            .agg(total_sales=('total_price', 'sum'))
            .sort_values('total_sales',ascending=False)
        )
    
    @staticmethod
    def sales_by_month(df: pd.DataFrame) -> pd.DataFrame:
        df['month'] = df['purchase_date'].dt.month
        return (
            df.groupby('month', as_index=False)
            .agg(total_sales=('total_price', 'sum'))
        )
