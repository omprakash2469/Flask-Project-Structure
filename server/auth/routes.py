from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .models import User

@auth.route("/")
def index():
    return render_template('admin/index.html')


@auth.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
            return redirect(url_for('admin.index'))

    return render_template('auth/login.html', form=form)


@auth.route("/signup", methods=['GET', 'POST'])
def signup():

    form = RegistrationForm()
    if form.validate_on_submit():
        form.register()
        return redirect(url_for('admin.index'))

    return render_template('auth/signup.html', form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

    
@auth.route("/forgot-password")
def forgot_password():
    return render_template('pages/about.html')