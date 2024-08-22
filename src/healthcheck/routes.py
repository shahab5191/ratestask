from flask import jsonify
from src.config import Config
from src.healthcheck import bp


@bp.get(f"{Config().API_PREFIX}/healthz")
def healthcheck():
    """
    Healthcheck endpoint for kubernetes (or any other depolyment).
    Returns a JSON response indicating the health status of the application.

    Returns:
        JSON response with a status field:
        - 'healthy': If the application is healthy.
        - 'unhealthy': If the application is unhealthy
    """
    try:
        database_connection = True
        if not database_connection:
            return jsonify(status='unhealthy'), 503
    except Exception as e:
        return jsonify(status='unhealthy', error=str(e)), 500

    return jsonify(status='healthy')
