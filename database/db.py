import psycopg2
from config_db import db_params

conn = psycopg2.connect(database=db_params["postgres"], user=db_params["user"],
                        password=db_params["password"], host=db_params["host"], port=db_params["port"])

cur = conn.cursor()