from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup
from pyrogram import filters , Client
from pykeyboard import InlineKeyboard, InlineButton
from helpers.filters import * 
from helpers.keyboards import *
from helpers.userdata import user_data_mode

import os 
import requests
import json
import sys
sys.path.append(str(os.getcwd()).replace('\\','/')+'/helpers')




# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs , get_msgs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']
def check_user(username,password) -> bool:      
    users_file= str(os.getcwd().replace('\\','/'))+'/dbupdates/'+'users.json'
    with open(users_file,'r') as f :
        data = json.load(f)   
    for user in data:
        if username==user['username'] and password==user['password']:
            return True
        

    return False    
















user_info= {}
@Client.on_message(filters.private & USER_ID)
async def user_handler(b,m):
    global user_info

    user_id = m.chat.id
    text = m.text
    

    if user_id not in user_info:
        user_info[user_id] = {
       'username' : '',
       'password' : '',
       'step' : ''
    }
    user_start_kb = ReplyKeyboardMarkup([
        ['وضعیت اشتراک من'],['پشتیبانی','سوالات متداول'],['راهنمای استفاده']
    ])
    print(m)
    try:
        if text.split(' ')[0]=='/start':
            print('meow')
            print(text.split(' ')[1])
            data = text.split(' ')[1].split('-')
            username = data[1]
            password = data[-1]
            print(username,password)
            if check_user(username=username
                        ,password=password):
                print('yes')
                user_info[user_id]['step']= ''
                user_data = user_data_mode(username)

                user_info_kb = user_data[1]
                user_info_text = user_data[0]
                await m.reply(text=user_info_text,reply_markup=user_info_kb)
                pin_message_text = '''ازین پس با کلیک بر روی دکمه زیر وضعیت اشتراک خود را مشاهده کنید و یا برای تمدید اقدام بفرمایید .


    👇👇👇👇👇👇'''

                link_click = InlineKeyboardMarkup([
                    [InlineKeyboardButton(
                        'مشاهده وضعیت اشتراک',
                        url=f'https://t.me/{botid}?start=username-{username}-password-{password}'
                    )]
                ])
                pin_msg = await m.reply(text=pin_message_text,reply_markup=link_click)
                await b.pin_chat_message(m.chat.id, pin_msg.id,both_sides=True)
                user_info[user_id]['step']= ''
            elif not check_user(username=username,password=password):
                print('no')
                user_info[user_id]['step']= ''
                await b.send_sticker(chat_id=m.chat.id,sticker  = "CAACAgQAAxkBAAEPwwNlL9EI4M39EyXPv8wUDVoCWNuyigACtxIAAsuUgFGHuLEoz66DTjAE") 
                await m.reply(text= get_msgs('user_menu'),reply_markup=user_start_kb) 
    except:
        pass
    if text=='/start' :
        print(m)
        username = m.from_user.first_name
        await m.reply(text= get_msgs('user_menu').format(username),reply_markup=user_start_kb)
    if text=='وضعیت اشتراک من':
          #checking db for user existence 🐥🐥🐥🐥🐥
          # ## #if user in db show user the user prifile else req username and password .  
          
          await m.reply(get_msgs('username_req'))
          user_info[user_id]['step'] = 'username'
    elif user_info[user_id]['step']=='username':
        user_info[user_id]['username'] = text
        user_info[user_id]['step'] = 'password'
        await m.reply(text=get_msgs('password_req'))
        

    elif user_info[user_id]['step']=='password':
        user_info[user_id]['password'] = text
        
        #check user inputs 
        username = user_info[user_id]['username']
        password = user_info[user_id]['password']
        if check_user(username=user_info[user_id]['username']
                      ,password=password):
            user_info[user_id]['step']= ''
            user_data = user_data_mode(username)

            user_info_kb = user_data[1]
            user_info_text = user_data[0]
            await m.reply(text=user_info_text,reply_markup=user_info_kb)
            pin_message_text = '''ازین پس با کلیک بر روی دکمه زیر وضعیت اشتراک خود را مشاهده کنید و یا برای تمدید اقدام بفرمایید .


👇👇👇👇👇👇'''

            link_click = InlineKeyboardMarkup([
                [InlineKeyboardButton(
                    'مشاهده وضعیت اشتراک',
                    url=f'https://t.me/{botid}?start=username-{username}-password-{password}'
                )]
            ])
            pin_msg = await m.reply(text=pin_message_text,reply_markup=link_click)
            await b.pin_chat_message(m.chat.id, pin_msg.id,both_sides=True)
            user_info[user_id]['step']= ''
        elif not check_user(username=username,password=password):
            user_info[user_id]['step']= ''
            await b.send_sticker(chat_id=m.chat.id,sticker  = "CAACAgQAAxkBAAEPwwNlL9EI4M39EyXPv8wUDVoCWNuyigACtxIAAsuUgFGHuLEoz66DTjAE") 
            username = m.from_user.first_name
            await m.reply(text= get_msgs('user_menu').format(username),reply_markup=user_start_kb)
            




        

    elif text=='راهنمای استفاده':
         how_text = '''با توجه به سیستم عامل خود نرم افزار مورد نیاز رو دانلود کنید و با آموزش میتونید به کانفیگ خودتون متصل بشید . 

    ┈┅┅━⊷⊰ اندروید ⊱⊶━┅┅┈
‏° Ssh netmod 
🐥 [اموزش](https://t.me/sshhowto/3) | [دانلود](https://play.google.com/store/apps/details?id=com.netmod.syna&hl=en_US)
‏° Napestenetv 
🐥 [اموزش](https://t.me/sshhowto/16) | [دانلود](https://play.google.com/store/apps/details?id=com.napsternetlabs.napsternetv&hl=en_US)



    ┈┅┅━⊷⊰ آیفون ⊱⊶━┅┅┈
‏° Napestenetv 
🐥 [اموزش](https://t.me/sshhowto/25) | [دانلود](https://apps.apple.com/gb/app/napsternetv/id1629465476)



    ┈┅┅━⊷⊰ ویندوز ⊱⊶━┅┅┈
‏° Ssh netmod 
🐥 [اموزش](https://t.me/sshhowto/4) | [دانلود](https://sourceforge.net/projects/netmodhttp/files/latest/download)
‏° Respite vpn
🐥 [اموزش](https://www.youtube.com/watch?v=zJEi2c9BCyA) | [دانلود](https://sourceforge.net/projects/respite-vpn/files/latest/download)'''
         await m.reply(text=how_text,disable_web_page_preview=True)
    elif text=='پشتیبانی'  :
        sup_text = '''🔰 در صورتی که سوال شما در بخش (⁉️ سوالات متداول) یافت نشد، با پشتیبانی ارتباط بگیرید

⭕️ تا زمان دریافت پیام خود صبور باشید.

⭕️ از ارسال پیام های پی در پی خودداری کنید.

⭕️ پیام خود را خارج از مسائل مربوطه ارسال نکنید.

⭕️ درخواست امتیاز و موجودی رایگان نکنید

📛 در صورت عدم رعایت قوانین، حساب کاربری شما مسدود خواهد شد.

✅ آیا با قوانین ما موافقت میکنید؟'''
        sup_button = InlineKeyboard()
        sup_button.row(
            InlineButton(
                'تایید قوانین و ارتباط با پشتیبانی',
                'sup'
            )
        )
        sup_msg = await m.reply(text=sup_text,reply_markup=sup_button)
    elif text=='سوالات متداول' :
        await m.reply('''☑️ سوالات و مشکلات متداول ؛

اگر در اتصال مشکل دارید و کانفیگ شما وصل نمیشود احتمالا به دلایل زیر است اگر مشکل شما با  بررسی موارد زیر حل نشد به پشتیبانی اطلاع دهید . 

۱. از صحّت تنظیم نقطه اتصال همراه (APN) اینترنت خود مطمین شوید « تنظیمات صحیح APN »

۲. مطمئن شوید که ارور فضای داخلی ناکافی از تلفن خود دریافت نکردید چون در این صورت کانفیگ شما متصل نخواهد شد . 

۳. از اینکه بسته اینترنتی شما تمام نشده است مطمئن شوید

۴. چک کنید که روی اینترنت گوشی شما حالت دانش آموزی  یا ( بومینو ) فعال نباشد برای بررسی این مورد با شماره گیری ستاره ۱۰۰ ستاره ۶۴ مربع میتونید استعلام بگیرید ، اگر فعال بود غیرفعال کنید و مجدد به کانفیگتون متصل بشید .


۵ . ممکن هست در شبکه اینترنت شما اختلال وجود داشته باشه معمولاً با یک بار خاموش روشن کردن حالت هواپیما (air plane mode) و بعد خاموش و روشن کردن اینترنت مشکل شما حل بشه .

مشکلات نرم افزار ؛
در صورتی که برنامه شما crash می‌کنه مشکلی از کانفیگ وجود نداره برای حل مشکل حتما برنامه رو از لینک های موجود در بخش راهنما دانلود کنید . 


در انتها حتما ازتون میخوام آموزش هارو با دقت ببینید و بعدش در اخرین مرحله اگر مشکلی وجود داشت به پشتیبانی پیام بدین ''')  


    

   
    
