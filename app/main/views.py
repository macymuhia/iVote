from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required, current_user
from .. import  photos

#Views
@main.route("/")
@main.route("/home")
def index():

  '''
  View root page function that returns the index page and its data
  '''

  return render_template('index.html')


@main.route('/president', methods=['GET', 'POST'])
def president():
    '''
    Function the returns what the user plans to do during breaktime
    '''
    return render_template('president.html')


@main.route('/users', methods=['GET', 'POST'])
def users():
    '''
    Function the returns what the user plans to do during breaktime
    '''
    return render_template('user/user.html')