"""Module designated for all no jobs endpoints V1"""
from app.resources.decorators import token_required
from flask import Blueprint, jsonify, request
import app

views = Blueprint("views", __name__)

@views.route("/ping")
def main() -> str:
    """Ping endpoint, used to know if the app is up."""

    return "pong"

@views.route("/users", methods=["POST"])
def create_user():
    """Create user"""

    json_data = request.get_json(force = True)
    response = app.controller.create_user(json_data)
    return response

@views.route("/users/authenticate", methods=["POST"])
def authenticate():
    """Authenticate user"""

    json_data = request.get_json(force = True)
    response = app.controller.authenticate_user(json_data)
    return response

@views.route("/restricted_ping")
@token_required
def restricted_ping() -> str:
    """Ping endpoint, used to know if the app is up."""

    return "pong"
