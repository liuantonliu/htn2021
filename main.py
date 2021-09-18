import logging
import os
import json
from flask import Flask, jsonify, request
import time, datetime

from maps_api import *


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return "Goodbye world"

@app.route('/get_locations', methods=['GET'])
def get_locations():
    try:
        print("#######################################")
        start_time = json.loads(request.args.get("start_time").lower())
        start_location = json.loads(request.args.get("start_location").lower())
        end_time = json.loads(request.args.get("end_time").lower())
        end_location = json.loads(request.args.get("end_location").lower())
        location_type = json.loads(request.args.get("location_type").lower())
        print(start_time, start_location, end_time, end_location, location_type)

        locationsList = list_locations(start_location, location_type)

        return jsonify({"results": locationsList}), 200
    except Exception as e:
        return jsonify({"error": e}), 400


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
