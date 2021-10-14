"""Module designated for all no jobs endpoints V1"""
from app.resources.decorators import token_required, basic_decorator
from flask import Blueprint, request
import app
from app.resources.utilities import validate_json_schema
from app.resources.schemas.users_schemas import create_user_schema, authenticate_user_schema

views = Blueprint("views", __name__)

@views.route("/ping")
@basic_decorator
def ping():
    """Ping endpoint, used to know if the app is up."""

    return "pong"

@views.route("/users", methods=["POST"])
@basic_decorator
def create_user():
    """Create user"""

    json_data = request.get_json(force = True)
    validate_json_schema(json_data, create_user_schema)
    return app.controller.create_user(json_data)

@views.route("/users/authenticate", methods=["POST"])
@basic_decorator
def authenticate():
    """Authenticate user"""

    json_data = request.get_json(force = True)
    validate_json_schema(json_data, authenticate_user_schema)
    return app.controller.authenticate_user(json_data)

@views.route("/restricted_ping")
@basic_decorator
@token_required
def restricted_ping():
    """Ping endpoint, used to know if the app is up."""

    return "pong"

