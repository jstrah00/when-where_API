from flask import request, jsonify
from functools import wraps
import jwt
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError
from app.resources.exceptions import BadAuthorizationException, UnauthorizedAccessException
from app.resources.credentials import JWT_SECRET
from app.resources.logger import logger

def token_required(f):
   print('el dcorator de token_required')
   @wraps(f)
   def decorator(*args, **kwargs):
       print('aca si entraaa')
       token = None
       if "x-access-token" in request.headers:
           token = request.headers["x-access-token"]
       if not token:
           raise BadAuthorizationException("Authorization token is missing")
       try:
           jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
       except InvalidSignatureError:
           raise BadAuthorizationException("Invalid token")
       except ExpiredSignatureError:
           raise BadAuthorizationException("Expired token")
       return f(*args, **kwargs)
   return decorator

def basic_decorator(f):
    print('entra al basic_decorator')
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('y sigue por el wrapper')
        try:
            print('a')
            result = f(*args, **kwargs)
            print('result')
            return jsonify({"data":result})
        except Exception as e:
            print('exception')
            logger.exception("Exception raised.")
            if "get_status_code" in dir(e):
                print('siif')
                if e.get_status_code() == 500: return jsonify({"Desc": "There was an error"}), 500
                else: return jsonify({"Desc": str(e)}), e.get_status_code()
            else:
                print('elseee')
                return jsonify({"Desc": "There was an error"}), 500
    return wrapper

def required_roles(func):
   print("Estoy en el required roles decorator")
   print('Los func sonjj: ')
   print(func)
   @wraps(func)
   def inner(*args, **kwargs):
       try:
           jwt_data = jwt.decode(request.headers["x-access-token"], JWT_SECRET, algorithms=["HS256"])
           print('LA DATA DEL JWT ES ')
           print(jwt_data)
           if jwt_data["role"] != "admin":
               raise UnauthorizedAccessException("You are not authorized to access to this resource")
       except InvalidSignatureError:
           raise BadAuthorizationException("Invalid token")
       return func(*args, **kwargs)
   return inner

