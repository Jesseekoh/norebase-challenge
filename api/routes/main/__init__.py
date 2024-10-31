from flask import Blueprint

bp = Blueprint('main', __name__)

from api.routes.main import routes
