import os
from dotenv import load_dotenv
from flask import Flask
from waitress import serve
from extract import extract_dataframe
from transform import TransformDataframe
from clean import CleanDataframe
from plot import chart_sales_by_rep

load_dotenv()
url = os.getenv('API_URL', '')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    # 1) Extract
    df_raw = extract_dataframe(url)

    # 2) Clean
    df_clean = CleanDataframe.clean(df_raw)

    # 3) Transform
    df_sales_by_rep = TransformDataframe.sales_by_rep(df_clean)

    # 4) Graphics Plot
    fig = chart_sales_by_rep(df_sales_by_rep)
    return fig.to_html(full_html=True)

if __name__ == '__main__':
    print("✅ Server running...")
    print("Press CTRL+C to quit.")

    serve(app, host="0.0.0.0", port=5001)