import bcrypt
import jwt
import datetime
from app.resources.credentials import JWT_SECRET
from app.resources.exceptions import ResourceAlreadyExistsException, ResourceNotFoundException

class WWController:
    def __init__(self, database):
        self.database = database

    def authenticate_user(self, json_data: dict): 
        """Main function for user authentication"""
        user_data = self.database.get_user_data_by_email(json_data["email"])
        if not user_data: 
            raise ResourceNotFoundException("User not found")
        password = json_data["password"].encode("utf-8")
        if bcrypt.checkpw(password, user_data["hashed_password"]):
            token = jwt.encode({
                "email": user_data["email"],
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
                "role": user_data["role"],
                "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
                }, JWT_SECRET, "HS256")
            self.update_last_login(user_data["email"])
            return {"token" : token}
        return "Invalid username or password"

    def create_user(self, json_data: dict): 
        """Main fuction for create user endpoint"""
        if self.database.get_user_data_by_email(json_data["email"]):
            raise ResourceAlreadyExistsException("User already exists")
        password = json_data["password"].encode("utf-8")
        password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        last_login = datetime.datetime.now()
        self.database.create_user(
                json_data["email"], json_data["name"], json_data["last_name"], password_hash, last_login)
        return "User created successfully"

    def update_last_login(self, email: str):
        """Update user last login"""

        payload = {"last_login": datetime.datetime.now()}
        self.database.update_user_data(email, payload)

    def build_user_dict(self, user: dict):
            return {
                "email": user["email"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "role": user["role"],
                "last_login": user["last_login"]
                }

    def build_get_users_response(self, users: list) -> list:
        """Function for building the get_users endpoint response"""
        response = []
        for user in users:
            response.append(self.build_user_dict(user))
        return response

    def get_users(self):
        """Main function for get users endpoint"""
        users = list(self.database.get_users())
        return self.build_get_users_response(users)

    def get_user_data_by_email(self, email:str):
        """Main function for get user data by email endpoint"""
        response = self.database.get_user_data_by_email(email)
        return self.build_user_dict(response)

    def update_user(self, email:str, json_data: dict): 
        """Main function for update user data endpoint"""
        self.database.update_user_data(email, json_data)
        return "User updated successfully"

