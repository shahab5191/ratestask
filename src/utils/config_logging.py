import logging
from flask import Flask
from loguru import logger

from src.config import Config


def configure_logging(app: Flask):
    """
    Configures logging for the given Flask application.

    This function sets up logging based on the application's environment and configuration.
    It adjusts the logging behavior according to whether the environment is "production" or not,
    and adds an `InterceptHandler` to route logs from Flask's logger to the application's logger.

    Args:
        app (Flask): The Flask application instance to configure logging for.

    Returns:
        None

    Notes:
        - If the application's environment is set to "TESTING", logging configuration is bypassed.
        - In a "production" environment, logs are written to `logs/production.log` with a 
          `WARNING` level and rotate every 10 MB with retention for 10 days.
        - In other environments, logs are written to `logs/debug.log` with a `DEBUG` level and 
          similar rotation and retention settings.
        - All error logs are written to `logs/errors.log` with an `ERROR` level and similar 
          rotation and retention settings.

    Example:
        app = Flask(__name__)
        configure_logging(app)
    """ # noqa

    if app.config.get("ENV") == "TESTING":
        return

    app.logger.removeHandler(app.logger.handlers[0])

    environment = Config.ENV

    if environment == "production":
        logger.add(
            "logs/production.log",
            rotation="10 MB",
            retention="10 days",
            compression="zip",
            level="WARNING"
        )
    else:
        logger.add(
            "logs/debug.log",
            rotation="10 MB",
            retention="10 days",
            level="DEBUG"
        )

    logger.add(
        "logs/errors.log",
        level="ERROR",
        rotation="10 MB",
        retention="10 days"
    )

    class InterceptHandler(logging.Handler):
        def emit(self, record):
            logger_opt = logger.opt(depth=0, exception=record.exc_info)
            logger_opt.log(record.levelname, record.getMessage())

    app.logger.addHandler(InterceptHandler())
