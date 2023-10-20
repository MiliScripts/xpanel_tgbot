##########Import##########
import random
import asyncio
import os
import yaml
from pyrogram import Client,idle,filters,enums,errors 
from asyncio import get_event_loop
from time import time
from config import config
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ReplyKeyboardRemove , ForceReply
from pyrogram.errors import BadRequest
import requests
import pyromod
from helpers.filters import *
from helpers.db_tools import * 
from plugins.inline_kb_handler import backup_settings
from helpers.backup import *
from pyromod.helpers import ikb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handle_configs import * 
###########CMDs###########




Api = Client(
            name="xpanel-bot",
            api_id=get_configs()['Api_id'],
            api_hash=get_configs()['Api_hash'],
            app_version="1.0.0",
            device_model="Xpanel-v3.8",
            bot_token=get_configs()['Bot_token'],
            plugins=dict(root="plugins"),
            workers=20
        )



async def job():
    if backup_settings['mode']=='on':
       await backup_func(chat_id=get_configs()['owner'],app=Api)
    else:
       return   



scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=backup_settings['interval'])





async def main():
   await Api.start()
   print('Bot is Running !')
   scheduler.start()
   await idle()
   await Api.stop()


Loop = get_event_loop()
Loop.run_until_complete(main())