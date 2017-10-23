"""Initialize Flask and configuration"""
import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
APP = Flask(__name__)

# set the config
app_settings = os.getenv('APP_SETTINGS')
APP.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(APP)
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# model
class User(db.Model):
    """The user class"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow()

# print(APP.config)

@APP.route('/ping', methods=['GET'])
def ping_pong():
    """Test app endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
