from flask import Blueprint

blogs = Blueprint('blogs', __name__)

from . import admin, routes