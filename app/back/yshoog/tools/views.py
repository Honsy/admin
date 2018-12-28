from .. import yshoog
from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify
from ....models import ToolCategory,Tool
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
    return utils.network.Network.responseCode(utils.network.HttpSuccess, {'category':category.as_dict()}, '添加成功')


# 修改工具分类
@yshoog.route('/toolcategory/update', methods=['POST'])
def updateCategory():
    if 'id' not in request.json :
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '参数错误')

    if request.json['categoryname'] is None:
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '名称不能为空')

    oldcategory = ToolCategory.query.filter_by(categoryname=request.json['id']).first()
    if oldcategory is None:
        return utils.network.Network.responseCode(utils.network.HttpVailateError,None,'该分类不存在，请检查数据正确性！')

    oldcategory.categoryname = request.json['categoryname']
    oldcategory.color = request.json['color']
    db.session.commit()

    return ''


# 刪除工具分类
@yshoog.route('/toolcategory/del',methods = ['POST'])
def delCategory():
    if 'id' not in request.json :
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '参数错误')

    oldcategory = ToolCategory.query.filter_by(id=request.json['id']).first()

    if oldcategory is None:
        return utils.network.Network.responseCode(utils.network.HttpVailateError,None,'该分类不存在，请检查数据正确性！')
    db.session.delete(oldcategory)
    db.session.commit()
    return utils.network.Network.responseCode(utils.network.HttpSuccess, None, '删除成功')

# 添加工具
@yshoog.route('/tools/add',methods = ['POST'])
def addTool():
    if 'name' not in request.json :
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '参数错误')

    if request.json['name'] is None:
        return utils.network.Network.responseCode(utils.network.HttpParamsError, None, '名称不能为空')

    oldTool = Tool.query.filter_by(name=request.json['name']).first()
    if oldTool is not  None:
        return utils.network.Network.responseCode(utils.network.HttpVailateError, None, '该工具已存在，请重新添加')

    tool = Tool(name=request.json['name'],icon=request.json['icon'],href=request.json['href'],categoryid=request.json['categoryid'],subtitle= request.json['subtitle'])
    db.session.add(tool)
    db.session.commit()
    return utils.network.Network.responseCode(utils.network.HttpSuccess, {'tool':tool.as_dict()}, '添加成功')

# 查询所有工具分类
@yshoog.route('/tools/all',methods = ['GET','POST'])
def getToolAll():
    try:
        tools = Tool.query.all()
    except:
        return utils.network.Network.responseCode(utils.network.HttpVailateError, None, '服务端出现异常')
    else:
        toollist = []
        for category in tools:
            toollist.append(category.as_dict())

        return  utils.network.Network.responseCode(utils.network.HttpSuccess,{'list':toollist},'查询成功')