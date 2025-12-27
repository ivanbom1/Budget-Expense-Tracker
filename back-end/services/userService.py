from ..models.userModel import User

def get_all_by_users():
    return User.find_all

def get_by_user_id(user_id):
    return User.find_by_id(user_id)

def create_user(data):
    return User.create(data)

def update_user(user_id, data):
    return User.update(user_id, data)

def delete_user(user_id):
    return User.delete(user_id)

def count_users():
    return User.count()