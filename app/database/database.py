import os
import pymongo

connection_url = "mongodb://localhost:27017/" #Develop
#connection_url = os.getenv("DB_CONN") #Prod

class Database:
    def __init__(self): 
        myclient = pymongo.MongoClient(connection_url)
        self.db = myclient['whenwhere']

    def create_user(self, email: str, first_name: str, last_name: str, hashed_password: str) -> None:
        self.db.users.insert_one({
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "hashed_password": hashed_password
            })

    def get_user_data_by_email(self, email: str):
        return self.db.users.find_one({"email": email})
