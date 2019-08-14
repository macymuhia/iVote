
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BlogForm,CommentForm
from app.request import get_quote
from ..models import Role,User,Vote,
from flask_login import login_required, current_user

from .. import db,photos
import markdown2 
import math as m
import random as r

@main.route("/OTPgen")
def OTPgen():
   # Declare a string variable
   # which stores all alpha-numeric characters
   string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   OTP = ""
   varlen = len(string)
   for i in range(6):
       OTP += string[m.floor(r.random() * varlen)]

   return (OTP)
   print("Your One Time Password is ", OTPgen())
@main.route("/")
@main.route("/home")
def home():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Welcome to Pitch app'

    
   page = request.args.get('page', 1, type=int)
   
   return render_template('home.html',posts=posts,quotes=quotes)
