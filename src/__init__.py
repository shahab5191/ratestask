from flask import Flask
from src.config import Config
from flask_cors import CORS
from loguru import logger


app: Flask


def create_app(config_class=Config):
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
