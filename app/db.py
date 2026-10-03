import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    schema = os.getenv("DB_SCHEMA", "monster_quiz_battle")
    return psycopg.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "5432")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
        connect_timeout=3,
        options=f"-c search_path={schema}",
    )