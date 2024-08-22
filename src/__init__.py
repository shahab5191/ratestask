from flask import Flask
from src.config import Config
from flask_cors import CORS
from loguru import logger


app: Flask


def create_app(config_class=Config):
    """
    Create and configure the Flask application.

    This function initializes a Flask application with the provided configuration 
    class, sets up Cross-Origin Resource Sharing (CORS), and registers blueprints 
    for different parts of the application.

    The following blueprints are registered:
    - `rate_bp`: Handles endpoints related to rates (imported from `src.rates`).
    - `healthcheck_bp`: Handles endpoints for health checks (imported from `src.healthcheck`).

    Args:
        config_class (class, optional): The configuration class to use for the Flask 
        app. Defaults to `Config`.

    Returns:
        Flask: The initialized Flask application instance.
    """ # noqa

    logger.debug("Initializing flask app")

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)

    from src.rates import bp as rate_bp
    from src.healthcheck import bp as healthcheck_bp

    app.register_blueprint(rate_bp)
    app.register_blueprint(healthcheck_bp)

    logger.debug("Flask app created successfully!")
    return app
