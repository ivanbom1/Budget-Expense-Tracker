from flask import request, jsonify
from services.pocketService import PocketService


class PocketController:


    @staticmethod
    def get_pocket(pocket_id):

        pocket = PocketService.getPocketById(pocket_id)
        
        if pocket:
            return jsonify({"status": "success", "pocket": pocket.to_dict()}), 200
        return jsonify({"status": "error", "message": "Pocket not found"}), 404
    
    
    @staticmethod
    def get_user_pockets(user_id):

        pockets = PocketService.getPocketByUserId(user_id)
        
        if pockets:
            return jsonify({"status": "success", "pockets": [p.to_dict() for p in pockets]}), 200
        return jsonify({"status": "error", "message": "No pockets found"}), 404


    @staticmethod
    def create_pocket(user_id):
        try:
            data = request.get_json()
            print(f"Received data: {data}")
            print(f"User ID: {user_id}")
        
            if not data:
                return jsonify({"status": "error", "message": "Request body required"}), 400
        
            pocket = PocketService.createPocket(user_id, data)
            print(f"Created pocket: {pocket}")
        
            if pocket:
                return jsonify({"status": "success", "pocket": pocket.to_dict()}), 201
            return jsonify({"status": "error", "message": "Failed to create pocket"}), 400
        except Exception as e:
            print(f"Error creating pocket: {e}")
            import traceback
            traceback.print_exc()
            return jsonify({"status": "error", "message": str(e)}), 500


    @staticmethod
    def update_pocket(user_id, pocket_id):
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Request body required"}), 400
    
    # Verify pocket belongs to user
        pocket = PocketService.getPocketById(pocket_id)
        if not pocket or pocket.user_id != user_id:
            return jsonify({"status": "error", "message": "Pocket not found"}), 404
    
        updated_pocket = PocketService.updateById(pocket_id, data)
        if updated_pocket:
            return jsonify({"status": "success", "pocket": updated_pocket.to_dict()}), 200
        return jsonify({"status": "error", "message": "Failed to update pocket"}), 400


    @staticmethod
    def delete_pocket(user_id, pocket_id):
        try:
            # Verify pocket belongs to user
            pocket = PocketService.getPocketById(pocket_id)
            if not pocket or pocket.user_id != user_id:
                return jsonify({"status": "error", "message": "Pocket not found"}), 404
        
            PocketService.deleteById(pocket_id)
            return jsonify({"status": "success", "message": "Pocket deleted"}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 400