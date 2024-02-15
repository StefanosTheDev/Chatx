
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, BooleanField
from wtforms.validators import DataRequired

class Search_Friend_Form(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired()])
    search = SubmitField('Search')

class Friend_Request_Form(FlaskForm):
    request_friend_button = SubmitField('Send Friend Request')

class Delete_Friend_Form(FlaskForm):
    remove_friend = SubmitField('Remove Friend')
    cancel = SubmitField('Cancel')

class Accept_Friend_Request_Form(FlaskForm):
    accept_friend_request = SubmitField('Accept Request')
    deny_friend_request = SubmitField('Deny Friend Request')

