import os
from dotenv import load_dotenv

print(load_dotenv())          # True = a .env file was found
print(os.getenv("DB_PORT"))   # should print 5432