import json
import pytest
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from model import db, PersonDb
from src.car import Car
from src.person import Person
from src.car import Car
from src.utils import verify_object_exist

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test-secret-key'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)
    api.add_resource(Person, '/people', '/people/<int:person_id>')
    api.add_resource(Car, '/car', '/car/<int:car_id>')

    jwt = JWTManager(app)

    yield app

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

def test_get_cars(client):
    test_post_person(client)
    test_post_car(client)
    response = client.get('/car')
    assert response.status_code == 200

def test_get_people(client):
    test_post_person(client)
    response = client.get('/people')
    assert response.status_code == 200

def test_post_car(client):
    test_post_person(client)
    data = {
        'model': 'hatch',
        'color': 'yellow',
        'year': '2022',
        'owner_id': '1'
    }
    response = client.post('/car', data=data)
    assert response.status_code == 201
    assert 'status' in response.json
    assert 'data' in response.json
    assert response.json['status'] == 201
    assert 'id' in response.json['data'][0]
    assert 'model' in response.json['data'][0]
    assert 'color' in response.json['data'][0]
    assert 'year' in response.json['data'][0]
    assert 'owner_id' in response.json['data'][0]

def test_post_car_error_400(client):
    test_post_person(client)
    data = {
        'model': None,
        'color': 'yellow',
        'year': '2022',
        'owner_id': '1'
    }
    response = client.post('/car', data=data)
    assert response.status_code == 400

def test_post_car_error_400_validate_color(client):
    test_post_person(client)
    data = {
        'model': None,
        'color': 'pink',
        'year': '2022',
        'owner_id': '1'
    }
    response = client.post('/car', data=data)
    assert response.status_code == 400

def test_post_person(client):
    data = {
        'name': 'Test Person',
        'born_date': '10/10/2010',
        'address': 'male',
        'phone': '898989',
        'email': 'feferfe',
        'have_car': 'True'
    }
    response = client.post('/people', data=data)
    assert response.status_code == 201
    assert 'status' in response.json
    assert 'data' in response.json
    assert response.json['status'] == 201
    assert 'id' in response.json['data'][0]
    assert 'name' in response.json['data'][0]
    assert 'born_date' in response.json['data'][0]
    assert 'address' in response.json['data'][0]
    assert 'phone' in response.json['data'][0]
    assert 'have_car' in response.json['data'][0]

def test_post_person_error_400(client):
    data = {
        'name': 'Test Person',
        'born_date': '10/10/2010',
        'address': None,
        'phone': '898989',
        'email': 'feferfe',
        'have_car': 'True'
    }
    response = client.post('/people', data=data)
    assert response.status_code == 400

def test_delete_car(client):
    test_post_person(client)
    test_post_car(client)
    response = client.delete('/car/1')
    assert response.status_code == 202


def test_delete_person(client):
    test_post_person(client)
    response = client.delete('/people/1')
    assert response.status_code == 202

def test_post_car_error_400_model(client):
    test_post_person(client)
    data = {
        'model': 'htch',
        'color': 'yellow',
        'year': '1999',
        'owner_id': '1'
    }
    response = client.post('/car', data=data)
    assert response.status_code == 400

def test_post_car_error_400_year(client):
    test_post_person(client)
    data = {
        'model': 'hatch',
        'color': 'yellow',
        'year': '1900',
        'owner_id': '1'
    }
    response = client.post('/car', data=data)
    assert response.status_code == 400

def test_post_car_error_400_color(client):
    test_post_person(client)
    data = {
        'model': 'hatch',
        'color': 'pink',
        'year': '1999',
        'owner_id': '1'
    }
    response = client.post('/car', data=data)
    assert response.status_code == 400

