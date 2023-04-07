from flask import request
from model import Cars, add, delete_db
from flask_restful import Resource

class Car(Resource):

    def validate(self):

        self.name = request.form.get('name', None)
        self.owner_id = request.form.get('owner_id', None)
        self.model = request.form.get('model', None)
        self.color = request.form.get('color', None)

        print('Car -> ',Cars.__dict__.keys())
        print('Request -> ',request.form.keys())

        if not self.name:
            return {'status': 400, 'message': '400 field empty or wrong name of field'} , 400

    def insert_in_dict(self, car):
        cars = {}
        cars['id'] = car.id
        cars['name'] = car.name
        cars['owner_id'] = car.owner_id

        return cars


    def post(self):
        data = self.validate()
        if data:
            return data

        print(self.name, self.owner_id)
        car = Cars(name=self.name, owner_id=int(self.owner_id), model=self.model, color=self.color)
        print(car)
        add(car)

        data = []
        data.append(self.insert_in_dict(car))
        return {'status': 201, 'data': data} , 201

    def get(self):
        cars_db = Cars.query.all()
        result = []
        for car in cars_db:
            result.append(self.insert_in_dict(car))
        return {'status': 200, 'data': result} , 200

    def delete(self, car_id):
        car = Cars.query.get(car_id)  # Busca o registro pelo ID
        if car:
            delete_db(car)
            return {'status': 202, 'data': self.insert_in_dict(car)} , 202
        else:
            return {'status': 400, 'data': self.insert_in_dict(car)} , 400


