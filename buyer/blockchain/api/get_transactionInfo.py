import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

URL = os.environ['GATEWAY_URL']
PATH = os.environ['GATEWAY_PATH']
FUNC = os.environ['FUNC_GETTXINFO']
AUTHORIZATION = os.environ['AUTHORIZATION']
KLD_FORM = os.environ['KLD_FORM']

url = f'https://{URL}/{PATH}/{FUNC}'

headers = {
    'accept': 'application/json',
    'Authorization': AUTHORIZATION,
}

def get_tx(purchase_id):
    params = {
        'purchase_id': purchase_id,
        'kld-from': KLD_FORM,
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
    )

    ret = response.status_code
    dic = json.loads(response.text)
    print(dic)
