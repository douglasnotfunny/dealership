import logging

from flask_sqlalchemy import SQLAlchemy
from flask import abort

from model import PersonDb, Cars

db = SQLAlchemy()

def mount_dict_to_return(data: PersonDb | Cars):
    logging.info(f"function.mount_dict_to_return({data})")
    data_dict = data.__dict__
    data.__dict__.pop('_sa_instance_state')

    result = {}
    for key in data_dict.keys():
        result[key] = data_dict[key]
    return result

def verify_if_exist_more_than_three(id):
    logging.info(id)
    get_object = Cars.query.filter(Cars.owner_id == id).count()
    logging.info(get_object)
    if get_object < 3:
        return id
    abort(400, f'Exist more than 3 cars for this person')

def verify_object_exist(object: PersonDb | Cars, id: int) -> int:
    get_object = object.query.get(id)
    logging.info(len(get_object))
    if get_object:
        return get_object
    abort(404, f'Not exist {str(id)} in DB')
