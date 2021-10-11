from flask import jsonify
import bcrypt
import jwt
import datetime

JWT_SECRET = "mysecret1234"

class WWController():
    def __init__(self, database):
        self.database = database

    def create_user(self, json_data: dict): 
        """Main fuction for create user endpoint"""
        
        password_hash = bcrypt.hashpw(json_data["password"].encode('utf-8'), bcrypt.gensalt())
        self.database.create_user(json_data["email"], json_data["name"], json_data["last_name"], password_hash)
        return "User created successfully"

    def authenticate_user(self, json_data: dict): 
        user_data = self.database.get_user_data_by_email(json_data["email"])
        if bcrypt.checkpw(json_data["password"].encode('utf-8'), user_data["hashed_password"]):
            token = jwt.encode({"email": user_data["email"], "first_name": user_data["first_name"], "last_name": user_data["last_name"], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, JWT_SECRET, "HS256")
 
            return jsonify({'token' : token})
        return "Invalid username or password"
