from extensions import db 
from datetime import datetime
from sqlalchemy import Numeric

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(80), unique=True, nullable=False )
    password=db.Column(db.String(40), nullable=False)

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique= True, nullable=False)
    users_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
class Expense(db.Model):
    __tablename__='expenses'
    id=db.Column(db.Integer, primary_key=True)
    amount=db.Column(Numeric(10,2), nullable=False)
    description=db.Column(db.String(140))
    date=db.Column(db.DateTime, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id=db.Column(db.Integer, db.ForeignKey('categories.id'))

class Budget(db.Model):
    __tablename__="budgets"
    id=db.Column(db.Integer, primary_key=True)
    amount=db.Column(Numeric(10,2), nullable=False)
    month=db.Column(db.Integer, nullable=False)
    year=db.Column(db.Integer, nullable=False)
    day=db.Column(db.Integer, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)