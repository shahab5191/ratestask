from flask import Blueprint

bp = Blueprint('healthcheck', __name__)

from src.healthcheck import routes  # noqa: F401, E402
