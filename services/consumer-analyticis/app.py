import os
import plotly.express as px
from dotenv import load_dotenv
from flask import Flask
from waitress import serve
from extract import extract_dataframe
from transform import TransformDataframe
from clean import CleanDataframe

load_dotenv()
url = os.getenv('API_URL', '')

app = Flask(__name__)

df_raw = extract_dataframe(url)
df_clean = CleanDataframe.clean(df_raw)

@app.route('/', methods=["GET"])
def home():
    df_sales_by_rep = TransformDataframe.sales_by_rep(df_clean)
    fig = px.bar(df_sales_by_rep, x='sales_rep', y='total_sales', labels={"total_sales": "Quantidade(Milhões)", "sales_rep":"Vendedores"}, title="Total de Vendas Por Vendedor")
    return fig.to_html()

if __name__ == '__main__':
    print("✅ Server running...")
    print("Press CTRL+C to quit.")

    serve(app, host="0.0.0.0", port=5001)