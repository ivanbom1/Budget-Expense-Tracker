from flask import Flask
from back_end.routes.pocketRoutes import pocket_bp
from back_end.routes.userRoutes import user_routes


app = Flask(__name__)

app.register_blueprint(pocket_bp) # Register pocket blueprint
app.register_blueprint(user_routes, url_prefix='/users') # Register user blueprint


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)