"""
Main blueprint for the flask app
"""

from flask import Blueprint
from flask import jsonify

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/', methods=['GET'])
def index():
    """
    Index route from main blueprint
    :return:
    """
    return jsonify({'Hello': 'API!!'})
