import json
import requests
from pykeyboard import InlineKeyboard, InlineButton
from helpers.convert_persian_data import convert_to_persian_date
from helpers.convert_traffic import convert_mb_to_gb
from helpers.remaining_days import remaining , plan_date
from helpers.db_tools import *




import random
backup_settings = {
    'mode':'off',
    'interval':1000
}
show_users_sort = ''

owner_keyboard = InlineKeyboard()
owner_keyboard.row(
    InlineButton('🚻  نمایش کاربران','show-users')
)
owner_keyboard.row(
    InlineButton('🆓 کاربر تست','create-test')
)
owner_keyboard.row(
    InlineButton('➕ افزودن کاربر','add-user'),
    InlineButton('➖ حذف کاربر','del-user'),
)
owner_keyboard.row(
    InlineButton('🚻 دسته بندی کاربران','user-type'),
    InlineButton('🪪 مدیریت فروشندگان','manage-admins'),
)
owner_keyboard.row(
    InlineButton("🔄 بکاپ",'backup')
)



admin_keyboard = InlineKeyboard()
admin_keyboard.row(
    InlineButton('🚻  نمایش کاربران','show-users')
)
admin_keyboard.row(
    InlineButton('🆓 کاربر تست','create-test')
)
admin_keyboard.row(
    InlineButton('➕ افزودن کاربر','add-user'),
    InlineButton('➖ حذف کاربر','del-user'),
)
admin_keyboard.row(
    InlineButton('🚻 دسته بندی کاربران','user-type'),
)


back_up_kb = InlineKeyboard()
back_up_kb.row(
    InlineButton('تنظیمات بکاپ خودکار','action:auto-backup-setting'),
)
back_up_kb.row(
        InlineButton('دریافت بکاپ از کاربران','action:get-back-up'),
   
)
back_up_kb.row(
    
    InlineButton('➡️ بازگشت', 'back:main-menu'),
)


    

def  back_up_setting():
    back_up_setting = InlineKeyboard()

    if backup_settings['mode']=='off':
        print('its off')
        print(backup_settings)
        back_up_setting.row(
            InlineButton('✅ روشـــن','auto-backup-on'),
        )
    elif backup_settings['mode']=='on':
        print(backup_settings)
        back_up_setting.row(
                InlineButton("❌ خاموش",'auto-backup-off'),
        
    )
    back_up_setting.row(
        
        InlineButton("زمانبندی بکاپ", 'set-backup-time'),
    )
    back_up_setting.row(
            InlineButton('➡️ بازگشت', 'back:main-menu'),
    )
    return back_up_setting

def back_up_interval():
    back_up_interval=InlineKeyboard(row_width=3)
    intervals = {
        '🕔 هرساعت':'backupmode:3600',
        '🕔 هر 12 ساعت':'backupmode:43200',
        '🕔 هر روز':'backupmode:86400',
        '🕔 دو روز یکبار':'backupmode:172800',
        '🕔 سه روز یکبار':'backupmode:259200',
        '🕔 هفتگی':'backupmode:604800',
    }
    list_of_buttons = []
    for k,v in intervals.items():
        if int(v.split(':')[1])==backup_settings['interval']:
            list_of_buttons.append(
                InlineButton(k.replace('🕔','✅'),v)
            )
        else:
            list_of_buttons.append(
                InlineButton(k,v)
            )

    back_up_interval.add(
       *list_of_buttons
    )
    back_up_interval.row(
            InlineButton('➡️ بازگشت', 'action:auto-backup-setting'),
    )
    return back_up_interval

cancel_kb = InlineKeyboard()
cancel_kb.row(
   InlineButton('انصراف','action:cancel-adding')
)

