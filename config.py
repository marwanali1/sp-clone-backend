import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))


class Config:
    FLASK_ENV = 'development'

    BCRYPT_LOG_ROUNDS = 13

    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') + os.environ.get('DATABASE_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'

    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'

    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') + os.environ.get('DATABASE_NAME') + '_test'


class ProductionConfig(Config):
    FLASK_ENV = 'production'
