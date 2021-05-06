#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import request
from flask_jwt import jwt_required

from flask_restful import Resource

from app.api.controllers.user import UserController
from app.api.success_response import HttpSuccess
from util.decorators.endpoint_api import api_resource_endpoint


class UserAPI(Resource):
    """
    Class UserAPI resource to perform communications with Controllers
    """

    @jwt_required()
    @api_resource_endpoint()
    def get(self):
        """
        Get all Users model
        """
        response = UserController.get_all()
        return HttpSuccess().get_response(payload=response)

    @jwt_required()
    @api_resource_endpoint()
    def post(self):
        """
        Save User model
        """
        payload_data = json.loads(request.data)
        response = UserController.save(payload_data)
        return HttpSuccess().get_response(payload=response)


class UserAuthAPI(Resource):
    """
    User UserAuthAPI Resource
    """
    @api_resource_endpoint()
    def post(self):
        """
        Get Auth User
        """
        payload_data = json.loads(request.data)
        response = UserController.get_auth_user(payload_data)
        return HttpSuccess().get_response(payload=response)


class UserVerificationAPI(Resource):
    """
    User UserVerificationAPI Account Resource
    """

    @jwt_required()
    @api_resource_endpoint()
    def post(self):
        """
        User Account Verification
        """
        payload_data = json.loads(request.data)
        response = UserController.validate_user_account(payload_data)
        return HttpSuccess().get_response(payload=response)
