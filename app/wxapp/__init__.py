from flask import Blueprint

wxapp = Blueprint('wxapp', __name__)

from . import views
from .index import views