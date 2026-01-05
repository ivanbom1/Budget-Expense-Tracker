from flask import Flask
from routes.pocketRoutes import pocket_bp
from routes.userRoutes import user_routes

app = Flask(__name__)
app.register_blueprint(pocket_bp)
app.register_blueprint(user_routes, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)