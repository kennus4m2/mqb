import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Open a MySQL connection using the values in .env."""
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        connect_timeout=3,
    )
