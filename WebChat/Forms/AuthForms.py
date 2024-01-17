
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, BooleanField
from wtforms.validators import DataRequired
from re import match

class RegForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired()])
    password = StringField('Enter Password', validators=[DataRequired()])
    email = StringField('Enter Emal', validators=[DataRequired()])
    register = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired()])
    password = StringField('Enter Password', validators=[DataRequired()])
    login = SubmitField('Login')

