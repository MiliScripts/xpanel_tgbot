import requests
from helpers.remaining_days import remaining
import json
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
# ┈┅┅━━━⊷⊰🤍 panel credentials ⊱⊶━━━┅┅┈
from handle_configs import get_configs
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']
domain = get_configs()['domain']
port = get_configs()['port']
roo_b_etmam  = get_configs()['roo_b_etmam']




def users_status(status):
   link = host_url+f"{api_token}/listuser"
   response = requests.get(link)
   data = json.loads(response.text)

   

   active = []
   deactive = []
   expired = []
   c = 0
   if status=='all':
      pass
   elif status=='active':

     for user in data :
        if user['status'] =='active':
           active.append('/user_'+user['username'])
     return active      

   elif status=='deactive':
      for user in data :
        if user['status'] =='deactive':
           deactive.append('/user_'+user['username'])
      return deactive

   elif status=='expired' :
      for user in data :
        if user['status'] =='expired':
           expired.append('/user_'+user['username'])
      return expired
   
def etmam():
   link = host_url+f"{api_token}/listuser"
   
   nazdik = []
   response = requests.get(link)

   data = json.loads(response.text)
   text = 'کاربرانی که انقضای آنها نزدیک است : \n\n'
   for user  in data :
         finishdate = user['end_date']
         if finishdate=='' or finishdate=="NULL":
            pass
         else:
             try: 
               remaining_dayes = remaining(finishdate)
               if int(remaining_dayes)<=roo_b_etmam and not int(remaining_dayes)<=0:
                  nazdik.append('''ℹ️  نام کاربری کانفیگ :  {}
🗓 روزهای مانده به انقضا : {} روز'''.format('[{}](https://t.me/{}?start=profile-{})'.format(user['username'],botid,user['username']),remaining_dayes))

             except Exception as e :
                continue     
             
   if len(nazdik)==0:
               
               return 'کاربر رو به انقضایی یافت نشد'
   else:
      return text+"\n\n".join(nazdik)


def deactives():
   link = host_url+f"{api_token}/listuser"
   response = requests.get(link)
   data = json.loads(response.text)
   text = '''لیست کاربران غیرفعال  '''+'\n'
   deactives = []
   c = 0
   for user in data :
     if user['status'] =='deactive':
        c+=1
        deactives.append('''({}) {}'''.format(c,'[{}](https://t.me/{}?start=profile-{})'.format(user['username'],botid,user['username'])))
   if len(deactives)==0:
               
               return 'کاربر غیرفعالی یافت نشد'
   else:
      return text+"\n\n".join(deactives)     
   

def expired():
   link = host_url+f"{api_token}/listuser"
   response = requests.get(link)
   data = json.loads(response.text)
   text = '''لیست کاربران منقضی'''+'\n'
   expired_users = []
   c=0
   for user in data :
     if user['status'] =='expired':
        c+=1
        expired_users.append('''({}) {}'''.format(c,'[{}](https://t.me/{}?start=profile-{})'.format(user['username'],botid,user['username'])))
   if len(expired_users)==0:
               
               return 'کاربر منقضی یافت نشد'
   else:
      return text+"\n\n".join(expired_users) 

    
        

        
      


