from .. import yshoog
from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify
from ....models import ToolCategory
from ....utils import utils
from app import db


# 查询所有工具分类
@yshoog.route('/toolcategory/all',methods = ['GET','POST'])
def getAll():
    try:
        categorys = ToolCategory.query.all()
    except:
        return utils.network.Network.responseCode(utils.network.HttpVailateError, None, '服务端出现异常')
    else:
        categorylist = []
        for category in categorys:
            categorylist.append(category.as_dict())

        return  utils.network.Network.responseCode(utils.network.HttpSuccess,{'list':categorylist},'查询成功')

# 添加工具分类
@yshoog.route('/toolcategory/add',methods = ['POST'])
def addCategory():
    print(request.json)
    if 'categoryname' not in request.json :
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '参数错误')

    if request.json['categoryname'] is None:
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '名称不能为空')

    oldcategory = ToolCategory.query.filter_by(categoryname=request.json['categoryname']).first()
    if oldcategory is not None:
        return utils.network.Network.responseCode(utils.network.HttpVailateError, None, '该分类已存在，请更换名称！')

    category = ToolCategory(categoryname=request.json['categoryname'],color=request.json['color'])
    db.session.add(category)
    db.session.commit()
    return utils.network.Network.responseCode(utils.network.HttpSuccess, None, '添加成功')
