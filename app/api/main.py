from flask import Blueprint
from flask import jsonify

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return jsonify({'Hello': 'World!!'})
