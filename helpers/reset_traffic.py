import requests
import json
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





def reset_traffic(username):
    try:
        username = username
        token = api_token
        link = host_url+'retraffic'
        payload = {
            'token':token,
            'username':username
        }
        response = requests.get(link,payload)
        print(response.content)
        print(json.loads(response.content))
        result_text = '''❚ ترافیک کاربر <code>{}</code> با موفقیت ریست شد .'''.format(
            username
        )
        return result_text
    except :
        return 'با خطای سرور روبرو شد'


