from flask import Blueprint

bp = Blueprint("playground", __name__)

from src.playground import routes  # noqa: F401, E402
