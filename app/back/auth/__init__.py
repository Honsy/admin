from flask import Blueprint

backauth = Blueprint('back.auth', __name__)

from . import views