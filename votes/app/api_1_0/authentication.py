# -*- coding: utf-8 -*-
from flask import g, jsonify
from flask.ext.httpauth import HTTPBasicAuth
from ..models import User, AnonymousUser
from . import api

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email, password):
    """根据邮箱获取用户信息同密码进行比对验证"""
    if email == '':
        g.current_user = AnonymousUser()
        return True
    if password == '':
        return False
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)


