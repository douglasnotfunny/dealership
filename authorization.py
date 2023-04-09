import logging

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

def verify_password(username, password):
    logging.info(f"funcion.verify_password({username, password})")
    return username == 'user' and password == 'password'
