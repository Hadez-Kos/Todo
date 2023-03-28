import os
from dotenv import load_dotenv

load_dotenv()

db_port = os.getenv('db_port')
db_host = os.getenv('db_host')
db_database = os.getenv('db_database')
db_user = os.getenv('db_user')
db_password = os.getenv('db_password')
secret_key = os.getenv('secret_key')
