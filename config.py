import os
from dotenv import load_dotenv


load_dotenv()


HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
DATABASE = os.getenv('DATABASE')
