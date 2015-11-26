# -*- coding: utf-8 -*-
from .config import DefaultConfig
from .remote import remote
from .API import API
from flask import Flask

def create_app(config=DefaultConfig):
    """ Create an instance of MicroMote """
    app = Flask(config.IMPORT_NAME)

    app.config.from_object(config)
    app.register_blueprint(API)
    app.register_blueprint(remote)

    return app
