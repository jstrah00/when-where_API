import bcrypt
import jwt
import datetime
from app.resources.credentials import JWT_SECRET
from app.resources.exceptions import ResourceAlreadyExistsException, ResourceNotFoundException, UnauthorizedAccessException

class WWController:
    def __init__(self, database):
        self.database = database

    def authenticate_user(self, json_data: dict): 
        """Main function for user authentication"""
        user_data = self.database.get_user_data_by_email(json_data["email"])
        if not user_data: 
            raise ResourceNotFoundException("User not found")
        password = json_data["password"].encode("utf-8")
        if user_data["status"] == "active" and bcrypt.checkpw(password, user_data["hashed_password"]):
            token = jwt.encode({
                "email": user_data["email"],
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
                "roles": user_data["roles"],
                "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
                }, JWT_SECRET, "HS256")
            self.update_last_login(user_data["email"])
            return {"token" : token}
        raise UnauthorizedAccessException("Invalid username or password")

    def create_user(self, json_data: dict): 
        """Main fuction for create user endpoint"""
        if self.database.get_user_data_by_email(json_data["email"]):
            raise ResourceAlreadyExistsException("User already exists")
        password = json_data["password"].encode("utf-8")
        password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        self.database.create_user(
                json_data["email"], json_data["name"], json_data["last_name"], password_hash)
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
                "roles": user["roles"],
                "last_login": user["last_login"],
                "status": user["status"]
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
        allowed_keys = ["first_name", "last_name"] #Allowed propieties to update with this method
        payload = dict((key,value) for key,value in json_data.items() if key in allowed_keys)
        self.database.update_user_data(email, payload)
        return "User updated successfully"

    def update_user_status(self, email:str, json_data: dict):
        """Main function to update user status"""
        self.database.update_user_data(email, json_data)
        operation = "disabled" if json_data["status"] == "inactive" else "activated"
        return f"User {operation} successfully"

    def update_user_roles(self, email:str, operation: str, json_data: dict): 
        """Main function to update user roles"""
        user_data = self.get_user_data_by_email(email)
        print('user data')
        print(user_data)
        print('json')
        print(json_data)
        if not user_data: 
            raise ResourceNotFoundException("User not found")
        if operation == "remove":
            if not json_data["role"] in user_data["roles"]:
                raise ResourceNotFoundException("Role not found in user")
            user_data["roles"].remove(json_data["role"])
        else:
            if json_data["role"] in user_data["roles"]:
                raise ResourceAlreadyExistsException("Role was already assigned")
            user_data["roles"].append(json_data["role"])
        self.database.update_user_data(email, {"roles": user_data["roles"]})
        word = "removed" if operation == "remove" else "assigned"
        return f"Role {word} successfully"

