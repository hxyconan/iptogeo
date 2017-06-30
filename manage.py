#!/usr/bin/env python
import os
from sys import stderr, exit
from app import create_app
from flask.ext.script import Manager
from flask.ext import restful
import geoip2.database


app = create_app('development')
# Try to create a database reader
try:
    db = geoip2.database.Reader(app.config['IPL_PATH_TO_GEOIP_DB'])
except TypeError:
    stderr.write('Could not find MaxMind database\n')
    exit(1)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()

