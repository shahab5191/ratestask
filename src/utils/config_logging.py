import logging
from flask import Flask
from loguru import logger

from src.config import Config


def configure_logging(app: Flask):
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
