from .helpers import lookup
from flask import request
from flask import Blueprint, current_app
import json
import logging

routes = Blueprint('routes', __name__)

# Router to get geo data via ip
@routes.route("/getgeo", methods=["GET"])
@routes.route("/getgeo/", methods=["GET"])
@routes.route("/getgeo/<string:ips>", methods=["GET"])
def getgeo(ips=None):

    # Generate ips list
    if ips:
        if len(ips) > current_app.config['MAX_REQUEST_LENGTH']:
            return {'error': 'too many input ips...'}, 400
        else:
            ips = ips.split(',')
    else:
        # Since it after proxy, should use more sophisticated way to get remote ip
        if request.headers.getlist("X-Forwarded-For"):
            x_forwarded_for_header = request.headers.getlist("X-Forwarded-For")
            ips = [x_forwarded_for_header[0].split(',')[0]] #Always get first element in X-Forwarded-For header
        else:
            ips = [request.remote_addr]

    logging.debug("Request to check geo for IP: %s", ', '.join(ips))

    response_in_json = ''
    if len(ips) == 1:
        response_in_json = json.dumps(lookup(ips[0]))
    else:
        results_list = []
        for ip in ips:
            results_list.append(lookup(ip))
        response_in_json = json.dumps(results_list)

    logging.debug("Response json string: %s", response_in_json)

    return response_in_json


# Router for testing
@routes.route('/', methods=['GET', 'POST'])
@routes.route('/ping', methods=['GET', 'POST'])
def ping():
    """
    testing message
    """
    logging.debug("Ping test.")

    return 'OK'

