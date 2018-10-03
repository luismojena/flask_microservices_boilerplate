"""
Initializer for app module
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

from .api import api_blueprint
from .app import main_blueprint

__all__ = ['create_app', 'db']

db = SQLAlchemy()

from . import models  # noqa


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('APP_CONFIG', 'development')
    app_ = Flask(__name__)
    app_.config.from_object(config[config_name])

    # Init flask extensions
    db.init_app(app_)

    # Register blueprints
    app_.register_blueprint(main_blueprint, url_prefix='/')
    app_.register_blueprint(api_blueprint, url_prefix='/api')

    return app_
