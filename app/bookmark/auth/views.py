from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify
from . import bookmarkauth
from app import db
from ..models import bmUser
from ...utils import utils

# 登录
@bookmarkauth.route('/login', methods=['POST'])
def login():

    if request.json or 'username' not in request.json or 'password' not in request.json:
        if request.json['username'] == "" or request.json['password'] == "":
            return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '数据不能为空')

        user = bmUser.query.filter_by(username=request.json['username']).first()
        if user is None :
            return utils.network.Network.responseCode(utils.network.HttpVailateError,None,'用户名或者密码错误')


        user.password = request.json['password']
        user.verify_password(request.json['password'])
        token = utils.network.Network.generate_auth_token(user.id)
        return utils.network.Network.responseCode(utils.network.HttpSuccess,{'token': token.decode('ascii'),'id':user.id,'username':user.username},'')
    else:
        return utils.network.Network.responseCode(utils.network.HttpParamsError,None,'数据不能为空')
    return ""

# 注册
@bookmarkauth.route('/register', methods=['POST'])
def register():
    if request.json or 'username' not in request.json or 'password' not in request.json:

        if request.json['username'] == "" or request.json['password'] == "":
            return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '数据不能为空')

        user = bmUser(username=request.json['username'],
                    password=request.json['password'])
        olduser = bmUser.query.filter_by(username=request.json['username']).first()
        if olduser is not None:
            return utils.network.Network.responseCode(utils.network.HttpVailateError,'None','账号已经存在')
        else:
            db.session.add(user)
            db.session.commit()
            return utils.network.Network.responseCode(utils.network.HttpSuccess, 'None', '')
    else:
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '数据不能为空')

    return ""

# 登出
@bookmarkauth.route('/logout', methods=['POST'])
def logout():
    return utils.network.Network.responseCode(utils.network.HttpSuccess, 'None', '')
