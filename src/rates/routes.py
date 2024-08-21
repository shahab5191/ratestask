from flask import jsonify
from src.config import Config
from src.db import execute_query
from src.rates import bp


@bp.get(f"{Config().API_PREFIX}/rates")
def rates_endpoint():
    return {"data": "test"}


@bp.get(f"{Config().API_PREFIX}/prices")
def get_prices():
    query = 'SELECT * FROM prices LIMIT 3'
    colnames, rows = execute_query(query)
    print(colnames)
    print(rows)
    return jsonify({"test": "test"})
