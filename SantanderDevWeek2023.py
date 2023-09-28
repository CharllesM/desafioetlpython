sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

import pandas as pd

df = pd.read_csv('C:\GitBash\Desafio_Santander\SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id) is not None)]

print(json.dumps(users, indent=2))

#Extract - Adiciona as mensagens aos usuários

for user in users:
  news = f"Este é um exemplo de mensagem de marketing manual, pois estou sem crédito no chatgpt."
  print(news)


# Load

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json =user)
  return True if response.status.code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}")


