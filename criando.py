import json
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")
url = f"https://viacep.com.br/ws/%s/json/"
url_clima = f"https://api.openweathermap.org/data/2.5/weather?q=%s&APPID={API_KEY}&units=metric"

df = pd.read_csv("listanova.csv")

transform = []

def get_endereco(cep):
    response = requests.get(url % cep)
    print(response)
    if "erro" in response.json():
        return None
    else:
        return response.json() if response.status_code == 200 else None

def get_clima_cidade(cidade):
    temp = requests.get(url_clima % cidade).json()
    return temp['main']['temp']

for i in df.index:
    endereco = get_endereco(df['cep'][i])
    clima = get_clima_cidade(endereco['localidade'])
    endereco['nome'] = df['nome'][i]
    endereco['temp'] = clima
    print(endereco)








