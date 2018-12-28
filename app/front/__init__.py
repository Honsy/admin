from flask import Blueprint


front = Blueprint('front', __name__)

from . import views
from .home import views