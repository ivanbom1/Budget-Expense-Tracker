from ..db_connect import Database

class ModelName:
    table_name = "budgets"

    @staticmethod
    def find_all():
        ...

    @staticmethod
    def find_by_id(id):
        ...

    @staticmethod
    def create(data):
        ...

    @staticmethod
    def update(id, data):
        ...

    @staticmethod
    def delete(id):
        ...
