from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required, current_user
from .. import  photos
import os
from app import db
import base64
from ..models import User
from io import BytesIO
from .forms import LoginForm,RegisterForm
from flask import Flask, render_template, redirect, url_for, flash, session, \
    abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, \
    current_user
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, EqualTo
import onetimepass
import pyqrcode
import base64
#Views
@main.route("/")
@main.route("/index")
def index():

  '''
  View root page function that returns the index page and its data
  '''

  return render_template('index.html')


@main.route('/thanks')
def thanks():
    return render_template('thanks.html')
@main.route('/vote')
def vote():
    return render_template('vote.html')
@main.route('/gover')
def gover():
    return render_template('gover.html')
@main.route('/user')
def user():
    return render_template('users.html')










@main.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    if current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            flash('Username already exists.')
            return redirect(url_for('main.register'))
        # add new user to the database
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        # redirect to the two-factor auth page, passing username in session
        session['username'] = user.username
        return redirect(url_for('main.two_factor_setup'))
    return render_template('register.html', form=form)


@main.route('/twofactor')
def two_factor_setup():
    if 'username' not in session:
        return redirect(url_for('main.index'))
    user = User.query.filter_by(username=session['username']).first()
    if user is None:
        return redirect(url_for('main.index'))
    # since this page contains the sensitive qrcode, make sure the browser
    # does not cache it
    return render_template('two-factor-setup.html'), 200, {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'}


@main.route('/qrcode')
def qrcode():
    if 'username' not in session:
        abort(404)
    user = User.query.filter_by(username=session['username']).first()
    if user is None:
        abort(404)

    # for added security, remove username from session
    del session['username']

    # render qrcode for FreeTOTP
    url = pyqrcode.create(user.get_totp_uri())
    stream = BytesIO()
    url.svg(stream, scale=3)
    return stream.getvalue(), 200, {
        'Content-Type': 'image/svg+xml',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'}


@main.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    if current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data) or \
                not user.verify_totp(form.token.data):
            flash('Invalid username, password or token.')
            return redirect(url_for('main.login'))

        # log user in
        login_user(user)
        flash('You are now logged in!')
        return redirect(url_for('main.vote'))
    return render_template('login.html', form=form)


@main.route('/logout')
def logout():
    """User logout route."""
    logout_user()
    return redirect(url_for('main.index'))


# create database tables if they don't exist yet





