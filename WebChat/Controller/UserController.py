import logging
from flask import jsonify, Blueprint, request, render_template

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/search', methods=['POST'])
def searchByUsername():
    return render_template('chat.html')
