from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField,  SelectField,  FileField,TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired,  Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app import csrf
from wtforms.fields import DateField

class LoginForm(FlaskForm):
     email = StringField('Enter Email',validators=[Email(),DataRequired()])
     password = PasswordField('Enter Password', validators=[DataRequired()])
     submit = SubmitField('Sign in')

     