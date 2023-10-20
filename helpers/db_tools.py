import pymongo
import json
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
sys.path.append(str(os.getcwd().replace('\\','/'))+'/dbupdates')
from fetch import store_data
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs
botid = get_configs()['botid']
client = pymongo.MongoClient("mongodb+srv://admin:pvsender64523@pvsender.p4x3bno.mongodb.net/?retryWrites=true&w=majority")
bot_name = botid
db = client[bot_name]
sellers= db["sellers"]
users = db['users']




def show_sellers():
   admins_file= str(os.getcwd().replace('\\','/'))+'/dbupdates/'+'admins.json'
   with open(admins_file,'r') as f :
        data = json.load(f)
   return data     
        

def add_seller(user_id):
    existing_seller = sellers.find_one({'_id':user_id})
    if not existing_seller :
        sellers.insert_one({'_id':user_id})
        store_data()
        return "ادمین {} با موفقیت اضافه شد"
    
    else:
            return "ادمین {} از قبل به لیست ادمین ها اضافه شده است .".format(user_id)

    


def del_seller(user_id):
    bot = sellers.find_one({'_id':bot_name})
    existing_seller = sellers.find_one({'_id':user_id})
    if not existing_seller:
          return 'حذف با خطا روبرو شد . (علت : کاربر با این ایدی عددی در لیست ادمین ها قرار ندارد)'
    else:
          sellers.delete_one(existing_seller)
          store_data()
          return 'کاربر {} از لیست ادمین ها حذف شد .'.format(user_id)

          


