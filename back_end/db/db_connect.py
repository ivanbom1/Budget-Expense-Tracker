
import psycopg2
from .db_config import Config

class Database:
    @staticmethod
    def query(sql, params=None, one=False):
        conn = psycopg2.connect(
            host=Config.DB_HOST,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT
        )
        cur = conn.cursor()
        cur.execute(sql, params)
        result = cur.fetchone() if one else cur.fetchall()
        cur.close() 
        conn.close()
        return result


    @staticmethod
    def execute(sql, params=None):
        conn = psycopg2.connect(
            host=Config.DB_HOST,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT
        )
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
    
        result = cur.fetchone() if "RETURNING" in sql else None
    
        cur.close()
        conn.close()
        return result
    