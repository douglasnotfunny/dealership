import logging

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def mount_dict_to_return(data):
    logging.info(f"function.mount_dict_to_return({data})")
    data.pop('_sa_instance_state')
    return data
