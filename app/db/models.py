from datetime import datetime
from typing import Self, Optional

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


from app.extensions import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    projects = db.relationship("Project", backref="user")

    @property
    def password(self):
        raise AttributeError("Password attribute can't be read")

    @password.setter
    def password(self, password: str) -> None:
        """Generates password hash

        Assigns generated password hash to password_hash attribute

        Args:
            password: Password to be hashed
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        """Checks given password against hashed password

        Args:
            password: Password to be checked

        Returns:
             True if the password matched, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    @classmethod
    def email_exists(cls, email: str) -> bool:
        """Checks if user with given email already exists

        Args:
            email: Given email to be checked

        Returns:
            True if the email exists, False otherwise.
        """
        if User.query.filter_by(email=email).first():
            return True
        return False

    @classmethod
    def create_user(cls, email: str, password: str) -> None:
        """Creates new user

        Args:
            email: User email
            password: User password
        """
        user = User(email=email, password=password, created_at=datetime.now())
        db.session.add(user)
        db.session.commit()

    @classmethod
    def get_user(cls, email: str) -> Optional[Self]:
        """Get user by email

        Args:
            email: User email

        Returns:
            User instance if user with given exists, None otherwise
        """
        return User.query.filter_by(email=email).first()


class Inventory(db.Model):
    __tablename__ = "inventories"

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey("inventory_types.id"), nullable=False)

    rows = db.relationship("InventoryRow", backref="inventory")


class InventoryType(db.Model):
    __tablename__ = "inventory_types"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15), nullable=False)


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    inventory_id = db.Column(db.Integer, db.ForeignKey("inventories.id"), nullable=False)


class InventoryRow(db.Model):
    __tablename__ = "inventory_rows"

    id = db.Column(db.Integer, primary_key=True)
    row_number = db.Column(db.Integer, nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey("inventories.id"), nullable=False)


class RowCells(db.Model):
    __tablename__ = "row_cells"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    error_id = db.Column(db.Integer, db.ForeignKey("error_messages.id"), nullable=False)
    row_id = db.Column(db.Integer, db.ForeignKey("inventory_rows.id"), nullable=False)


class ErrorMessage(db.Model):
    __tablename__ = "error_messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)







