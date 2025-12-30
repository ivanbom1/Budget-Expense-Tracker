from ..models.pocketModel import Pocket
from ..models.userModel import User

class PocketService:
    
    
    @staticmethod
    def getPocketById(id):
        try:
            pocket = Pocket.find_by_id(id)
            if pocket is None:
                return None
            return pocket
        
        except ValueError:
            print(f"Invalid pocket ID: {id}")
            return None
        
        except Exception as e:
            print(f"Database error: {e}")
            return None
        

    @staticmethod        
    def getPocketByUserId(user_id):
        try:
            pockets = Pocket.find_by_user(user_id)
            if pockets is None:
                return None
            return pockets
        
        except ValueError:
            print(f"Invalid user ID: {user_id}")
            return None
        
        except Exception as e:
            print(f"Database error: {e}")
            return None
        

    @staticmethod
    def createPocket(user_id, data):
        try:
            user = User.find_by_id(user_id)
            if not user:
                print(f"User {user_id} not found")
                return None

            if 'pocket_name' not in data or not data['pocket_name']:
                print("pocket_name is required")
                return None

            balance = data.get('balance', 0)
            if not isinstance(balance, (int, float)) or balance < 0:
                print("balance must be a non-negative number")
                return None

            goal = data.get('goal', 0)
            if goal and (not isinstance(goal, (int, float)) or goal < 0):
                print("goal must be a non-negative number")
                return None

            currency = data.get('currency')
            if currency and (not isinstance(currency, str) or len(currency) != 3):
                print("currency must be 3-letter code (e.g., USD)")
                return None

            new_pocket = Pocket.create(user_id, data)
            return new_pocket
            
        except Exception as e:
            print(f"Error creating pocket: {e}")
            return None

    
    @staticmethod
    def updateById(id, data):
        try:
            pocket = Pocket.find_by_id(id)
            if not pocket:
                print(f"Pocket {id} not found")
                return None

            if 'pocket_name' not in data or not data['pocket_name']:
                print("pocket_name is required")
                return None

            if data.get('balance') and not isinstance(data['balance'], (int, float)):
                print("balance must be a number")
                return None
            
            if data.get('goal') and not isinstance(data['goal'], (int, float)):
                print("goal must be a number")
                return None

            updated_pocket = Pocket.update(id, data)
            return updated_pocket
            
        except Exception as e:
            print(f"Error updating pocket: {e}")
            return None

    
    @staticmethod
    def deleteById(id):
        try:
            Pocket.delete(id)
            
        except Exception as e:
            print(f"Error deleting pocket: {e}")
        