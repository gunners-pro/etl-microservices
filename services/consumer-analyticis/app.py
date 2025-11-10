import requests
import pandas as pd

response = requests.get('http://localhost:5000/data')
data = response.json()

df = pd.DataFrame(data)

df.dropna()
df["purchase_date"] = pd.to_datetime(df["purchase_date"])
df["total_price"] = df["quantity"] * df["unit_price"]

print(df.head())