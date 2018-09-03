from flask import Blueprint

jdjsauth = Blueprint('jdjs.auth', __name__)

from . import views