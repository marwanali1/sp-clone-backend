import os

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))


class Config(object):
    ENV = 'development'

    DEBUG = False

    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'skunkworks-secret'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    ENV = 'development'
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
