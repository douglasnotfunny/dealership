from flask import request, abort
from flask_restful import Resource

import logging
import traceback

from model import PersonDb, add, delete_db
from .utils import mount_dict_to_return

class Person(Resource):

    def get_data(self) -> None:
        self.name = request.form.get('name', None)
        self.born_date = request.form.get('born_date', None)
        self.address = request.form.get('address', None)
        self.phone = request.form.get('phone', None)
        self.email = request.form.get('email', None)
        self.have_car = request.form.get('have_car', None)

        logging.info(f"payload->{request.form.to_dict()}")

    def post(self):
        self.get_data()
        person = PersonDb(name=self.name, born_date=self.born_date, address=self.address,
                          phone=self.phone, email=self.email)
        # person_dict = mount_dict_to_return(person.__dict__)

        data = []
        try:
            add(person)
        except Exception as exc:
            logging.error(exc, traceback.format_exc())
            abort(400, 'Error to insert')

        data = []
        return {'status': 201, 'data': data} , 201

    def get(self):
        people_db = PersonDb.query.all()
        result = []
        for person in people_db:
            result.append(person)
        return {'status': 200, 'data': result} , 200

    def delete(self, person_id):
        person = PersonDb.query.get(person_id)  # Busca o registro pelo ID
        if person:
            try:
                delete_db(person)
            except Exception as exc:
                Exception('Error to delete', exc.with_traceback)
            return {'status': 202, 'data': self.insert_in_dict(person)} , 202
        else:
            return {'status': 400, 'data': self.insert_in_dict(person)} , 400

