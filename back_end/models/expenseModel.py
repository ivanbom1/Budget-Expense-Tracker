from ..db_connect import Database

class Expense:
    table_name = "expenses"

    @staticmethod
    def find_all_by_user(user_id):
        return Database.query(
            f"""
            SELECT e.*, c.name AS category_name
            FROM {Expense.table_name} e
            LEFT JOIN categories c ON e.category_id = c.id
            WHERE e.user_id=%s
            ORDER BY e.date DESC
            """,
            (user_id,)
        )

    @staticmethod
    def find_by_id(expense_id):
        return Database.query(
            f"SELECT * FROM {Expense.table_name} WHERE id=%s LIMIT 1",
            (expense_id,),
            one=True
        )

    @staticmethod
    def create(data):
        sql = f"""
        INSERT INTO {Expense.table_name}
        (amount, description, date, user_id, category_id)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """
        expense_id = Database.query(
            sql,
            (
                data['amount'],
                data.get('description'),
                data.get('date'),
                data['user_id'],
                data.get('category_id')
            ),
            one=True
        )[0]

        return Expense.find_by_id(expense_id)

    @staticmethod
    def delete(expense_id):
        Database.execute(
            f"DELETE FROM {Expense.table_name} WHERE id=%s",
            (expense_id,)
        )
        return True
