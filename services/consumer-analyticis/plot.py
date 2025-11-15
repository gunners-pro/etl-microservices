import plotly.express as px
from plotly.graph_objects import Figure
import pandas as pd

def chart_sales_by_rep(df: pd.DataFrame) -> Figure:
    fig = px.bar(
        df,
        x='sales_rep', 
        y='total_sales', 
        labels={"total_sales": "Quantidade(Milhões)", "sales_rep":"Vendedores"}, 
        title="Total de Vendas Por Vendedor"
    )
    return fig