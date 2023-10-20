import json
import requests
from pykeyboard import InlineKeyboard, InlineButton
from helpers.convert_persian_data import convert_to_persian_date
from helpers.convert_traffic import convert_mb_to_gb
from helpers.remaining_days import remaining , plan_date
import os 
import sys

sys.path.append(str(os.getcwd().replace('\\','/'))+'/dbupdates')
sys.path.append(str(os.getcwd().replace('\\','/')))
import random
from helpers.db_tools import *
from pyromod.helpers import ikb
from fetch import user_data_json

# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']











def user_data(username):
   print(username)
   data = user_data_json(username)
   print('data is : ______________')
   print(data)
   print(type(data))
   for i in data.keys() :
         print(i)
         print(type(i))
         if i=='username':
             usernamee = data[i]
         elif i=='password':

             password = data[i]
         elif i=='status':    
            status =  data[i]
         elif i== 'traffic':

             traffic = data[i]
             if traffic==0 or traffic=='0':
                traffic = '♾'
         elif i=='traffics':       
                traffics = data[i]
                for k in traffics:
                    download = int(k['download'])
                    upload = int(k['upload'])
                    total = int(k['total']) 
         elif i=='start_date':

            startdate = data[i]
         elif i== 'end_date':

            finishdate = data[i]
         elif i== 'multiuser':  
              multiuser = data[i]
         


         icon = random.choice('👩🏼‍💼,🧑‍🔬,🧑‍🏫,👩🏼‍🏭,👩🏼‍💻,🧑🏼‍💻,👨🏿‍💻,👩🏼‍🏫,🕵🏻‍♀️,🤵🏻‍♀️,🤵🏻,🤵🏻‍♂️,👰‍♀️,🫅🏼'.split(','))
         users_status_marks = {
            'active' : ' ✅ فعال',
            'deactive':' ⭕️ غیر فعال'  ,
            'expired' :'🧮 منقضی '
         }

         
         try : 
            remaining_dayes = remaining(finishdate)
         except Exception as e:

            remaining_dayes = ' '   
         
         try:
           if remaining_dayes==' ':
              plane =  'نامعلوم'      
           else:   
               plane = plan_date(finishdate,startdate)
               if plane=='31' or plane=='30':
                  plane='یکماهه'
               elif plane=='NULL':
                  plane='نامعلوم'   
               elif plane!='31' or plane!='30':
                  plane = plane + 'روزه'  
         except ValueError :
              plane =  'نامعلوم'
   bt = '' 
   if status=='deactive':
      bt =('🟢 فعال ', f'user-action:activate-{usernamee}')
   elif status=='active':
      bt = ('🔴 غیرفعال ', f'user-action:deactivate-{usernamee}')
   else:
      pass   

             
   keyboard = ikb([
      [("مشخصات اتصال کاربر", 'user-connection:{}'.format(usernamee))],
      [("حجم", 'hidden'),("کل مصرفی", 'hidden'),("دانلود", 'hidden'),("آپلود", 'hidden')],
      [(convert_mb_to_gb(traffic), 'hidden'),(convert_mb_to_gb(total), 'hidden'),(convert_mb_to_gb(download), 'hidden'),(convert_mb_to_gb(upload), 'hidden')],
      [("پلن ", 'hidden'),("شروع", 'hidden'),("انقضا", 'hidden'),("مانده", 'hidden')],
      [(plane, 'hidden'),(convert_to_persian_date(startdate), 'hidden'),(convert_to_persian_date(finishdate)+' روز','hidden'),(remaining_dayes, 'hidden')],
      [bt,("🔂 تمدید ",f'user-action:extent-{usernamee}'),("🗑 حذف", f'user-action:delete-{usernamee}')],[('ویرایش', f'user-action:edit-{usernamee}')],
      [('بازگشت','show-users')]
   ])  
 
   text_info = '''• مشخصات کاربر « {} »

➖➖➖➖➖➖➖➖

° برای دیدن لینک اتصال و اطلاعات کانکشن کاربر رو گزینه « مشخصات اتصال کاربر » کلیک کنید .

➖➖➖➖➖➖➖➖'''.format(usernamee)

   return [text_info,keyboard]
   

