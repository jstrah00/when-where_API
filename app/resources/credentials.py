import os

if os.getenv("ENV") == "production":
    DB_CONNECTION_URL = os.getenv("DB_CONN")
    JWT_SECRET = os.getenv("JWT_SECRET")
    
elif os.getenv("ENV") == "development":
    DB_CONNECTION_URL = os.getenv("DEV_DB_CONN")
    JWT_SECRET = os.getenv("DEV_JWT_SECRET")
