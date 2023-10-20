#libs 
import os
from handle_configs import get_configs
from time_tools import gn , convert_to_persian_date


# ┈┅┅━━━⊷⊰🤍 panel main username and password for getting backup⊱⊶━━━┅┅┈
username = get_configs()["db_username"]
password = get_configs()["db_password"]


async def backup_func(chat_id,app):
   file_path = "/root/meow.sql"
   if os.path.exists(file_path):
      os.remove(file_path)
   os.system(f"mysqldump -u {username} --password={password} XPanel_plus > {file_path}")
   await app.send_document(chat_id=chat_id,document='backups/'+file_path,file_name=convert_to_persian_date(gn())+'.sql')
   try:
      os.remove(file_path)
   except:
      pass   