def user_data_mode(username):
   print(username)
   data = user_data_json(username)
   print('data is : ______________')
   print(data)
   print(type(data))
   for i in data.keys() :
         print(i)
         print(type(i))
         if i=='username':
             usernamee = data[i]
         elif i=='password':

             password = data[i]
         elif i=='status':    
            status =  data[i]
         elif i== 'traffic':

             traffic = data[i]
             if traffic==0 or traffic=='0':
                traffic = '♾'
         elif i=='traffics':       
                traffics = data[i]
                for k in traffics:
                    download = int(k['download'])
                    upload = int(k['upload'])
                    total = int(k['total']) 
         elif i=='start_date':

            startdate = data[i]
         elif i== 'end_date':

            finishdate = data[i]
         elif i== 'multiuser':  
              multiuser = data[i]
         


         icon = random.choice('👩🏼‍💼,🧑‍🔬,🧑‍🏫,👩🏼‍🏭,👩🏼‍💻,🧑🏼‍💻,👨🏿‍💻,👩🏼‍🏫,🕵🏻‍♀️,🤵🏻‍♀️,🤵🏻,🤵🏻‍♂️,👰‍♀️,🫅🏼'.split(','))
         users_status_marks = {
            'active' : ' ✅ فعال',
            'deactive':' ⭕️ غیر فعال'  ,
            'expired' :'🧮 منقضی '
         }

         
         try : 
            remaining_dayes = remaining(finishdate)
         except Exception as e:

            remaining_dayes = ' '   
         
         try:
           if remaining_dayes==' ':
              plane =  'نامعلوم'      
           else:   
               plane = plan_date(finishdate,startdate)
               if plane=='31' or plane=='30':
                  plane='یکماهه'
               elif plane=='NULL':
                  plane='نامعلوم'   
               elif plane!='31' or plane!='30':
                  plane = plane + 'روزه'  
         except ValueError :
              plane =  'نامعلوم'
   keyboard = InlineKeyboard()   
   keyboard.row(
         InlineButton("🪩  ترافیک مصرفی", 'hidden'))
   keyboard.row(
         InlineButton(" 🗳 ترافیک خریداری شده", 'hidden'),
         InlineButton(convert_mb_to_gb(traffic), 'hidden'))
   keyboard.row(
         InlineButton("📥 میزان حجم دانلود", 'hidden'),
         InlineButton(convert_mb_to_gb(download), 'hidden'))
   keyboard.row(
         InlineButton("📤 میزان حجم آپلود", 'hidden'),
         InlineButton(convert_mb_to_gb(upload), 'hidden'))
   keyboard.row(
         InlineButton("🗃 کل حجم مصرفی ",'hidden'),
         InlineButton(convert_mb_to_gb(total), 'hidden'))
   keyboard.row(
         InlineButton("📅 تاریخ کانفیگ", 'hidden'))
   keyboard.row(
         InlineButton("پلن خریداری شده ", 'hidden'),
         InlineButton(plane, 'hidden'))
   keyboard.row(
         InlineButton("تاریخ شروع کانفیگ ", 'hidden'),
         InlineButton(convert_to_persian_date(startdate), 'hidden'))
   keyboard.row(
         InlineButton("تاریخ انقضای کانفیگ ", 'hidden'),
         InlineButton(convert_to_persian_date(finishdate),'hidden'))
   keyboard.row(
         InlineButton("روز های باقی مانده ", 'hidden'),
         InlineButton(remaining_dayes, 'hidden'))
   keyboard.row(
         InlineButton("درخواست تمدید کانفیگ", f'extent-req:{usernamee}'))
   keyboard.row(
         InlineButton('بازگشت به لیست کانفیگها', f'configs:{usernamee}')
         )

   
   text_info = '''● مشخصات اکانت <code>{}</code>

◂وضعیت : {}
◂تعداد دستگاه مجاز : {}

➖➖➖➖➖➖➖'''.format(
   usernamee,users_status_marks[status],multiuser
)
   return [text_info,keyboard]



def get_user_connection(username):
   username = username
   host = host_url+api_token
   link = host+f'/user/{username}'

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
   text='''user name : <code>{}</code> 
password   : <code>{}</code>
Host : <code>{}</code>
port : <code>{}</code>
udpgw port : <code>7400</code>'''.format(username,password,domain,port)
   return text
   