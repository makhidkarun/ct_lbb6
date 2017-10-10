'''app/__init__.py'''

import logging
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    # format='%(asctime)-15s %(name)s %(funcName)s(): %(message)s',
    format='%(relativeCreated)d %(name)s %(funcName)s(): %(message)s',
    level=logging.INFO
)


def create_app(config_name):
    '''Create app method'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    if app.config['DEBUG']:
        LOGGER.setLevel(logging.DEBUG)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
