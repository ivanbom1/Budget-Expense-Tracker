from ..db.db_connect import Database

class Pocket:
    table_name = "pockets"
    
    def __init__(self, user_id, pocket_name, description=None, balance=0, goal=0, currency=None, pocket_id=None):
        self.id = pocket_id
        self.user_id = user_id  #Foreign key to users table to refer each pocket to particular user
        self.pocket_name = pocket_name
        self.description = description
        self.balance = balance
        self.goal = goal
        self.currency = currency
    
    
    def __str__(self):
        goal_str = f"/{self.goal}{self.currency}" if self.goal else ""
        return f"{self.pocket_name} pocket has: {self.balance}{self.currency}{goal_str}"
    
    
    @staticmethod
    def create(user_id, data):
        sql = f"""
        INSERT INTO {Pocket.table_name} (user_id, pocket_name, description, balance, goal, currency)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """
        
        pocket_id = Database.query(
            sql,
            (user_id, data['pocket_name'], data.get('description'), 
             data.get('balance', 0), data.get('goal', 0), data.get('currency')),
            one=True)[0]
        
        return Pocket.find_by_id(pocket_id)
    
    
    @staticmethod
    def find_by_id(pocket_id):
        result = Database.query(
            f"SELECT * FROM {Pocket.table_name} WHERE id=%s",
            (pocket_id,),
            one=True)
        
        if result:
            return Pocket(*result)
        return None
    
    
    @staticmethod
    def find_by_user(user_id):
        results = Database.query(
            f"SELECT * FROM {Pocket.table_name} WHERE user_id=%s",
            (user_id,))
        
        return [Pocket(*row) for row in results]
    
    
    @staticmethod
    def update(pocket_id, data):
        sql = f"""
        UPDATE {Pocket.table_name}
        SET pocket_name=%s, description=%s, balance=%s, goal=%s, currency=%s
        WHERE id=%s
        """
        
        Database.execute(
            sql,
            (data['pocket_name'], data.get('description'), 
             data.get('balance'), data.get('goal'), data.get('currency'), pocket_id))
        
        return Pocket.find_by_id(pocket_id)
    
    
    @staticmethod
    def delete(pocket_id): #delete pocket by its id
        Database.execute(
            f"DELETE FROM {Pocket.table_name} WHERE id=%s",
            (pocket_id,))
        
        return True
    