from .helpers import lookup
from flask import request
from flask import Blueprint, current_app
import json


routes = Blueprint('routes', __name__)

# Router to get geo data via ip
@routes.route("/getgeo/<string:ips>", methods=["GET"])
def getgeo(ips):

    # Generate ips list
    if ips:
        if len(ips) > current_app.config['MAX_REQUEST_LENGTH']:
            return {'error': 'too many input ips...'}, 400
        else:
            ips = ips.split(',')
    else:
        ips = [request.environ['REMOTE_ADDR']]

    response = {}
    for ip in ips:
        response.update(lookup(ip))

    return json.dumps(response)


# Router for testing
@routes.route('/', methods=['GET', 'POST'])
@routes.route('/ping', methods=['GET', 'POST'])
def ping():
    """
    testing message
    """
    return 'OK'

