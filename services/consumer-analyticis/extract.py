import requests
import pandas as pd

def extract_dataframe(url: str) -> pd.DataFrame:
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    return df