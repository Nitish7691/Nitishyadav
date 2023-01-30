# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23388932"))
API_HASH = os.environ.get("API_HASH", "fb0ca41bae7937090bc6aba2f6f85a29")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5652432118:AAEAjrQVwp-o-ZHhMcGtkuSpdmhoXkZX2Dc")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5309651681")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "earnspace7691")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://earnspace7691:8hZTEqKu5hGh!R#@cluster0.8k4dii4.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5309651681")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5309651681)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1695261980")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "earnspaceofficial") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
