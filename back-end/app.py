from flask import Flask
from routes.pocketRoutes import pocket_bp


app = Flask(__name__)

app.register_blueprint(pocket_bp) # Register blueprint

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)