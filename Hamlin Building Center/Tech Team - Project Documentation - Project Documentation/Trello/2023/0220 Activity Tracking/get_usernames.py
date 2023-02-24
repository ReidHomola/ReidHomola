import requests
import json

KEY = '135e060c189bf0f4d6b8a021b3804e1e'
TOKEN = 'ATTAc7971e017e294d0507b749e386b16a9e364b1cc93690191afad1cf2ea061d6f608A7C79C'
ORGANIZATION_ID = '623c69ec71b7c34f81e9e68d'
ENTERPRISE_ID = '61b75fc63cc8a72dc1e04781'

url = 'https://api.trello.com/1/organizations/' + ORGANIZATION_ID + '/members'
# url = 'https://api.trello.com/1/enterprises/' + ENTERPRISE_ID + '/members'

headers = {
    'Accept': 'application/json'
}

query = {
    'key': KEY,
    'token': TOKEN
}

response = requests.request(
    'GET',
    url,
    headers=headers,
    params=query
)

with open('usernames.json', 'w') as f:
    f.write(response.text)
