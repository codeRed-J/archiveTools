from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap5()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

# List of all extensions that should be initialized in application factory
EXTENSIONS_LIST = [bootstrap, db, login_manager]
