from app.extensions import db, login_manager


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    projects = db.relationship("Project", backref="user")


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
    message = db.Columnt(db.String, nullable=False)







