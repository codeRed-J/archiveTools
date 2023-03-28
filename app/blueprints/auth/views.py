"""Module for authentication views"""
from flask import render_template, request, url_for, redirect
from flask_login import login_required, login_user, logout_user

from app.blueprints.auth import auth
from app.blueprints.auth.forms import LoginForm, RegistrationForm
from app.db.models import User


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user(form.email.data)
        if user and user.verify_password(form.password.data):
            login_user(user)
            next_url = request.args.get("next")
            return redirect(next_url or url_for("user.index"))
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        User.create_user(form.email.data,
                         form.password.data)
        return redirect(url_for("auth.login"))
    return render_template("registration.html", form=form)
