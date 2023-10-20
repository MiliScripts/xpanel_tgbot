import requests
import datetime
from handle_configs import get_configs
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']

import os 
import sys

sys.path.append(str(os.getcwd().replace('\\','/'))+'/dbupdates')
from fetch import store_users_json



def convert_date(plan):
      dates = {'test':1}
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




def create_new_user(username,password,teraffic,expadte,multiuser,desc=''):
   host = host_url
   
   link = host+"adduser"
   if 'نامحدود' in teraffic:
       teraffic = 0
       
   payload1 = {
            "token":api_token,
            "username": username,
            "password": password,
            "multiuser": multiuser,
            "traffic": teraffic,
            "type_traffic": "gb",
            "expdate": convert_date(expadte),
   
        }

   a = requests.post(link,payload1)
   result = '''❇️ کاربر {} با حجم {} گیگابایت و مدت زمان {} روز با موفقیت ساخته شد 

‏🪪  اطلاعات کانفیگ \n
👤  ‏username : \n‏ <code>{}</code>\n
‏🔑  password  : \n‏ <code>{}</code>\n
‏🔗  host : \n‏ <code>{}</code>\n
‏🧷 port : \n‏ <code>{}</code>\n
'''.format(username,teraffic,expadte,username,password,domain,port)
   
   store_users_json()
   return result
