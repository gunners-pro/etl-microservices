import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('API_URL', '')

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

df.dropna()
df["purchase_date"] = pd.to_datetime(df["purchase_date"])
df["total_price"] = df["quantity"] * df["unit_price"]

print(df.head())