from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, HiddenField
from wtforms.validators import Required, EqualTo

class CreatePasswordForm(FlaskForm):
    password = PasswordField('Create Password', validators=[Required(), EqualTo('confirm_password', message='Password must match')])
    confirm_password = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Submit')
