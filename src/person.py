from flask import request
from model import PersonDb, add
from flask_restful import Resource

class Person(Resource):

    def validate(self):
        self.name = request.form.get("name", None)
        print("AQUI -> ", self.name)
        if not self.name:
            return {"error": "400 field empty or wrong name of field"}

    def post(self):
        data = self.validate()
        if data:
            return data
        # if not name:
        #     return Exception('oi')
        person = PersonDb(name=self.name)
        add(person)
        return {'name': self.name}

    def get(self):
        pessoas = PersonDb.query.all()
        print("OI")
        print(pessoas)
        for pessoa in pessoas:
            print('ID:', pessoa.id)
            print('Nome:', pessoa.name)
            print('Idade:', pessoa.born_date)
            print('---')
        return {'status': 200}
