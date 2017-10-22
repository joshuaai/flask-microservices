"""Initialize Flask and configuration"""
import os
from flask import Flask, jsonify

# instantiate the app
APP = Flask(__name__)

# set the config
app_settings = os.getenv('APP_SETTINGS')
APP.config.from_object(app_settings)

# print(APP.config)

@APP.route('/ping', methods=['GET'])
def ping_pong():
    """Test app endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
