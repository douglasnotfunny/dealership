from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def add(data):
    db.session.add(data)
    db.session.commit()

def delete_db(data):
    db.session.delete(data)
    db.session.commit()

class PersonDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    born_date = db.Column(db.String(10), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(30), nullable=True)
    have_car = db.Column(db.Boolean, nullable=True)


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(100), nullable=True)
    color = db.Column(db.String(15), nullable=True)
    ownier_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)  # Chave estrangeira para a tabela Pessoa
    proprietario = db.relationship('Pessoa', backref='carros', lazy=True)  # Relacionamento com a tabela Pessoa



