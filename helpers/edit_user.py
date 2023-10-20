import requests
import json
import datetime
from helpers.convert_traffic import *
from helpers.convert_persian_data import *
from pyrogram import Client
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)

dates = {'test':1}
user_edit_data_dict = {
    'original':{},
    'edit':{
        "username" : '',
        "password" : '',
        "multiuser"  : '',
        "traffic"  : '',
        "type_traffic" : '',
        "expdate" : '',
        "activate" :'active'
    }
}
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






import urllib.parse

def encode_url(url):
    encoded_url = urllib.parse.quote(url)
    return encoded_url
from datetime import datetime, timedelta

def add_days_to_date(date_str, days):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")

# print(add_days_to_date('2023-09-30',20))

def get_user_data(username):
   global user_edit_data_dict
   host = host_url+api_token
   link = host+f'/user/{username}'

   response = requests.get(link)
   data = json.loads(response.text)
   print(data)
   host = host_url+api_token
   link = host+f'/user/{username}'
   traffics = []
   response = requests.get(link)
   data = json.loads(response.text)
   for i in data[0].keys() :
        
         print(f' data : {i}')
         print('___________________')
         if i=='username':
            usernamee = data[0][i]
            print(data[0][i])
         if i=='password': 
            password = data[0][i]
         if i=='traffic':   
            traffic = int(data[0][i])
            if traffic==0 or traffic=='0':
               traffic = '♾'
         if i=='end_date':
            finishdate = data[0][i]
         if i=='multiuser':   
              multiuser = data[0][i]

   for i in data :
       try:
         trf = convert_mb_to_gb(int(traffic))
       except:
           trf = 0 
       user_edit_data_dict["original"] ={
        "username" : usernamee,
        "password" : password,
        "multiuser"  : multiuser,
        "traffic"  : trf,
        "type_traffic" : 'gb' ,
        "expdate" : finishdate
        
    } 
   d = user_edit_data_dict['original']  
   text = '''• توجه کنید| اطلاعات کنونی کاربر :

نام کاربری: {}
پسورد : {}
ترافیک : {}
تعداد دستگاه مجاز :  {}
تاریخ انقضا: {}

‏➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

• وارد کنید | اطلاعات جدید کاربر (ادیت ):

نام کاربری: {}
پسورد : {}
ترافیک :
تعداد دستگاه مجاز : 
تاریخ انقضا:'''.format(d['username'],d['password'],d['traffic'],d['multiuser'],d["expdate"],d['username'],d['password'])
   print(user_edit_data_dict)
   return text   


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




def edit_user_info(payload):
    host = host_url
    link = host+"edituser"
    payload['token']=api_token,
    a = requests.post(link,payload)
    try:
        if json.loads(a.content)["message"]=="User Updated":
            store_users_json()
            return True
        else:
            return False
    except:
        return False    


def get_edit_data_kb(user):
    text = encode_url(get_user_data(username=user))
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(  # Opens a web URL
                            "کلیک کن و ربات را انتخاب کنید",
                            url=f"https://t.me/share/url?url=%D8%AF%D8%B1%D8%AE%D9%88%D8%A7%D8%B3%D8%AA+%D8%A7%D8%AF%DB%8C%D8%AA+%DA%A9%D8%A7%D8%B1%D8%A8%D8%B1&text={text}"
                        )]
    ])
    return kb

