from flask import request, jsonify
import jwt
from app.controller.controller import JWT_SECRET
from functools import wraps

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'x-access-token' in request.headers:
           token = request.headers['x-access-token']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
       except:
           return jsonify({'message': 'token is invalid'})
 
       return f(*args, **kwargs)
   return decorator
