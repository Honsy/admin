from flask import Blueprint

bmbusiness = Blueprint('bookmark.business', __name__)

from . import views