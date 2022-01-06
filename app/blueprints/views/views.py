"""Module designated for all no jobs endpoints V1"""
from app.resources.decorators import token_required, basic_decorator, roles_required
from flask import Blueprint, request
import app
from app.resources.utilities import validate_json_schema
from app.resources.schemas.users_schemas import create_user_schema, authenticate_user_schema, update_user_schema, update_user_status_schema
from app.resources.schemas.roles_schemas import add_remove_user_roles_schema
from app.resources.schemas.email_verification_schemas import verify_email_schema

views = Blueprint("views", __name__)

@views.route("/ping")
@basic_decorator
def ping():
    """Ping endpoint, used to know if the app is up."""
    return "pong"

@views.route("/restricted_ping")
@basic_decorator
@token_required
def restricted_ping():
    """Ping endpoint, used to know if the app is up."""
    return "pong"

@views.route("/users/authenticate", methods=["POST"])
@basic_decorator
def authenticate():
    """Authenticate user"""
    json_data = request.get_json(force = True)
    validate_json_schema(json_data, authenticate_user_schema)
    return app.controller.authenticate_user(json_data)

@views.route("/users", methods=["POST"])
@basic_decorator
def create_user():
    """Create user"""
    json_data = request.get_json(force = True)
    validate_json_schema(json_data, create_user_schema)
    return app.controller.create_user(json_data)

@views.route("/users", methods=["GET"])
@basic_decorator
@token_required
@roles_required(["admin"])
def get_users():
    """Get all users"""
    return app.controller.get_users()

@views.route("/users/<string:email>/email", methods=["GET"])
@basic_decorator
@token_required
@roles_required(["admin", "self"])
def get_user_by_email(email):
    """Get user data by email"""
    return app.controller.get_user_data_by_email(email)

@views.route("/users/<string:email>/email", methods=["PUT"])
@basic_decorator
@token_required
@roles_required(["admin","self"])
def update_user(email):
    """Update user data by email"""
    json_data = request.get_json(force = True)
    validate_json_schema(json_data, update_user_schema)
    return app.controller.update_user(email, json_data)

@views.route("/users/<string:email>/status", methods=["PUT"])
@basic_decorator
@token_required
@roles_required(["admin"])
def update_user_status(email):
    """Update user status by email"""
    json_data = request.get_json(force = True)
    validate_json_schema(json_data, update_user_status_schema)
    return app.controller.update_user_status(email, json_data)

@views.route("/users/<string:email>/roles", methods=["PUT"])
@basic_decorator
@token_required
@roles_required(["admin"])
def add_roles_to_user(email):
    """Add roles to user by email"""
    json_data = request.get_json(force = True)
    validate_json_schema(json_data, add_remove_user_roles_schema)
    return app.controller.update_user_roles(email, "add", json_data)

@views.route("/users/<string:email>/roles", methods=["PATCH"])
@basic_decorator
@token_required
@roles_required(["admin"])
def remove_roles_to_user(email):
    """Remove roles to user by email"""
    json_data = request.get_json(force = True)
    validate_json_schema(json_data, add_remove_user_roles_schema)
    return app.controller.update_user_roles(email, "remove", json_data)

@views.route("/users/<string:email>/verification_email", methods=["POST"])
@basic_decorator
@token_required
@roles_required(["admin","self"])
def send_verification_email(email):
    """Send verification email"""
    return app.controller.generate_email_verification_code(email)


@views.route("/users/verify", methods=["POST"])
@basic_decorator
@token_required
@roles_required(["admin","self"])
def send_verification_email():
    """Verify email"""
    json_data = request.get_json(force = True)
    validate_json_schema(json_data, verify_email_schema)
    return app.controller.verify_email(json_data)
