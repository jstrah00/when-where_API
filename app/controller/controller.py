from flask import jsonify
import bcrypt
import jwt
import datetime
from app.resources.credentials import JWT_SECRET
from app.resources.exceptions import ResourceAlreadyExistsException, ResourceNotFoundException

class WWController:
    def __init__(self, database):
        self.database = database

    def create_user(self, json_data: dict): 
        """Main fuction for create user endpoint"""

        if self.database.get_user_data_by_email(json_data["email"]):
            raise ResourceAlreadyExistsException("User already exists")
        password = json_data["password"].encode("utf-8")
        password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        self.database.create_user(json_data["email"], json_data["name"], json_data["last_name"], password_hash)
        return "User created successfully"

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
                "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
                }, JWT_SECRET, "HS256")
            return {"token" : token}
        return "Invalid username or password"
