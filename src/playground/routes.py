from flask import render_template, request
from loguru import logger
from pydantic import ValidationError
from src.playground import bp
from src.rates.query import get_rates
from src.rates.schema import RateQueryParams


@bp.route('/playground', methods=['GET', 'POST'])
def playground():
    if request.method == 'POST':
        params = {
            "destination": request.form.get("destination"),
            "origin": request.form.get("origin"),
            "date_from": request.form.get("date_from"),
            "date_to": request.form.get("date_to")
        }

        input_schema = RateQueryParams
        try:
            validated_inputs = input_schema.model_validate(params)
            rates = get_rates(validated_inputs)

            return render_template('rates.html', table_data=rates, form_data=params)
        except ValidationError as ve:
            logger.warning("Input validation error:", ve)
        except Exception as e:
            logger.error("Error while compiling rate data:", e)

    params = {
        "destination": "",
        "origin": "",
        "date_from": "2016-01-01",
        "date_to": "2016-01-30"
    }
    return render_template('rates.html', table_data=[], form_data=params)
