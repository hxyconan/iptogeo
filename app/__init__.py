# Copyright 2017

from flask import Flask
from config import config
import geoip2.database
import gzip, os

DB_PATH_DEFAULT = '/tmp/GeoLite2-City.mmdb'
if not os.path.exists(DB_PATH_DEFAULT):
    mmdb_url = 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'
    download_mmdb_file_cmd = 'wget -O - ' + mmdb_url + ' | gunzip - > ' + DB_PATH_DEFAULT
    os.system(download_mmdb_file_cmd)
db = geoip2.database.Reader(DB_PATH_DEFAULT)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Specific database reader
    try:
        db = geoip2.database.Reader(app.config['IPL_PATH_TO_GEOIP_DB'])
    except TypeError:
        stderr.write('Could not find MaxMind database\n')
        exit(1)


    from .routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app

