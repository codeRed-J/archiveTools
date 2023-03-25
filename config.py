import os

from app.constants import DEVELOPMENT, TESTING, DEFAULT

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class.

    Contains default configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'KeyString'
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Configuration for development"""
    DEBUG = True


class TestingConfig(Config):
    """Configuration for testing"""
    TESTING = True


config = {
    DEVELOPMENT: DevelopmentConfig,
    TESTING: TestingConfig,
    DEFAULT: DevelopmentConfig
}