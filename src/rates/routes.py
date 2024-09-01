from flask import request
from pydantic import ValidationError
from src.config import Config
from src.rates import bp
from src.rates.query import get_rates, get_rates_from_m_view
from loguru import logger
from src.rates.schema import RateQueryParams


@bp.get(f"{Config.API_PREFIX}/rates")
def rates_endpoint():
    """
    Retrieve rate data based on query parameters.

    This endpoint retrieves rate information filtered by the provided query parameters:
    - `date_from` (str): Start date for filtering the rates (format: YYYY-MM-DD).
    - `date_to` (str): End date for filtering the rates (format: YYYY-MM-DD).
    - `origin` (str): Origin location code for filtering the rates.
    - `destination` (str): Destination location code for filtering the rates.

    The function processes these parameters, validates them, and fetches the corresponding 
    rates from the data source. In case of validation errors, an error message is returned. 
    For other exceptions, an internal server error is returned.

    Returns:
        dict: A JSON object containing either the rate data under the "rates" key 
        or an error message under the "error" key.
    """ # noqa

    logger.debug("Rate request received")
    try:
        query_param_schema = RateQueryParams
        query_params = {
                "date_from": request.args.get("date_from"),
                "date_to": request.args.get("date_to"),
                "origin": request.args.get("origin"),
                "destination": request.args.get("destination")
        }

        logger.debug("Validating request params")
        validated_params = query_param_schema.model_validate(query_params)
        logger.debug("Request param validation finished successfully")

        rates = get_rates(validated_params)
        logger.debug("Rates fetched successfully")

    except ValidationError as ve:
        logger.warning("Error while validating query:", ve)
        return {"error": "query parameters are not valid!"}, 400

    except Exception as e:
        logger.error("Error while running rates query:", e)
        return {"error": "Internal error"}, 500

    logger.debug("Returning rate query result")
    return {"rates": rates}


@bp.get(f"{Config.API_PREFIX}/rates/m_view")
def rates_from_m_view():
    """
    Retrieve rate data based on query parameters.

    This endpoint retrieves rate information filtered by the provided query parameters:
    - `date_from` (str): Start date for filtering the rates (format: YYYY-MM-DD).
    - `date_to` (str): End date for filtering the rates (format: YYYY-MM-DD).
    - `origin` (str): Origin location code for filtering the rates.
    - `destination` (str): Destination location code for filtering the rates.

    The function processes these parameters, validates them, and fetches the corresponding 
    rates from the data source. In case of validation errors, an error message is returned. 
    For other exceptions, an internal server error is returned.

    Returns:
        dict: A JSON object containing either the rate data under the "rates" key 
        or an error message under the "error" key.
    """ # noqa

    logger.debug("Rate request received")
    try:
        query_param_schema = RateQueryParams
        query_params = {
                "date_from": request.args.get("date_from"),
                "date_to": request.args.get("date_to"),
                "origin": request.args.get("origin"),
                "destination": request.args.get("destination")
        }

        logger.debug("Validating request params")
        validated_params = query_param_schema.model_validate(query_params)
        logger.debug("Request param validation finished successfully")

        rates = get_rates_from_m_view(validated_params)
        logger.debug("Rates fetched successfully")

    except ValidationError as ve:
        logger.warning("Error while validating query:", ve)
        return {"error": "query parameters are not valid!"}, 400

    except Exception as e:
        logger.error("Error while running rates query:", e)
        return {"error": "Internal error"}, 500

    logger.debug("Returning rate query result")
    return {"rates": rates}
