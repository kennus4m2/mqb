import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME"),
)
with conn.cursor() as cur:
    cur.execute("SELECT 1")
    print(cur.fetchone())  # (1,)
conn.close()