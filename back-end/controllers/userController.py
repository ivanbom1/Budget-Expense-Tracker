from flask import request, jsonify
from ..services.userService import UserService

class UserController:

    @staticmethod
    def get_all_users():
        try:
            users = UserService.get_all_by_users()
            if users:
                return jsonify({"status": "success", "users": users}), 200
            return jsonify({"status": "error", "message": "No users found"}), 404
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @staticmethod
    def get_user(user_id):
        try:
            user = UserService.get_by_user_id(user_id)
            if user:
                return jsonify({"status": "success", "user": user}), 200
            return jsonify({"status": "error", "message": "User not found"}), 404
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @staticmethod
    def create_user():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"status": "error", "message": "Request body required"}), 400

            if not all(k in data for k in ("username", "email", "password")):
                 return jsonify({"status": "error", "message": "Missing required fields (username, email, password)"}), 400

            user = UserService.createUser(data)
            
            if user:
                return jsonify({"status": "success", "user": user}), 201
            return jsonify({"status": "error", "message": "Failed to create user. Email or Username might already exist."}), 400
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @staticmethod
    def update_user(user_id):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"status": "error", "message": "Request body required"}), 400

            user = UserService.update_user(user_id, data)
            
            if user:
                return jsonify({"status": "success", "user": user}), 200
            return jsonify({"status": "error", "message": "Failed to update user. User might not exist."}), 404
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @staticmethod
    def delete_user(user_id):
        try:
            success = UserService.delete_user(user_id)
            if success:
                return jsonify({"status": "success", "message": "User deleted successfully"}), 200
            return jsonify({"status": "error", "message": "Failed to delete user"}), 400
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500