# TO ADD A NEW SCHEDULED CARD: add another 'elif' statement following the same format as used below (In the 'CREATE THE CARDS' condition below).
# You'll have to get the id of the card you are wanting to copy from. This goes in the origin_card_id field (as used below).
# To get the id of the card you are wanting to copy from: in the card (within Trello), press Share (bottom right of card). Then, press 'Export JSON'. The id is in the top right of the next page.
# Note: you must create a Trello calendar rule to trigger the code in zapier. In addition, you must update the Zapier rule as well.

# IMPORT MODULES
import sys
import requests
import datetime

# GLOBAL VARIABLES
KEY         = '135e060c189bf0f4d6b8a021b3804e1e'            # Used to connect to the Trello API
TOKEN       = 'ATTAc7971e017e294d0507b749e386b16a9e364b1cc93690191afad1cf2ea061d6f608A7C79C' # Used to connect to the Trello API
TODAY       = datetime.date.today().isoformat()             # All cards will be created with todays date at the end of the name
today_datetime = datetime.datetime.fromisoformat(TODAY)
DUE_DATE    = today_datetime + datetime.timedelta(days=1, hours=23)  # All cards will be created with this due date
RICKS_LIST_ID  = '636125ff2f293f037e185a4d'                    # BM List in Lake Norden Estimating
JASONS_LIST_ID = '62e28fd31d9a77064e10a8b3'                    # Inbox in Jason Saathoff

# FUNCTION DEFINITIONS
def create_card(name, origin_card_id, dest_list_id):
    # Sends an HTTP request to Trello to create the card in the BM list
    # Read documentation here: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
    parameters = {
            'key': KEY,
            'token': TOKEN,
            'idList': dest_list_id,
            'name': name,
            'desc': 'Created via Zapier on ' + TODAY + '.',
            'due': DUE_DATE,
            'pos': 'top',
            'idCardSource': origin_card_id,
            'keepFromSource': 'attachments,checklists'
        }
    response = requests.request(
        'POST',
        'https://api.trello.com/1/cards',
        headers={
            'Accept': 'application/json'
            },
        params=parameters
    )

def archive_card(cardId):
    # Sends an HTTP request to Trello to archive the card that triggered this script
    # Read the documentation here: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-put
    response = requests.request(
        "PUT",
        'https://api.trello.com/1/cards/' + cardId,
        headers={
            'Accept': 'Application/json'
        },
        params={
            'key': KEY,
            'token': TOKEN,
            'closed': 'true'
        }
    )

# INITIALIZING THE PARAMETERS
input_str  = sys.argv[1] # Gets the input str which starts with 'zap'
input_list = input_str.split(sep=';')
trigger_card_id = sys.argv[2] # Id of card to archive after completion

if input_list[0] != 'zap': # Checks if comment is meant to trigger a zap
    print("input doesn't start with 'zap'")
    exit()
cmd_type = input_list[1]
cmds = input_list[2:]

# CREATE THE CARDS
for cmd in cmds:
    if cmd == 'site_walk_around':
        name = 'Site Walk Around - ' + TODAY                 # Set name of new card
        origin_card_id = '63ea765c4994881246a24666'          # Set destination list id
        create_card(name, origin_card_id, RICKS_LIST_ID)     # Call function to create new card
        create_card(name, origin_card_id, JASONS_LIST_ID)    # Call function to create new card

    elif cmd == 'customer_profitability':
        name = 'Customer Profitability - ' + TODAY
        origin_card_id = '63ea7631654b8ea91b818b83'
        create_card(name, origin_card_id, RICKS_LIST_ID)
        create_card(name, origin_card_id, JASONS_LIST_ID)

    elif cmd == 'invoiced_orders_left_in_order_monitor':
        name = 'Invoiced Orders left in Order Monitor - ' + TODAY
        origin_card_id = '63ea78362ebe0f1ed72075f9'
        create_card(name, origin_card_id, RICKS_LIST_ID)
        create_card(name, origin_card_id, JASONS_LIST_ID)

    elif cmd == 'review_product_group_sales':
        name = 'Review Product Group Sales - ' + TODAY
        origin_card_id = '63ea76e7032fd4b41d25b47c'
        create_card(name, origin_card_id, RICKS_LIST_ID)
        create_card(name, origin_card_id, JASONS_LIST_ID)

    elif cmd == 'review_open_orders':
        name = 'Review Open Orders - ' + TODAY
        origin_card_id = '63ea6d897031a3d74ea26e39'
        create_card(name, origin_card_id, RICKS_LIST_ID)
        create_card(name, origin_card_id, JASONS_LIST_ID)

    elif cmd == 'bistrack_review_zz_on_hand_not_allocated':
        name = 'Bistrack - Review ZZ on Hand Not Allocated - ' + TODAY
        origin_card_id = '63ea6e8a1d1911891ed61ed8'
        create_card(name, origin_card_id, RICKS_LIST_ID)
        create_card(name, origin_card_id, JASONS_LIST_ID)

    elif cmd == 'review_job_closures_tax_codes':
        name = 'Review Job Closures / Tax Codes - ' + TODAY
        origin_card_id = '63ea6f4c85b41d394dcfef9c'
        create_card(name, origin_card_id, RICKS_LIST_ID)
        create_card(name, origin_card_id, JASONS_LIST_ID)

    elif cmd == 'customer_ar_report':
        name = 'Customer AR Report - ' + TODAY
        origin_card_id = '63ea7809247630aa57ad6515'
        create_card(name, origin_card_id, RICKS_LIST_ID)
        create_card(name, origin_card_id, JASONS_LIST_ID)

    else:
        print(f'Command not found ({cmd})')

# ARCHIVE THE TRIGGER CARD
archive_card(trigger_card_id)
