from ..models.userModel import User

class userService:
    @staticmethod
    def get_all_by_users():
        try:
            return User.find_all()
        except Exception as e:
            print(f"Error while fetching user:{e}")
            return None

    @staticmethod
    def get_by_user_id(user_id):
        try:
            return User.find_by_id(user_id)
        except Exception as e:
            print(f"Error while fetching user:{e}")
            return None

    @staticmethod
    def createUser(data):
        try:
            if not data.get('username') or not data.get('email') or not data.get('password'):
                print("username, email and password are required")
                return None
            return User.create(data)

        except Exception as e:
            print(f"Error creating user: {e}")
            return None
        

    @staticmethod
    def update_user(user_id, data):
        try:
            if not User.find_by_id(user_id):
                print("user not found")
                return None
            return User.update(user_id, data)
        
        except Exception as e :
            print(f"error while updating user:{e}")
            return None


    @staticmethod
    def delete_user(user_id):
        try:
            return User.delete(user_id)
        except Exception as e:
            print(f"error while deleting user:{e}")
            return None
        
    @staticmethod
    def count_user():
        try:
            return User.count()
        except Exception as e:
            print(f"error while counting users:{e}")
            return None

