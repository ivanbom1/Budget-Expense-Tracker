import os
from dotenv import load_dotenv

load_dotenv()

class Config:


    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'expense_tracker')
    DB_USER = os.getenv('DB_USER', 'postgres')     #user may vary for each dev who want to host his local db
    DB_PASSWORD = os.getenv('DB_PASSWORD', '1234') #users pwd may be different for everyone too
    DB_PORT = int(os.getenv('DB_PORT', 5432))


    DEBUG = True
    JSON_SORT_KEYS = False