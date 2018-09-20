from flask import Blueprint

yshoog = Blueprint('yshoog', __name__)

from . import views
from .tools import views