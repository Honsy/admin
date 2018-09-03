from flask import render_template, session, redirect, url_for,request, jsonify
from . import bookmark
from app import db
from ..models import User


@bookmark.route('/login', methods=['POST'])
def login():
    return ""


@bookmark.route('/register', methods=['POST'])
def register():
    return ""