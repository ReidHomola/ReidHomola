import requests
import json

KEY = '135e060c189bf0f4d6b8a021b3804e1e'
TOKEN = 'ATTAc7971e017e294d0507b749e386b16a9e364b1cc93690191afad1cf2ea061d6f608A7C79C'
BOARD_ID = '5b000bde9bb5dee945febd49'
    
headers = {
    'Accept': 'application/json'
}

query = {
    'key': KEY,
    'token': TOKEN
}

response = requests.request(
    'GET',
    url='https://api.trello.com/1/boards/' + BOARD_ID + '/actions',
    headers=headers,
    params=query
)

with open('andrews_board_activity.json', 'w') as f:
    f.write(response.text)