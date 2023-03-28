import os

from app.constants import DEVELOPMENT, TESTING, DEFAULT

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class.

    Contains default configuration."""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "KeyString"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configuration for development"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "dev_database.sqlite")


class TestingConfig(Config):
    """Configuration for testing"""
    TESTING = True


config = {
    DEVELOPMENT: DevelopmentConfig,
    TESTING: TestingConfig,
    DEFAULT: DevelopmentConfig
}