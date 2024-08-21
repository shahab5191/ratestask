import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SERVER_PORT = int(os.environ.get("PORT") or 5000)
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_PREFIX = "/v1"
