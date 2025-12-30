from ..db.db_connect import Database
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    table_name = "users"

    def __init__(self, id=None, username=None, email=None, password=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def find_all():
        results = Database.query(f"SELECT * FROM {User.table_name}")
        return [User(id=r[0], username=r[1], email=r[2], password=r[3]) for r in results] if results else []

    @staticmethod
    def find_by_id(user_id):
        result = Database.query(
            f"SELECT * FROM {User.table_name} WHERE id=%s",
            (user_id,),
            one=True
        )
        if not result:
            return None
        return User(id=result[0], username=result[1], email=result[2], password=result[3])

    @staticmethod
    def find_by_email(email):
        result = Database.query(
            f"SELECT * FROM {User.table_name} WHERE email=%s",
            (email,),
            one=True
        )
        if not result:
            return None
        return User(id=result[0], username=result[1], email=result[2], password=result[3])

    @staticmethod
    def find_by_username(username):
        result = Database.query(
            f"SELECT * FROM {User.table_name} WHERE username=%s",
            (username,),
            one=True
        )
        if not result:
            return None
        return User(id=result[0], username=result[1], email=result[2], password=result[3])

    @staticmethod
    def create(data):
        try:
            if User.find_by_email(data['email']) or User.find_by_username(data['username']):
                return None
            hashed_password = generate_password_hash(data['password'])
        
            sql = f"""
            INSERT INTO {User.table_name} (username, email, password)
            VALUES (%s, %s, %s) RETURNING id
            """
            result = Database.execute(
                sql,
                (data['username'], data['email'], hashed_password)
            )
     
            if not result:
                return None
            user_id = result[0]
            user = User.find_by_id(user_id)
            return user
        except Exception as e:
            print(f"ERROR: {e}")
            return None

    @staticmethod
    def update(user_id, data):
        sql = f"""
        UPDATE {User.table_name}
        SET username=%s, email=%s, password=%s
        WHERE id=%s
        """
        hashed_password = generate_password_hash(data['password']) if 'password' in data else data.get('password')
        Database.execute(sql, (data['username'], data['email'], hashed_password, user_id))
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
        result = Database.query(
            f"SELECT COUNT(*) FROM {User.table_name}",
            one=True
        )
        return result[0] if result else 0

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def verify_password(self, password):
        return check_password_hash(self.password, password)