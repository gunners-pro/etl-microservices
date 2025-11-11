import requests
import pandas as pd

url = 'https://producer-api.internal.icymeadow-dc61bc99.centralus.azurecontainerapps.io/data'
# url = 'http://producer-api:5000/data' Local

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

df.dropna()
df["purchase_date"] = pd.to_datetime(df["purchase_date"])
df["total_price"] = df["quantity"] * df["unit_price"]

print(df.head())