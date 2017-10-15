'''config.py'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    '''Config'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'karat coddle foamy'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        '''Init app'''
        pass


class DevelopmentConfig(Config):
    '''Dev config'''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'star.sqlite')


class TestingConfig(Config):
    '''Testing config'''
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'star.sqlite')


class ProductionConfig(Config):
    '''Production config'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'star.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
