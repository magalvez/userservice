#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.api.models import User
from util.dict_helper import get


class UserManager(object):
    """
    Class UserManager to perform communications within MongoEngine and MongoDB
    """

    @staticmethod
    def get(user_id):
        """
        Select User DB records
        :param user_id:
        :returns Object, Ie {'user_id': 10, 'pin': 20 ....}
        """
        return User.objects(user_id=user_id).first()

    @staticmethod
    def get_all():
        """
        Get All User DB records
        :returns List, [{'user_id': 10, 'pin': 20}, {'user_id': 10, 'pin': 20} ...]
        """
        return User.objects()

    @staticmethod
    def get_auth_user(user_data):
        """
        Get authenticated User DB record
        :param user_data:
        :returns Object, Ie {'user_id': 10, 'pin': 20 ....}
        """
        return User.objects(user_name=user_data['user_name'], password=user_data['password']).first()

    @staticmethod
    def validate_user_account(user_data):
        """
        Validate User account by user_id and pin
        :param user_data: dict, Ie {'user_id': 10, 'pin': 20}
        :returns Object, Ie {'user_id': 10, 'pin': 20 ....}
        """
        return User.objects(user_id=get(user_data, ['user_id']), pin=get(user_data, ['pin'])).first()

    @staticmethod
    def save(user_data):
        """
        Save User Collection record
        :param user_data: dict, Ie {'user_id': 10, 'pin': 20, ....}
        :returns Object, Ie {'user_id': 10, 'pin': 20 ....}
        """
        user = User(user_id=user_data['user_id'], pin=user_data['pin'], user_name=user_data['user_name'],
                    password=user_data['password'])
        user.save()
        return user