traffic_kb = InlineKeyboard()
traffic_kb.row(
   InlineButton('♾ نامحدود','traffic:♾ نامحدود') 
)
traffic_kb.row(
   InlineButton('10 ᴳᴮ','traffic:10'),
   InlineButton('20 ᴳᴮ','traffic:20'),
   InlineButton('30 ᴳᴮ','traffic:30'),
   InlineButton('40 ᴳᴮ','traffic:40'), 
)
traffic_kb.row(
   InlineButton('50 ᴳᴮ','traffic:50'),
   InlineButton('60 ᴳᴮ','traffic:60'),
   InlineButton('70 ᴳᴮ','traffic:70'),
   InlineButton('80 ᴳᴮ','traffic:80'), 
)
traffic_kb.row(
   InlineButton('90 ᴳᴮ','traffic:90'),
   InlineButton('100 ᴳᴮ','traffic:100'),
   InlineButton('150 ᴳᴮ','traffic:150'),
   InlineButton('200 ᴳᴮ','traffic:200'), 
)

traffic_kb.row(
   InlineButton('انصراف','action:cancel-adding')
)


multiuser_kb = InlineKeyboard()
multiuser_kb.row(
    InlineButton('1','multiuser:1'),
    InlineButton('2','multiuser:2'),
    InlineButton('3','multiuser:3'),
    InlineButton('4','multiuser:4'),
    InlineButton('5','multiuser:5'),
)
multiuser_kb.row(
    InlineButton('6','multiuser:6'),
    InlineButton('7','multiuser:7'),
    InlineButton('8','multiuser:8'),
    InlineButton('9','multiuser:9'),
    InlineButton('10','multiuser:10'),
)
multiuser_kb.row(
   InlineButton('انصراف','action:cancel-adding')
)

exp_kb = InlineKeyboard()
exp_kb.row(
   InlineButton('یک ماهه','expdate:30'), 
)
exp_kb.row(
   InlineButton('دو ماهه','expdate:60'),
   InlineButton('سه ماهه','expdate:90'), 
   InlineButton('چهار ماهه','expdate:120'),  
)
exp_kb.row(
   InlineButton('انصراف','action:cancel-adding')
)

confirm_creation = InlineKeyboard()
confirm_creation.row(
    InlineButton('تایید','action:add-confirm'),
   InlineButton('انصراف','action:cancel-adding')
)

back_to_menu = InlineKeyboard()
back_to_menu.row(
    InlineButton('➡️ بازگشت', 'back:main-menu')

)


user_category = InlineKeyboard()
user_category.row(
    InlineButton(
        'کاربران آنلاین','online-users'
    ),
    InlineButton(
        'کاربران منقضی','expired-users'
    )
)
user_category.row(
    InlineButton(
        'کاربران غیرفعال','deactive-users'
    ),
    InlineButton(
        'کاربران رو به انقضا','on-expired-users'
    )
)
user_category.row(
    InlineButton('➡️ بازگشت', 'back:main-menu')

)

back_to_types = InlineKeyboard()
back_to_types.row(
    InlineButton('➡️ بازگشت', 'user-type')

)

back_to_online = InlineKeyboard()
back_to_online.row(
InlineButton('بازگشت به لیست کاربران انلاین','online-users')
)


manage_sellers_kb=InlineKeyboard()
manage_sellers_kb.row(
    InlineButton('اضافه کردن فروشنده',
                 'manage-sellers:add')
)
manage_sellers_kb.row(
    InlineButton('نمایش فروشندگان',
                 'manage-sellers:show')
)
manage_sellers_kb.row(
    InlineButton('حذف کردن فروشنده',
                 'manage-sellers:del')
)

manage_sellers_kb.row(
    InlineButton('➡️ بازگشت',
                 'back:main-menu')
)

def show_users_sort_kb():
    show_users_sort_kb = InlineKeyboard(row_width=3)
    list_of_buttons = []
    sorts = {
        'زمان ساخت':'sort:creation-time',
        'انقضا':'sort:traffic',
        ' پر مصرف':'sort:exprie-date'
    }
    print('++++++sort of showing users is : ')
    print(show_users_sort)
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
        InlineButton('➡️ بازگشت','show-users')
    )
    return show_users_sort_kb


