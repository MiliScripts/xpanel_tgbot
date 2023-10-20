import requests
import json
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']

import os 
import sys

sys.path.append(str(os.getcwd().replace('\\','/')))
sys.path.append(str(os.getcwd().replace('\\','/'))+'/dbupdates')
from fetch import store_users_json





def extent_user(username,days):
    host = host_url
    link = host+"renewal"
    payload = {
        'token':api_token,
        'username':username,
        'day_date':days,
        're_date':'yes',
        're_traffic':'yes'

    }
    print(payload)
    a = requests.post(link,payload)
    print(a.content)
    store_users_json()
    