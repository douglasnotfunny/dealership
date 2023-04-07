from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def add(data):
    db.session.add(data)
    db.session.commit()

def delete_db(data):
    db.session.delete(data)
    db.session.commit()

class PersonDb(db.Model):
    __tablename__ = 'person_db'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    born_date = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    have_car = db.Column(db.Boolean, nullable=False)


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(15), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person_db.id'))
    owner = db.relationship('PersonDb')
