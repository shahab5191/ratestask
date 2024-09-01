import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    ENV = os.environ.get("ENV", "development")
    SERVER_PORT = int(os.environ.get("PORT") or 5000)
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_PREFIX = "/v1"
    RETRY_DELAY = 2
    RETRY_MAX = 5
    DATABASE_CONFIG = {
        'dbname': os.environ.get("DB_NAME") or "postgres",
        'user': os.environ.get("DB_USER"),
        'password': os.environ.get("DB_PASSWORD"),
        'host': os.environ.get("DB_HOST") or "localhost",
        'port': os.environ.get("DB_PORT") or '5432'
    }
