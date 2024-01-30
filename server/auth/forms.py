from flask import flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_login import login_user
from wtforms.fields import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from .models import User
from ..extensions import db

# Define login and registration form
class LoginForm(FlaskForm):
    email = EmailField("Enter Email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter Password", validators=[DataRequired()])
    login = SubmitField("Login", validators=[DataRequired()])
    
    def validate_login(self, field):
        user = self.get_user()

        if not user:
            flash("User doesn't exists!")
            return redirect(url_for("auth.login"))
        
        if not check_password_hash(user.password, self.password.data):
            flash("Incorrect Password!")
            return False
        else:
            login_user(user)
            user.last_login = datetime.now()
            db.session.commit()
            return True
        
    def get_user(self):
        return User.query.filter_by(email=self.email.data).first()
    

class RegistrationForm(FlaskForm):
    name = StringField("Enter Name", validators=[DataRequired()])
    email = EmailField("Enter Email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter Password", validators=[DataRequired()])
    submit = SubmitField("Register", validators=[DataRequired()])

    def validate_login(self):
        if User.query.filter_by(email=self.email.data).count() > 0:
            flash("Email already exists")
            return False
        return True
    
    def register(self):
        user = User(name=self.name.data, email=self.email.data, password=generate_password_hash(self.password.data), registration_date=datetime.now(), last_login = datetime.now())
        db.session.add(user)
        db.session.commit()
        flash("Registered Successfully! Please login")
