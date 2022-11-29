import os


class Config(object):
    FLASK_ENV = 'production'
    TESTING = False


class ProdConfig(Config):
    FLASK_ENV = 'production'
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    TESTING = True
