import os

class Config(object):
    SECRET_KEY = 'la_palabra_clave'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:palomo@localhost/examen02'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

