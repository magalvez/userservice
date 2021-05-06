#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from app import db


class User(db.Document):
    """
    User Model Class
    """
    user_id = db.StringField()
    pin = db.IntField()
    user_name = db.StringField()
    password = db.StringField()
    create_date = db.DateTimeField(default=datetime.utcnow)
