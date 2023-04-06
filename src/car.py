from flask import request

class Car():

    def __init__(self) -> None:
        self.car = request.form.get("language")

    def validate(self):
        pass

    def post(self):
        return {"oi": self.car}
