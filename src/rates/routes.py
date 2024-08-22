from flask import jsonify
from src.config import Config
from src.database.connection import execute_query
from src.database.convert_to_dict import convert_to_dict
from src.rates import bp
from src.rates.query import get_rates
from loguru import logger


@bp.get(f"{Config().API_PREFIX}/rates")
def rates_endpoint():
    try:
        rates = get_rates()
    except Exception as e:
        logger.error("Error while running rates query:", e)
        return {"error": "Internal error"}, 500
    return {"rates": rates}


@bp.get(f"{Config().API_PREFIX}/prices")
def get_prices():
    query = 'SELECT * FROM prices LIMIT 10'
    colnames, rows = execute_query(query)

    prices = convert_to_dict(colnames, rows)

    return jsonify({"prices": prices})


@bp.get(f"{Config().API_PREFIX}/ports")
def get_ports():
    query = 'SELECT * FROM ports LIMIT 10'
    colnames, rows = execute_query(query)

    ports = convert_to_dict(colnames, rows)

    return jsonify({"ports": ports})
