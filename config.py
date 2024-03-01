import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "25015843"))
API_HASH = environ.get("API_HASH", "3f225798a2834c821dfeeeaf76ca7614")
BOT_TOKEN = environ.get("BOT_TOKEN", "6667359811:AAFqvqV9Y6GYhWNisEfsAz0Gds62v0FpgfU")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", ""))
DB_URI = environ.get("DB_URI", "mongodb+srv://olawale:olawale@cluster0.o7a2fdj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
