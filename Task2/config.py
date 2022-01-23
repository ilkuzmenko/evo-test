import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.environ['PG_USER']
POSTGRES_PASSWORD = os.environ['PG_PASS']
PG_HOST = os.environ['PG_HOST']
POSTGRES_DB = os.environ['PG_DB_NAME']
