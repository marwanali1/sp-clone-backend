import logging
import os
from config import DevelopmentConfig
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

api = Api()
bcrypt = Bcrypt()
cors = CORS()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.auth import auth_bp
    api.init_app(auth_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')

        file_handler = RotatingFileHandler(filename='logs/sp-clone.log', maxBytes=10240, backupCount=10)
        logger_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        file_handler.setFormatter(logger_formatter)
        file_handler.setLevel(logging.INFO)

        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)

    return app


from app import models
