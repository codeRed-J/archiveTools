"""Module for logged-in user views"""
from flask import render_template
from flask_login import login_required

from app.blueprints.user import user


@user.route("/")
@login_required
def index():
    return render_template("index.html")
