from flask import Blueprint

bp = Blueprint('rates', __name__)

from src.rates import routes  # noqa: F401, E402
