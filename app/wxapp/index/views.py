from .. import wxapp
from  random import sample
from ...utils import utils
from ...models import Word
from flask import render_template, session, redirect, url_for,request, jsonify
from app import db

array = ['怎么这么可爱','小猪佩奇身上纹','入口即化','霸气侧漏','嘤嘤嘤','嘟嘟嘟','帅','男友力MAX',
         '可爱','眉清目秀','短发菇凉','蕙质兰心','春风十里','一定会幸福','牛奶系','大哥抽中华','正直','善良','坚强','可爱',
         '可爱','可爱','可爱']

@wxapp.route('/index', methods=['GET', 'POST'])
def index():
    try:
        words = Word.query.all()
    except:
        return utils.network.Network.responseCode(utils.network.HttpVailateError, None, '服务端出现异常')
    else:
        categorylist = []
        for category in words:
            categorylist.append(category.as_dict())
        sup = sample(categorylist, 8)
        return  utils.network.Network.responseCode(utils.network.HttpSuccess,{'list':sup},'查询成功')

@wxapp.route('/word/add', methods = ['GET','POST'])
def addWord():
    if 'name' not in request.json :
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '参数错误')
    if request.json['name'] is None:
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '名称不能为空')

    category = Word(categoryname=request.json['categoryname'],color=request.json['color'])
    db.session.add(category)
    db.session.commit()
    return utils.network.Network.responseCode(200, '添加成功', '')
