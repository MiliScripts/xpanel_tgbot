import random    
import requests
import datetime 


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

sys.path.append(str(os.getcwd().replace('\\','/'))+'/dbupdates')
from fetch import store_users_json


dates = {'test':1}
def convert_date(plan):
      if plan=='test':
         now = datetime.datetime.now()
         days_after = datetime.timedelta(days=dates[plan])
         plan_date = now + days_after
         
         
         return plan_date.strftime("%Y-%m-%d")
      
      else:
         now = datetime.datetime.now()
         days_after = datetime.timedelta(days=int(plan))
         plan_date = now + days_after
         
         
         return plan_date.strftime("%Y-%m-%d")




def create_test_user():

    link = host_url+"adduser"
    username = 'test'+str(random.randint(1,100000))
    password = str(random.randint(1,100000))
    payload1 = {
            "token":api_token,
            "username": username,
            "password": password,
            "multiuser": 1,
            "traffic": 200,
            "type_traffic": "mb",
            "expdate": convert_date('test'),
   
        }
    n = requests.post(link,payload1)
    result = '''❇️ کاربر تست با حجم200 مگابایت و مدت زمان 1 روز با موفقیت ساخته شد 

‏🪪  اطلاعات کانفیگ \n
👤  ‏username : \n‏ <code>{}</code>\n
‏🔑  password  : \n‏ <code>{}
‏🔗  host : \n‏ <code>{}</code>\n
‏🧷 port : \n‏ <code>{}</code>\n'''.format(username,password,domain,port)
    
    store_users_json()
    return result
