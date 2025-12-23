from werkzeug.security import generate_password_hash, check_password_hash
from back_end.models.userModel import User
from extensions import db 

def register_user(username, email, password):
    if User.query.filter_by(email=email).first():
        return {"error": "Email already registered", "status": 400}
    
    new_user = User(
        username=username, 
        email=email, 
        password=generate_password_hash(password)
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User registered successfully!", "status": 201}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e), "status": 500}

def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        return {"message": "Login successful", "user": user.username, "status": 200}
    
    return {"error": "Invalid email or password", "status": 401}