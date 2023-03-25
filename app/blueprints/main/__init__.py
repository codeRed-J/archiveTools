"""Module for main blueprint initialization"""

from flask import Blueprint

main = Blueprint("main",
                 __name__,
                 template_folder="templates",
                 static_folder="static")

from app.blueprints.main import views
