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
trigger_card_id = sys.argv[2]
input_str  = sys.argv[1] # Gets the input str which starts with 'zap'
inputs = input_str.split(sep=';')

if inputs[0] != 'zap': # Checks if comment is meant to trigger a zap
    print("input_str doesn't start with 'zap'")
    exit()

cmd_type = inputs[1][inputs[1].find('=') + 1:]

if cmd_type == 'BM_scheduled_cards':
    cmds = inputs[2:]

    # CREATE THE CARDS FOR EACH COMMAND
    for cmd in cmds:
        # SETUP PARAMETERS FOR THIS COMMAND
        cmd_params = cmd.split()
        cmd_name = cmd_params[0][cmd_params[0].find('=') + 1:]
        origin_card_id = cmd_params[1][cmd_params[1].find('=') + 1:]
        dest_list_ids = cmd_params[2][cmd_params[2].find('=') + 1:].split(',')

        # DEFINE LOCAL FUNCTION
        def create_cards(name):
            for dest_list_id in dest_list_ids:
                create_card(name, origin_card_id, dest_list_id)
        
        # CREATE THE CARDS
        if   cmd_name == 'site_walk_around':                         create_cards('Site Walk Around - ' + TODAY)
        elif cmd_name == 'customer_profitability':                   create_cards('Customer Profitability - ' + TODAY)
        elif cmd_name == 'invoiced_orders_left_in_order_monitor':    create_cards('Invoiced Orders left in Order Monitor - ' + TODAY)
        elif cmd_name == 'review_product_group_sales':               create_cards('Review Product Group Sales - ' + TODAY)
        elif cmd_name == 'review_open_orders':                       create_cards('Review Open Orders - ' + TODAY)
        elif cmd_name == 'bistrack_review_zz_on_hand_not_allocated': create_cards('Bistrack - Review ZZ on Hand Not Allocated - ' + TODAY)
        elif cmd_name == 'review_job_closures_tax_codes':            create_cards('Review Job Closures / Tax Codes - ' + TODAY)
        elif cmd_name == 'customer_ar_report':                       create_cards('Customer AR Report - ' + TODAY)
        else:                                                        print(f'Command not found ({cmd_name})')

    # ARCHIVE THE TRIGGER CARD
    archive_card(trigger_card_id)

else:
    print(f"cmd_type '{cmd_type}' not found")
    exit()
