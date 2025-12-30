from flask import Blueprint
from ..controllers.pocketController import PocketController

pocket_bp = Blueprint('pocket', __name__)

pocket_bp.route('/<int:pocket_id>', methods=['GET'])(PocketController.get_pocket)
pocket_bp.route('/users/<int:user_id>', methods=['GET'])(PocketController.get_user_pockets)
pocket_bp.route('/users/<int:user_id>', methods=['POST'])(PocketController.create_pocket)
pocket_bp.route('/<int:pocket_id>', methods=['PUT'])(PocketController.update_pocket)
pocket_bp.route('/<int:pocket_id>', methods=['DELETE'])(PocketController.delete_pocket)