import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)
app.config.from_object(config[os.environ.get('APP_CONFIG', 'development')])

db = SQLAlchemy(app)


# import models below (because of ciclic dependency)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run(debug=True)
