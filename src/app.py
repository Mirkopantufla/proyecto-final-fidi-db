import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# DEBUG: When using flask run to start the development server, an interactive debugger will be shown for unhandled exceptions, and the server will be reloaded when code changes.
app.config['DEBUG'] = True
# ENV: deprecado en la 2.3
app.config['ENV'] = 'development' 
# SQLALCHEMY_TRACK_MODIFICATIONS: If you want to disable track modifications add False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLALCHEMY_DATABASE_URI: The database URI that should be used for the connection comes from .env file in this case
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASEURI')
# app.url: Este comando sirve para que la url la tome con o sin el / al final de la ruta
app.url_map.strict_slashes = False
# Config JWT 
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')

db.init_app(app)

@app.route('/')
def main():
    return jsonify({ "message": "API REST With Flask"}), 200


if __name__ == '__main__':
    app.run()