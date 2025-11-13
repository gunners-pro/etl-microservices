import requests
import os
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from flask import Flask
from waitress import serve

load_dotenv()
url = os.getenv('API_URL', '')

app = Flask(__name__)

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

df.dropna()
df["purchase_date"] = pd.to_datetime(df["purchase_date"])
df["total_price"] = df["quantity"] * df["unit_price"]

total_sales_by_rep = df.groupby('sales_rep', as_index=False).agg(total_sales=('total_price', 'sum')).sort_values('total_sales',ascending=False)

@app.route('/', methods=["GET"])
def home():
    fig = px.bar(total_sales_by_rep, x='sales_rep', y='total_sales', labels={"total_sales": "Quantidade(Milhões)", "sales_rep":"Vendedores"}, title="Total de Vendas Por Vendedor")
    return fig.to_html()

if __name__ == '__main__':
    print("✅ Server running...")
    print("Press CTRL+C to quit.")

    serve(app, host="0.0.0.0", port=5001)