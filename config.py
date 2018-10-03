import os

basedir = os.path.abspath(os.path.dirname(__name__))

default_database_url = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '5ceba5ab-3079-45ce-9c96-ab608c5e7ba2')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default_database_url)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
