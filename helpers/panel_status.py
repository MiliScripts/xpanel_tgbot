import json
import requests
from pykeyboard import InlineKeyboard, InlineButton
from helpers.convert_persian_data import convert_to_persian_date
from helpers.convert_traffic import convert_mb_to_gb
from helpers.remaining_days import remaining , plan_date
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
from handle_configs import get_configs
import shutil


# ┈┅┅━━━⊷⊰🤍 panel host url and api token⊱⊶━━━┅┅┈
host_url = get_configs()['host_url']
api_token = get_configs()['api_token']
botid = get_configs()['botid']





def online_users_info():
   host =  host_url+ api_token
   link = host+'/online'
   response = requests.get(link)
   data = json.loads(response.text)
   # print(data)
   users = {}
   for user in data :
         if user['username'] not in users : 
           users[user['username']] = {'username':user['username'],'ips':[user['ip']]}
         elif user['username'] in users :
            users[user['username']]['ips'].append(user['ip'])  
   number_of_users = len(users)
   starting_text = '🚻  لیست افراد آنلاین ( {} نفر ) : \n➖➖➖➖➖➖➖\n'.format(number_of_users)

   text = ''
   for user,d in users.items() : 
      text+='''‏👤🌐  <code>{}</code> 
🌀برای مدیریت کانکشن ها کلیک کنید  ‏◄ {}
┘  آیپی های متصل  ({}) : {}'''.format(user,'[{}](https://t.me/{}?start=online-{})'.format(user, botid,user),len(d['ips']),''.join(['\n‏◃ <code>'+ip+'</code>' for ip in d['ips']]))
      text+='\n\n'
      

   online_text = starting_text+'\n\n'+text+'\n➖➖➖➖➖➖➖'

   return online_text   







#server status info
def get_memory_usage():
    mem = shutil.disk_usage('.')
    memtotal = round(mem.total / 1000000, 2)
    memused = round(mem.used / 1000000, 2)
    memfree = round(mem.free / 1000000, 2)
    memtotal = float(str(memtotal).replace(" GB", "").replace(" MB", ""))
    memused = float(str(memused).replace(" GB", "").replace(" MB", ""))
    memfree = float(str(memfree).replace(" GB", "").replace(" MB", ""))
    usedperc = 100 * memused / memtotal
    return str(round(usedperc))+'%'

def get_cpu_usage():
   #  exec_loads = os.getloadavg()
   #  exec_cores = subprocess.run("grep -P '^processor' /proc/cpuinfo | wc -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  
   #  exec_cores = exec_cores.stdout.strip()
   #  cpu = round(exec_loads[1] / (int(exec_cores) + 1) * 100, 0)
   #  return str(cpu)+'%'
   return 'ee'

def get_disk_usage():
    disk_free = round(shutil.disk_usage('.').free / 1000000000)
    disk_total = round(shutil.disk_usage('.').total / 1000000000)
    disk_used = round(disk_total - disk_free)
    disk_usage = round(disk_used / disk_total * 100)
    return str(disk_usage)+'%'

def server_info():
   disk_usage = get_disk_usage()
   cpu_usage = get_cpu_usage()
   memory_usage = get_memory_usage()
   return [disk_usage,cpu_usage,memory_usage]
   

#server ssh traffic usage
def traffic_usage():
   host =  host_url
   link = host+f"{ api_token}/listuser"
   response = requests.get(link)
   data = json.loads(response.text)
   upload = 0
   download = 0
   for user in data :
      traffics = user['traffics']
      for i in traffics:
         download+=int(i['download'])
         upload+=int(i['upload'])
      
   total = upload+download
   data = {'download':round(download/ 1024),'upload' : round(upload/ 1024),'total': round(total/ 1024)}
   return [str(round(total/ 1024))+' ɢʙ',str(round(upload/ 1024))+' ɢʙ',str(round(download/ 1024))+' ɢʙ']



def user_connections(username):
   host =  host_url+ api_token
   link = host+'/online'
   response = requests.get(link)
   data = json.loads(response.text)
   users = {}
   for user in data :
         if user['username'] not in users : 
           users[user['username']] = {'username':user['username'],'ips':[[user['ip'],user['pid']]]}
         elif user['username'] in users :
            users[user['username']]['ips'].append([user['ip'],user['pid']])  
   
   text_info = ''
   con_kb = InlineKeyboard()
   if username in users:
      
      con_kb = InlineKeyboard()
      ips = users[username]['ips']
      for connection in  ips :
         con_kb.row(
            InlineButton('قطع اتصال {}'.format(connection[0]),'kill:id-{}'.format(connection[1]))
         )  
      text_info = '''‏👤🌐  <code>{}</code> 
┘  آیپی های متصل  ({}) 

برای قطع کردن هر اتصال تنها روی کانکشن مورد نظر کلیک کنید . 
➖➖➖➖➖➖➖
'''.format(username,str(len(ips)))
      con_kb.row(
         InlineButton('قطع اتصال همه کانکشن های کاربر','kill:user-{}'.format(username))
      )
      con_kb.row(
         InlineButton('بازگشت به لیست کاربران آنلاین','online-users')
      )
      return [text_info,con_kb]
   else:
      return
