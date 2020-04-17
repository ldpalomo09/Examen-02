from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


import datetime

db = SQLAlchemy()

class User(db.Model): # crea la tabla de usuarios, con sus respectivas campos
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(40))
    password = db.Column(db.String(120))
    comments = db.relationship('Comment')
    teams = db.relationship('Teams')
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, nombre, apellido, email, password):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = self.__create_password(password)

  
    def __create_password(self, password): #combiente el password string a un hash para seguridad interna en la base de datos
        return generate_password_hash(password)

    def verify_password(self, password): #permite que el password que se digita en modo texto se convierta y se valide contra el password encriptado
        return check_password_hash(self.password, password)
    
class Comment(db.Model): # crea la tabla de comentarios, relacionada con usuarios.
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete="CASCADE"),nullable=False )
    text = db.Column(db.Text())
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Teams(db.Model): # crea la tabla de equipos.
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete="CASCADE"),nullable=False )
    nombre = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

