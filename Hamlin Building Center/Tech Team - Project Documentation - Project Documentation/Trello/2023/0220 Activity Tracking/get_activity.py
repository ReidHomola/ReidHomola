import requests
import json
import os

KEY = '135e060c189bf0f4d6b8a021b3804e1e'
TOKEN = 'ATTAc7971e017e294d0507b749e386b16a9e364b1cc93690191afad1cf2ea061d6f608A7C79C'
board_ids = [
    '5b000bde9bb5dee945febd49', # Joe Homola
    '63c1cc3045fcaf0016463c46', # Ruben Lopez
    '5a84a60c863c552358f519ff', # Cameron Larson
    '5a958b46beac45adb69d8e04', # Erin Thiex
    '5a84a5f52fe5a3670b22da17', # Jenny Jasper
    '5a84a522c6c12d4e35689369', # Kamden Homola
    '62e14eb9ddd9da37a7a0b32e', # Lars Williamson
    '5bfd7c1bd97b0a09ade4e5b6', # Lason Wilen
    '63eabae597b4646ccc4226d1'  # Shane VanDamme
]

with open('output.json', 'w') as f:
    f.write('')

for board_id in board_ids:
    print(board_id)
    headers = {
        'Accept': 'application/json'
    }

    query = {
        'key': KEY,
        'token': TOKEN,
        'fields': 'name,labels,url,idShort,idList,dateLastActivity',
        'since': '2023-02-13'
    }

    response = requests.request(
        'GET',
        'https://api.trello.com/1/board/' + board_id + '/actions',
        headers=headers,
        params=query
    )

    with open('output.json', 'a') as f:
        if response.text != 'The requested resource was not found.':
            f.write(response.text)
            f.write('\n// ################################################################################################################\n')
