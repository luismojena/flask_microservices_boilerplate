#!/usr/bin/env python
"""
Manager module for the flask app
"""
import os
import subprocess
import sys

from flask_script import Manager
from app import create_app, db

manager = Manager(create_app)


@manager.command
def createdb(drop_first=False):
    """Creates the database"""
    if drop_first:
        db.drop_all()
    db.create_all()


@manager.command
def test():
    """Runs tests"""
    tests = subprocess.call(['python', '-c', 'import tests; tests.run()'])
    sys.exit(tests)


@manager.command
def lint():
    """Runs linter """
    linter = subprocess.call(['pylint', 'app/', 'manage.py', 'tests/']) == 0
    if linter:
        print('OK')
    sys.exit(linter)


@manager.command
def mypy():
    """Runs mypy static type analyzer"""
    _mypy = subprocess.call(['mypy', 'app/'])
    sys.exit(_mypy)


if __name__ == '__main__':
    if sys.argv[1] == 'lint':
        os.environ['APP_CONFIG'] = 'testing'
    manager.run()
