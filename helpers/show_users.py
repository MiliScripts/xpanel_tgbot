import json
import requests
import os 
import sys

sys.path.append(str(os.getcwd().replace('\\','/')))
sys.path.append(str(os.getcwd().replace('\\','/'))+'/dbupdates')

from pykeyboard import InlineKeyboard, InlineButton
from helpers.convert_persian_data import convert_to_persian_date
from helpers.convert_traffic import convert_mb_to_gb
from helpers.remaining_days import remaining , plan_date
# from convert_persian_data import convert_to_persian_date
# from convert_traffic import convert_mb_to_gb
# from remaining_days import remaining , plan_date
from config import config as C
import random
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']






# from plugins.inline_kb_handler import show_users_sort
def convert_to_lists(users_list, users_per_list):
    result = []
    for i in range(0, len(users_list), users_per_list):
        result.append(users_list[i:i+users_per_list])
   #  print(result)    
    return result
from datetime import date
import datetime
def remaining(startdate):
   today = date.today()
   now = today.strftime("%Y-%m-%d")
   date1 = datetime.datetime.strptime(startdate, "%Y-%m-%d")
   date2 = datetime.datetime.strptime(now, "%Y-%m-%d")

   diff =  date1 - date2
   return str(diff).split(' ')[0]




def get_end_date(d):
    try:
       today = datetime.date.today()
       return datetime.datetime.strptime(d.get('end_date'), '%Y-%m-%d').date() - today 
    except:
         return 'نامشخص'


def sort_dicts_by_end_date(dicts):
    new_dict = []
    unknown_date = []
    for i in dicts:
        if get_end_date(i)=='نامشخص':
            unknown_date.append(i)
        else:
            new_dict.append(i)    
    a = sorted(new_dict, key=get_end_date)
    for i in unknown_date:
        a.append(i)
    return a     
def show_users(mode):      
    users_file= str(os.getcwd().replace('\\','/'))+'/dbupdates/'+'users.json'
    with open(users_file,'r') as f :
        data = json.load(f)    
    mn = []
    today = datetime.date.today()
    traffic_sorted_list = sorted(data, key=lambda x: int(x['traffics'][0]['total']), reverse=True)
    expire_sorted = sort_dicts_by_end_date(data)
    # for e,i in enumerate(traffic_sorted_list):
    #     print(e,i['username'])
    #     print(i['end_date'])
    #     print('______________________________')
    list_of_users = []    
    if mode== 'exprie-date':
        list_of_users = expire_sorted
    elif mode== 'creation-time' or mode=='' :
        list_of_users = data 
    elif mode== 'traffic':
        list_of_users = traffic_sorted_list
    users_list = []    
    for user in list_of_users :
       users_list.append(user)
    #    print(user['username'],user['traffics'][0]['total']+'mb')
    #    print(user['end_date'],f"remining days : {remaining(user['end_date'])}")
    u = convert_to_lists(users_list,8)
    keyboards = []    
    c = 0
    for e,user_list in enumerate(u): 

         keyboard = InlineKeyboard()   
         keyboard.row(
         InlineButton('کاربر',  'hidden'),
         InlineButton('کل',  'hidden'),
         InlineButton('مصرف',  'hidden'),
         InlineButton('انقضا',  'hidden'),

      )
         
         for user in user_list:
            # print(user)
            keyboard.row(
            InlineButton(user['username'], f"profile:{user['username']}"),
            InlineButton(f"{convert_mb_to_gb(int(user['traffic']))}", 'hidden'),
            InlineButton(f"{convert_mb_to_gb(int(user['traffics'][0]['total']))}", 'hidden'),
            InlineButton(convert_to_persian_date(user['end_date']), 'hidden'),

        )
         
         keyboard.row(
    InlineButton('🧐 ترتیب نمایش', 'sort-show-users'),
)
         if e==0:
             keyboard.row(InlineButton('➡️ بعدی',f'userspage:{e+1}'))   
         elif e==len(u)-1:
             keyboard.row(InlineButton('قبلی  ⬅️',f'userspage:{e-1}')) 
         else:
              keyboard.row(
                 InlineButton('قبلی  ⬅️',f'userspage:{e-1}'),InlineButton('➡️ بعدی',f'userspage:{e+1}') 
              )    
         
         keyboard.row(
    InlineButton('⇥ بازگشت', 'back:main-menu'),
)
         keyboards.append(keyboard) 

    return keyboards       


                  


        