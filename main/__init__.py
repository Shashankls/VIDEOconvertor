from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID","16621664") 
API_HASH = config("API_HASH", "8b283f2943729318995738b5963f0bcc") 
BOT_TOKEN = config("BOT_TOKEN","6586439577:AAERjnKohzK6QBOs01WbVcSUjiY0sUwvsVk") 
BOT_UN = config("BOT_UN","VideoWatermarkme_Bot")
AUTH_USERS = config("AUTH_USERS","6561715152",cast=int)
LOG_CHANNEL = config("LOG_CHANNEL","mmmmcxz")
LOG_ID = config("LOG_ID","-1001976098815")
FORCESUB = config("FORCESUB","-1001976098815")
FORCESUB_UN = config("FORCESUB_UN","mmmmcxz")
ACCESS_CHANNEL = config("ACCESS_CHANNEL","-1001976098815")
MONGODB_URI = config("MONGODB_URI","mongodb+srv://Shashanklsgg:shashank.ls1324@cluster0.9pv92ou.mongodb.net/?retryWrites=true&w=majority")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
