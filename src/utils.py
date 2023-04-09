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

def verify_object_exist(object: PersonDb | Cars, id: int) -> int:
    one_object = object.query.get(id)
    if one_object:
        return one_object
    abort(404, f'Not exist {str(id)} in DB')
