"""
Flask app module
"""

from os import environ

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': environ.get('MONGO_URI') or 'mongodb://playbox:pl4yv0x@localhost:27100/userservice'
}

db = MongoEngine()
db.init_app(app)
