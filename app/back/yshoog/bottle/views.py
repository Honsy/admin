from .. import yshoog
from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify
from ....models import ToolCategory,Tool
from ....utils import utils
from app import db

@yshoog.route('/bottle/throw',methods = ['GET','POST'])
def throw():

    return ''


@yshoog.route('/bottle/pick', methods=['GET', 'POST'])
def pick():

    return ''