#!/usr/bin/python3
"""
app
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown function
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Not found"""
    return jsonify({'error': 'Not found'}), 404


@app.teardown_appcontext
def teardown(exception):
    """Remove current session"""
    storage.close()


if _name_ == '_main_':
    """Main function"""
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
