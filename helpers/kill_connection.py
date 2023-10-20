import json
import requests
from pykeyboard import InlineKeyboard, InlineButton
from helpers.convert_persian_data import convert_to_persian_date
from helpers.convert_traffic import convert_mb_to_gb
from helpers.remaining_days import remaining , plan_date
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
from handle_configs import get_configs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']








#kiling pid conection
def kill_pid(pid):
   token = api_token
   link = host_url+token+f'/kill/id/{pid}'
   response = requests.get(link)
   print(response.text)


def kill_user(username):
       token = api_token
       link = host_url+token+f'/kill/user/{username}'
       print(link)
       print(link)
       response = requests.get(link)
       
       print(response.text)  



