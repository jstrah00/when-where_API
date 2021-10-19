import os
from app.resources.logger import logger

logger.info(f"Running on {os.getenv('ENV')} enviroment.")

if os.getenv("ENV") == "production":
    DB_CONNECTION_URL = os.getenv("DB_CONN")
    DB_NAME = os.getenv("DB_NAME")
    JWT_SECRET = os.getenv("JWT_SECRET")
    
else:
    DB_CONNECTION_URL = os.getenv("DEV_DB_CONN")
    DB_NAME = os.getenv("DEV_DB_NAME")
    JWT_SECRET = os.getenv("DEV_JWT_SECRET")

