"""
Main file for the flask  app

"""
from flask import Blueprint

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return '<h1>Client App</h1>'
