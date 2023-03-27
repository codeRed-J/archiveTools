"""Package contains application blueprints"""

from app.blueprints.auth import auth
from app.blueprints.user import user

# List of all blueprints that should be registered in application factory
BLUEPRINTS_LIST = [auth, user]
