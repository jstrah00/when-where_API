import pymongo
from app.resources.credentials import DB_CONNECTION_URL, DB_NAME

class Database:
    def __init__(self): 
        myclient = pymongo.MongoClient(DB_CONNECTION_URL)
        self.db = myclient[DB_NAME]

    def create_user(
            self, email: str, first_name: str, last_name: str, hashed_password: str, roles, last_login
            ) -> None:
        self.db.users.insert_one({
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "hashed_password": hashed_password,
            "roles": roles,
            "last_login": last_login
            })

    def get_user_data_by_email(self, email: str):
        return self.db.users.find_one({"email": email})

    def get_users(self):
        return self.db.users.find()
    
    def update_user_data(self, email:str, payload:dict):
        return self.db.users.update_one(
                {"email": email},
                {"$set": payload})

    def create_role(self, name: str, description: str) -> None:
        self.db.roles.insert_one({
            "name": name,
            "description": description
            })

    def get_single_role(self, name: str):
        return self.db.roles.find_one({"name": name})

    def get_roles(self):
        return self.db.roles.find()
