from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db, photos

#Views
@main.route("/")
@main.route("/home")
def index():

  '''
  View root page function that returns the index page and its data
  '''
  title = 'IVOTE'

  # Getting reviews by category
  page = request.args.get('page', 1, type=int)


  return render_template('index.html')
