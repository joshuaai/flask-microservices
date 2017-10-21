"""Initialize Flask and configuration"""

from flask import Flask, jsonify

# instantiate the app
APP = Flask(__name__)

# set the config
APP.config.from_object('project.config.DevelopmentConfig')

@APP.route('/ping', methods=['GET'])
def ping_pong():
    """Test app endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
