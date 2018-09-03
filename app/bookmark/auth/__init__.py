from flask import Blueprint

bookmarkauth = Blueprint('bookmark.auth', __name__)

from . import views