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
        req = json.loads(request.data.decode(encoding='UTF-8'))
        start_time, start_location, end_time, end_location, location_type = req["start_time"], req["start_location"], req["end_time"], req["end_location"], req["location_type"]

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
