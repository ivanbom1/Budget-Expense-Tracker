from ..db_connect import Database

class User:
    table_name = "users"

    @staticmethod
    def find_all():
        return Database.query(f"SELECT * FROM {User.table_name}")

    @staticmethod
    def find_by_id(user_id):
        return Database.query(
            f"SELECT * FROM {User.table_name} WHERE id=%s",
            (user_id,),
            one=True
        )

    @staticmethod
    def create(data):
        sql = f"""
        INSERT INTO {User.table_name} (username, email, password)
        VALUES (%s, %s, %s) RETURNING id
        """
        user_id = Database.query(
            sql,
            (data['username'], data['email'], data['password']),
            one=True
        )[0]
        return User.find_by_id(user_id)

    @staticmethod
    def update(user_id, data):
        sql = f"""
        UPDATE {User.table_name}
        SET username=%s, email=%s, password=%s
        WHERE id=%s
        """
        Database.execute(sql, (data['username'], data['email'], data['password'], user_id))
        return User.find_by_id(user_id)

    @staticmethod
    def delete(user_id):
        Database.execute(
            f"DELETE FROM {User.table_name} WHERE id=%s",
            (user_id,)
        )
        return True

    @staticmethod
    def count():
        return Database.query(
            f"SELECT COUNT(*) FROM {User.table_name}",
            one=True
        )[0]

