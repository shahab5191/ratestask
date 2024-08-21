from flask import jsonify
from src.config import Config
from src.database.connection import execute_query
from src.database.convert_to_dict import convert_to_dict
from src.rates import bp


@bp.get(f"{Config().API_PREFIX}/rates")
def rates_endpoint():
    return {"data": "test"}


@bp.get(f"{Config().API_PREFIX}/prices")
def get_prices():
    query = 'SELECT * FROM prices LIMIT 3'
    colnames, rows = execute_query(query)
    
    prices = convert_to_dict(colnames, rows)

    return jsonify({"prices": prices})
