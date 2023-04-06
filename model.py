from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def add(person):
    db.session.add(person)
    db.session.commit()

class PersonDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    born_date = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    have_car = db.Column(db.Boolean, nullable=True)


