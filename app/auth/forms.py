from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from wtforms import StringField,PasswordField,BooleanField,SubmitField,NumberInput
from ..models import User
from wtforms import ValidationError
class RegistrationForm(FlaskForm):
    id_number =  NumberInput('I.D number',validators=[Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

        # .......
    def validate_id_number(self,data_field):
        if User.query.filter_by(id_number =data_field.data).first():
            raise ValidationError('There is an account with that id_number')



class LoginForm(FlaskForm):
  
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


