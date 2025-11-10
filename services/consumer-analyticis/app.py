import requests
import pandas as pd

response = requests.get('http://localhost:5000/data')
data = response.json()

df = pd.DataFrame(data)
print(df.head())