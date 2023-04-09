from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv
import os

load_dotenv()

jwt_secret_key = os.environ.get('SECRET_KEY')

from src.person import Person
from src.car import Car
from model import db

import logging

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = jwt_secret_key
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'

jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

if app.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

api = Api(app)
api.add_resource(Person, '/people', '/people/<int:person_id>')
api.add_resource(Car, '/car', '/car/<int:car_id>')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
