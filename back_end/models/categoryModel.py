from ..db_connect import Database

class Category:
    table_name = "categories"

    @staticmethod
    def find_all_by_user(user_id):
        return Database.query(
            f"SELECT * FROM {Category.table_name} WHERE user_id=%s",(user_id,))
    
        

    @staticmethod
    def find_by_id(category_id):
        return Database.query(f"SELECT * FROM {Category.table_name} WHERE id=%s LIMIT 1",(category_id,), one=True)
    
            
    @staticmethod
    def create(data):
        sql=f"""INSERT INTO {Category.table_name} (name, user_id) VALUES (%s , %s) RETURNING id """

        category_id= Database.query(sql, (data['name'], data['user_id']), one=True) [0]

        return Category.find_by_id(category_id)


    @staticmethod
    def update(category_id, data):
        sql= f"""UPDATE {Category.table_name} SET name=%s WHERE id=%s"""

        Database.execute(sql, (data['name'], category_id))
        return Category.find_by_id(category_id)

    @staticmethod
    def delete(category_id):
        Database.execute(f"DELETE FROM {Category.table_name} WHERE id=%s",(category_id,))
        return True
        
