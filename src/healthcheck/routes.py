from loguru import logger
from src.config import Config
from src.healthcheck import bp
from src.utils.database_connection_check import is_db_connection_healthy


@bp.get(f"{Config.API_PREFIX}/healthz")
def healthcheck():
    """
    Healthcheck endpoint for kubernetes (or any other depolyment).
    Returns a JSON response indicating the health status of the application.

    Returns:
        JSON response with a status field:
        - 'healthy': If the application is healthy.
        - 'unhealthy': If the application is unhealthy
    """ # noqa

    logger.debug("Health check request received")
    try:
        if not is_db_connection_healthy():
            logger.error("Database connection problem, returning unhealthy")
            return {"status": 'unhealthy'}, 503
    except Exception as e:
        logger.error("Error while checking for servre health:", e)
        return {"status": 'unhealthy', "error": str(e)}, 500

    return {"status": "healthy"}, 200
