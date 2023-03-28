from flask import Flask

from config import config
from app.blueprints import BLUEPRINTS_LIST
from app.extensions import EXTENSIONS_LIST


def create_app(config_name: str) -> Flask:
    """Flask application factory

    Args:
        config_name: String of configuration name

    Returns:
        Flask instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Register all blueprints
    register_blueprint(app)

    # Initialize extensions
    register_extensions(app)

    return app


def register_blueprint(app: Flask):
    """Registers all blueprints in application

    Args:
        app: Flask instance.
    """
    for bp in BLUEPRINTS_LIST:
        app.register_blueprint(bp)


def register_extensions(app: Flask):
    """Initializes all extensions in application

    Args:
        app: Flask instance
    """
    for ext in EXTENSIONS_LIST:
        ext.init_app(app)
