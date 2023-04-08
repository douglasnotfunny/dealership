from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate

from src.person import Person
from src.car import Car
from model import db
import logging

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

if app.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

api.add_resource(Person, '/people', '/people/<int:person_id>')
api.add_resource(Car, '/car', '/car/<int:car_id>')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
