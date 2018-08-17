from flask import Blueprint

jdjs = Blueprint('jdjs', __name__)

from . import views