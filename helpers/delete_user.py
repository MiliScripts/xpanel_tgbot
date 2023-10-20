import requests

# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
from handle_configs import get_configs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']

sys.path.append(str(os.getcwd().replace('\\','/'))+'/dbupdates')
from fetch import store_users_json

def del_user(username):
    host = host_url
    link = host+"delete"
    payload1 = {
       'token' : api_token,
       'username' : username
    }
    requests.post(link,payload1)
    store_users_json()






