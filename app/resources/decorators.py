from flask import request, jsonify
from functools import wraps
import jwt
from jwt.exceptions import InvalidSignatureError
from app.resources.exceptions import BadAuthorizationException, UnauthorizedAccessException
from app.resources.credentials import JWT_SECRET
from app.resources.logs import logger

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if "x-access-token" in request.headers:
           token = request.headers["x-access-token"]
       if not token:
           raise BadAuthorizationException("Authorization token is missing")
       try:
           jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
       except InvalidSignatureError:
           raise BadAuthorizationException("Invalid token")
       return f(*args, **kwargs)
   return decorator

def basic_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
            return jsonify({"data":result})
        except Exception as e:
            logger.exception("Exception raised.")
            if "get_status_code" in dir(e):
                if e.get_status_code() == 500: return jsonify({"Desc": "There was an error"}), 500
                else: return jsonify({"Desc": str(e)}), e.get_status_code()
            else:
                return jsonify({"Desc": "There was an error"}), 500
    return wrapper

def admin_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       try:
           jwt_data = jwt.decode(request.headers["x-access-token"], JWT_SECRET, algorithms=["HS256"])
           if jwt_data["role"] != "admin":
               raise UnauthorizedAccessException("You are not authorized to access to this resource")
       except InvalidSignatureError:
           raise BadAuthorizationException("Invalid token")
       return f(*args, **kwargs)
   return decorator

