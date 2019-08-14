from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField,RadioField
from wtforms.validators import DataRequired, Length
class PresidentForm(FlaskForm):
   presidentname = RadioField('Your president choice', choices = [('Xystus Ngigi','Xystus Ngigi'),('Sylviah Rutto','Sylviah Rutto'),('Michelle Mukami','Michelle Mukami')])
class WomanRepForm(FlaskForm):
   womanname = RadioField('Your woman rep choice', choices = [('Nimo Said','Nimo Said'),('Mercy Muhia','Mercy Muhia'),('Linda Mukami','Linda Mukami')])
class ConstitutionalForm(FlaskForm):
   conname = RadioField('Your constitutional choice', choices = [('Wangombe Ngigi','Wangmbe Ngigi'),('Sylviah Wangari','Sylviah Wangari'),('Michelle Njoki','Michelle Njoki')])