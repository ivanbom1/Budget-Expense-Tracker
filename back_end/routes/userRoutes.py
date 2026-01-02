from flask import Blueprint
from controllers.userController import UserController

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_routes.route("/username/<username>", methods=["GET"])
def get_user_by_username(username):
    return UserController.get_user_by_username(username)

@user_routes.route("/", methods=["POST"])
def create_user():
    return UserController.create_user()

@user_routes.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return UserController.update_user(user_id)

@user_routes.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return UserController.delete_user(user_id)