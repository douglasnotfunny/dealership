from flask import request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

import traceback
import logging

from model import Cars, PersonDb, add, delete_db
from .utils import mount_dict_to_return, verify_object_exist, verify_if_exist_more_than_three


class Car(Resource):

    def validate_year(self, year: int) -> int:
        if year >= 1908:
            return year
        abort(400, 'Year is less than 1908')

    def validate_color(self, color: str) -> str:
        if color in ['yellow', 'blue', 'gray']:
            return color
        abort(400, 'Color must be yellow or blue or gray')

    def validate_model(self, model: str) -> str:
        if model in ['hatch', 'sedan','convertible']:
            return model
        abort(400, 'Model must be hatch or sedan or convertible')

    def get_data(self) -> None:
        self.model = self.validate_model(request.form.get('model'))
        self.color = self.validate_color(request.form.get('color'))
        self.year = self.validate_year(int(request.form.get('year')))
        person = verify_if_exist_more_than_three(int(request.form.get('owner_id')))
        self.owner_id = int(request.form.get('owner_id'))

        logging.info(f"payload: {request.form.to_dict()}")

    @jwt_required(optional=True)
    def post(self) -> tuple:
        logging.info("post()")
        self.get_data()
        car = Cars(model=self.model, color=self.color,
                      year=self.year, owner_id=self.owner_id)

        data = []
        id = add(car)
        data.append(mount_dict_to_return(Cars.query.get(id)))

        return {'status': 201, 'data': data} , 201

    @jwt_required(optional=True)
    def get(self) -> tuple:
        cars_db = Cars.query.all()
        result = []
        for car in cars_db:
            result.append(mount_dict_to_return(car))
        return {'status': 200, 'data': result} , 200

    @jwt_required(optional=True)
    def delete(self, car_id: int):
        car = verify_object_exist(Cars, car_id)
        delete_db(car)
        return {'status': 202, 'data': mount_dict_to_return(car)} , 202
