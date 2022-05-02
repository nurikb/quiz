import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.environ["DB_NAME"] if os.environ.get("DB_NAME") else "postgres"
DB_USER = os.environ["DB_USER"] if os.environ.get("DB_USER") else "postgres"
DB_PASS = os.environ["DB_PASS"] if os.environ.get("DB_PASS") else "postgres"
DB_HOST = os.environ["DB_HOST"] if os.environ.get("DB_HOST") else "db"
DB_PORT = os.environ["DB_PORT"] if os.environ.get("DB_PORT") else "5432"
