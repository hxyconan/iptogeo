# Copyright 2017

from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app

