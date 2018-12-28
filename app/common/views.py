from . import common
from flask import render_template, session, redirect, url_for,request, jsonify,current_app
import os
import datetime
import random
from ..utils import utils
from config import Config

# basedir = os.path.abspath(os.path.dirname(__file__))

# 图片上传
@common.route('/img/upload', methods =['post'])
def uploadImg():
    img = request.files.get('file')
    print(request.files)

    print(img)
    path = Config.basedir+"/static/img/"
    print(path)
    # 如果路径不存在
    if not os.path.exists(path):
        os.makedirs(path)

    if img and allowed_file(img.filename):
        fname = img.filename
        # 分割后缀名
        ext = fname.rsplit('.', 1)[1]
        # 重新生成新名字
        new_name = create_name()+'.'+ext
        save_path = os.path.join(path,new_name)
        img.save(save_path)
        server_path = current_app.config['HOST']+"/static/img/"+new_name
        print(current_app.config['HOST'])

        return utils.network.Network.responseCode(200,{'url':server_path},"上传成功")
    else:
        return utils.network.Network.responseCode(utils.network.HttpVailateError,None,"上传失败")

# 允许通过的图片格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#随机生成图片名
def create_name(): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
        randomNum = random.randint(0, 100)  # 生成的随机整数n，其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum
