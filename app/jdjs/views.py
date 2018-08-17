from flask import render_template, session, redirect, url_for,request, jsonify
from . import jdjs
from app import db
from ..models import User


@jdjs.route('/login', methods=['POST'])
def login():
    return ""


@jdjs.route('/register', methods=['POST'])
def register():
    return ""