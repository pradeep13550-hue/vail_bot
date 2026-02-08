import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_FILE = "veil.db"

MIN_PLAYERS = 5
MAX_PLAYERS = 20

REVEAL_ROLE_ON_DEATH = True
