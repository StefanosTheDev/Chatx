import logging
from flask import jsonify, Blueprint, request, render_template

user_blueprint = Blueprint('user', __name__)

##**TODO This will allow you to search through the DB and see if that user exists.

@user_blueprint.route('/search', methods=['POST'])
def searchByUsername():

    return render_template('chat.html')
