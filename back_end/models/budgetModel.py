from ..db_connect import Database

class Budget:
    table_name = "budgets"

    @staticmethod
    def find_by_month(user_id, month, year):
        return Database.query(f"""SELECT * FROM {Budget.table_name} WHERE id=%s AND month=%s AND year=%s LIMIT 1""", (user_id,month, year),one=True)
    

    @staticmethod
    def create(data):
        sql=f"""INSERT INTO {Budget.table_name}(amount,month, year, user_id)values (%s,%s,%s) RETURNING id"""
        budget_id=Database.query(sql,(data['amount'],data['month'],data['year'],data['user_id']),
        one=True)[0]

        return Budget.find_by_month(data['user_id'],data['month'],data['year'])
    

    @staticmethod
    def update(budget_id, data):
        sql=f"""UPDATE{Budget.table_name} SET amount=%s, where id=%s """
        Database.execute(sql,(data['amount'],budget_id))
        return Database.query(f"SELECT * FROM {Budget.table_name} WHERE id=%s LIMIT 1",(budget_id), one=True)

    @staticmethod
    def delete(budget_id):
        Database.execute(f"DELETE FROM {Budget.table_name} WHERE id=%s",(budget_id))
        return True
