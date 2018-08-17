from flask import render_template, session, redirect, url_for,request, jsonify,json
from . import backuser
from app import db
from ...models import User
from ...utils import utils

@backuser.route('/info',methods = ['GET','POST'])
def info():
    if utils.network.Network.verift_auth_token(request.headers['token']) is not None:
        if request.args is not None:
            if 'id' in request.args:
                user = User.query.filter_by(id=request.args.get('id')).first()
                if user is not None:
                    return utils.network.Network.responseCode(200, {'user':user.as_dict()}, '')
                else:
                    return utils.network.Network.responseCode(400, None, '用户不存在')
            else:
                return utils.network.Network.responseCode(400, None, '未知用户')
        else:
            return utils.network.Network.responseCode(400,None,'参数错误')
    else:
        return  utils.network.Network.responseCode(400,None,'Token验证失败')
    return ""