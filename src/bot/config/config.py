import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DOCTOR_SECRET_KEY = "22042doc"
RW_SECRET_KEY = "22042rw"

BOT_TOKEN = os.getenv("BOT_TOKEN")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
DATABASE = os.getenv("DATABASE")
DBHOST = os.getenv("DBHOST")

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"

API_VERSION = os.getenv("API_VERSION")
API_NAME = os.getenv("API_NAME")
SCOPES = [os.getenv("SCOPE")]

# if __name__ == '__main__':
# print(NASTAVNIK_SECRET_KEY)
