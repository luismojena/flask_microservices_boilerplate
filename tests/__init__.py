import os
import sys
import unittest

import coverage


def run():
    os.environ['FLASK_TESTING'] = 'testing'

    # start coverage engine
    coverage_engine = coverage.Coverage(branch=True)
    coverage_engine.start()

    # run tests
    tests = unittest.TestLoader().discover('.')
    ok = unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful()

    # print coverage report
    coverage_engine.stop()
    print('')
    coverage_engine.report(omit=['manage.py', 'tests/*'])

    sys.exit(0 if ok else 1)
