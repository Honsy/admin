from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify
from . import backauth
from app import db
from ...models import User
from ...utils import utils

@backauth.route('/login', methods=['POST'])
def login():
    if request.json or 'username' not in request.json or 'password' not in request.json:
        user = User.query.filter_by(username=request.json['username']).first()
        if user is not None :
            user.password = request.json['password']
            user.verify_password(request.json['password'])
            token = utils.network.Network.generate_auth_token(user.id)
            return utils.network.Network.responseCode(200,{'token': token.decode('ascii'),'id':user.id},'')
        else:
            return utils.network.Network.responseCode(404,None,'用户名或者密码错误')
    else:
        return utils.network.Network.responseCode(400,None,'数据不能为空')
    return ""


@backauth.route('/register', methods=['POST'])
def register():
    if request.json or 'username' not in request.json or 'password' not in request.json:
        user = User(username=request.json['username'],
                    password=request.json['password'])
        olduser = User.query.filter_by(username=request.json['username']).first()
        if olduser is not None:
            return utils.network.Network.responseCode(400,'None','账号已经存在')
        else:
            db.session.add(user)
            db.session.commit()
            return utils.network.Network.responseCode(200, 'None', '')
    else:
        return utils.network.Network.responseCode(400, None, '数据不能为空')

    return ""

