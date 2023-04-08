from flask import request, abort
from flask_restful import Resource

import logging

from model import Cars, add, delete_db
from .utils import mount_dict_to_return

class Car(Resource):

    def validate_year(self, year):
        if year >= 1908:
            return year
        abort(400, 'Year is less than 1908')

    def validate_color(self, color):
        if color in ['yellow', 'blue', 'gray']:
            return color
        abort(400, 'Color must be yellow or blue or gray')

    def validate_model(self, model):
        if model in ['hatch', 'sedan','convertible']:
            return model
        abort(400, 'Model must be hatch or sedan or convertible')

    def get_data(self):
        self.model = self.validate_model(request.form.get('model'))
        self.color = self.validate_color(request.form.get('color'))
        self.year = self.validate_year(int(request.form.get('year')))
        self.owner_id = request.form.get('owner_id', None)

        logging.info(f"payload->{request.form.to_dict()}")

    def post(self):
        self.get_data()
        car = Cars(model=self.model, color=self.color,
                   year=int(self.year), owner_id=int(self.owner_id))
        car_dict = mount_dict_to_return(car)

        try:
            add(car)
        except Exception as exc:
            abort(400, f'Error to insert {exc.with_traceback}')

        data = []
        data.append(car_dict)
        return {'status': 201, 'data': data} , 201

    def get(self):
        cars_db = Cars.query.all()
        logging.info(f'DICT -> {cars_db}')
        result = []
        for car in cars_db:
            logging.info(f'DICT -> {car.__dict__}')
            result.append(car.__dict__)
        return {'status': 200, 'data': result} , 200

    def delete(self, car_id):
        car = Cars.query.get(car_id)  # Busca o registro pelo ID
        if car:
            try:
                delete_db(car)
            except Exception as exc:
                abort(400, f'Error to delete {exc.with_traceback}')
            return {'status': 202, 'data': self.insert_in_dict(car)} , 202
        else:
            abort(404, f'Car not founded')
