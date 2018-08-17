from flask import Blueprint

backuser = Blueprint('back.user', __name__)

from . import views