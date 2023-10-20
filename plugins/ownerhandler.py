from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup
from pyrogram import filters , Client
from config import config as C
from helpers.db_tools import show_sellers
from helpers.filters import * 
from helpers.keyboards import *
import json
import requests
from pykeyboard import InlineKeyboard, InlineButton
from helpers.convert_persian_data import convert_to_persian_date
from helpers.convert_traffic import convert_mb_to_gb
from helpers.remaining_days import remaining , plan_date

import random
from plugins.inline_kb_handler import ADD_STEPS , user_creation_info , desc
from helpers.step_handler import *
from helpers.keyboards import *
from helpers.userdata import *
from helpers.panel_status import *
from helpers.add_user import create_new_user
from helpers.db_tools import *
from helpers.edit_user import *
m_ids = []


@Client.on_message(filters.private & OWNER_ID)
async def owner_handler(b,m):
    global ADD_STEPS

    global desc
    global m_ids
    print(ADD_STEPS)
    global user_edit_data_dict
    global user_creation_info
    user_id = m.chat.id
    text=m.text
    
 
    if '/start' in text:

       if len(text.split(' '))>1:
                command=text.split(' ')[1] 
                if command.split('-')[0]=='online':
                    
                    username = command.split('-')[1]
                    print(username)
                    connections = user_connections(username)
                    try:
                        if len(connections)!=0:
                            await m.reply(text=connections[0],reply_markup=connections[1])
                        else:
                            await m.reply('کانکشن یافت نشد') 
                    except:
                        await m.reply('کانکشن یافت نشد') 

                elif  command.split('-')[0]=='profile':
                    print('[viewing user prifile] : by owner')
                    username = command.split('-')[1]  
                    get_user = user_data(username)
                    gutext = get_user[0]
                    kb = get_user[1]
                    await m.reply(text=gutext,reply_markup =kb)
       else:
       
            start_text = '''● مالک عزیز خوش آمدین برای ادامه عملیات مورد نظر خود را انتخاب کنید 

    ➖➖➖➖➖➖➖
    '''
            a = await m.reply(start_text,reply_markup =owner_keyboard)
            m_ids.append(a.id)

    else:
        try:
            if ADD_STEPS[user_id]=='':
                
                pass
            else:
                if user_id not in user_creation_info:
                    
                    user_creation_info[user_id]={}
                    try:
                        await b.delete_messages(
                            chat_id=user_id,
                            message_ids=m_ids[0]
                        )
                        m_ids.clear()
                    except :
                        pass    
                
                if ADD_STEPS[user_id]=='add-admin':
                    print('LOGS [ admin add process] : tg id  input')
                    admin_to_add = m.text
                    add_seller(admin_to_add)
                    m_ids.append(m.id-1)
                    try:
                        await b.delete_messages(
                            chat_id=user_id,
                            message_ids=m_ids[0]
                        )
                        m_ids.clear()
                    except :
                        pass
                    kb = InlineKeyboard()
                    kb.row(
                        InlineButton('➡️ بازگشت','back:main-menu')
                    )
                    await m.reply('ادمین {} با موفقیت به لیست فروشندگان اضافه شد'.format(admin_to_add),reply_markup=kb)
                    ADD_STEPS[user_id] = ''

                if  ADD_STEPS[user_id]=='name-input':
                    print('LOGS [ user creation process] : name input')
                    user_creation_info[user_id]['name']=m.text
                    ADD_STEPS[user_id] = 'password-input'
                    a = await m.reply(text=steps[ADD_STEPS[user_id]],reply_markup=cancel_kb) 
                    m_ids.append(a.id)
                    
                    print(user_creation_info)
                
                    


                elif ADD_STEPS[user_id]=='password-input': 
                    try:
                        await b.delete_messages(
                            chat_id=user_id,
                            message_ids=m_ids[0]
                        )
                    except:
                        pass    
                    m_ids.clear()
                    user_creation_info[user_id]['password']=m.text
                    print('LOGS [ user creation process] : password input')
                    ADD_STEPS[user_id] = 'traffic'
                    a = await m.reply(text=steps[ADD_STEPS[user_id]],reply_markup=traffic_kb)
                    m_ids.append(a.id) 
                    
                elif ADD_STEPS[user_id]=='traffic':  
                    await b.delete_messages(
                        chat_id=user_id,
                        message_ids=m_ids[0]
                    )
                    m_ids.clear() 
                    user_creation_info[user_id]['traffic']=m.text
                    print('LOGS [ user creation process] : traffic input')
                    ADD_STEPS[user_id] = 'multiuser'
                    a = await m.reply(text=steps[ADD_STEPS[user_id]],reply_markup=multiuser_kb) 
                    m_ids.append(a.id)
                    
                elif ADD_STEPS[user_id]=='multiuser': 
                    try:
                        await b.delete_messages(
                            chat_id=user_id,
                            message_ids=m_ids[0]
                        )
                    except:
                        pass 
                    m_ids.clear()  
                    user_creation_info[user_id]['multiuser']=m.text
                    print('LOGS [ user creation process] : multiuser input')
                    ADD_STEPS[user_id] = 'expire-input'
                    a = await m.reply(text=steps[ADD_STEPS[user_id]],reply_markup=exp_kb) 
                    m_ids.append(a.id)
                    print(user_creation_info)
                elif ADD_STEPS[user_id]=='expire-input':   
                    user_creation_info[user_id]['expire-input']=m.text
                    ADD_STEPS[user_id] = 'confirm-creation'
                    print('LOGS [ user creation process] : expire input')
                    await m.reply(text=steps[ADD_STEPS[user_id]],reply_markup=confirm_creation) 
                    print(user_creation_info)

                elif ADD_STEPS[user_id]=='del-user-input-name':
                    try:
                        dm = user_data(text)
                        info = dm[0]
                        kb = dm[1]
                        await m.reply(text=info,reply_markup=kb)
                        ADD_STEPS.clear()
                    except Exception as e:
                        
                        not_found = '''» کاربر وارد شده یافت نشد

    از نمایش کاربران کاربر مورد نظر را انتخاب کرده یا مجددا نام کاربر را به درستی وارد کنید .'''
                        keyboard = InlineKeyboard()
                        keyboard.row(
        InlineButton("بازگشت به نمایش کاربران", 'back:show-users')
    )   
                        ADD_STEPS.clear()
                        await m.reply(text=not_found,reply_markup=keyboard)
                elif ADD_STEPS[user_id]=='find-user-input-name':
                    try:
                        dm = user_data(text)
                        info = dm[0]
                        kb = dm[1]
                        await m.reply(text=info,reply_markup=kb)
                        ADD_STEPS.clear()
                    except Exception as e:
                        print(e)
                        not_found = '''» کاربر وارد شده یافت نشد

    از نمایش کاربران کاربر مورد نظر را انتخاب کرده یا مجددا نام کاربر را به درستی وارد کنید .'''
                        keyboard = InlineKeyboard()
                        keyboard.row(
        InlineButton("بازگشت به نمایش کاربران", 'back:show-users')
    )   
                        ADD_STEPS.clear()
                        await m.reply(text=not_found,reply_markup=keyboard)
 

                elif ADD_STEPS[user_id]=='edit-user':  
                    print('LOGS : Edit user')
                    try:
                        nb = await m.reply('در حال درخواست ادیت کاربر ...') 
                        x = m.text.splitlines()
                        new_username = x[13].split(':')[1].strip()    
                        new_password = x[14].split(':')[1].strip()   
                        new_traffic = x[15].split(':')[1].strip()   
                        new_multiuser = x[16].split(':')[1].strip()   
                        new_exp = x[17].split(':')[1].strip().replace('+','')   
                        old_date = x[7].split(':')[1].strip()
                       
                        user_edit_data_dict["edit"] ={
            "username" : new_username.lower(),
            "password" : new_password.lower(),
            "multiuser"  : new_multiuser,
            "traffic"  : new_traffic,
            "type_traffic" : 'gb' ,
            "expdate" : add_days_to_date(old_date,int(new_exp)),
            "activate":'active'
            
        } 

                        
                        if edit_user_info(user_edit_data_dict["edit"]):
                            nb_kb = InlineKeyboard()
                            nb_kb.row(
                                InlineButton('بازگشت به لیست کاربران','show-users')
                            )
                            await nb.edit_text('اطلاعات کاربر {} با موفقیت آپدیت شد'.format(user_edit_data_dict['original']['username']),reply_markup=nb_kb)
                        else :
                            nb_kb = InlineKeyboard()
                            nb_kb.row(
                                InlineButton('بازگشت به لیست کاربران','show-users')
                            )
                            await nb.edit_text('عملیات ویرایش کاربر با خطا روبرو شد',reply_markup=nb_kb)

                    except : 
                            nb_kb = InlineKeyboard()
                            nb_kb.row(
                                InlineButton('بازگشت به لیست کاربران','show-users')
                            )
                            await nb.edit_text('عملیات ویرایش کاربر با خطا روبرو شد',reply_markup=nb_kb)

                        

                    
                    

        except KeyError:
            pass                


                    
  






