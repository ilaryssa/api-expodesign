import os 
from dotenv import load_dotenv
import psycopg2 #liga o python ao postgres

#frufru do .env
load_dotenv()
db_password = os.environ.get('DB_PASSWORD')

def get_connection():
    return psycopg2.connect(
        dbname="expodesign",
        user="postgres",
        password= db_password, #crie um novo arquivo .env e adicione lá DB_PASSWORD = sua_senha_linda_do_postgres
        host="localhost",
    )