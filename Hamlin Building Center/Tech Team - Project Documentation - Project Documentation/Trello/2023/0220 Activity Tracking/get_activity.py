import requests
from datetime import datetime, timedelta

KEY = '135e060c189bf0f4d6b8a021b3804e1e'
TOKEN = 'ATTAc7971e017e294d0507b749e386b16a9e364b1cc93690191afad1cf2ea061d6f608A7C79C'
ORGANIZATION_ID = '623c69ec71b7c34f81e9e68d'
ACTION_TYPES = 'addAttachmentToCard,addChecklistToCard,commentCard,convertToCardFromCheckItem,copyCard,copyCommentCard,createCard,createList,deleteCard,emailCard,moveCardFromBoard,moveListFromBoard,removeChecklistFromCard,updateBoard,updateCard,updateCheckItemStateOnCard,updateChecklist,updateList'


usernames = [
    'andrewjulson',
    # 'brucekoski',
    'cameronlehtola',
    'carolinehallstrom',
    'codyweber22',
    'cory83963449',
    'damonstormo',
    'daniellesnar',
    # 'dennisstrait2',
    'erinthiex',
    'jasonsaathoff',
    'jennyjasper3',
    'joe37201934',
    'kamdenhomola1',
    # 'kelsysmith87',
    'masonbunker',
    'mattsquires5',
    # 'nathanbeld',
    # 'rickhamlinbccom',
    'rick36618919',
    'rubenlopez270',
    'ryanlove21',
    'shanevandamme1',
    # 'tylersmith360',
    'cameronlarson3',
    'lasonwilen2'
]

member_activity = {}    # {'username': count_of_activity}

def get_last_monday():
    now = datetime.now()
    last_monday = now + timedelta(days=(0 - now.weekday()))
    return (last_monday if last_monday < now
            else last_monday - timedelta(weeks=1))

def get_members():
    headers = {
        'Accept': 'application/json'
    }

    query = {
        'key': KEY,
        'token': TOKEN
    }

    response = requests.request(
        'GET',
        'https://api.trello.com/1/organizations/' + ORGANIZATION_ID + '/members',
        headers=headers,
        params=query
    )

    return response

def get_member_activity(username):
    headers = {
        'Accept': 'application/json'
    }

    query = {
        'key': KEY,
        'token': TOKEN,
        'filter': ACTION_TYPES,
        'limit': 1000,
        'since': get_last_monday()
    }

    response = requests.request(
        'GET',
        'https://api.trello.com/1/members/' + username + '/actions',
        headers=headers,
        params=query
    )

    return response


    f.write('')

# Set count of activity by member_id
for username in usernames:
    this_member_activity = get_member_activity(username).json()
    member_activity[username] = len(this_member_activity)

# Clear output file
with open('output', 'w') as f:
    f.write('')

# Write content to output file
with open('output', 'a') as f:
    for activity in member_activity:
        f.write(activity + ': ' + str(member_activity[activity]) + '\n')
    action_types = ACTION_TYPES.split(',')
    f.write('\nActions That Trigger an Activity in the Report:\n')
    for i in range(0, len(action_types), 3):
        f.write(' ' + action_types[i])
        f.write(' ' * (30 - len(action_types[i])))
        if len(action_types) > i + 1:
            f.write(action_types[i + 1])
            f.write(' ' * (30 - len(action_types[i + 1])))
        if len(action_types) > i + 2: f.write(action_types[i + 2] + '\n')