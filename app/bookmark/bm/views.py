from datetime import datetime
from flask import render_template, session, redirect, url_for,request, jsonify
from . import bm
from app import db
from ..models import bmUser
from ...utils import utils

@bm.route('/add', methods=['POST'])
def bmAdd():
    return ''
