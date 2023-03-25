from flask import Flask

from config import config


def create_app(config_name: str):
    """Flask application factory

    Args:
        config_name: String of configuration name
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    return app

