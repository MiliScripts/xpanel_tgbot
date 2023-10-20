import requests
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']



def activate(username):
    link = host_url+"active"
    payload1 = {
            "token":api_token,
            "username": username
        }
    requests.post(link,payload1)



def deactivate(username):
    link = host_url+"deactive"
    payload1 = {
            "token":api_token,
            "username": username
        }
    requests.post(link,payload1)


