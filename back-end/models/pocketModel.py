from userModel import User

#from extensions import db
from app import db

class Pocket(User):
    
    def __init__(self, userId, pocket_name, description=None, balance=0, goal=0, currency=None):
        
        self.userId = User.id #shared instance to refer pocket to particular user
        self.pocket_name = pocket_name
        self.description = description
        self.balance = balance
        self.goal = goal #optional saving goal on the current pocket
        self.currency = currency
        
            
    def __str__(self):
        return (f"{self.pocket_name} pocket has: {self.balance}{self.currency}/{self.goal}{self.currency}.") if self.goal else (f"{self.pocket_name} pocket has: {self.balance}{self.currency}.")
    
    
