#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.api.managers.user import UserManager
from util.dict_helper import get
from util.exceptions.exceptions import BadRequest, UserInvalidVerification, UserAuthNotFound


class UserController(object):
    """
    Class UserController to perform communications with Managers
    """

    @staticmethod
    def get_all():
        """
        Get All Users
        :returns List, [{'user_id': 10, 'pin': 20}, {'user_id': 10, 'pin': 20} ...]
        """
        return UserManager.get_all()

    @staticmethod
    def get_auth_user(user_data):
        """
        Get Auth User by user_name and password
        :param user_data: Filters to get users. Ie {user_id: 10}
        :returns Object, Ie {'user_id': 10, 'pin': 20 ....}
        """
        if not get(user_data, ['user_name']) or not get(user_data, ['password']):
            raise BadRequest

        user = UserManager.get_auth_user(user_data=user_data)
        if not user:
            raise UserAuthNotFound(user_data['user_name'], user_data['password'])

        return user

    @staticmethod
    def validate_user_account(user_data):
        """
        Validate user account by filters user_id and pin
        :param user_data: Filters to get users. Ie {id: 10}
        :returns dict, Ie {'valid_user': True}
        """
        if not get(user_data, ['user_id']) or not get(user_data, ['pin']):
            raise BadRequest

        user = UserManager.validate_user_account(user_data)
        if not user:
            raise UserInvalidVerification(user_data['user_id'], user_data['pin'])

        return {'valid_user': True}

    @staticmethod
    def save(user_data):
        """
        Save User model
        :param user_data: Data to be store in User collection. Ie {id: 10}
        :returns dict, Ie {'message': 'User created'}
        """
        if not get(user_data, ['user_id']) or not get(user_data, ['pin']) or \
                not get(user_data, ['user_name']) or not get(user_data, ['password']):
            raise BadRequest

        user = UserManager.save(user_data)
        if not user:
            raise UserInvalidVerification(user_data['user_id'], user_data['pin'])

        return {'message': 'User created'}
