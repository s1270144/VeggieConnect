import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.environ['GATEWAY_URL']
PATH = os.environ['GATEWAY_PATH']
FUNC = os.environ['FUNC_SETTXINFO']
AUTHORIZATION = os.environ['AUTHORIZATION']
KLD_FORM = os.environ['KLD_FORM']

url = f'https://{URL}/{PATH}/{FUNC}'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION,
}

params = {
    'kld-from': KLD_FORM,
    'kld-sync': 'true'
}

def set_info(purchase_id, user_id, item_id, purchase_price, quantity):
    json_data = {
        '_purchase_id': purchase_id,
        '_user_id': user_id,
        '_item_id': item_id,
        '_purchase_price': purchase_price,
        '_quantity': quantity,
    }

    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=json_data,
    )
