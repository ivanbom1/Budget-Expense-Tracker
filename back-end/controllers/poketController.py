from flask import request, jsonify
from ..services.pocketService import PocketService


class PocketController:


    @staticmethod
    def get_pocket(pocket_id):

        pocket = PocketService.getPocketById(pocket_id)
        
        if pocket:
            return jsonify({"status": "success", "pocket": pocket.__dict__}), 200
        return jsonify({"status": "error", "message": "Pocket not found"}), 404
    
    
    @staticmethod
    def get_user_pockets(user_id):

        pockets = PocketService.getPocketById(user_id)
        
        if pockets:
            return jsonify({"status": "success", "pockets": [p.__dict__ for p in pockets]}), 200
        return jsonify({"status": "error", "message": "No pockets found"}), 404


    @staticmethod
    def create_pocket(user_id):

        data = request.get_json()

        if not data:
            return jsonify({"status": "error", "message": "Request body required"}), 400
        
        pocket = PocketService.createPocket(user_id, data)
        
        if pocket:
            return jsonify({"status": "success", "pocket": pocket.__dict__}), 201
        return jsonify({"status": "error", "message": "Failed to create pocket"}), 400


    @staticmethod
    def update_pocket(pocket_id):

        data = request.get_json()

        if not data:
            return jsonify({"status": "error", "message": "Request body required"}), 400

        pocket = PocketService.updateById(pocket_id, data)

        if pocket:
            return jsonify({"status": "success", "pocket": pocket.__dict__}), 200
        return jsonify({"status": "error", "message": "Failed to update pocket"}), 400


    @staticmethod
    def delete_pocket(pocket_id):

        try:
            PocketService.deleteById(pocket_id)
            return jsonify({"status": "success", "message": "Pocket deleted"}), 200

        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 400
