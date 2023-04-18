import os

from dotenv import load_dotenv

load_dotenv()

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
CHOSEN_DB = os.getenv("CHOSEN_DB")
