import os
from app.resources.logger import logger

logger.info(f"Running on {os.getenv('ENV')} enviroment.")

if os.getenv("ENV") == "production":
    DB_CONNECTION_URL = os.getenv("DB_CONN")
    DB_NAME = os.getenv("DB_NAME")
    JWT_SECRET = os.getenv("JWT_SECRET")
    VERIF_EMAIL_TOKEN_SECRET = os.getenv("VERIF_EMAIL_TOKEN_SECRET")
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    APP_NAME = os.getenv("APP_NAME")
    APP_URL = os.getenv("APP_URL")
    SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")
else:
    DB_CONNECTION_URL = os.getenv("DEV_DB_CONN")
    DB_NAME = os.getenv("DEV_DB_NAME")
    JWT_SECRET = os.getenv("DEV_JWT_SECRET")
    VERIF_EMAIL_TOKEN_SECRET = os.getenv("DEV_VERIF_EMAIL_TOKEN_SECRET")
    EMAIL_ADDRESS = os.getenv("DEV_EMAIL_ADDRESS")
    EMAIL_PORT = os.getenv("DEV_EMAIL_PORT")
    EMAIL_PASSWORD = os.getenv("DEV_EMAIL_PASSWORD")
    APP_NAME = os.getenv("DEV_APP_NAME")
    APP_URL = os.getenv("DEV_APP_URL")
    SUPPORT_EMAIL = os.getenv("DEV_SUPPORT_EMAIL")
