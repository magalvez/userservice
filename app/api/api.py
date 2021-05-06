#!flask/bin/python

"""
Restful API
"""

from flask_cors import CORS
from flask_restful import Api

from app import app
from app.api.resources.user import UserAPI, UserAuthAPI, UserVerificationAPI


api = Api(app)


api.add_resource(
    UserAPI,
    '/userservice/api/v1.0/user',
    endpoint='user-api'
)

api.add_resource(
    UserAuthAPI,
    '/userservice/api/v1.0/auth-user',
    endpoint='user-auth-api'
)

api.add_resource(
    UserVerificationAPI,
    '/userservice/api/v1.0/validate-user-account',
    endpoint='user-api-validation'
)

CORS(
  app,
  origins="*",
  allow_headers="*",
  supports_credentials=True
)
