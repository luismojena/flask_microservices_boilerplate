"""
Main blueprint for the flask app
"""

from flask import Blueprint
from flask import jsonify

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    """
    Index route from main blueprint
    :return:
    """
    return jsonify({'Hello': 'World!!'})
