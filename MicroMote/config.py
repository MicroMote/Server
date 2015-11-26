# -*- coding: utf-8 -*-

class BaseConfig(object):
    ''' The base config that all configuration objects variables will default to '''

    IMPORT_NAME = "MicroMote"

    DEBUG = True
    TESTING = False

    # TODO make this better
    ADMINS = ['melody@melody.blue']

    # Set this to something when deploying
    # this command works to generate something sufficently random.
    # python -c "import os; os.urandom(24)"
    SECRET_KEY = 'secret key'

class TestingConfig(BaseConfig):
    ''' The testing configuration, this makes things deterministic. '''
    DEBUG = False
    TESTING = True

class DefaultConfig(BaseConfig):
    ''' The default configuration '''
    DEBUG = False
    TESTING = False
