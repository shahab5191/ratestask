import os


class Config:
    SQLALCHEMY_DATABASE_URI = "test" if os.getenv("ENV_STAGE") == "test" else os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
