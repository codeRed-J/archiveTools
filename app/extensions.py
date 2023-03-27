from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap5()
db = SQLAlchemy()

# List of all extensions that should be initialized in application factory
EXTENSIONS_LIST = [bootstrap, db]
