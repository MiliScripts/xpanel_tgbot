import pymongo
import sys
import os 
import json
import requests
#route to handle configs
sys.path.append(str(os.getcwd()))

# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈

from handle_configs import get_configs
botid = get_configs()['botid']
mongo_string = get_configs()['mongo']
client = pymongo.MongoClient(mongo_string)
bot_name = botid
db = client[bot_name]
sellers= db["sellers"]
users = db['users']

host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']




def show_sellers():
   users = [x['_id'] for x in sellers.find({})]
   return users


def store_data():
   admins = show_sellers()

   json_file=str(os.getcwd().replace('\\','/'))+'/dbupdates/'+'admins.json'
   with open(json_file,'w') as file : 
      json.dump(admins,file)
      print('data updated in json file . ')
      

def store_users():
   pass


def store_users_json():      
     
    host = host_url
    link = host+f"{api_token}/listuser"
    print('link : ',link)
    response = requests.get(link)
    data = json.loads(response.text)
    json_file = str(os.getcwd().replace('\\','/'))+'/dbupdates/'+'users.json'
    with open(json_file,'w') as file :
       json.dump(data, file)
       print('users saved in users.json file . ')

    return



def user_data_json(username):
   
    users_file= str(os.getcwd().replace('\\','/'))+'/dbupdates/'+'users.json'
    with open(users_file,'r') as f :
        users_list = json.load(f)   
    for user in users_list:
       if user['username']==username:
          print('showing user {} details '.format(username))
          print(user)
          return user
    
    return ' user {} not found '.format(
       username
    )

