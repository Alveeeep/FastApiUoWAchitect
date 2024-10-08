from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DB_HOST_TEST = os.getenv('DB_HOST_TEST')
DB_USER_TEST = os.getenv('DB_USER_TEST')
DB_PASS_TEST = os.getenv('DB_PASSWORD_TEST')
DB_PORT_TEST = os.getenv('DB_PORT_TEST')
DB_NAME_TEST = os.getenv('DB_NAME_TEST')