import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.environ["POSTGRES_DB"] if os.environ.get("POSTGRES_DB") else "postgres"
DB_USER = os.environ["POSTGRES_USER"] if os.environ.get("POSTGRES_USER") else "postgres"
DB_PASS = os.environ["POSTGRES_PASSWORD"] if os.environ.get("POSTGRES_PASSWORD") else "postgres"
DB_HOST = "db"
DB_PORT = os.environ["DB_PORT"] if os.environ.get("DB_PORT") else "5432"
