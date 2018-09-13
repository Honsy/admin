from flask import Blueprint

bm = Blueprint('bookmark.bm', __name__)

from . import views