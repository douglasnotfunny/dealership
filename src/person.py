from flask import request
from model import PersonDb, add, delete_db
from flask_restful import Resource

class Person(Resource):

    def validate(self):

        self.name = request.form.get('name', None)
        self.born_date = request.form.get('born_date', None)
        self.address = request.form.get('address', None)
        self.phone = request.form.get('phone', None)
        self.email = request.form.get('email', None)
        self.have_car = request.form.get('have_car', None)

        if not self.name:
            return {'status': 400, 'message': '400 field empty or wrong name of field'} , 400

    def insert_in_dict(self, person):
        people = {}
        people['id'] = person.id
        people['name'] = person.name
        people['born_date'] = person.born_date
        people['address'] = person.address
        people['have_car'] = person.have_car

        return people

    def post(self):
        data = self.validate()
        if data:
            return data

        person = PersonDb(name=self.name)
        add(person)

        data = []
        data.append(self.insert_in_dict(person))
        return {'status': 201, 'data': data} , 201

    def get(self):
        people_db = PersonDb.query.all()
        result = []
        for person in people_db:
            result.append(self.insert_in_dict(person))
        return {'status': 200, 'data': result} , 200

    def delete(self, person_id):
        person = PersonDb.query.get(person_id)  # Busca o registro pelo ID
        if person:
            delete_db(person)
            return {'status': 202, 'data': self.insert_in_dict(person)} , 202
        else:
            return {'status': 400, 'data': self.insert_in_dict(person)} , 400

