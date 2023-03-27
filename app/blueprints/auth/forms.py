from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class Registration(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(),
                                         EqualTo("password2",
                                                 message="Password must match.")])
    password2 = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Register")


class Login(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

