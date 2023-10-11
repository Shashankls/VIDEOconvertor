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

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
