#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexter import Contexter

from app import app, auth
from app.api import api

from test.test_helper import BaseTest, TestHttpRequest, deserialize_json


class UserTest(BaseTest):
    """
    Set of tests for user endpoint
    """

    user_data = {
        'user_id': '105398890',
        'pin': 2091
    }

    @classmethod
    def setUpClass(cls):

        cls.__endpoint_url = '/userservice/api/v1.0/validate-user-account'

        # So the exception would be catch by flask-restful
        app.config['PROPAGATE_EXCEPTIONS'] = False
        cls.app = app.test_client()

        cls.http_request = TestHttpRequest(cls.app, cls.__endpoint_url)

    def setUp(self):
        db = self.set_up_db()
        self.db = db

    def get_patches(self, new_patches=None):
        """
        Get the mock patches to be used.
        :return: list, the mock patches to apply.
        """

        patch_dict = {}

        if new_patches is not None:
            for key, value in new_patches.iteritems():
                patch_dict[key] = value

        return self.build_patches(patch_dict)

    def test_user_bad_request(self):
        """
        Check the endpoint returns an error message because the user resource was bad request (HTTP 400)
        """

        with Contexter(*self.get_patches()):

            user_data = {
                'user_id': '105398890'
            }

            response = self.http_request.post(user_data)
            self.json_structure_response_code_assert(400, response)

    def test_user_verification_true(self):
        """
        Check the endpoint returns True response with a user validation True (HTTP 200)
        """

        with Contexter(*self.get_patches()):

            response = self.http_request.post(self.user_data)
            self.json_structure_response_code_assert(200, response)

            data = deserialize_json(response.data)
            self.assertEqual(data['is_valid'], True)

    def test_user_verification_false(self):
        """
        Check the endpoint returns False response with a COP withdrawal (HTTP 200)
        """

        with Contexter(*self.get_patches()):

            user_data = {
                'user_id': '105398899',
                'pin': 2093
            }

            response = self.http_request.post(user_data)
            self.json_structure_response_code_assert(200, response)

            data = deserialize_json(response.data)
            self.assertEqual(data['is_valid'], False)
