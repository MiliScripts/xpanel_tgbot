import random
import asyncio
from pyrogram import Client,idle,filters,enums,errors 
from asyncio import get_event_loop
from time import time
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ReplyKeyboardRemove , ForceReply
from pyrogram.errors import BadRequest
import requests
import pyromod
from helpers.show_users import show_users
from helpers.userdata import *
from helpers.create_test_user import *
from helpers.keyboards import *
from helpers.delete_user import *
from helpers.edit_user import *
from helpers.user_setting import *
from helpers.backup import *
from helpers.step_handler import steps
from helpers.add_user import create_new_user
from helpers.panel_status import online_users_info
from helpers.users_status import *
from helpers.reset_traffic import reset_traffic
from helpers.kill_connection import *
from helpers.extent import *
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs 
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']
owner = get_configs()['owner']
sup_id = get_configs()['sup_id']







user_creation_info = {
    
}

ADD_STEPS = {

}



desc = ''



@Client.on_callback_query()
async def handle_delete(b,q):
    global show_users_sort
    global back_up_settings
    global desc
    global ADD_STEPS
    global user_creation_info
    text = q.data  
    user_id=q.from_user.id
    if text=='show-users':
        await q.edit_message_text('⏳') 
        users= show_users(show_users_sort)
        show_users_ui = users[0]
        show_users_text='''» بخش نمایش کاربران 
✓ برای دیدن اطلاعات کاربر مورد نظر یا انجام تغییرات روی کاربر لطفا از منوی زیر کاربر موردنظر را انتخاب کنید 

✓ از صفحات که به شکل دکمه های  «۲» یا «۱» هستند میتونید بقیه یوزر هارو تو صفحات بعدی ببینید .


✓ برای یافتن کاربرد مورد نظر شما میتونید اسم کاربر رو ارسال کنید .
➖➖➖➖➖➖➖
'''
        await q.edit_message_text(text=show_users_text,reply_markup=show_users_ui)
        ADD_STEPS[user_id] = 'find-user-input-name'

    elif text=='sup':
        await q.edit_message_text(f'''☎️  آیدی پشتیبانی   :‌

{sup_id}''')
    
       

    elif text.split(":")[0]=='user-connection':
        username = text.split(":")[1]

        text = get_user_connection(username)
        
        kb = InlineKeyboard()
        kb.row(
            InlineButton('⇥ بازگشت','profile:{}'.format(username))
        )
        await q.edit_message_text(text=text,reply_markup=kb)
    elif text.split(':')[0]=='userspage':
        # await q.edit_message_text('⏳') 
        page_number = int(text.split(':')[1])
        users= show_users(show_users_sort)
        show_users_ui = users[page_number]
        show_users_text='''● بخش نمایش کاربران

➖➖➖➖➖➖➖
◂ برای مدیریت هر کاربر روی نام کاربر کلیک کنید 
◂ برای دیدن کاربران بیشتر از صفحات استفاده کنید . 

➖➖➖➖➖➖➖
'''
        await q.edit_message_text(text=show_users_text,reply_markup=show_users_ui)

    elif text.split(':')[0]=='profile':    
        ADD_STEPS[user_id] = ''
        username = text.split(':')[1]
        await q.edit_message_text('⏳') 
        userdata = user_data(username=username)

        user_data_ui = userdata[1]
        user_data_text= userdata[0]

        await q.edit_message_text(text=user_data_text,reply_markup=user_data_ui)
    elif text.split(':')[0]=='profile-user':    
        username = text.split(':')[1]
        await q.edit_message_text('⏳') 
        userdata = user_data_mode(username=username)

        user_data_ui = userdata[1]
        user_data_text= userdata[0]

        await q.edit_message_text(text=user_data_text,reply_markup=user_data_ui)
    elif text.split(':')[0]=='extent-req':
        username = text.split(':')[1]
        ex_report ='''درخواست تمدید کانفیگ با نام کاربری <code>{}</code>  


➖➖➖➖➖➖➖'''.format(username)   
        user_check_kb = InlineKeyboard()
        user_check_kb.row(
            InlineButton('مشاهده اطلاعات کانفیگ',f'profile:{username}')
        )
        ad = InlineKeyboard()
        ad.row(
         InlineButton('⇥ بازگشت به لیست کانفیگها', f'configs:{username}')
         )
        await q.edit_message_text('درخواست تمدید این اشتراک با موفقیت به ادمین ارسال شد')
        await b.send_message(chat_id= owner,text=ex_report,reply_markup=user_check_kb)  

    elif text=='on-expired-users':
        kb = back_to_types
        
        etmam_text = etmam()
        await q.edit_message_text(text=etmam_text,reply_markup =kb) 
    elif text=='expired-users':
        kb = back_to_types  
        
        ex_text= expired()
        await q.edit_message_text(text=ex_text,reply_markup =kb)  
    elif text=='deactive-users':
        kb = back_to_types 
            
        du_text = deactives()
        await q.edit_message_text(text=du_text,reply_markup =kb) 

    elif text.split(':')[0]=='kill':
        type_of_kill = text.split(':')[1].split('-')[0] 

        if type_of_kill=='id':
            pid = text.split(':')[1].split('-')[1] 
            
            kill_pid(pid)

            await q.edit_message_text(text='اتصال کانکشن مورد نظر قطع شد',reply_markup=back_to_online)
        elif type_of_kill=='user':
            username = text.split(':')[1].split('-')[1] 

            
            kill_user(username)

            await q.edit_message_text(text=' تمام اتصال های  کاربر {}   قطع شد'.format(username),reply_markup=back_to_online)
    elif text=='create-test':
        
        await q.edit_message_text(text=create_test_user(),reply_markup=back_to_menu)
    elif  text.split(':')[0]=='back':
        back_to = text.split(':')[1]  
        if back_to=='show-users':
            
            users= show_users(show_users_sort)
            number_of_users = str(users[0])
            show_users_ui = users[1]
            show_users_text='''● بخش نمایش کاربران

    ➖➖➖➖➖➖➖
    ◂ برای مدیریت هر کاربر روی نام کاربر کلیک کنید 
    ◂ تعداد کاربران : <code>{}</code>
    ◂ برای دیدن کاربران بیشتر از صفحات استفاده کنید . 

    ➖➖➖➖➖➖➖
    '''.format(number_of_users)
            await q.edit_message_text(text=show_users_text,reply_markup=show_users_ui)
        elif  back_to=='main-menu' :
            if q.from_user.id== owner:

                main_menu_text = '''● به منوی اصلی  بازگشتید , برای ادامه عملیات مورد نظر خود را انتخاب کنید 

    ➖➖➖➖➖➖➖
    '''
                await q.edit_message_text(text=main_menu_text,reply_markup=owner_keyboard)
            else:
                  main_menu_text = '''● به منوی اصلی  بازگشتید , برای ادامه عملیات مورد نظر خود را انتخاب کنید 

    ➖➖➖➖➖➖➖
    '''
                  await q.edit_message_text(text=main_menu_text,reply_markup=admin_keyboard)

        elif back_to=='type':
           
           category_text = '''» بخش دسته بندی کاربران

✓ دسته بندی مورد نظر خود را برای مشاهده انتخاب کنید .'''
           await  q.edit_message_text(text=category_text,reply_markup=user_category)     
    if text.split(':')[0]=='backupmode':
        interval = text.split(':')[1]
        
        backup_settings['interval'] = int(interval)

        await  q.edit_message_text('زمان بندی بکاپ خودکار تنظیم شد',reply_markup= back_up_interval())
    elif text=='hidden':
        await q.answer('دکمه نمایشی')
    elif  text.split(':')[0]=='extent':
        parametrs =  text.split(':')[1] 
        username = parametrs.split('-')[0]
        day_to_extent = parametrs.split('-')[1]
        extent_user(username,int(day_to_extent))
        await  q.edit_message_text('اشتراک کاربر {} با موفقیت تمدید شد')
        
        kb = InlineKeyboard()
        kb.row(
            InlineButton('⇥ بازگشت','profile:{}'.format(username))
        )
        await q.edit_message_text('اشتراک کاربر {} با موفقیت تمدید شد'.format(username),reply_markup=kb)

    elif text=='auto-backup-on':
        backup_settings['mode'] = 'on' 

        bu_set_kb = InlineKeyboard()
        bu_set_kb.row(
            InlineButton('⇥ بازگشت','auto-backup-on')
        )
        text = '''عملیات مورد نظر خود را انتخاب کنید
➖➖➖➖➖➖'''
        await  q.edit_message_text(text=text,reply_markup= back_up_setting()) 
    elif text=='sort-show-users':
        if show_users_sort =='':
            show_users_sort = 'creation-time'
        text_susk = '''◄ تنظیمات نمایش کاربران 
انتخاب کنید نمایش کاربران بر چه مبنایی باشد 
❚ با انتخاب هر گزینه مبنای نمایش کاربران به آن تغییر پیدا میکنید

❯❯ ترتیب [ زمان ساخت](پیشنهادی)

نمایش کاربران بر اساس زمان ایجاد اشتراک از جدید ترین کاربر به قدیمی ترین کاربر ساخته شده 

❯❯ ترتیب [ انقضا ]
نمایش کاربران به ترتیب از کاربرانی که زمان پایان اشتراک آنها نزدیک است .

❯❯ ترتیب [ پر مصرف ]
نمایش کاربران بصورت از پر مصرف به کاربرانی که حجم مصرفی کمتری داشته اند

➖➖➖➖➖➖➖➖➖➖➖➖

ترتیب فعلی : {}'''.format(show_users_sort)   
        show_users_sort_kb = InlineKeyboard(row_width=3)
        list_of_buttons = []
        sorts = {
            'زمان ساخت':'sort:creation-time',
            'انقضا':'sort:traffic',
            ' پر مصرف':'sort:exprie-date'
        }

        for k,v in sorts.items():
           if v.split(':')[1]==show_users_sort:
            list_of_buttons.append(
                InlineButton('✅ '+k,v)
            )
           else:
            list_of_buttons.append(
                InlineButton(k,v)
            )
        show_users_sort_kb.add(*list_of_buttons)
        show_users_sort_kb.row(
            InlineButton('  ⇥ بازگشت','show-users')
        )
        await  q.edit_message_text(text=text_susk,reply_markup=show_users_sort_kb) 
    elif text.split(':')[0]=='sort':
        show_users_sort = text.split(':')[1]

        sort_farsi = {
            'exprie-date' :'ترتیب [ انقضا ]',
            'traffic' :'ترتیب [ پر مصرف ]',
            'creation-time' : 'پیشفرض (ترتیب [ زمان ساخت])'
        }
        back_to_show = InlineKeyboard()
        back_to_show.row(
            InlineButton('  ⇥ بازگشت','show-users')
        )
        text_susk = '''◄ تنظیمات نمایش کاربران 
انتخاب کنید نمایش کاربران بر چه مبنایی باشد 
❚ با انتخاب هر گزینه مبنای نمایش کاربران به آن تغییر پیدا میکنید

❯❯ ترتیب [ زمان ساخت](پیشنهادی)

نمایش کاربران بر اساس زمان ایجاد اشتراک از جدید ترین کاربر به قدیمی ترین کاربر ساخته شده 

❯❯ ترتیب [ انقضا ]
نمایش کاربران به ترتیب از کاربرانی که زمان پایان اشتراک آنها نزدیک است .

❯❯ ترتیب [ پر مصرف ]
نمایش کاربران بصورت از پر مصرف به کاربرانی که حجم مصرفی کمتری داشته اند

ترتیب فعلی : {}

➖➖➖➖➖➖➖➖➖➖➖➖'''.format(sort_farsi[show_users_sort])
        show_users_sort_kb = InlineKeyboard(row_width=3)
        list_of_buttons = []
        sorts = {
            'زمان ساخت':'sort:creation-time',
            'انقضا':'sort:exprie-date',
            ' پر مصرف':'sort:traffic'
        }

        for k,v in sorts.items():
          if v.split(':')[1]==show_users_sort:
            list_of_buttons.append(
                InlineButton('✅ '+k,v)
            )
          else:
            list_of_buttons.append(
                InlineButton(k,v)
            )
        show_users_sort_kb.add(*list_of_buttons)
        show_users_sort_kb.row(
            InlineButton('  ⇥ بازگشت','show-users')
        )
        await  q.edit_message_text(text=text_susk,reply_markup=  show_users_sort_kb)
    elif text=='cancel':
        await  q.edit_message_text(text='''❚  به منوی اصلی  بازگشتید

❯❯  برای ادامه میتوانید یکی از آپشن های منو را انتخاب کنید .


➖➖➖➖➖➖➖➖''',reply_markup=admin_keyboard)    
    elif text.split(':')[0]=='manage-sellers':
        action = text.split(':')[1]
        if action=='add':
            ADD_STEPS[user_id] = 'add-admin'
            add_admin_text = 'آیدی عددی ادمین مورد نظر را برای افزودن ارسال کنید'
            cancel_kb1 = InlineKeyboard()
            cancel_kb1.row(
                InlineButton(
                    'انصراف',
                    'cancel'
                )
            )
            await  q.edit_message_text(text=add_admin_text,reply_markup=cancel_kb1)
        elif action=='del':

             show_admins = show_sellers()
             if len(show_admins)!=0:
                del_admin_text = 'برای حذف ادمین از لیست ادمین ها بر روی ایدی عددی ادمین کلیک کنید'
                del_admin = InlineKeyboard()
                for i in show_sellers():
                    del_admin.row(
                        InlineButton(i,f'del-admin:{i}')
                    )
                del_admin.row(
            InlineButton('  ⇥ بازگشت','manage-admins')
        )       
                await  q.edit_message_text(text=del_admin_text,reply_markup=del_admin)
             else:
                empty_show='❚  لیست ادمین های ربات خالی می‌باشد'  
                kb = InlineKeyboard()
                kb.row(
             InlineButton('  ⇥ بازگشت','manage-admins')
        )        
                await  q.edit_message_text(text=empty_show,reply_markup=kb)      
        elif action=='show':
            show_admins = show_sellers()
            kb = InlineKeyboard()
            kb.row(
           InlineButton('  ⇥ بازگشت','manage-admins')
        )       
            if len(show_admins)!=0:
                show_sellers_text = '❯❯  لیست ادمین :'+'\n'
                for admin in show_sellers():

                    user_name = f'[{str(admin)}](tg://user?id={str(admin)})'

                    show_sellers_text+=user_name+'\n'
                await  q.edit_message_text(text=show_sellers_text,reply_markup=kb)
            else:
                empty_show='❚  لیست ادمین های ربات خالی می‌باشد'  
                kb = InlineKeyboard()
                kb.row(
           InlineButton('  ⇥ بازگشت','manage-admins')
        )        
                await  q.edit_message_text(text=empty_show,reply_markup=kb)

    elif text=='manage-admins':
        text_admin_menu='''❚ بخش مدیریت ادمین ها

یک گزینه را برای ادامه انتخاب کنید . 

➖➖➖➖➖➖➖➖''' 
        await  q.edit_message_text(text=text_admin_menu,reply_markup=manage_sellers_kb)       
    elif text.split(':')[0]=='del-admin':
        admin_to_delete =  text.split(':')[1]
        kb = InlineKeyboard()
        kb.row(
            InlineButton('  ⇥ بازگشت','manage-admins')
        )        
        await  q.edit_message_text(text=del_seller(admin_to_delete),reply_markup=kb)
    elif text=='auto-backup-off':
        bu_set_kb = InlineKeyboard()
        bu_set_kb.row(
            InlineButton('  ⇥ بازگشت','action:auto-backup-setting')
        )
        backup_settings['mode'] = 'off'

        text = '''عملیات مورد نظر خود را انتخاب کنید
➖➖➖➖➖➖''' 
        await  q.edit_message_text(text=text,reply_markup= back_up_setting()) 

             
    elif text.split(':')[0]=='user-action':
        action = text.split(':')[1].split('-')[0]
        username = text.split(':')[1].split('-')[1]    
        #delete user 
        if action=='delete':
            confirm_delete_text = '''● آیا از حذف کاربر <code>{}</code> اطمینان دارید ؟
 

➖➖➖➖➖➖➖
'''.format(username)        
            confirm_delete_kb = InlineKeyboard()
            confirm_delete_kb.row(
                InlineButton("🗑 تایید حذف",f'action:confirm-delete={username}'),
                InlineButton('❌ لغو','action:cancel'),

            )
            await q.edit_message_text(text=confirm_delete_text,reply_markup=confirm_delete_kb)
            

        elif action=='extent':

            extent_kb = InlineKeyboard()
            extent_kb.row(
                InlineButton('تمدید برای یک ماه','extent:{}-30'.format(username))
            )
            extent_kb.row(
                InlineButton('تمدید برای دو ماه','extent:{}-60'.format(username))
            )
            extent_kb.row(
                InlineButton('تمدید برای سه ماه','extent:{}-90'.format(username))
            )
            extent_kb.row(
                    InlineButton('⇥ بازگشت به منوی اصلی', 'back:main-menu'),
            )    
            await q.edit_message_text(text='''برای تمدید ماهانه کاربر {} یکی از گزینه های زیر را انتخاب کنید 


    ➖➖➖➖➖➖➖'''.format(username),reply_markup=extent_kb)
        #edit
        elif action=='edit':
            ADD_STEPS[user_id] ='edit-user'
            user_creation_info[user_id]={}
            text_edit_user = '''#راهنما_ویرایش_کاربر 

🖌 مواردی که میخواهید ادیت کنید را تغییر دهید و بدون مواردی که نمیخواهید تغییر دهید را بدون تغییر رها کرده و به بات ارسال کنید .
🖍 برای اضافه کردن به تاریخ انقضای کاربر تعداد روزهایی که میخواهید اضافه کنید را به  جلوی مقدار تاریخ انقضا قرار دهید .

برای تغییر یا ادیت هر پارامتر برای کاربر در جلوی هر پارامتر مقدار مدنظر خود را قرار دهید برای مثال :

• وارد کنید | اطلاعات جدید کاربر (ادیت ):
نام کاربری: milad
پسورد : milad
ترافیک : 30
تعداد دستگاه مجاز : 4
تاریخ انقضا: 

حالا روی دکمه زیر کلیک کرده و بات را از صفحه باز شده ( لیست چت ها ) انتخاب کنید و سپس متنی که در قسمت تایپ دارید را با مقادیری مه میخواهید ادیت کنید کامل کنید و بعد به ربات ارسال کنید.

‏➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖'''
            await q.edit_message_text(text=text_edit_user,reply_markup=get_edit_data_kb(username))
        #reset traffic
        elif action=='reset':
            kb = InlineKeyboard()
            kb.row(
                InlineButton('  ⇥ بازگشت',f'profile:{username}')
            )
            await q.edit_message_text(text=reset_traffic(username))
        #activation
        elif action=='activate':
            await q.edit_message_text('⏳') 
            activate(username)
            activate_user_report = '''✅  کاربر <code>{}</code> با موفقیت غیرفعال شد
 

➖➖➖➖➖➖➖
'''.format(username)
            back_to_users_list_kb = InlineKeyboard()
            back_to_users_list_kb.row(
                InlineButton("⇥ بازگشت", 'back:main-menu')
            )
            await q.edit_message_text(text=activate_user_report,reply_markup=back_to_users_list_kb)
        #deactivation
        elif action=='deactivate':
            await q.edit_message_text('⏳') 
            deactivate(username)
            deactivate_user_report = '''✅  کاربر <code>{}</code> با موفقیت غیرفعال شد
 

➖➖➖➖➖➖➖
'''.format(username)
            back_to_users_list_kb = InlineKeyboard()
            back_to_users_list_kb.row(
                InlineButton("⇥ بازگشت", 'back:main-menu')
            )
            await q.edit_message_text(text=deactivate_user_report,reply_markup=back_to_users_list_kb)

        #extent
        elif action=='extent':
            pass
    elif text=='set-backup-time':
        sbt_text ='''انتخاب کنید بکاپ خودکار چگونه ارسال شود


    ➖➖➖➖➖➖➖'''
        await q.edit_message_text(text=sbt_text,reply_markup=back_up_interval())
    elif text.split(':')[0]=='action':
        action = text.split(':')[1]   
        if action=='cancel' or action=='close':
            await q.message.delete()
        elif action.split('=')[0]=='confirm-delete':
            username = action.split('=')[1]
            del_user(username)
            delete_user_report = '''✅  کاربر <code>{}</code> با موفقیت حذف شد
 

➖➖➖➖➖➖➖
'''.format(username)
            back_to_users_list_kb = InlineKeyboard()
            back_to_users_list_kb.row(
                InlineButton("⇥ بازگشت", 'back:main-menu')
            )
            await q.edit_message_text(text=delete_user_report,reply_markup=back_to_users_list_kb)

        elif action=="get-back-up":
            await backup_func(user_id,b)


        elif action=="auto-backup-setting":
            abs_text ='''عملیات مورد نظر خود را انتخاب کنید
➖➖➖➖➖➖'''
            await q.edit_message_text(text=abs_text,reply_markup=back_up_setting())


        elif action=='cancel-adding':
            await q.edit_message_text('''عملیات ساخت کاربر لغو شد ''',reply_markup=back_to_menu)
            user_creation_info.clear()
            ADD_STEPS.clear()
        elif action=='add-confirm':
              await q.edit_message_text('''🕜 در حال ساخت کاربر ...''')
              await q.edit_message_text(create_new_user(
                  user_creation_info[user_id]['name'],
                  user_creation_info[user_id]['password'],
                  user_creation_info[user_id]['traffic'],
                  user_creation_info[user_id]['expdate'],
                  user_creation_info[user_id]['multiuser']),reply_markup=back_to_menu)
                         
              user_creation_info.clear()
              ADD_STEPS.clear() 

    elif text=='backup':
        bu_text = '''عملیات مورد نظر را انتخاب کنید'''
        await  q.edit_message_text(text=bu_text,reply_markup=back_up_kb)
    #creating new user _________________________________________________
    elif text=='add-user':
      ADD_STEPS[user_id] = 'name-input'
      await  q.edit_message_text(text=steps[ADD_STEPS[user_id]],reply_markup=cancel_kb)


    elif text.split(':')[0]=='traffic':
        traffic =  text.split(':')[1]
        ADD_STEPS[user_id]='multiuser'
        user_creation_info[user_id]['traffic'] = traffic

        await q.message.delete()

        await b.send_message(chat_id = user_id,text=steps[ADD_STEPS[user_id]],reply_markup=multiuser_kb)
    elif text.split(':')[0]=='multiuser':
        multiuser =  text.split(':')[1]
        ADD_STEPS[user_id]='expire-input'
        user_creation_info[user_id]['multiuser'] = multiuser

        await q.message.delete()

        await b.send_message(chat_id = user_id,text=steps[ADD_STEPS[user_id]],reply_markup=exp_kb)

    elif text.split(':')[0]=='expdate':
        expdate =  text.split(':')[1]

        user_creation_info[user_id]['expdate'] = expdate

        await q.message.delete()
        ADD_STEPS[user_id] = 'confirm-creation'

        await b.send_message(chat_id = user_id,text=steps[ADD_STEPS[user_id]].format(
            user_creation_info[user_id]['name'],
            user_creation_info[user_id]['password'],
            user_creation_info[user_id]['traffic'],
            user_creation_info[user_id]['multiuser'],
            user_creation_info[user_id]['expdate']

        ),reply_markup=confirm_creation)  


    elif text=='del-user':
          ADD_STEPS[user_id] = 'del-user-input-name'
          del_user_text = '''کاربر مورد نظر خود را از منوی زیر برای حذف انتخاب کنید یا نام کاربری را  ارسال کنید'''
          users= show_users(show_users_sort)
          show_users_ui = users[1]
          await  q.edit_message_text(text=del_user_text,reply_markup=show_users_ui)

    elif text=='user-type':
              category_text = '''» بخش دسته بندی کاربران

✓ دسته بندی مورد نظر خود را برای مشاهده انتخاب کنید .'''
              await  q.edit_message_text(text=category_text,reply_markup=user_category) 

    elif text=='online-users':
          
          back_to_type = InlineKeyboard()
          back_to_type.add(
              InlineButton('⇥ بازگشت به دسته بندی کاربران','back:type')
          )
          await  q.edit_message_text(text=online_users_info(),reply_markup=back_to_type)   

             


        
    


                





               




