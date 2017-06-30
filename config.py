# config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Common configurations
    """
    # App round variables
    DEBUG = True
    IPL_PATH_TO_GEOIP_DB = '/tmp/GeoLite2-City.mmdb'
    MAX_REQUEST_LENGTH = 1000

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


