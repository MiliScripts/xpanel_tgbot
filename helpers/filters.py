from pyrogram import filters , Client
# ┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
from handle_configs import get_configs
owner_id = get_configs()['owner']




from helpers.db_tools import show_sellers
#admin filter from mongodb
async def AdminId(_, __, update):
  print('checking admins')
  print(show_sellers())
  print(update.from_user.id)
  if str(update.from_user.id) in show_sellers():
    return True
  else:
       print(show_sellers())
       print(update.from_user.id)
       return False

ADMIN_ID = filters.create(AdminId)
         

#ownre filter from mongodb
async def owner(_, __, update):
  print('checking onwer auth')
  if update.from_user.id == owner_id:
    print('its admin')
    return True
  else:
    return False

OWNER_ID = filters.create(owner)




async def user(_, __, update):
  print(str(update.from_user.id))
  if update.from_user.id != owner_id and str(update.from_user.id) not in show_sellers():
    print('its user')
    return True
  else:
    print('not user')
    return False
USER_ID = filters.create(user)

