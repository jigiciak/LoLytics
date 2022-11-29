import os


class Config(object):
    PATH_ASSETS = os.environ.get("PATH_ASSETS")
    REGIONS = os.environ.get("REGIONS")
    PATH_API = os.environ.get("PATH_API")


class ProdConfig(Config):
    FLASK_ENV = 'production'
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    TESTING = True
